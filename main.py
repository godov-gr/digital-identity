import os
import random
import string
import datetime
from flask import Flask, request, jsonify, render_template_string, send_file
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

        # Генерация ника с рандомным соединителем "_"
        connector1 = "_" if random.choice([True, False]) else "" # 50% шанс на использование "_"
        connector2 = "_" if random.choice([True, False]) else "" # 50% шанс на использование "_"
        nickname = f"{random.choice(adjectives)}{connector1}{random.choice(nouns)}{connector2}{random.choice(cool_numbers)}"

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
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Digital-identity v1.5</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 2em;
                background-color: #121212;
                color: #e0e0e0;
            }
            h1 {
                color: #bb86fc;
                text-align: center;
            }
            form {
                margin-bottom: 2em;
                text-align: center;
            }
            input, button {
                padding: 0.5em;
                font-size: 1em;
                margin: 0.2em;
                background-color: #1f1f1f;
                border: 1px solid #333;
                color: #e0e0e0;
                border-radius: 4px;
            }
            button {
                background-color: #bb86fc;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #9c70f6;
            }
            .profiles {
                margin-top: 2em;
                border: 1px solid #333;
                padding: 1em;
                border-radius: 8px;
                background-color: #1f1f1f;
            }
            .profile {
                margin-bottom: 1em;
                padding: 0.5em;
                border-bottom: 1px solid #333;
            }
            .download-button {
                margin-top: 2em;
                display: block;
                text-align: center;
            }
            .download-button a {
                padding: 0.7em 1.5em;
                background-color: #03dac6;
                color: #121212;
                text-decoration: none;
                border-radius: 5px;
            }
            .download-button a:hover {
                background-color: #01bfa5;
            }
        </style>
    </head>
    <body>
        <h1>Digital-identity v1.8</h1>
        <form action="/generate_profiles" method="get">
            <label for="count">Number of profiles:</label>
            <input type="number" id="count" name="count" value="10" min="1">
            <button type="submit">Generate</button>
        </form>
        <div id="profiles" class="profiles"></div>
        <div id="download" class="download-button"></div>
        <script>
            document.querySelector('form').onsubmit = async function(event) {
                event.preventDefault();
                const count = document.querySelector('#count').value;
                const response = await fetch(`/generate_profiles?count=${count}`);
                const profiles = await response.json();
                const container = document.querySelector('#profiles');
                const downloadContainer = document.querySelector('#download');
                container.innerHTML = profiles.map(profile => `
                    <div class="profile">
                        <strong>Name:</strong> ${profile.name} <br>
                        <strong>Email:</strong> ${profile.email} <br>
                        <strong>Nickname:</strong> ${profile.nickname} <br>
                        <strong>Birthday:</strong> ${profile.birthday} <br>
                        <strong>Country:</strong> ${profile.country} <br>
                        <strong>City:</strong> ${profile.city} <br>
                        <strong>Password:</strong> ${profile.password}
                    </div>
                `).join('');

                // Create a download link for the JSON file
                const blob = new Blob([JSON.stringify(profiles, null, 2)], { type: 'application/json' });
                const url = URL.createObjectURL(blob);
                downloadContainer.innerHTML = `<a href="${url}" download="profiles.json">Download JSON</a>`;
            };
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route("/generate_profiles", methods=["GET"])
def generate_profiles():
    """Generates a list of random profiles."""
    try:
        count = int(request.args.get("count", 10))
        profiles = generate_profile(count)
        return jsonify(profiles)
    except ValueError:
        return jsonify({"error": "Invalid count parameter, must be an integer."}), 400

if __name__ == "__main__":
    app.run(debug=True)
