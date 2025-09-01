import re
import os
import random
import string
from time import sleep

# Colors
R = "\033[91m"  # Red
G = "\033[92m"  # Green
Y = "\033[93m"  # Yellow
C = "\033[96m"  # Cyan
W = "\033[0m"   # Reset

# Banner
def banner():
    os.system("clear")
    print(f"""{C}
    ╔════════════════════════════╗
    ║   🔐 PASSWORD CHECKER 🔐   ║
    ╚════════════════════════════╝
    {W}""")

# Password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12: score += 30
    elif len(password) >= 8: score += 20
    else: feedback.append(f"{R}[!] Password too short (min 8).{W}")

    if re.search(r"[a-z]", password): score += 15
    else: feedback.append(f"{Y}[-] Add lowercase letters.{W}")

    if re.search(r"[A-Z]", password): score += 15
    else: feedback.append(f"{Y}[-] Add uppercase letters.{W}")

    if re.search(r"[0-9]", password): score += 15
    else: feedback.append(f"{Y}[-] Add numbers.{W}")

    if re.search(r"[@$!%*?&]", password): score += 25
    else: feedback.append(f"{Y}[-] Add special characters (@$!%*?&).{W}")

    if score >= 80: strength = f"{G}STRONG{W}"
    elif score >= 50: strength = f"{Y}MEDIUM{W}"
    else: strength = f"{R}WEAK{W}"

    return strength, score, feedback

# Random password generator
def generate_password(length=16):
    chars = string.ascii_letters + string.digits + "@$!%*?&"
    return ''.join(random.choice(chars) for _ in range(length))

# Main menu
def main_menu():
    while True:
        banner()
        print(f"""{C}
        [1] Check Password Strength
        [2] Generate Strong Random Password
        [3] About
        [0] Exit
        {W}""")
        choice = input(f"{G}Enter your choice > {W}")
        
        if choice == "1":
            pwd = input("\n🔑 Enter your password: ")
            strength, score, tips = check_password_strength(pwd)
            print(f"\nScore: {score} | Strength: {strength}\n")
            if tips:
                print("💡 Suggestions:")
                for t in tips:
                    print("-", t)
            input(f"\n{C}Press Enter to continue...{W}")

        elif choice == "2":
            length = input("Password length (default 16): ")
            if not length.isdigit(): length = 16
            else: length = int(length)
            new_pwd = generate_password(length)
            print(f"\n🔑 Suggested Strong Password: {G}{new_pwd}{W}\n")
            input(f"{C}Press Enter to continue...{W}")

        elif choice == "3":
            print(f"""{Y}
            Password Strength Checker v1.0
            Password analysis + strong random password generator
            Coded by: codewriter42
            İnstagram: coderoot42
            {W}""")
            input(f"{C}Press Enter to continue...{W}")

        elif choice == "0":
            print(f"{G}Goodbye!{W}")
            sleep(1)
            break
        else:
            print(f"{R}Invalid choice!{W}")
            sleep(1)

if __name__ == "__main__":
    main_menu()
