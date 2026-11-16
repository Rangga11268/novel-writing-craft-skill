<div align="center">
  <img src="assets/logo.png" width="140" height="140" alt="Novel Writing Craft Logo" style="border-radius: 28px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);" />
  <h1>Novel Writing Craft Engine</h1>
  <p><b>The Universal Fiction Architecture, Cinematic Storytelling & Narrative Intelligence Engine for AI Agents</b></p>

  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="License: MIT" /></a>
    <a href="https://github.com/Rangga11268/novel-writing-craft-skill/actions"><img src="https://img.shields.io/badge/CI-Passing-success.svg?style=for-the-badge&logo=githubactions&logoColor=white" alt="CI Status" /></a>
    <a href="#-compatible-ai-agents"><img src="https://img.shields.io/badge/AI%20Agents-Antigravity%20%7C%20Claude%20%7C%20Cursor-purple.svg?style=for-the-badge" alt="Compatible Agents" /></a>
    <a href="#-the-10-deep-craft-modules"><img src="https://img.shields.io/badge/Modules-10%20Deep%20Guides-amber.svg?style=for-the-badge" alt="10 Modules" /></a>
    <a href="#-zero-ai-slop-creed"><img src="https://img.shields.io/badge/Prose%20Quality-Anti--AI--Slop-red.svg?style=for-the-badge" alt="Anti Slop" /></a>
  </p>
</div>

---

## 🌟 Why This Exists

Most AI models write fiction that reads like generic, melodramatic summaries: characters *"feel intensely sad"*, villains *"sneer with malice"*, and chapters conclude with unprompted philosophical morality lessons. 

The **Novel Writing Craft Engine** transforms AI agents (Google Antigravity, Claude Code, Cursor, ChatGPT) from passive conversationalists into a relentless **Master Story Architect** and **Senior Developmental Editor**. It bridges classic screenwriting, literary masterclasses, cognitive neuroscience, and global fiction tropes into an executable agent skill.

| Default AI Generation ❌ | Engine-Crafted Fiction ✅ |
|---|---|
| **Abstract Telling:** *"He was terrified of the dark hallway."* | **Somatic Showing:** *"His sneakers squeaked on wet linoleum. His pulse hammered in his teeth while his thumb pressed the pocketknife’s brass rivets."* |
| **Melodramatic Tags:** *"he hissed", "she sneered"* | **Action Beats & Subtext:** Grounded physical movement; dialogue as tactical combat. |
| **Head-Hopping:** Floating POV that betrays reader intimacy | **Strict POV Lock:** Camera welded behind the protagonist’s retinas. |
| **Moralizing Endings:** *"And that night, he learned that love was..."* | **Zeigarnik Open Loops:** Ending on micro-dilemmas and ticking clocks that force the next page turn. |
| **Flat Protagonists:** Adjective lists (*kind, smart, brave*) | **3D Psychological Triad:** The Wound $\rightarrow$ The Lie $\rightarrow$ The Want vs The Need. |

---

## 🏛️ Architecture Overview

The repository is built around **Progressive Disclosure** (Anthropic & Antigravity standard), keeping the primary agent instruction (`SKILL.md`) razor-sharp while providing 10 specialized domain modules on demand:

```
novel-writing-craft-skill/
├── assets/
│   ├── logo.svg                        # Master vector brand mark
│   └── logo.png                        # Rendered 512px high-res asset
├── .github/workflows/
│   └── validate-skill.yml              # Automated CI/CD diagnostic tester
├── references/                         # The 10 In-Depth Craft Modules
│   ├── 01_narrative_architectures.md   # 3-Act, Save the Cat 15 Beats, 7-Point, Story Grid
│   ├── 02_character_psychology_and_arcs.md # The Wound, The Lie Believed, Want vs Need, 4 Arcs
│   ├── 03_scene_and_sequel_mechanics.md    # Goal-Conflict-Disaster & Reaction-Dilemma-Decision
│   ├── 04_visceral_prose_and_sensory.md    # Somatic responses, 5-Sense calibration, Anti-Telling
│   ├── 05_dialogue_subtext_and_combat.md   # Verbal combat, Iceberg Theory, Linguistic Fingerprints
│   ├── 06_danmei_and_romance_tropes.md     # Huan Gong (换攻), Crematorium (火葬场), Awakening
│   ├── 07_cinematic_storytelling_and_screenwriting.md # Truby 22 Steps, Harmon Circle, Hitchcock Suspense, Murch Rule of Six, Pixar
│   ├── 08_neuroscience_of_storytelling_and_suspense.md # Narrative Transportation, Curiosity Gap, Zeigarnik Effect
│   ├── 09_worldbuilding_and_magic_systems.md # Sanderson 3 Laws, Promise-Progress-Payoff, Hemingway Iceberg
│   └── 10_literary_mastery_and_prose_stylistics.md # Palahniuk Submerged "I", King Adverbs, Saunders Gas Station
├── templates/                          # Production-Ready Plotting Cards
│   ├── character_dossier_template.md   # 3D character psychological spec
│   ├── chapter_outline_template.md     # Scene & Sequel chapter blueprint
│   ├── scene_beat_sheet_template.md    # 5-beat micro-scene rhythm
│   └── book_proposal_pitch_template.md # Logline, comps & premise pitch
├── scripts/
│   └── check_pacing.py                 # Automated CLI for word counts, dialogue ratios & slop detection
├── SKILL.md                            # Universal Agent Entrypoint
├── CONTRIBUTING.md                     # Community contribution guidelines
├── LICENSE                             # MIT Open Source
└── README.md
```

---

## 🎯 Operating Modes

When instructing your AI agent, invoke specific modes for targeted execution:

