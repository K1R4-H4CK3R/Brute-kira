import random
import string

# Função para gerar uma senha aleatória
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Gera 5000 senhas aleatórias
num_passwords = 50000
with open("wordlist.txt", "w") as file:
    for _ in range(num_passwords):
        password = generate_password()
        file.write(password + "\n")

print(f"Arquivo wordlist.txt com {num_passwords} senhas foi criado.")
