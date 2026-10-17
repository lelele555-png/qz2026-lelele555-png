import json
import os

def analyze_log(filepath: str) -> dict:
    if not os.path.exists(filepath):
        return {}

    total = 0
    by_level = {}
    by_user = {}
    last_error = None

    try:
        with open(filepath, 'r', encoding="utf-8") as f:
            first_line = f.readline()
            if not first_line.strip():
                return {}

            f.seek(0)
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    log_entry = json.loads(line)
                    level = log_entry["level"]
                    user = log_entry["user"]
                    message = log_entry["message"]
                except (json.JSONDecodeError, TypeError, KeyError):
                    continue

                total += 1
                by_level[level] = by_level.get(level, 0) + 1
                by_user[user] = by_user.get(user, 0) + 1

                if level == "ERROR":
                    last_error = message
    except OSError:
        return {}

    return {
        "total": total,
        "by_level": by_level,
        "by_user": by_user,
        "last_error": last_error
    }