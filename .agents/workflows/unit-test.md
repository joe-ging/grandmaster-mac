---
description: Run the backend and frontend unit tests individually or continuously
---

# Unit Test Workflow

## Purpose
Run granular unit tests to quickly verify functions in the frontend or backend while developing.

## Usage

### 1. Run all tests
To run everything (Frontend + Backend), simply use the existing `/test` workflow:
```bash
# This is usually what you want to do before committing
@[/test]
```

### 2. Run Backend Tests Only
If you are only working on Python code:
```bash
cd /Users/jingsmacbookpro/.gemini/antigravity/scratch/grandmaster-mac/backend
source ../venv/bin/activate
# Run all backend tests
pytest -W ignore
# Or run a specific test file:
pytest test_eco_lookup.py -W ignore
```

### 3. Run Frontend Tests Only
If you are only working on React code:
```bash
cd /Users/jingsmacbookpro/.gemini/antigravity/scratch/grandmaster-mac/frontend
# Run all frontend tests once
npm test
# Run tests in watch mode (auto-reloads on save)
npm test -- --watch
```

## How to use this workflow
1. Add new tests in `frontend/src/__tests__/` or `backend/` files prefixed with `test_`.
2. Follow the commands above to verify they pass!
