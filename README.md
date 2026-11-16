# 🖋️ Universal Novel Writing Craft Engine (AI Agent Skill)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Validate Skill](https://github.com/Rangga11268/novel-writing-craft-skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/Rangga11268/novel-writing-craft-skill/actions)
[![AI Agent Ready](https://img.shields.io/badge/AI%20Agent-Universal-brightgreen.svg)]()
[![Compatible: Antigravity | Claude Code | Cursor](https://img.shields.io/badge/Compatible-Antigravity%20%7C%20Claude%20Code%20%7C%20Cursor-purple.svg)]()

A master-level fiction and novel writing craft engine designed for AI Agents (Google Antigravity, Claude Code, Cursor, ChatGPT). It elevates AI from generating generic prose into a rigorous, industry-grade **Story Architect** and **Developmental Editor**, integrating cinematic masterclasses, neuroscience of suspense, and literary discipline.

---

## 🌟 Repository Architecture (10 Deep Craft Modules)

```
novel-writing-craft-skill/
├── .github/workflows/
│   └── validate-skill.yml              # CI/CD validation for skill & scripts
├── references/                         # In-depth craft theory modules
│   ├── 01_narrative_architectures.md   # 3-Act, Save the Cat, 7-Point, Story Grid
│   ├── 02_character_psychology_and_arcs.md # The Wound, The Lie, Want vs Need
│   ├── 03_scene_and_sequel_mechanics.md    # Goal-Conflict-Disaster & Reaction
│   ├── 04_visceral_prose_and_sensory.md    # Somatic showing, Anti-Telling
│   ├── 05_dialogue_subtext_and_combat.md   # Iceberg theory & distinct voices
│   ├── 06_danmei_and_romance_tropes.md     # Huan Gong, Crematorium, Awakening
│   ├── 07_cinematic_storytelling_and_screenwriting.md # Truby 22 Steps, Harmon Circle, Hitchcock, Murch Rule of Six, Pixar
│   ├── 08_neuroscience_of_storytelling_and_suspense.md # Narrative Transportation, Curiosity Gap, Zeigarnik Effect
│   ├── 09_worldbuilding_and_magic_systems.md # Sanderson 3 Laws, Promise-Progress-Payoff, Hemingway Iceberg
│   └── 10_literary_mastery_and_prose_stylistics.md # Palahniuk Submerged "I", King Adverbs, Saunders Gas Station
├── templates/                          # Ready-to-use plotting cards
│   ├── character_dossier_template.md
│   ├── chapter_outline_template.md
│   ├── scene_beat_sheet_template.md
│   └── book_proposal_pitch_template.md
├── scripts/
│   └── check_pacing.py                 # Automated pacing & anti-slop diagnostic CLI
├── SKILL.md                            # Core universal skill entrypoint
├── CONTRIBUTING.md                     # Community contribution guidelines
├── LICENSE                             # MIT License
└── README.md
```

---

## 🚀 Installation & Usage

### 1. Google Antigravity
Clone or place the repository in your personal skills directory:
```bash
git clone https://github.com/Rangga11268/novel-writing-craft-skill.git ~/.gemini/config/skills/novel-writing-craft
```
Antigravity automatically discovers and loads the skill whenever you request novel plotting, worldbuilding, or chapter writing.

### 2. Claude Code
Place the skill inside your project's `.claude/skills/` directory:
```bash
mkdir -p .claude/skills
git clone https://github.com/Rangga11268/novel-writing-craft-skill.git .claude/skills/novel-writing-craft
```

### 3. Cursor / Windsurf / VS Code
Place the contents of `SKILL.md` inside your `.cursorrules` or `.cursor/rules/novel-writing-craft.mdc`.

---

## 🛠️ Built-in Diagnostics CLI

Run the automated pacing and anti-slop diagnostic on any chapter markdown file:
```bash
python scripts/check_pacing.py path/to/chapter.md
```
Output includes:
* Word count & dialogue-to-narrative ratio assessment
* Over-narration / white-room syndrome alerts
* Automatic detection of generic AI-slop telling patterns and thought verbs

---

## 📄 License
MIT License. Open-source and free for both personal and commercial fiction workflows.
