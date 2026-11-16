#!/usr/bin/env python3
"""
Pacing and Anti-Slop Diagnostic Checker for Novel Chapters.
Analyzes word count, dialogue ratio, and flags generic AI prose patterns.
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

def analyze_chapter(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    words = re.findall(r"\b\w+\b", content)
    total_words = len(words)
    
    # Dialogue detection (quoted text)
    dialogues = re.findall(r'["“](.*?)["”]', content)
    dialogue_words = sum(len(re.findall(r"\b\w+\b", d)) for d in dialogues)
    dialogue_ratio = (dialogue_words / total_words * 100) if total_words > 0 else 0

    print("=" * 50)
    print(" 📖 NOVEL CHAPTER DIAGNOSTIC REPORT")
    print("=" * 50)
    print(f"File              : {file_path}")
    print(f"Total Words       : {total_words:,}")
    print(f"Dialogue Words    : {dialogue_words:,} ({dialogue_ratio:.1f}%)")
    
    # Pacing evaluation
    if dialogue_ratio < 15:
        print("Pacing Assessment : ⚠️ Narrative heavy / Potential infodump risk.")
    elif dialogue_ratio > 65:
        print("Pacing Assessment : ⚠️ Dialogue heavy / White-room syndrome risk.")
    else:
        print("Pacing Assessment : ✅ Balanced narrative-to-dialogue ratio.")

    # Anti-slop checks
    print("\n🔍 Checking for Banned AI-Slop & Abstract Telling Patterns:")
    slop_count = 0
    for pattern in BANNED_TELL_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            slop_count += len(matches)
            print(f"  ❌ Found {len(matches)}x: '{pattern}'")

    if slop_count == 0:
        print("  ✅ Clean! No banned AI-slop patterns detected.")
    else:
        print(f"\n⚠️ Total issues flagged: {slop_count}. Please replace with visceral somatic reactions or action beats.")
    print("=" * 50)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_pacing.py <path_to_chapter_markdown>")
        sys.exit(1)
    analyze_chapter(sys.argv[1])
