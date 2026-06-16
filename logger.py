import hashlib
import json
import datetime
import os

LOG_FILE = "logs.json"

# Calculate SHA256 hash of any entry
def calculate_hash(entry):
    entry_str = json.dumps(entry, sort_keys=True)
    return hashlib.sha256(entry_str.encode()).hexdigest()

# Load existing logs from file
def load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)

# Save logs to file
def save_logs(logs):
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

# Add a new log entry
def add_log(event_type, description):
    logs = load_logs()

    if len(logs) == 0:
        previous_hash = "0" * 64  # first entry has no previous
    else:
        previous_hash = logs[-1]["current_hash"]

    entry = {
        "id": len(logs) + 1,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event_type": event_type,
        "description": description,
        "previous_hash": previous_hash
    }

    entry["current_hash"] = calculate_hash(entry)
    logs.append(entry)
    save_logs(logs)
    print(f"\n[+] Log entry #{entry['id']} added successfully.")

# View all logs
def view_logs():
    logs = load_logs()
    if len(logs) == 0:
        print("\n[!] No logs found.")
        return

    print("\n--- LOG ENTRIES ---")
    for entry in logs:
        print(f"\nID        : {entry['id']}")
        print(f"Timestamp : {entry['timestamp']}")
        print(f"Event     : {entry['event_type']}")
        print(f"Details   : {entry['description']}")
        print(f"Prev Hash : {entry['previous_hash'][:30]}...")
        print(f"Curr Hash : {entry['current_hash'][:30]}...")
    print("\n-------------------")

# Verify integrity of all logs
def verify_logs():
    logs = load_logs()

    if len(logs) == 0:
        print("\n[!] No logs to verify.")
        return

    print("\n[*] Checking log integrity...\n")
    tampered = False

    for i, entry in enumerate(logs):
        stored_hash = entry["current_hash"]

        # Recalculate hash without the current_hash field
        entry_copy = entry.copy()
        del entry_copy["current_hash"]
        calculated_hash = calculate_hash(entry_copy)

        # Check if entry itself was modified
        if stored_hash != calculated_hash:
            print(f"[!!!] TAMPERED: Entry #{entry['id']} has been modified!")
            tampered = True
            continue

        # Check if chain link is broken
        if i > 0:
            expected_prev = logs[i - 1]["current_hash"]
            if entry["previous_hash"] != expected_prev:
                print(f"[!!!] CHAIN BROKEN at Entry #{entry['id']} - entry deleted or rearranged!")
                tampered = True
                continue

        print(f"[OK] Entry #{entry['id']} - {entry['event_type']} - Clean")

    if not tampered:
        print("\n[+] All logs verified. No tampering detected.")
    else:
        print("\n[!!!] WARNING: Log tampering detected!")

# Main menu
def menu():
    while True:
        print("\n====================================")
        print("   Tamper-Evident Logging System")
        print("====================================")
        print("1. Add Log Entry")
        print("2. View All Logs")
        print("3. Verify Log Integrity")
        print("4. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            event_type = input("Event Type (e.g. LOGIN, LOGOUT, TRANSACTION): ").upper()
            description = input("Description: ")
            add_log(event_type, description)

        elif choice == "2":
            view_logs()

        elif choice == "3":
            verify_logs()

        elif choice == "4":
            print("\nExiting. Goodbye.")
            break

        else:
            print("[!] Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
