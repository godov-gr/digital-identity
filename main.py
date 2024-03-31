import random
from datetime import datetime, timedelta
import string



def generate_random_birthdate(start_date, end_date):
    start = datetime.strptime(start_date, "%d.%m.%Y")
    end = datetime.strptime(end_date, "%d.%m.%Y")
    
    # Разница между датами в днях
    delta = end - start
    
    # Генерируем случайное число дней в пределах интервала
    random_days = random.randint(0, delta.days)
    
    # Добавляем случайное количество дней к начальной дате
    random_date = start + timedelta(days=random_days)
    
    return random_date.strftime("%d.%m.%Y")

start_date = "01.01.1970"
end_date = "31.12.2006"
random_birthdate = generate_random_birthdate(start_date, end_date)


def generate_profile(n):
    nouns = ["sky", "fire", "ice", "wind", "earth", "shadow", "light", "water", "storm", "star", "bolt", "wolf", "rabbit", "wild", "demon", "hunter", "soul", "nut", "light", "darkness", "deep",
              "rider", "dream", "men", "dog", "cat", "elf", "troll", "baby", "frog", "god", "mrak", "smoke", "drink", "next", "sniper", "dragon", "spirit", "beast", "doctor", "force", 
             "mad", "missle", "ghoul", "dude", "bird", "bro", "eye", "face", "hand", "king", "lion", "life", "person", "piece", "place", "rock", "ship", "sound", "state"]
    adjectives = ["sky", "fire", "ice", "wind", "earth", "shadow", "light", "water", "critical", "star", "agressive", "bad", "additional", "blue", "black", "red", "white", "hard", "light", "cool", "cold", "alive", 
                  "angry", "crazy", "basic", "boring", "central", "clear", "common", "curious", "current", "dark", "deep", "dead", "desperate", "early", "easy", "every", "final", "free", "freedom",
                   "general", "global", "great", "high", "hot", "huge", "impressive", "large", "late", "little", "local", "lucky", "main", "mantal", "military", "old", "hyper"]
    names = ["Mary", "Patricia", "Linda", "Barbara", "Elizabeth", "Jennifer", "Maria", "Susan", "Margaret", "Lisa", "Nancy", "Karen", "Betty", "Helen", "Sandra", "Sharon", "Sarah", "Amber", 
                    "Jessica", "Angela", "Melissa", "Martha", "James", "John", "Robert", "Michael", "William", "David", "Richard", "Charles", "Joseph", "Thomas", "Christopher", "Daniel", 
                    "Paul", "Mark", "Donald", "George", "Steven", "Edward", "Brian", "Ronald", "Anthony", "Kevin", "Jason", "Frank", "Scott", "Eric", "Andrew", "Peter", "Walter", "Samuel", 
                    "Adam", "Harry", "Fred", "Billy", "Howard", "Victor", "Todd", "Stanley"]
    surnames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "White", "Harris", "Thompson", "Garcia", "Martinez", 
                "Robinson", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Lopez", "Hill", "Green", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", 
                "Roberts", "Turner", "Phillips", "Parker", "Evans", "Edwards", "Collins", "Sanchez", "Morris", "Rogers", "Murphy", "Richardson", "Cooper", "Torres", "Peterson", "Ramirez", "Sanders", 
                "Price", "Barnes", "Henderson", "Jenkins", "Powell", "Flores", "Diaz", "Hayes"]
    domains = ["example.com", "mail.com", "inbox.com", "mailworld.com", "emailplanet.org", "letterbox.co", "post.com", "message.io", "sendmail.today",
    "mailbox.com", "emailservice.io", "digitalpost.net", "virtualmail.com", "proton.me", "gmail.com"]
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
        country = random.choice(list(cities_and_countries.keys()))
        city = random.choice(cities_and_countries[country])
        noun = random.choice(nouns)
        cool_number = random.choice(cool_numbers)
        adjective = random.choice(adjectives)
        nickname = adjective + noun + cool_number
        birthday = generate_random_birthdate(start_date, end_date)
        domain = random.choice(domains)
        email = f"{name.lower()}.{surname.lower()}{cool_number}@{domain}"
        password = ''.join(random.choice(characters) for _ in range(18))
        profile = f"{name} {surname} | {city}, {country} | {birthday} | {email} | {nickname} | {password}"
        profiles.append(profile)
    return profiles


def save_profiles_to_file(profiles, filename):
    with open(filename, 'w') as file:
        for profile in profiles:
            file.write(profile + '\n')

profiles = generate_profile(50)
filename = 'profiles.txt'
save_profiles_to_file(profiles, filename)

print(f"profiles saved to {filename}")
