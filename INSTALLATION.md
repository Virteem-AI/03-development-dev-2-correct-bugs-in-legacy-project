# Installation - DEV-2

## Prerequisites

- Python 3.11+.
- `pip`.
- GitHub Copilot Chat or Agent Mode.
- Claude Code in Copilot if available.

## Setup

From the `repo/` folder:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Run the tests:

```bash
pytest test_buggy_app.py -v
```

The tests are expected to fail at the beginning.
