Title: Common workflows - Claude Code Docs

URL Source: https://docs.anthropic.com/en/docs/claude-code/common-workflows

Markdown Content:
> ## Documentation Index
> 
> 
> Fetch the complete documentation index at: [https://code.claude.com/docs/llms.txt](https://code.claude.com/docs/llms.txt)
> 
> 
> Use this file to discover all available pages before exploring further.

This page covers practical workflows for everyday development: exploring unfamiliar code, debugging, refactoring, writing tests, creating PRs, and managing sessions. Each section includes example prompts you can adapt to your own projects. For higher-level patterns and tips, see [Best practices](https://code.claude.com/docs/en/best-practices).

## Understand new codebases

### Get a quick codebase overview

Suppose you’ve just joined a new project and need to understand its structure quickly.

1

2

3

4

### Find relevant code

Suppose you need to locate code related to a specific feature or functionality.

1

2

3

* * *

## Fix bugs efficiently

Suppose you’ve encountered an error message and need to find and fix its source.

1

2

3

* * *

## Refactor code

Suppose you need to update old code to use modern patterns and practices.

1

2

3

4

* * *

## Use specialized subagents

Suppose you want to use specialized AI subagents to handle specific tasks more effectively.

1

2

3

4

* * *

## Use Plan Mode for safe code analysis

Plan Mode instructs Claude to create a plan by analyzing the codebase with read-only operations, perfect for exploring codebases, planning complex changes, or reviewing code safely. In Plan Mode, Claude uses [`AskUserQuestion`](https://code.claude.com/docs/en/tools-reference) to gather requirements and clarify your goals before proposing a plan.

### When to use Plan Mode

*   **Multi-step implementation**: When your feature requires making edits to many files
*   **Code exploration**: When you want to research the codebase thoroughly before changing anything
*   **Interactive development**: When you want to iterate on the direction with Claude

### How to use Plan Mode

**Turn on Plan Mode during a session**You can switch into Plan Mode during a session using **Shift+Tab** to cycle through permission modes.If you are in Normal Mode, **Shift+Tab** first switches into Auto-Accept Mode, indicated by `⏵⏵ accept edits on` at the bottom of the terminal. A subsequent **Shift+Tab** will switch into Plan Mode, indicated by `⏸ plan mode on`.**Start a new session in Plan Mode**To start a new session in Plan Mode, use the `--permission-mode plan` flag:

```
claude --permission-mode plan
```

**Run “headless” queries in Plan Mode**You can also run a query in Plan Mode directly with `-p` (that is, in [“headless mode”](https://code.claude.com/docs/en/headless)):

```
claude --permission-mode plan -p "Analyze the authentication system and suggest improvements"
```

### Example: Planning a complex refactor

```
claude --permission-mode plan
```

```
I need to refactor our authentication system to use OAuth2. Create a detailed migration plan.
```

Claude analyzes the current implementation and create a comprehensive plan. Refine with follow-ups:

```
What about backward compatibility?
```

```
How should we handle database migration?
```

When you accept a plan, Claude automatically names the session from the plan content. The name appears on the prompt bar and in the session picker. If you’ve already set a name with `--name` or `/rename`, accepting a plan won’t overwrite it.

### Configure Plan Mode as default

```
// .claude/settings.json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

See [settings documentation](https://code.claude.com/docs/en/settings#available-settings) for more configuration options.

* * *

## Work with tests

Suppose you need to add tests for uncovered code.

1

2

3

4

Claude can generate tests that follow your project’s existing patterns and conventions. When asking for tests, be specific about what behavior you want to verify. Claude examines your existing test files to match the style, frameworks, and assertion patterns already in use.For comprehensive coverage, ask Claude to identify edge cases you might have missed. Claude can analyze your code paths and suggest tests for error conditions, boundary values, and unexpected inputs that are easy to overlook.

* * *

## Create pull requests

You can create pull requests by asking Claude directly (“create a pr for my changes”), or guide Claude through it step-by-step:

1

2

3

When you create a PR using `gh pr create`, the session is automatically linked to that PR. To return to it later, run `claude --from-pr <number>` or paste the PR URL into the [`/resume` picker](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-the-session-picker) search.

## Handle documentation

Suppose you need to add or update documentation for your code.

1

2

3

4

* * *

## Work in notes and non-code folders

Claude Code works in any directory. Run it inside a notes vault, a documentation folder, or any collection of markdown files to search, edit, and reorganize content the same way you would code.The `.claude/` directory and `CLAUDE.md` sit alongside other tools’ config directories without conflict. Claude reads files fresh on each tool call, so it sees edits you make in another application the next time it reads that file.

* * *

## Work with images

Suppose you need to work with images in your codebase, and you want Claude’s help analyzing image content.

1

2

3

4

* * *

## Reference files and directories

Use @ to quickly include files or directories without waiting for Claude to read them.

1

2

3

* * *

## Use extended thinking (thinking mode)

[Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) is enabled by default, giving Claude space to reason through complex problems step-by-step before responding. This reasoning is visible in verbose mode, which you can toggle on with `Ctrl+O`. During extended thinking, the spinner shows inline progress hints such as “still thinking” and “almost done thinking” to indicate Claude is actively working.Additionally, [models that support effort](https://code.claude.com/docs/en/model-config#adjust-effort-level) use adaptive reasoning: instead of a fixed thinking token budget, the model dynamically decides whether and how much to think based on your effort level setting and the task at hand. Adaptive reasoning lets Claude respond faster to routine prompts and reserve deeper thinking for steps that benefit from it.Extended thinking is particularly valuable for complex architectural decisions, challenging bugs, multi-step implementation planning, and evaluating tradeoffs between different approaches.

### Configure thinking mode

Thinking is enabled by default, but you can adjust or disable it.

| Scope | How to configure | Details |
| --- | --- | --- |
| **Effort level** | Run `/effort`, adjust in `/model`, or set [`CLAUDE_CODE_EFFORT_LEVEL`](https://code.claude.com/docs/en/env-vars) | Control thinking depth on [supported models](https://code.claude.com/docs/en/model-config#adjust-effort-level) |
| **`ultrathink` keyword** | Include “ultrathink” anywhere in your prompt | Adds an in-context instruction telling the model to reason more on that turn. Does not change the effort level itself; see [Adjust effort level](https://code.claude.com/docs/en/model-config#adjust-effort-level) for that |
| **Toggle shortcut** | Press `Option+T` (macOS) or `Alt+T` (Windows/Linux) | Toggle thinking on/off for the current session (all models). May require [terminal configuration](https://code.claude.com/docs/en/terminal-config) to enable Option key shortcuts |
| **Global default** | Use `/config` to toggle thinking mode | Sets your default across all projects (all models). Saved as `alwaysThinkingEnabled` in `~/.claude/settings.json` |
| **Limit token budget** | Set [`MAX_THINKING_TOKENS`](https://code.claude.com/docs/en/env-vars) environment variable | Limit the thinking budget to a specific number of tokens. On models with adaptive reasoning, only `0` applies unless adaptive reasoning is disabled. Example: `export MAX_THINKING_TOKENS=10000` |

To view Claude’s thinking process, press `Ctrl+O` to toggle verbose mode and see the internal reasoning displayed as gray italic text.

### How extended thinking works

Extended thinking controls how much internal reasoning Claude performs before responding. More thinking provides more space to explore solutions, analyze edge cases, and self-correct mistakes.On [models that support effort](https://code.claude.com/docs/en/model-config#adjust-effort-level), thinking uses adaptive reasoning: the model dynamically allocates thinking tokens based on the effort level you select. This is the recommended way to tune the tradeoff between speed and reasoning depth. If you want Claude to think more or less often than your effort level would otherwise produce, you can also say so directly in your prompt or in `CLAUDE.md`.With older models, thinking uses a fixed token budget drawn from your output allocation. The budget varies by model; see [`MAX_THINKING_TOKENS`](https://code.claude.com/docs/en/env-vars) for per-model ceilings. You can limit the budget with that environment variable, or disable thinking entirely via `/config` or the `Option+T`/`Alt+T` toggle.On models with adaptive reasoning, `MAX_THINKING_TOKENS` only applies when set to `0` to disable thinking, or when `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` reverts the model to the fixed budget. `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` applies to Opus 4.6 and Sonnet 4.6 only. Opus 4.7 always uses adaptive reasoning and does not support a fixed thinking budget. See [environment variables](https://code.claude.com/docs/en/env-vars).

* * *

## Resume previous conversations

When starting Claude Code, you can resume a previous session:

*   `claude --continue` continues the most recent conversation in the current directory
*   `claude --resume` opens a conversation picker or resumes by name
*   `claude --from-pr 123` resumes sessions linked to a specific pull request

From inside an active session, use `/resume` to switch to a different conversation.When the selected session is old and large enough that re-reading it would consume a substantial share of your usage limits, `--resume`, `--continue`, and `/resume` offer to resume from a summary instead of loading the full transcript. This prompt is not available on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry.Sessions are stored per project directory. By default, the `/resume` picker shows interactive sessions from the current worktree, with keyboard shortcuts to widen the list to other worktrees or projects, search, preview, and rename. Sessions started elsewhere that added the current directory with `/add-dir` are also included by default. See [Use the session picker](https://docs.anthropic.com/en/docs/claude-code/common-workflows#use-the-session-picker) below for the full shortcut reference.When you select a session from another worktree of the same repository, Claude Code resumes it directly without requiring you to switch directories first. Selecting a session from an unrelated project copies a `cd` and resume command to your clipboard instead.Resuming by name resolves across the current repository and its worktrees. Both `claude --resume <name>` and `/resume <name>` look for an exact match and resume it directly, even if the session lives in a different worktree.When the name is ambiguous, `claude --resume <name>` opens the picker with the name pre-filled as a search term. `/resume <name>` from inside a session reports an error instead, so run `/resume` with no argument to open the picker and choose.Sessions created by `claude -p` or SDK invocations do not appear in the picker, but you can still resume one by passing its session ID directly to `claude --resume <session-id>`.

### Name your sessions

Give sessions descriptive names to find them later. This is a best practice when working on multiple tasks or features.

1

2

### Use the session picker

The `/resume` command (or `claude --resume` without arguments) opens an interactive session picker with these features:**Keyboard shortcuts in the picker:**

| Shortcut | Action |
| --- | --- |
| `↑` / `↓` | Navigate between sessions |
| `→` / `←` | Expand or collapse grouped sessions |
| `Enter` | Select and resume the highlighted session |
| `Space` | Preview the session content. `Ctrl+V` also works on terminals that do not capture it as paste |
| `Ctrl+R` | Rename the highlighted session |
| `/` or any printable character other than `Space` | Enter search mode and filter sessions. Paste a GitHub, GitHub Enterprise, GitLab, or Bitbucket pull or merge request URL to find the session that created it |
| `Ctrl+A` | Show sessions from all projects on this machine. Press again to restore the current repository |
| `Ctrl+W` | Show sessions from all worktrees of the current repository. Press again to restore the current worktree. Only shown in multi-worktree repositories |
| `Ctrl+B` | Filter to sessions from your current git branch. Press again to show sessions from all branches |
| `Esc` | Exit the picker or search mode |

**Session organization:**The picker displays sessions with helpful metadata:

*   Session name if set, otherwise the conversation summary or first user prompt
*   Time elapsed since last activity
*   Message count
*   Git branch (if applicable)
*   Project path, shown after widening to all projects with `Ctrl+A`

Forked sessions (created with `/branch`, `/rewind`, or `--fork-session`) are grouped together under their root session, making it easier to find related conversations.

* * *

## Run parallel Claude Code sessions with Git worktrees

When working on multiple tasks at once, you need each Claude session to have its own copy of the codebase so changes don’t collide. Git worktrees solve this by creating separate working directories that each have their own files and branch, while sharing the same repository history and remote connections. This means you can have Claude working on a feature in one worktree while fixing a bug in another, without either session interfering with the other.Use the `--worktree` (`-w`) flag to create an isolated worktree and start Claude in it. The value you pass becomes the worktree directory name and branch name:

```
# Start Claude in a worktree named "feature-auth"
# Creates .claude/worktrees/feature-auth/ with a new branch
claude --worktree feature-auth

# Start another session in a separate worktree
claude --worktree bugfix-123
```

If you omit the name, Claude generates a random one automatically:

```
# Auto-generates a name like "bright-running-fox"
claude --worktree
```

Worktrees are created at `<repo>/.claude/worktrees/<name>` and branch from the default remote branch, which is where `origin/HEAD` points. The worktree branch is named `worktree-<name>`.The base branch is not configurable through a Claude Code flag or setting. `origin/HEAD` is a reference stored in your local `.git` directory that Git set once when you cloned. If the repository’s default branch later changes on GitHub or GitLab, your local `origin/HEAD` keeps pointing at the old one, and worktrees will branch from there. To re-sync your local reference with whatever the remote currently considers its default:

```
git remote set-head origin -a
```

This is a standard Git command that only updates your local `.git` directory. Nothing on the remote server changes. If you want worktrees to base off a specific branch rather than the remote’s default, set it explicitly with `git remote set-head origin your-branch-name`.For full control over how worktrees are created, including choosing a different base per invocation, configure a [WorktreeCreate hook](https://code.claude.com/docs/en/hooks#worktreecreate). The hook replaces Claude Code’s default `git worktree` logic entirely, so you can fetch and branch from whatever ref you need.You can also ask Claude to “work in a worktree” or “start a worktree” during a session, and it will create one automatically.

### Subagent worktrees

Subagents can also use worktree isolation to work in parallel without conflicts. Ask Claude to “use worktrees for your agents” or configure it in a [custom subagent](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields) by adding `isolation: worktree` to the agent’s frontmatter. Each subagent gets its own worktree that is automatically cleaned up when the subagent finishes without changes.

### Worktree cleanup

When you exit a worktree session, Claude handles cleanup based on whether you made changes:

*   **No changes**: the worktree and its branch are removed automatically
*   **Changes or commits exist**: Claude prompts you to keep or remove the worktree. Keeping preserves the directory and branch so you can return later. Removing deletes the worktree directory and its branch, discarding all uncommitted changes and commits

Subagent worktrees orphaned by a crash or an interrupted parallel run are removed automatically at startup once they are older than your [`cleanupPeriodDays`](https://code.claude.com/docs/en/settings#available-settings) setting, provided they have no uncommitted changes, no untracked files, and no unpushed commits. Worktrees you create with `--worktree` are never removed by this sweep.To clean up worktrees outside of a Claude session, use [manual worktree management](https://docs.anthropic.com/en/docs/claude-code/common-workflows#manage-worktrees-manually).

### Copy gitignored files to worktrees

Git worktrees are fresh checkouts, so they don’t include untracked files like `.env` or `.env.local` from your main repository. To automatically copy these files when Claude creates a worktree, add a `.worktreeinclude` file to your project root.The file uses `.gitignore` syntax to list which files to copy. Only files that match a pattern and are also gitignored get copied, so tracked files are never duplicated.

.worktreeinclude

```
.env
.env.local
config/secrets.json
```

This applies to worktrees created with `--worktree`, subagent worktrees, and parallel sessions in the [desktop app](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions).

### Manage worktrees manually

For more control over worktree location and branch configuration, create worktrees with Git directly. This is useful when you need to check out a specific existing branch or place the worktree outside the repository.

```
# Create a worktree with a new branch
git worktree add ../project-feature-a -b feature-a

# Create a worktree with an existing branch
git worktree add ../project-bugfix bugfix-123

# Start Claude in the worktree
cd ../project-feature-a && claude

# Clean up when done
git worktree list
git worktree remove ../project-feature-a
```

Learn more in the [official Git worktree documentation](https://git-scm.com/docs/git-worktree).

### Non-git version control

Worktree isolation works with git by default. For other version control systems like SVN, Perforce, or Mercurial, configure [WorktreeCreate and WorktreeRemove hooks](https://code.claude.com/docs/en/hooks#worktreecreate) to provide custom worktree creation and cleanup logic. When configured, these hooks replace the default git behavior when you use `--worktree`, so [`.worktreeinclude`](https://docs.anthropic.com/en/docs/claude-code/common-workflows#copy-gitignored-files-to-worktrees) is not processed. Copy any local configuration files inside your hook script instead.For automated coordination of parallel sessions with shared tasks and messaging, see [agent teams](https://code.claude.com/docs/en/agent-teams).

* * *

## Get notified when Claude needs your attention

When you kick off a long-running task and switch to another window, you can set up desktop notifications so you know when Claude finishes or needs your input. This uses the `Notification`[hook event](https://code.claude.com/docs/en/hooks-guide#get-notified-when-claude-needs-input), which fires whenever Claude is waiting for permission, idle and ready for a new prompt, or completing authentication.

1

2

Optionally narrow the matcher

By default the hook fires on all notification types. To fire only for specific events, set the `matcher` field to one of these values:

| Matcher | Fires when |
| --- | --- |
| `permission_prompt` | Claude needs you to approve a tool use |
| `idle_prompt` | Claude is done and waiting for your next prompt |
| `auth_success` | Authentication completes |
| `elicitation_dialog` | An MCP server opens an elicitation form |
| `elicitation_complete` | An MCP elicitation form is submitted or dismissed |
| `elicitation_response` | An MCP elicitation response is sent back to the server |

3

For the complete event schema and notification types, see the [Notification reference](https://code.claude.com/docs/en/hooks#notification).

* * *

## Use Claude as a unix-style utility

### Add Claude to your verification process

Suppose you want to use Claude Code as a linter or code reviewer.**Add Claude to your build script:**

```
// package.json
{
    ...
    "scripts": {
        ...
        "lint:claude": "claude -p 'you are a linter. please look at the changes vs. main and report any issues related to typos. report the filename and line number on one line, and a description of the issue on the second line. do not return any other text.'"
    }
}
```

### Pipe in, pipe out

Suppose you want to pipe data into Claude, and get back data in a structured format.**Pipe data through Claude:**

```
cat build-error.txt | claude -p 'concisely explain the root cause of this build error' > output.txt
```

### Control output format

Suppose you need Claude’s output in a specific format, especially when integrating Claude Code into scripts or other tools.

1

2

3

* * *

## Run Claude on a schedule

Suppose you want Claude to handle a task automatically on a recurring basis, like reviewing open PRs every morning, auditing dependencies weekly, or checking for CI failures overnight.Pick a scheduling option based on where you want the task to run:

| Option | Where it runs | Best for |
| --- | --- | --- |
| [Routines](https://code.claude.com/docs/en/routines) | Anthropic-managed infrastructure | Tasks that should run even when your computer is off. Can also trigger on API calls or GitHub events in addition to a schedule. Configure at [claude.ai/code/routines](https://claude.ai/code/routines). |
| [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks) | Your machine, via the desktop app | Tasks that need direct access to local files, tools, or uncommitted changes. |
| [GitHub Actions](https://code.claude.com/docs/en/github-actions) | Your CI pipeline | Tasks tied to repo events like opened PRs, or cron schedules that should live alongside your workflow config. |
| [`/loop`](https://code.claude.com/docs/en/scheduled-tasks) | The current CLI session | Quick polling while a session is open. Tasks stop when you start a new conversation; `--resume` and `--continue` restore unexpired ones. |

* * *

## Ask Claude about its capabilities

Claude has built-in access to its documentation and can answer questions about its own features and limitations.

### Example questions

```
can Claude Code create pull requests?
```

```
how does Claude Code handle permissions?
```

```
what skills are available?
```

```
how do I use MCP with Claude Code?
```

```
how do I configure Claude Code for Amazon Bedrock?
```

```
what are the limitations of Claude Code?
```

* * *

## Next steps
