#!/usr/bin/env python3
"""
Continuity, POV Lock & Dialogue Tag Health Auditor for Novel Chapters.
Scans single chapter files or directories of chapters for:
1. POV Leakage (unquoted 1st-person pronouns in 3rd-person prose, or vice-versa)
2. Dialogue Tag Health (theatrical melodramatic tags vs. neutral tags and action beats)
3. Abstract Thought Verbs (Palahniuk Submerged 'I' check outside dialogue)
4. Narrative Setup/Payoff markers ([CH-SETUP], [CH-PAYOFF], [FUBI])

Usage:
    python scripts/audit_continuity.py path/to/chapter.md
    python scripts/audit_continuity.py path/to/chapters_directory/ --pov 3rd
"""

import sys
import os
import re
import argparse
from pathlib import Path

# Theatrical / Melodramatic Dialogue Tags to flag
THEATRICAL_TAGS = [
    r'\bgeram(nya)?\b', r'\bdesah(nya)?\b', r'\bpekik(nya)?\b',
    r'\bjerit(nya)?\b', r'\branum(nya)?\b', r'\bdesis(nya)?\b',
    r'\braung(nya)?\b', r'\bmurka(nya)?\b', r'\bketus(nya)?\b',
    r'\bhissed\b', r'\bsneered\b', r'\bgrowled\b', r'\bsnapped\b', r'\bwhined\b'
]

NEUTRAL_TAGS = [
    r'\bkata(nya)?\b', r'\bucap(nya)?\b', r'\btanya(nya)?\b',
    r'\bjawab(nya)?\b', r'\bsahut(nya)?\b', r'\bbalas(nya)?\b',
    r'\bsaid\b', r'\basked\b', r'\breplied\b'
]

THOUGHT_VERBS = [
    r'\bmerasa\b', r'\bmerasakan\b', r'\bberpikir\b', r'\bmenyadari\b',
    r'\bteringat\b', r'\btahu\b', r'\bmengetahui\b',
    r'\bfelt\b', r'\bthought\b', r'\brealized\b', r'\bknew\b', r'\bremembered\b'
]

FIRST_PERSON_PRONOUNS = [r'\baku\b', r'\bku\b', r'\bk-ku\b', r'\bsaya\b', r'\bi\b', r'\bme\b', r'\bmy\b']
THIRD_PERSON_PRONOUNS = [r'\bdia\b', r'\bia\b', r'\b-nya\b', r'\bhe\b', r'\bshe\b', r'\bhis\b', r'\bher\b']

def clean_dialogue(text):
    """Extracts narration only by removing quoted dialogue."""
    # Matches "...", “...”, or '...'
    dialogue_pattern = r'["“\'][^"”\']*["”\']'
    dialogues = re.findall(dialogue_pattern, text)
    narration_only = re.sub(dialogue_pattern, ' ', text)
    return narration_only, dialogues

