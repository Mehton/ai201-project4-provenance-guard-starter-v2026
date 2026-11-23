#!/usr/bin/env python3
"""
Provenance Guard on a real server. ← UNIT 9

    python serve.py

`python app.py` runs Flask's development server, which says so on every start.
This runs the same app under waitress, a production WSGI server that works on
Windows as well as macOS and Linux (gunicorn needs fork(), so it can't start on
Windows at all).

Same settings as app.py, all from the environment:

    HOST   default 127.0.0.1 — set 0.0.0.0 to accept traffic from other machines
    PORT   default 5000

Every request is recorded in logs/requests.jsonl (timing, memory, outcome);
every decision is still recorded in logs/audit.jsonl as before.
"""

from waitress import serve

import config
from app import app

# Requests are handled on this many threads. Scoring is CPU-bound and GPT-2 is
# shared, so more threads mostly means more requests waiting on the same cores.
THREADS = 4


def main():
    print(f"Provenance Guard (waitress) on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}  (loads on the first /submit)")
    print(f"  rate limiting:   {'ON' if config.RATE_LIMITING_ENABLED else 'off'}")
    print(f"  audit log:       {config.AUDIT_LOG}")
    print(f"  request log:     {config.REQUEST_LOG}")
    serve(app, host=config.HOST, port=config.PORT, threads=THREADS)


if __name__ == "__main__":
    main()
