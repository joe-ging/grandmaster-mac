---
description: How to commit and push code changes to GitHub
---

# Git Push Workflow

## When to Run
Run this workflow after completing any meaningful chunk of work:
- After adding a new feature
- After fixing a bug
- After refactoring code
- At the end of every session (even if work is incomplete)

## Prerequisites
- GitHub CLI (`gh`) is installed and authenticated as `joe-ging`
- Remote is already configured: `origin → https://github.com/joe-ging/grandmaster-mac.git`

## Steps

// turbo
1. Check what changed:
```bash
cd /Users/jingsmacbookpro/.gemini/antigravity/scratch/grandmaster-mac
git status
```

// turbo
2. Stage all changes:
```bash
git add -A
```

// turbo
3. Commit with a descriptive message (follow conventional commits):
```bash
git commit -m "feat: <short description of what was done>"
```

Use these prefixes:
- `feat:` for new features
- `fix:` for bug fixes
- `refactor:` for code restructuring
- `docs:` for documentation changes
- `chore:` for maintenance tasks

// turbo
4. Push to GitHub:
```bash
git push origin main
```

// turbo
5. Verify the push:
```bash
gh repo view joe-ging/grandmaster-mac --json pushedAt --jq '.pushedAt'
```

## Notes
- The `.gitignore` already excludes: `node_modules/`, `venv/`, `*.db`, `.env`, `__pycache__/`
- Database files are NOT tracked (they contain user data)
- If push fails with auth error, run: `gh auth login --hostname github.com --web`
