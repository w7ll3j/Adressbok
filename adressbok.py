import json
import time

# Read the file
try:
    with open("adressbok.json", encoding="utf-8") as f:
        adressbok = json.load(f)
except FileNotFoundError:
    adressbok = {}

print("=" * 32 + "\n||\033[7m N  O  T  E ""\033[0m"f" {chr(128366)}  \033[7m"" B  O  O  K " + "\033[0m||\n" + "=" * 32)

while True:
    print("\n\033[1m1. Add\033[0m")
    print("\033[1m2. Remove\033[0m")
    print("\033[1m3. Search\033[0m")
    print("\033[1m4. Exit and save\n\033[0m")
    print("=" * 32)
    selection = input("\n\033[2mChoose one alternative:\033[0m ")

    # Add a name and number
    if "1" in selection:
        print("\033[6mAdd name and phone number\033[0m")
        name = input("Name: ").upper()
        number = input("Phone number: ")
        adressbok[name] = number
        print(f"\033[2m{name} ({number}), is added.\033[0m\n")
        time.sleep(1)
        print("=" * 32)

    # Remove a name with its number
    elif "2" in selection:
        print("\033[6mRemove name and associated phone number\033[0m")
        name = input("Name: ").upper()
        if name in adressbok:
            del adressbok[name]
            print(f"\033[2m{name} is removed.\033[0m\n")
        else:
            time.sleep(0.5)
            print("\033[2mNot found.\033[0m")
        time.sleep(1)
        print("=" * 32)

    # Search for a name and number in the file
    elif "3" in selection:
        if not adressbok:
            print("\033[3mEmpty\033[0m")
            time.sleep(0.5)
            print("Returning to main menu", end="")
            for _ in range(3):
                print("\033[2m.\033[0m", end="", flush=True)
                time.sleep(0.8)
        else:
            print()
            print(f"{'NAME':<17}{'NUMBER':<12}")
            print("-" * 32)
            for name, number in adressbok.items():
                print(f"{name:<17}{number:<12}")
            print("\n\033[3m1. Return to main menu")
            print("2. Exit and save\033[0m")
            selection = input("\n\033[2m1 / 2:\033[0m ")
            if "2" in selection:
                break
        print("\n" + "=" * 32)

    # Exit the script
    elif "4" in selection:
        print("")
        break

    # Error message for wrong input
    else:
        print("\033[2mWrong input. Try again.\033[0m")



# Save the file
with open("adressbok.json", "w", encoding="utf-8") as f:
    json.dump(adressbok, f, indent=2, ensure_ascii=False)

