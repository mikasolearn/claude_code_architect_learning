# claude_code_architect_learning
a repo dedicated to honing ai agents orchestration skills to pass claude code architect exam
Proposed Architecture   
                    ┌──────────────────────────────┐
                    │   COORDINATOR (Claude Code)  │
                    │   Routes by intent + tracks  │
                    │   weakness across domains    │
                    └──────────────────────────────┘
                                  │
   ┌──────────┬──────────┬────────┼────────┬─────────────┬──────────┐
   ▼          ▼          ▼        ▼        ▼             ▼          ▼
┌──────┐ ┌────────┐ ┌────────┐ ┌──────┐ ┌────────┐ ┌──────────┐ ┌──────┐
│Exam  │ │Scenario│ │Question│ │Domain│ │Question│ │Evaluator/│ │Drill │
│Guide │ │Coach   │ │Bank    │ │Expert│ │Generator│ │Tutor    │ │Master│
└──────┘ └────────┘ └────────┘ └──────┘ └────────┘ └──────────┘ └──────┘

Agents

| Agent | Purpose | Why it matters for THIS exam |
| :-- | :-- | :-- |
| exam-guide | Answers exam logistics (passing score, format, domain weights) | Small but useful |
| scenario-coach | Walks you through each of the 6 scenarios as if you're the architect | Exam is scenario-framed; you need to think in scenarios |
| question-bank | Serves real-style questions filtered by domain + scenario | Core practice loop |
| domain-expert | Deep teaching on each Knowledge/Skill statement | Replaces generic "docs expert" — exam-specific |
| question-generator | Generates new questions matching official style (1 correct + 3 plausible distractors) | The exam guide explicitly says distractors are answers a partial-knowledge candidate would pick — the generator must master this |
| evaluator | Grades, explains why each distractor is wrong, logs by domain | Mirrors the official explanation style |
| drill-master | Runs timed scenario sets (4 scenarios, exam simulation) | Exam-day readiness |


cc-architect-prep/
├── .claude/
│   ├── agents/
│   │   ├── exam-guide.md
│   │   ├── scenario-coach.md
│   │   ├── question-bank.md
│   │   ├── domain-expert.md
│   │   ├── question-generator.md
│   │   ├── evaluator.md
│   │   └── drill-master.md
│   ├── commands/
│   │   ├── quiz.md           # /quiz <domain> <count>
│   │   ├── scenario.md       # /scenario <number>
│   │   ├── progress.md       # /progress
│   │   ├── weak-areas.md     # /weak-areas
│   │   └── mock-exam.md      # /mock-exam (simulates real conditions)
│   ├── skills/
│   │   └── generate-questions/
│   │       └── SKILL.md      # context: fork (verbose generation)
│   ├── rules/
│   │   └── question-quality.md  # paths: ["knowledge/questions/**"]
│   └── settings.json
├── knowledge/
│   ├── exam-blueprint/
│   │   ├── exam-guide.pdf           # the document you shared
│   │   └── domain-task-statements.json   # parsed for precise filtering
│   ├── scenarios/
│   │   ├── 01-customer-support.md
│   │   ├── 02-code-generation.md
│   │   ├── 03-multi-agent-research.md
│   │   ├── 04-developer-productivity.md
│   │   ├── 05-cicd.md
│   │   └── 06-data-extraction.md
│   ├── domains/
│   │   ├── d1-agentic-architecture/
│   │   │   ├── 1.1-agentic-loops.md
│   │   │   ├── 1.2-coordinator-subagent.md
│   │   │   ├── 1.3-subagent-config.md
│   │   │   ├── 1.4-multi-step-enforcement.md
│   │   │   ├── 1.5-hooks.md
│   │   │   ├── 1.6-task-decomposition.md
│   │   │   └── 1.7-session-state.md
│   │   ├── d2-tool-design-mcp/
│   │   ├── d3-claude-code-config/
│   │   ├── d4-prompt-engineering/
│   │   └── d5-context-reliability/
│   └── questions/
│       ├── seed/                    # 12 official sample questions
│       │   └── official-samples.json
│       ├── generated/               # questions you generate over time
│       └── mistakes/                # questions you got wrong (for SRS)
├── scripts/
│   ├── ingest_blueprint.py          # extracts task statements → JSON
│   ├── query_kb.py                  # simple knowledge query
│   └── stats.py                     # domain accuracy report
├── sessions/                        # JSONL logs per study session
├── mock-exams/                      # past mock exam results
└── CLAUDE.md
