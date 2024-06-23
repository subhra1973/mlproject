import logging
import os
from datetime import datetime

# Generate log file name based on current date and time
LOG_FILE = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

# Complete logging setup
logs_path = os.path.join(os.getcwd(), "logs")
##print(f"Logs path: {logs_path}")  # Debug print
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
#print(f"Log file path: {LOG_FILE_PATH}")  # Debug print

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("LOG file test")
    ##print(f"Log file created: {LOG_FILE_PATH}")  # Confirm log file creation

  
    
    



