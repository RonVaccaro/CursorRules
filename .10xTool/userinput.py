# userinput.py - Reads and logs messages from user_response.txt
# Usage: python .10xTool/userinput.py

import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESPONSE_FILE = os.path.join(SCRIPT_DIR, "user_response.txt")
LAST_MSG_FILE = os.path.join(SCRIPT_DIR, ".last_msg.txt")
COUNTER_FILE = os.path.join(SCRIPT_DIR, ".msg_counter.txt")
LOG_FILE = os.path.join(SCRIPT_DIR, "conversation_log.txt")

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""

def write_file(path, content):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except:
        pass

def append_file(path, content):
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(content)
    except:
        pass

def get_next_msg_id():
    try:
        count = int(read_file(COUNTER_FILE).strip() or "0")
    except:
        count = 0
    count += 1
    write_file(COUNTER_FILE, str(count))
    return count

def main():
    current = read_file(RESPONSE_FILE).strip()
    last_read = read_file(LAST_MSG_FILE).strip()
    
    if not current:
        print("[WAITING] user_response.txt is empty")
        return
    
    if current == last_read:
        print("[NO NEW MESSAGE]")
        return
    
    msg_id = get_next_msg_id()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tag = f"MSG-{msg_id:04d}"
    
    print(f"[{tag}] [{timestamp}]")
    print("-" * 50)
    print(current)
    print("-" * 50)
    
    append_file(LOG_FILE, f"\n{'='*60}\n[{tag}] [{timestamp}]\n{'='*60}\n{current}\n")
    write_file(LAST_MSG_FILE, current)

if __name__ == "__main__":
    main()
