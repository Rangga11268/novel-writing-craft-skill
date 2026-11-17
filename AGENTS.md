# 🤖 AGENTS.md: Autonomous Multi-Agent Fiction Studio Architecture

> *A production-grade multi-agent collaboration specification for long-form fiction, serial novels, and screenplays. Designed for Google Antigravity, Claude Code, OpenAI Swarms, Cursor, and autonomous writing workflows.*

---

## 1. STUDIO PHILOSOPHY: THE DUAL-STATE PIPELINE

Writing a 150,000-word novel with AI fails when a single model tries to outline, hold character state, draft prose, check continuity, and polish grammar in one turn. Inevitably, the model suffers from **Context Drift**, forgets character injuries from 5 chapters ago, rushes climaxes, and defaults to generic "AI-slop".

The **Novel Writing Craft Studio** solves this by separating concerns into a **Dual-State Multi-Agent Assembly Line**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        DUAL-STATE CONTEXT ISOLATION ARCHITECTURE                       │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ PERMANENT CANON (READ-ONLY)                                                            │
│ • Story Bible, World Rules, Linguistic Fingerprints, Fixed Character Dossiers          │
│ • BANNED from being rewritten during scene generation to prevent canon drift.          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ TRANSIENT CHAPTER STATE (VERSIONED)                                                    │
│ • Immediate physical inventory, carried wounds/injuries, active emotional baseline,    │
│   current secret/knowledge state, unresolved immediate tension (cliffhanger).          │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. THE 5 SPECIALIZED AGENT ROLES

```
       ┌───────────────────────────────┐
       │   1. STORY ARCHITECT          │ (Outlining & Beat Calibration)
       └──────────────┬────────────────┘
                      ▼
       ┌───────────────────────────────┐
       │   2. SCENE DRAFTER            │ (Sensory Immersion & Strict POV Lock)
       └──────────────┬────────────────┘
                      ▼
       ┌───────────────────────────────┐
       │   3. CONTINUITY AUDITOR       │ (Logic, Knowledge States & Timeline)
       └──────────────┬────────────────┘
                      ▼
       ┌───────────────────────────────┐
       │   4. HUMANIZER & LINE EDITOR  │ (Anti-Slop, Rhythm & Translationese)
       └──────────────┬────────────────┘
                      ▼
       ┌───────────────────────────────┐
       │   5. SIMULATED BETA READER    │ (Emotional Heatmap & Drop-Off Test)
       └───────────────────────────────┘
```

### Agent 1: Story Architect (`architect`)
* **Core Mandate:** Designs macro-structure, chapter budgets, and micro-beats before any prose is written.
* **Input:** Creative Intent Brief, Story Bible, and preceding chapter state.
* **Output:** `chapter_outline_template.md` (Goal, Conflict, Disaster, Life Value Shift $+ \rightarrow -$ or $- \rightarrow +$).
* **Guardrail:** Never writes full narrative prose. Stops after beat sheet approval.

### Agent 2: Scene Drafter (`drafter`)
* **Core Mandate:** Transforms the beat sheet into visceral, cinematic prose with strict POV discipline.
* **Rules:**
  * **Palahniuk Submerged "I":** Purge thought verbs (*felt, knew, thought, realized*).
  * **Sensory Calibration:** Engage at least 3 distinct senses (tactile, thermal, olfactory, auditory, visual).
  * **Strict POV Lock:** Camera welded behind the POV character's retinas; zero head-hopping.
  * **Sweet Spot Length:** 2,000 – 3,500 words per chapter (~10–14 min mobile reading window).

### Agent 3: Continuity Auditor (`continuity-auditor`)
* **Core Mandate:** Verifies that the draft violates zero physical, spatial, or epistemic laws.
* **Checklist:**
  * Did any character use information they haven't learned in-story yet (*Epistemic Check*)?
  * Are travel times, physical wounds, and carried items consistent with previous chapters?
  * Does every plot movement follow the *"Therefore/But"* causality rule (zero Idiot Plot)?
* **Action:** Rejects the draft back to `drafter` if a causal fracture or knowledge leak is detected.

### Agent 4: Multilingual Humanizer & Line Editor (`humanizer`)
* **Core Mandate:** Eradicates all traces of robotic machine cadence and awkward translationese.
* **Checklist:**
  * Purges 25+ specific Indonesian and English AI kalke (*"membuat akal sehat"*, *"menemukan dirinya"*, *"tapestri takdir"*, *"ruangan jatuh hening"*).
  * Enforces **Asymmetric Sentence Breathing** (StdDev $\ge 6.0$ words; mixes 3-word punchy staccatos with 28-word periodic clauses).
  * Eliminates nominalization light verbs (*melakukan pengamatan $\rightarrow$ mengamati*) and anticipatory negations (*"bukan berarti"*).
  * Conducts the **Tagless Blind Test** on dialogue.

### Agent 5: Simulated Beta Reader Panel (`beta-reader`)
* **Core Mandate:** Simulates 3 distinct human reader archetypes to score psychological engagement and drop-off risks:
  1. **The Casual Binge Reader:** Flags pacing drags, mobile cognitive fatigue, and boring exposition.
  2. **The Genre Purist / Hardcore Fan:** Validates genre promises (HEA in Romance, Fair Play in Mystery, Quantified Progress in Fantasy).
  3. **The Empathy & Emotional Reader:** Measures emotional resonance, cringe threshold, and cathartic tearjerker moments.
* **Output:** Generates a **Chapter Emotional Heatmap** ($0–100$ Tension Score) and verdict: `[PASS TO PUBLISH]` or `[REVISION RECOMMENDED]`.

---

## 3. DETERMINISTIC COMMAND-LINE VERIFICATION

Automate quality gates using the included Python CLI tools:

```bash
# 1. Check sentence rhythm, reading telemetry, dialogue balance, and AI tells
python scripts/check_pacing.py path/to/chapter.md

# 2. Audit POV consistency, dialogue tag health, and Chekhov gun setups/payoffs
python scripts/audit_continuity.py path/to/chapter.md
```

---

## 4. MULTI-AGENT INVOCATION GUIDE

When using multi-agent platforms (Antigravity Swarm, Claude Code subagents, OpenAI Assistant API):
1. Spawn the **Drafter** in an isolated conversation with read-only access to `references/` and the active chapter beat sheet.
2. Pass the raw draft to the **Continuity Auditor** along with `templates/story_bible_and_continuity_ledger.md`.
3. Pass the audited draft to the **Humanizer** for acoustic polishing.
4. Conclude with the **Beta Reader Simulator** for emotional scorecards.
