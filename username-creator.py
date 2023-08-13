import random
import string

common_usernames = [
    "admin", "user", "guest", "administrator", "root",
    "test", "demo", "support", "webmaster", "manager"
]

def generate_random_username():
    prefix = random.choice(common_usernames)
    suffix = ''.join(random.choices(string.digits, k=3))
    return prefix + suffix

num_usernames = 10000  # Gerar 10000 nomes de usuário

with open("username.txt", "w") as file:
    for _ in range(num_usernames):
        username = generate_random_username()
        file.write(username + "\n")

print("Nomes de usuário foram salvos em 'username.txt'.")
