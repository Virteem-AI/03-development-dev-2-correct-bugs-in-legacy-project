# Exercise Guide - DEV-2

## Goal

Fix all bugs in `repo/buggy_app.py` using the test feedback loop.

## Steps

1. Run:

```bash
pytest test_buggy_app.py -v
```

2. Copy the failing output.
3. Ask Copilot:

```text
Fix all bugs in buggy_app.py so that all tests in test_buggy_app.py pass.
Run the tests after each fix to verify.
```

4. Apply fixes progressively.
5. Re-run tests after each fix.
6. Reset to the broken version if needed.
7. Repeat the same task with Claude Code if available.
8. Compare the two approaches.

## Expected Output

- All tests pass.
- The five bugs are understood and explained.
- A short comparison of Copilot Agent Mode and Claude Code is written.
