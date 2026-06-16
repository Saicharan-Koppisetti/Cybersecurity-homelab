from flask import Flask, request, render_template
import datetime

app = Flask(__name__)
LOG_FILE = "honeypot_log.txt"

def log_attempt(ip, username, password):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] SUSPICIOUS ACTIVITY | IP: {ip} | Username: {username} | Password: {password}\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
    
    print(log_entry)

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        ip = request.remote_addr
        
        log_attempt(ip, username, password)
        message = "Invalid credentials. Please try again."

    return render_template("login.html", message=message)

if __name__ == "__main__":
    print("[*] Honeypot is running on http://localhost:5000")
    print("[*] Waiting for intruders...\n")
    app.run(host="0.0.0.0", port=5000, debug=False)
