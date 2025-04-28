# Paste your python file here 
# don't forget to upload it with your submission
import threading
import time
import json
import os

def monitor_json_file(json_file):
    last_critical_messages = set()  # Track already-seen critical messages

    while True:
        try:
            if os.path.exists(json_file):
                with open(json_file, 'r') as file:
                    data = json.load(file)

                print("\n--- Log Level Summary ---")
                for level, messages in data.items():
                    total_messages = sum(messages.values())
                    print(f"{level}: {total_messages} messages")

                if "CRITICAL" in data:
                    current_critical_messages = set(data["CRITICAL"].keys())
                    new_critical_messages = current_critical_messages - last_critical_messages

                    for msg in new_critical_messages:
                        print(f"\nNew CRITICAL Message: {msg}")

                    last_critical_messages.update(new_critical_messages)

                print("\nWaiting for updates...\n" + "-"*40)

            else:
                print(f"File '{json_file}' not found.")

        except json.JSONDecodeError:
            print("JSON file is not properly formatted yet. Waiting...")

        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(5)  # Wait before checking again

if __name__ == "__main__":
    json_file = 'combined_log_summary.json'  # Adjust if your file has a different name

    monitor_thread = threading.Thread(target=monitor_json_file, args=(json_file,), daemon=True)
    monitor_thread.start()

    while True:
        time.sleep(1)
