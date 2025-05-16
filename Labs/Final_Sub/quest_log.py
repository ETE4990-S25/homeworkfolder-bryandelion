from datetime import datetime

def log(message: str) -> None:
    """
    Logs a timestamped message to both the console and a log file.
    """
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f"{timestamp} {message}"

    print(log_entry)
    with open("quest_log.txt", mode="a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")
