import os
import random
import string
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Global configuration
DATA_FOLDER = "data"
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# Helper functions from the uploaded project
def generate_random_birthdate(start_date, end_date):
    start = datetime.datetime.strptime(start_date, "%d.%m.%Y")
    end = datetime.datetime.strptime(end_date, "%d.%m.%Y")
    delta = end - start
    random_days = random.randint(0, delta.days)
    random_date = start + datetime.timedelta(days=random_days)
    return random_date.strftime("%d.%m.%Y")

def generate_profile(n):
    nouns = ["sky", "fire", "ice", "wind", "earth", "shadow", "light", "water", "storm", "star", "bolt", "wolf", "rabbit", "wild", "demon", "hunter", "soul", "nut", "light", "darkness", "deep", "rider", "dream", "men", "dog", "cat", "elf", "troll", "baby", "frog", "god", "mrak", "smoke", "drink", "next", "sniper", "dragon", "spirit", "beast", "doctor", "force", "mad", "missle", "ghoul", "dude", "bird", "bro", "eye", "face", "hand", "king", "lion", "life", "person", "piece", "place", "rock", "ship", "sound", "state"]
    adjectives = ["sky", "fire", "ice", "wind", "earth", "shadow", "light", "water", "critical", "star", "agressive", "bad", "additional", "blue", "black", "red", "white", "hard", "light", "cool", "cold", "alive", "angry", "crazy", "basic", "boring", "central", "clear", "common", "curious", "current", "dark", "deep", "dead", "desperate", "early", "easy", "every", "final", "free", "freedom", "general", "global", "great", "high", "hot", "huge", "impressive", "large", "late", "little", "local", "lucky", "main", "mantal", "military", "old", "hyper"]
    names = ["Mary", "Patricia", "Linda", "Barbara", "Elizabeth", "Jennifer", "Maria", "Susan", "Margaret", "Lisa", "Nancy", "Karen", "Betty", "Helen", "Sandra", "Sharon", "Sarah", "Amber", "Jessica", "Angela", "Melissa", "Martha", "James", "John", "Robert", "Michael", "William", "David", "Richard", "Charles", "Joseph", "Thomas", "Christopher", "Daniel", "Paul", "Mark", "Donald", "George", "Steven", "Edward", "Brian", "Ronald", "Anthony", "Kevin", "Jason", "Frank", "Scott", "Eric", "Andrew", "Peter", "Walter", "Samuel", "Adam", "Harry", "Fred", "Billy", "Howard", "Victor", "Todd", "Stanley"]
    surnames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "White", "Harris", "Thompson", "Garcia", "Martinez", "Robinson", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Lopez", "Hill", "Green", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Roberts", "Turner", "Phillips", "Parker", "Evans", "Edwards", "Collins", "Sanchez", "Morris", "Rogers", "Murphy", "Richardson", "Cooper", "Torres", "Peterson", "Ramirez", "Sanders", "Price", "Barnes", "Henderson", "Jenkins", "Powell", "Flores", "Diaz", "Hayes"]
    domains = ["example.com", "mail.com", "inbox.com", "mailworld.com", "emailplanet.org", "letterbox.co", "post.com", "message.io", "sendmail.today", "mailbox.com", "emailservice.io", "digitalpost.net", "virtualmail.com", "proton.me", "gmail.com"]
    cool_numbers = ["007", "13", "42", "69", "88", "123", "228", "420", "666", "777", "911"]
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"

    profiles = []
    for _ in range(n):
        name = random.choice(names)
        surname = random.choice(surnames)
        domain = random.choice(domains)
        email = f"{name.lower()}.{surname.lower()}@{domain}"
        nickname = f"{random.choice(adjectives)}_{random.choice(nouns)}_{random.choice(cool_numbers)}"
        birthday = generate_random_birthdate("01.01.1970", "31.12.2006")
        password = "".join(random.choices(characters, k=18))
        profile = {
            "name": f"{name} {surname}",
            "email": email,
            "nickname": nickname,
            "birthday": birthday,
            "password": password
        }
        profiles.append(profile)
    return profiles

@app.route("/generate_profiles", methods=["GET"])
def generate_profiles():
    """Generates a list of random profiles."""
    try:
        count = int(request.args.get("count", 10))
        profiles = generate_profile(count)
        return jsonify(profiles)
    except ValueError:
        return jsonify({"error": "Invalid count parameter, must be an integer."}), 400

@app.route("/generate_identity", methods=["GET"])
def generate_identity():
    """Generates a digital identity with a random name, nickname, and password."""
    first_names = ["Alice", "Bob", "Charlie", "Dana", "Eve"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
    first_part = ["sky", "fire", "ice", "wind", "earth"]
    second_part = ["hunter", "rider", "master", "crafter", "builder"]
    numbers = ["007", "123", "456", "789", "999"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    nickname = f"{random.choice(first_part)}_{random.choice(second_part)}_{random.choice(numbers)}"
    password = "".join(random.choices(string.ascii_letters + string.digits, k=12))

    identity = {
        "name": f"{first_name} {last_name}",
        "nickname": nickname,
        "password": password
    }

    return jsonify(identity)

@app.route("/save_log", methods=["POST"])
def save_log():
    """Saves a log entry with a timestamp."""
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request, 'message' is required"}), 400

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = os.path.join(DATA_FOLDER, f"log_{timestamp}.txt")

    with open(log_filename, "w") as log_file:
        log_file.write(data["message"])

    return jsonify({"status": "success", "log": log_filename})

@app.route("/retrieve_logs", methods=["GET"])
def retrieve_logs():
    """Retrieves all log files with their content."""
    logs = {}
    for filename in os.listdir(DATA_FOLDER):
        if filename.startswith("log_"):
            with open(os.path.join(DATA_FOLDER, filename), "r") as log_file:
                logs[filename] = log_file.read()

    return jsonify(logs)

if __name__ == "__main__":
    app.run(debug=True)