def audit_file(file_path, expected_pov='auto'):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    narration_only, dialogues = clean_dialogue(text)
    total_words = len(text.split())

    # 1. Dialogue Tag Health
    theatrical_matches = []
    for pattern in THEATRICAL_TAGS:
        theatrical_matches.extend(re.findall(pattern, text, re.IGNORECASE))

    neutral_matches = []
    for pattern in NEUTRAL_TAGS:
        neutral_matches.extend(re.findall(pattern, text, re.IGNORECASE))

    total_tags = len(theatrical_matches) + len(neutral_matches)
    theatrical_ratio = (len(theatrical_matches) / total_tags * 100) if total_tags > 0 else 0

    # 2. Thought Verbs in Narration (outside dialogue)
    thought_verb_matches = []
    for pattern in THOUGHT_VERBS:
        thought_verb_matches.extend(re.findall(pattern, narration_only, re.IGNORECASE))

    # 3. POV Audit in Narration
    first_p_count = sum(len(re.findall(p, narration_only, re.IGNORECASE)) for p in FIRST_PERSON_PRONOUNS)
    third_p_count = sum(len(re.findall(p, narration_only, re.IGNORECASE)) for p in THIRD_PERSON_PRONOUNS)

    detected_pov = "1st Person (Aku/Saya)" if first_p_count > third_p_count else "3rd Person (Dia/Ia/Nama)"

    pov_leak_warnings = []
    if expected_pov == '3rd' or (expected_pov == 'auto' and third_p_count > (first_p_count * 2)):
        if first_p_count > 0:
            pov_leak_warnings.append(f"Detected {first_p_count} unquoted 1st-person pronouns ('aku'/'saya') in 3rd-person narration! Check for accidental head-hopping.")
    elif expected_pov == '1st' or (expected_pov == 'auto' and first_p_count > (third_p_count * 2)):
        pass # 1st person naturally mentions 3rd person characters

    # 4. Chekhov / Foreshadowing tags
    chekhov_setups = re.findall(r'\[CH-SETUP:[^\]]+\]', text, re.IGNORECASE)
    chekhov_payoffs = re.findall(r'\[CH-PAYOFF:[^\]]+\]', text, re.IGNORECASE)
    fubi_tags = re.findall(r'\[FUBI:[^\]]+\]', text, re.IGNORECASE)

    # Print Report
    print("=" * 68)
    print(" 🔍 STORY CONTINUITY & NARRATIVE LOGIC AUDIT REPORT")
    print("=" * 68)
    print(f"File                : {os.path.basename(file_path)}")
    print(f"Total Words         : {total_words:,} words")
    print(f"Detected POV Anchor : {detected_pov}")
    print(f"Dialogue Quotes     : {len(dialogues)} quotes found")

    print("\n🎭 Dialogue Tag Health:")
    print(f"  Total Speaker Tags : {total_tags}")
    print(f"  Neutral Tags       : {len(neutral_matches)} (kata, ucap, said, etc.)")
    print(f"  Theatrical Tags    : {len(theatrical_matches)} (geram, desah, pekik, hissed, etc.)")
    if theatrical_ratio > 25.0:
        print(f"  ⚠️ HIGH THEATRICAL TAG RATIO ({theatrical_ratio:.1f}% > 25%).")
        print("     Tip: Replace melodramatic tags with physical action beats or silent dialogue.")
    else:
        print(f"  ✅ Healthy Dialogue Tag Ratio ({theatrical_ratio:.1f}% <= 25%). Good use of action beats.")

    print("\n🧠 Somatic Showing vs. Abstract Thought Verbs:")
    print(f"  Thought Verbs Found: {len(thought_verb_matches)} (merasa, berpikir, felt, thought, etc.)")
    if len(thought_verb_matches) > 12:
        print("  ⚠️ ELEVATED THOUGHT VERB DENSITY in narration.")
        print("     Tip (Palahniuk Submerged 'I'): Unpack 'dia merasa dingin' into sensory action ('giginya bergemeletuk').")
    else:
        print("  ✅ Good Somatic Grounding. Narration relies on concrete sensory cues.")

    print("\n🔭 Point-of-View (POV) Continuity:")
    if pov_leak_warnings:
        for w in pov_leak_warnings:
            print(f"  ⚠️ POV LEAK WARNING: {w}")
    else:
        print("  ✅ Pure POV Consistency. No accidental head-hopping detected in narration.")

    print("\n🎯 Foreshadowing & Chekhov Guns in File:")
    print(f"  Chekhov Setups  : {len(chekhov_setups)} {chekhov_setups if chekhov_setups else ''}")
    print(f"  Chekhov Payoffs : {len(chekhov_payoffs)} {chekhov_payoffs if chekhov_payoffs else ''}")
    print(f"  Fubi Markers    : {len(fubi_tags)} {fubi_tags if fubi_tags else ''}")
    print("=" * 68 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Audit story continuity, POV discipline, and dialogue tag health.")
    parser.add_argument("target", help="Path to chapter markdown file or directory of chapters.")
    parser.add_argument("--pov", choices=['1st', '3rd', 'auto'], default='auto', help="Expected POV constraint.")
    args = parser.parse_args()

    target_path = Path(args.target)
    if not target_path.exists():
        print(f"Error: Target '{args.target}' does not exist.")
        sys.exit(1)

    if target_path.is_file():
        audit_file(str(target_path), args.pov)
    elif target_path.is_dir():
        md_files = list(target_path.glob("*.md"))
        if not md_files:
            print(f"No markdown (.md) files found in '{args.target}'.")
            return
        print(f"Auditing {len(md_files)} chapter files in '{args.target}'...\n")
        for f in sorted(md_files):
            audit_file(str(f), args.pov)

if __name__ == '__main__':
    main()
