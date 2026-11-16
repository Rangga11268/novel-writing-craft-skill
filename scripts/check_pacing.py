#!/usr/bin/env python3
"""
Pacing, Word Count, Telemetry & Multilingual Humanizer Diagnostic Checker for Novel Chapters.
Analyzes word count, reading duration, dialogue ratios, sentence length variation (metronome check),
and flags generic AI prose, translationese, connector bloat, and nominalization patterns.
"""

import sys
import re
import math

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
    (r"menghembuskan napas yang (?:tak|tidak) ia sadari", "Kalk 'breath he didn't know he was holding' -> Klise AI"),
    (r"senyum tipis bermain di bibir", "Kalk 'a ghost of a smile played' -> Ganti dengan 'sudut bibir terangkat'"),
    (r"keheningan yang memekakkan", "Kalk 'deafening silence' -> Ganti dengan 'senyap total'"),
    (r"melanggar ruang batas fisik", "Kalk 'violates physical boundary' -> Terlalu kaku, gunakan 'Lepas. Sakit' atau bahasa tubuh"),
    (r"baru saja menghindar dari tangan", "Kalk 'just dodged my hand' -> Subtitle anime kaku, gunakan 'Belagu amat lu nyingkir'"),
    (r"tidak membuatmu lebih pintar satu bit", "Kalk 'not one bit smarter' -> Punchline kaku, gunakan 'gak bikin lu lebih pinter'"),
    (r'["“]Tolak\.?["”]', "Penolakan kamus tunggal kaku -> Ganti dengan 'Ogah' / 'Gak sudi' / 'Gak mau'"),
    (r"pesuruh klan", "Pastiche fantasi kaku -> Ganti dengan 'babu lu' / 'suruhan keluarga lu'"),
    (r"tapestri takdir", "AI-slop cliché -> Ganti dengan detail indrawi konkret"),
    (r"relung (?:jiwa )?terdalam", "AI-slop cliché -> Ganti dengan respon somatik/fisik nyata"),
    (r"simfoni keheningan", "AI-slop cliché -> Ganti dengan suara akustik ruangan nyata"),
    (r"tarian bayang-bayang", "AI-slop cliché -> Ganti dengan kontras pencahayaan nyata"),
]

HUMANIZER_TELLS = [
    (r"\b(?:bukan berarti|ini bukan berarti|hal ini bukan berarti)\b", "Penyangkalan antisipatif (Anticipatory denial) -> Nyatakan langsung secara positif"),
    (r"\b(?:melakukan pengamatan|melakukan pemeriksaan|melakukan analisis|melakukan tatapan)\b", "Nominalisasi verba ringan -> Ganti dengan verba aktif langsung (menatap, memeriksa, menganalisis)"),
    (r"\b(?:di sisi lain|oleh karena itu|selain itu|lebih lanjut|namun demikian)\b", "Konektor formal berlebih -> Bangun kohesi lewat repetisi kata kunci dan klitik -nya"),
    (r"\b(?:testament to|rich tapestry|palpable tension|delve into)\b", "English AI cliché -> Replace with concrete sensory action"),
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

    # Sentence metrics (Sentence variation / Metronome check)
    raw_sentences = [s.strip() for s in re.split(r'[.!?]+', content) if s.strip()]
    sentence_lengths = [len(re.findall(r"\b\w+\b", s)) for s in raw_sentences if len(re.findall(r"\b\w+\b", s)) > 0]
    
    avg_sentence_len = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    variance = sum((x - avg_sentence_len) ** 2 for x in sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    std_dev_sentence_len = math.sqrt(variance)

    print("=" * 68)
    print(" 📖 NOVEL CHAPTER PACING & MULTILINGUAL HUMANIZER REPORT")
    print("=" * 68)
    print(f"File                 : {file_path}")
    print(f"Total Words          : {total_words:,} words")
    print(f"Reading Time (Print) : ~{print_time_mins:.1f} minutes (@ 260 WPM)")
    print(f"Reading Time (Mobile): ~{mobile_time_mins:.1f} minutes (@ 220 WPM)")
    print(f"Dialogue Words       : {dialogue_words:,} words ({dialogue_ratio:.1f}%)")
    print(f"Sentence Rhythms     : Avg {avg_sentence_len:.1f} words | StdDev {std_dev_sentence_len:.1f} words")
    
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

    # Rhythm Variation (Metronome Check)
    print("\n🎵 Sentence Rhythm & Metronome Check:")
    if std_dev_sentence_len < 6.0 and len(sentence_lengths) > 10:
        print(f"  ⚠️ Low Rhythm Variation (StdDev: {std_dev_sentence_len:.1f} < 6.0). Sentences feel metronomic; mix short staccato bursts with long periodic sentences.")
    else:
        print(f"  ✅ Dynamic Rhythm Breathing (StdDev: {std_dev_sentence_len:.1f} >= 6.0). Healthy cadence variation.")

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
    print("\n🌐 Checking for AI-Translationese & Kalke:")
    trans_count = 0
    for pattern, advice in TRANSLATIONESE_SLOP:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            trans_count += len(matches)
            print(f"  🚨 Translationese / Slop ({len(matches)}x): '{pattern}' -> {advice}")

    # Humanizer tells (Nominalization, Connector bloat, Anticipatory negations)
    print("\n🧬 Checking for Humanizer AI Tells (Connector bloat, Nominalizations, Negations):")
    humanizer_issues = 0
    for pattern, advice in HUMANIZER_TELLS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            humanizer_issues += len(matches)
            print(f"  ⚡ AI Tell ({len(matches)}x): '{pattern}' -> {advice}")

    total_issues = slop_count + trans_count + humanizer_issues
    if total_issues == 0:
        print("  ✅ Pristine Human Prose! No banned AI-slop, thought verbs, translationese, or connector bloat detected.")
    else:
        print(f"\n⚠️ Total issues flagged: {total_issues}. Please revise following references/20_multilingual_humanizer_and_anti_ai_tells.md")
    print("=" * 68)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_pacing.py <path_to_chapter_markdown>")
        sys.exit(1)
    analyze_chapter(sys.argv[1])
