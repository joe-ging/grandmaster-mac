---
description: How to refactor code for maintainability after completing a feature
---

# Refactoring Workflow

## When to Run
Run this workflow AFTER completing a feature and BEFORE starting the next one.
Think of it as "cleaning the kitchen after cooking, before starting the next meal."

Trigger phrases the user might say:
- "refactor" or "clean up the code"
- "this file is getting too big"
- "the code is messy"
- "/refactor"

## Pre-Flight Checks

// turbo
1. Make sure all current work is committed first (so we can revert if refactoring goes wrong):
```bash
cd /Users/jingsmacbookpro/.gemini/antigravity/scratch/grandmaster-mac
git add -A && git status
```

2. If there are uncommitted changes, commit them:
```bash
git commit -m "feat: <describe current work>"
```

## Refactoring Checklist

Go through each check IN ORDER. Fix what you find before moving to the next check.

### Check 1: File Size (The "Too Big" Test)
// turbo
3. Find files over 300 lines:
```bash
find frontend/src -name "*.jsx" -o -name "*.js" | xargs wc -l | sort -rn | head -15
find backend -name "*.py" | xargs wc -l | sort -rn | head -10
```

**Rule of thumb:**
- Under 200 lines → Leave it alone
- 200-400 lines → Watch it, might need splitting soon
- 400+ lines → Should be split into smaller files

For any file over 400 lines, look for:
- Data/constants that can be moved to a separate file (like ECO_OPENINGS was)
- Components defined inside other components (extract to their own files)
- Helper functions that could be in a utils file
- Repeated code blocks that could become a shared function

### Check 2: Duplication (The "Copy-Paste" Test)
4. Search for duplicated patterns:
```bash
# Look for fetch calls that could use a shared API helper
grep -rn "fetch(" frontend/src/pages/ | head -20

# Look for repeated style objects
grep -rn "backgroundColor:" frontend/src/pages/ | wc -l
```

If the same fetch pattern or style block appears 3+ times, extract it into:
- `src/utils/api.js` for API calls
- `src/styles/shared.js` for repeated style objects

### Check 3: Naming (The "Can I Understand This?" Test)  
5. Scan for unclear names:
```bash
# Single-letter variables (outside of loop indices)
grep -rn "const [a-z] =" frontend/src/pages/ | grep -v "const i " | grep -v "const e " | head -10

# Functions named "handle" without specifics
grep -rn "const handle = " frontend/src/ | head -10
```

Rename anything unclear:
- `data` → `gamesList` or `twicIssues`
- `handleClick` → `handleMoveSelection`
- `val` → `evalScore`

### Check 4: Dead Code (The "Is This Used?" Test)
// turbo
6. Check for commented-out code or unused imports:
```bash
grep -rn "// .*import\|// .*const\|// .*function" frontend/src/pages/ | head -10
grep -rn "TODO\|FIXME\|HACK\|XXX" frontend/src/ backend/ | head -10
```

Remove commented-out code — it lives in git history if you ever need it back.
Address or document any TODO/FIXME items.

## Post-Refactoring

// turbo
7. Verify the app still builds:
```bash
cd frontend && npm run build 2>&1 | tail -5
```

8. If build succeeds, commit the refactoring separately:
```bash
cd /Users/jingsmacbookpro/.gemini/antigravity/scratch/grandmaster-mac
git add -A
git commit -m "refactor: <describe what was reorganized>"
git push origin main
```

9. If build fails, revert:
```bash
git checkout -- .
```

## Key Principles
- **Never refactor and add features at the same time** — do one or the other
- **Commit before AND after** — so you can always revert
- **The app must work identically after refactoring** — no behavior changes
- **Small moves are safer than big rewrites** — extract one component at a time
