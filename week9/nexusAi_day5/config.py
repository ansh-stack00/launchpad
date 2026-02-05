from pathlib import Path

BASE_DIR = Path(".")

OUTPUT_DIR = BASE_DIR / "nexusAi_day5" / "nexus_output"
LOG_DIR = BASE_DIR /"nexusAi_day5" / "logs"

OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE_PATH = LOG_DIR / "nexus-ai.log"

MAX_RETRIES_PER_AGENT = 2
MAX_PLAN_RETRIES = 2