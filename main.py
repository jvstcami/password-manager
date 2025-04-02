# password manager

import json, os, sys
import gen

passwords = []

if os.path.exists("./passwords.json"):
    with open("./passwords.json") as file:
        passwords = json.load(file)
else:
    with open("./passwords.json", "w") as file:
        json.dump(passwords, file)

while True:
    for i in range(999):
        print("\n")
    print("password manager")

    print("""
A. new password
B. view passwords
EXIT. exit program
""")
    choice = input(">>> ").lower()

    if choice == "a":
        site = input("site: ")
        password_length = int(input("password length: "))
        generated_password = gen.password_generator(password_length)
        print(f"generated password: {generated_password}")
        passwords.append({
            "site": site,
            "password": generated_password
        })
        with open("./passwords.json", "w") as file:
            json.dump(passwords, file)
        input("---")
    if choice == "b":
        for password in passwords:
            print(f"""
id: {passwords.index(password)}
site: {password["site"]}
password: {password["password"]}
""")
        input("---")
    if choice == "exit":
        sys.exit()