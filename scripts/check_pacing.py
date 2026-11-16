#!/usr/bin/env python3
"""
Pacing, Word Count, Telemetry & Anti-Translationese Diagnostic Checker for Novel Chapters.
Analyzes word count, reading duration, dialogue ratios, and flags generic AI prose and translationese patterns.
"""

import sys
import re

BANNED_TELL_PATTERNS = [
    r"dia merasa",
    r"ia merasa",
    r"merasa sangat",
    r"ia mendesis",
    r"ia mencemooh",
    r"ia merintih",
    r"ia bergumam sinis",
    r"malam itu ia belajar bahwa",
    r"seperti yang kau tahu",
]

THOUGHT_VERBS = [
    r"\btahu bahwa\b",
    r"\bsadar bahwa\b",
    r"\bberpikir bahwa\b",
    r"\bmengingat bahwa\b",
    r"\bmenyadari bahwa\b",
    r"\bknew that\b",
    r"\brealized that\b",
    r"\bthought that\b",
]

TRANSLATIONESE_SLOP = [
    (r"menemukan dirinya", "Kalk 'he found himself' -> Ganti dengan 'mendapati dirinya' / 'tahu-tahu dia sudah'"),
    (r"membuat akal sehat", "Kalk 'makes sense' -> Ganti dengan 'masuk akal'"),
    (r"mengambil napas dalam", "Kalk 'take a deep breath' -> Ganti dengan 'menarik napas panjang'"),
    (r"di penghujung hari", "Kalk 'at the end of the day' -> Ganti dengan 'pada akhirnya' / 'biar bagaimanapun'"),
    (r"mata mereka terkunci", "Kalk 'their eyes locked' -> Ganti dengan 'tatapan mereka bersirobok' / 'bertemu'"),
    (r"(?:tidak|tak) bisa menahan diri untuk tidak", "Kalk 'couldn't help but' -> Ganti dengan 'tak kuasa menahan'"),
    (r"tapestri takdir", "AI-slop cliché -> Ganti dengan detail indrawi konkret"),
    (r"relung (?:jiwa )?terdalam", "AI-slop cliché -> Ganti dengan respon somatik/fisik nyata"),
    (r"simfoni keheningan", "AI-slop cliché -> Ganti dengan suara akustik ruangan nyata"),
    (r"tarian bayang-bayang", "AI-slop cliché -> Ganti dengan kontras pencahayaan nyata"),
]

def analyze_chapter(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    words = re.findall(r"\b\w+\b", content)
    total_words = len(words)
    
    # Reading speed calculations (Marc Brysbaert meta-analysis: 260 WPM print, 220 WPM mobile)
    print_time_mins = total_words / 260.0
    mobile_time_mins = total_words / 220.0
    
    # Dialogue detection (quoted text)
    dialogues = re.findall(r'["“](.*?)["”]', content)
    dialogue_words = sum(len(re.findall(r"\b\w+\b", d)) for d in dialogues)
    dialogue_ratio = (dialogue_words / total_words * 100) if total_words > 0 else 0

    print("=" * 65)
    print(" 📖 NOVEL CHAPTER PACING & STYLISTICS DIAGNOSTIC REPORT")
    print("=" * 65)
    print(f"File                 : {file_path}")
    print(f"Total Words          : {total_words:,} words")
    print(f"Reading Time (Print) : ~{print_time_mins:.1f} minutes (@ 260 WPM)")
    print(f"Reading Time (Mobile): ~{mobile_time_mins:.1f} minutes (@ 220 WPM)")
    print(f"Dialogue Words       : {dialogue_words:,} words ({dialogue_ratio:.1f}%)")
    
    # Chapter Length Assessment
    print("\n📏 Chapter Length & Cognitive Session Evaluation:")
    if total_words < 1000:
        print("  ⚠️ Micro-chapter (<1,000 words). May feel insubstantial unless written as a rapid thriller cut.")
    elif 2000 <= total_words <= 3500:
        print("  ✅ Goldilocks Zone (2,000–3,500 words). Optimal immersion and mobile retention window.")
    elif total_words > 4000:
        print("  ⚠️ Heavy Chapter (>4,000 words / >18 mins). Risk of cognitive fatigue; consider introducing a scene break.")
    else:
        print("  ℹ️ Acceptable range (1,000–2,000 words or 3,500–4,000 words).")

    # Pacing Ratio Assessment
    print("\n⚖️ Dialogue-to-Narrative Balance:")
    if dialogue_ratio < 15:
        print("  ⚠️ Narrative heavy (<15% dialogue). Risk of dry infodump or lack of interpersonal friction.")
    elif dialogue_ratio > 65:
        print("  ⚠️ Dialogue heavy (>65% dialogue). Risk of white-room syndrome; ground speakers in physical space.")
    else:
        print("  ✅ Balanced narrative-to-dialogue ratio (15%–65%).")

    # Anti-slop checks
    print("\n🔍 Checking for Banned AI-Slop & Abstract Telling Patterns:")
    slop_count = 0
    for pattern in BANNED_TELL_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            slop_count += len(matches)
            print(f"  ❌ Banned Tell ({len(matches)}x): '{pattern}'")

    for pattern in THOUGHT_VERBS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            slop_count += len(matches)
            print(f"  ⚠️ Thought Verb ({len(matches)}x): '{pattern}' (Unpack into sensory action)")

    # Translationese & Slop checks
    print("\n🌐 Checking for AI-Translationese & Pseudo-Poetic Clichés:")
    trans_count = 0
    for pattern, advice in TRANSLATIONESE_SLOP:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            trans_count += len(matches)
            print(f"  🚨 Translationese / Slop ({len(matches)}x): '{pattern}' -> {advice}")

    total_issues = slop_count + trans_count
    if total_issues == 0:
        print("  ✅ Clean! No banned AI-slop, thought verbs, or translationese detected.")
    else:
        print(f"\n⚠️ Total issues flagged: {total_issues}. Please revise following references/12_indonesian_stylistics_and_dialogue_slang.md")
    print("=" * 65)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_pacing.py <path_to_chapter_markdown>")
        sys.exit(1)
    analyze_chapter(sys.argv[1])
