# Here is a sample regex that parses a log file and extracts relevant information. 
# you will need to modify it. Review Lecture 11
#import re

#def parse_log_line(line):
 #  pattern = r"^(.*?)\s\|\s(\w+)\s\|\s(\w+)\s\|\s(.*)$"
  #  match = re.match(pattern, line)
  
  #part 3 b
  
  
import threading
import time
import json
import os
import matplotlib.pyplot as plt

def graph_log_levels(json_file):
    plt.ion()  # Interactive mode on

    while True:
        try:
            if os.path.exists(json_file):
                with open(json_file, 'r') as file:
                    data = json.load(file)

                levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
                counts = []

                for level in levels:
                    if level in data:
                        counts.append(sum(data[level].values()))
                    else:
                        counts.append(0)

                plt.clf()  # Clear previous graph
                plt.bar(levels, counts, color=['green', 'yellow', 'red', 'purple'])
                plt.title("Log Level Distribution")
                plt.xlabel("Log Levels")
                plt.ylabel("Number of Messages")
                plt.ylim(0, max(counts) + 5)  # Adjust y-axis for better visibility
                plt.tight_layout()
                plt.pause(5)  # Pause to update every 5 seconds
            else:
                print(f"File '{json_file}' not found.")

        except json.JSONDecodeError:
            print("JSON file is not properly formatted yet. Waiting...")

        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(1)

if __name__ == "__main__":
    json_file = 'combined_log_summary.json'  # Make sure this file exists

    graph_thread = threading.Thread(target=graph_log_levels, args=(json_file,), daemon=True)
    graph_thread.start()

    while True:
        time.sleep(1)

   
