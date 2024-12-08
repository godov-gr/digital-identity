import os
import random
import string
import datetime
from flask import Flask, request, jsonify, render_template, send_file
import json

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
    cities_and_countries = {
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'San Francisco', 'Miami', 'Seattle', 'Washington D.C.', 'Boston', 'Las Vegas'],
    'Poland': ['Warsaw', 'Krakow', 'Lodz', 'Wroclaw', 'Poznan', 'Gdansk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Katowice'],
    'Germany': ['Berlin', 'Munich', 'Frankfurt', 'Hamburg', 'Cologne', 'Stuttgart', 'Dusseldorf', 'Dortmund', 'Essen', 'Leipzig'],
    'UK': ['London', 'Birmingham', 'Manchester', 'Glasgow', 'Leeds', 'Liverpool', 'Newcastle', 'Belfast', 'Cardiff', 'Edinburgh'],
    'Canada': ['Toronto', 'Montreal', 'Vancouver', 'Calgary', 'Edmonton', 'Ottawa', 'Winnipeg', 'Quebec City', 'Hamilton', 'Halifax']
}
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
        country = random.choice(list(cities_and_countries.keys()))
        city = random.choice(cities_and_countries[country])
        password = "".join(random.choices(characters, k=18))
        profile = {
            "name": f"{name} {surname}",
            "email": email,
            "nickname": nickname,
            "birthday": birthday,
            "country": country,
            "city": city,
            "password": password
        }
        profiles.append(profile)
    return profiles

@app.route("/", methods=["GET"])
def home():
    return (
        "<h1>Digital-identity v 1.4 </h1>"
        "<form action='/generate_profiles' method='get'>"
        "<label for='count'>Number of profiles:</label>"
        "<input type='number' id='count' name='count' value='10' min='1'>"
        "<button type='submit'>Generate</button>"
        "</form>"
    )

@app.route("/generate_profiles", methods=["GET"])
def generate_profiles():
    """Generates a list of random profiles."""
    try:
        count = int(request.args.get("count", 10))
        profiles = generate_profile(count)
        file_path = os.path.join(DATA_FOLDER, "profiles.json")
        with open(file_path, "w") as file:
            json.dump(profiles, file, indent=4)
        return (
            jsonify(profiles),
            {"Content-Disposition": "attachment;filename=profiles.json"}
        )
    except ValueError:
        return jsonify({"error": "Invalid count parameter, must be an integer."}), 400

if __name__ == "__main__":
    app.run(debug=True)