```mermaid
flowchart LR
    A[User Request] --> B{Choose Mode}
    B -->|Plot Design| C[architect]
    B -->|Character Psychology| D[profiler]
    B -->|Prose Execution| E[drafter]
    B -->|Diagnostic Audit| F[editor]

    C --> G[plot_outline.md]
    D --> H[character_dossier.md]
    E --> I[Chapter_XX.md]
    F --> J[check_pacing.py Report]
```

* **`architect`:** Calibrates acts, milestones, pinch points, and dramatic questions using Three-Act, Truby 22 Steps, or Save the Cat.
* **`profiler`:** Excavates the character's Ghost/Wound, defines The Lie they live by, maps their Want vs Need, and establishes distinct vocal cadences.
* **`drafter`:** Writes immersive prose via Swain’s Scene & Sequel cycle, Chuck Palahniuk’s submerged sensory anchors, and multi-sensory palettes.
* **`editor`:** Audits chapters using Walter Murch’s Rule of Six, tests the Zeigarnik open loop at the chapter cut, and verifies the life value shift.

---

## 📚 The 10 Deep Craft Modules

1. **[01. Narrative Architectures](references/01_narrative_architectures.md):** Detailed breakdowns of Classic Three-Act (Syd Field/Weiland), Save the Cat! 15 Beats (Blake Snyder), Dan Wells 7-Point, and Shawn Coyne’s Story Grid 5 Commandments.
2. **[02. 3D Character Psychology](references/02_character_psychology_and_arcs.md):** The core triad (Wound $\rightarrow$ Lie $\rightarrow$ Want vs Need), Positive Change Arcs, Flat Arcs, Disillusionment Arcs, and Corruption/Tragedy Arcs.
3. **[03. Scene & Sequel Mechanics](references/03_scene_and_sequel_mechanics.md):** The rhythmic engine of fiction: Goal $\rightarrow$ Conflict $\rightarrow$ Disaster (No / Yes, BUT / No, AND FURTHERMORE) alternating with Reaction $\rightarrow$ Dilemma $\rightarrow$ Decision.
4. **[04. Visceral Prose & Sensory Execution](references/04_visceral_prose_and_sensory.md):** Somatic autonomic responses (involuntary biology), behavioral tells, objective correlatives, and 5-sense calibration.
5. **[05. Dialogue Subtext & Verbal Combat](references/05_dialogue_subtext_and_combat.md):** Dialogue as action verbs, Hemingway’s Iceberg Theory (the unsaid), and eliminating theatrical tags in favor of action beats.
6. **[06. Danmei & Romance Tropes](references/06_danmei_and_romance_tropes.md):** Deep mechanics of *Huàn Gōng* (换攻 - ML Replacement), *Failed Crematorium* (火葬场), *Heart-Death* (心死), and person-specific *Straight-to-Awakened* dynamics.
7. **[07. Cinematic Storytelling & Screenwriting](references/07_cinematic_storytelling_and_screenwriting.md):** John Truby’s 22 Building Blocks, Dan Harmon’s 8-step Story Circle, Alfred Hitchcock on Suspense vs. Surprise, Walter Murch’s Rule of Six, and Pixar’s 22 Rules.
8. **[08. Cognitive Neuroscience of Suspense](references/08_neuroscience_of_storytelling_and_suspense.md):** Narrative Transportation Theory (Green & Brock), Loewenstein’s Curiosity Gap, Dopamine anticipation curves, and weaponizing Zeigarnik open loops.
9. **[09. Worldbuilding & Magic Systems](references/09_worldbuilding_and_magic_systems.md):** Brandon Sanderson’s Three Laws of Magic/Systems, Promise-Progress-Payoff, and Hemingway's 90% submerged Iceberg worldbuilding.
10. **[10. Literary Mastery & Voice Stylistics](references/10_literary_mastery_and_prose_stylistics.md):** Chuck Palahniuk’s ban on Thought Verbs, Stephen King’s adverb elimination, George Saunders’ Gas Station sentence momentum, and Ursula K. Le Guin’s cadence.

---

## 🚀 Installation & Quickstart

### 1. Google Antigravity
Clone directly into your Antigravity skills configuration:
```bash
git clone https://github.com/Rangga11268/novel-writing-craft-skill.git ~/.gemini/config/skills/novel-writing-craft
```

### 2. Claude Code
Install into your project's `.claude/skills/` directory:
```bash
mkdir -p .claude/skills
git clone https://github.com/Rangga11268/novel-writing-craft-skill.git .claude/skills/novel-writing-craft
```

### 3. Cursor / Windsurf / VS Code
Copy `SKILL.md` into your `.cursorrules` or `.cursor/rules/novel-writing-craft.mdc`.

---

## 🛠️ Built-in Diagnostics CLI

The repository includes a Python CLI to analyze your chapter drafts:

```bash
python scripts/check_pacing.py path/to/Chapter_01.md
```

**Diagnostic Output:**
```
==================================================
 📖 NOVEL CHAPTER DIAGNOSTIC REPORT
==================================================
File              : Chapter_01.md
Total Words       : 3,420
Dialogue Words    : 1,120 (32.7%)
Pacing Assessment : ✅ Balanced narrative-to-dialogue ratio.

🔍 Checking for Banned AI-Slop & Abstract Telling Patterns:
  ✅ Clean! No banned AI-slop patterns detected.
==================================================
```

---

## 🤝 Contributing

Contributions from fiction writers, dramaturgs, and AI engineers are warmly welcomed! Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) for pull request guidelines, style conventions, and testing requirements.

---

## 📄 License

Distributed under the **MIT License**. Free for personal, commercial, and collaborative creative writing projects.
