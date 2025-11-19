
#!/usr/bin/env bash

# Force working directory to project folder
cd /home/anshagrawal/day5_automation || exit 1

LOG_FILE_PATH="logs/validate.log"

# if dir not present make it 
mkdir -p logs

echo "validation run at $(date) " >> "$LOG_FILE_PATH"


# checking src folder exist or not 

if [ ! -d "src" ]; then
  echo "[ERROR] src/ directory missing!" | tee -a "$LOG_FILE_PATH"
  exit 1
else
  echo "[INFO] src/ directory found and not empty." | tee -a "$LOG_FILE_PATH"
fi


# checking config.json exist or not 
if ! jq empty config.json 2>/dev/null; then
  echo "[ERROR] config.json is invalid JSON!" | tee -a "$LOG_FILE_PATH"
  exit 1
else
  echo "[INFO] config.json found and not empty." | tee -a "$LOG_FILE_PATH"
fi

echo "[OK] All checks passed!" | tee -a "$LOG_FILE_PATH"
exit 0
