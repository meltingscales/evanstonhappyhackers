import requests

SERVER_URL = "http://127.0.0.1:5000"

def register():
    username = input("Enter your username: ")
    response = requests.post(f"{SERVER_URL}/register", json={"username": username})
    if response.status_code == 200:
        print(response.json()['message'])
    else:
        print(response.json()['error'])

def gamble(username):
    print("\n--- Slot Machine ---")
    print("|🍒|🍋|🍉|")
    print("Spinning...\n")
    bet = int(input("Enter your bet: "))
    response = requests.post(
        f"{SERVER_URL}/play", 
        json={"username": username, "bet": bet,
              "w":[1, 1, 1]} # gee I sure hope nobody changes this. this is very secure :3
        )

    # this is the server code that runs to calculate the result
    # result = random.choices(['win', 'lose', 'jackpot'], probabilities)[0]

    if response.status_code == 200:
        data = response.json()
        print(f"Result: {data['result']}")
        print(f"New Balance: {data['balance']}")
    else:
        print(response.json()['error'])

def cashout(username):
    response = requests.post(f"{SERVER_URL}/cashout", json={"username": username})
    if response.status_code == 200:
        print(response.json()['message'])
    else:
        print(response.json()['error'])

def main():
    print("Welcome to the Slot Machine Game!")
    print("1. Register")
    username = input("Enter your username to log in/register: ")
    register()
    while True:
        print("\n1. Gamble")
        print("2. Cashout")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            gamble(username)
        elif choice == '2':
            cashout(username)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
