import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("./src/CHAT-LOGS.json")

def log_human_feedback(
    query,
    answer,
    context,
    rating,
    comment,
):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "query": query,
        "answer": answer,
        "context": context,
        "rating": rating,
        "comment": comment
    }

    
    if not LOG_FILE.exists():
        LOG_FILE.write_text("[]")

    logs = json.loads(LOG_FILE.read_text())
    logs.append(log_entry)

    LOG_FILE.write_text(json.dumps(logs, indent=2))
