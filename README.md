# Starter repo - DEV-2

Deliberately broken Flask project.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest test_buggy_app.py -v
```

## Files

- `buggy_app.py`: application with 5 intentional bugs.
- `test_buggy_app.py`: verification tests.

## Goal

Fix `buggy_app.py` until you get:

```text
5 passed
```
