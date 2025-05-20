import os
import csv
import random

storage = []
delivered_items = []
item_prices = {
    "LAPTOP": {
        "DELL":84000,
        "HP":72000,
        "LENOVO":68000,
        "ASUS":100000

    },

    "PHONE": {
        "SAMSUNG":138000,
        "IPHONE":10000,
        "VIVO":40000,
        "ONEPLUS":50000,

    },
    "HEADPHONE": {
        "BOSE":60000,
        "BOAT":5000,
        "JBL":10000,
        "APPLE":100000,
        "SONY":50000
    },
    "CHARGER": {
        "ARMSTRONG":599,
        "MOTO":259,
        "OPPO":159,
        "INFINIX":0.01,
    },
    "WATCHES": {
        "TITAN":25000,
        "JOHN JACOBS":1500000,
        "RADO":400000,
        "ROLEX":300000,
        "PATEK PHILLIPE":3000000,
        "BLANCPAIN":750000,
    },
    "SMART TV":{
        "LG":40000,
        "PANASONIC":45000,
        "BRAVE":50000,
        "HISENSE":60000,
        "HAIER":20000,
    }
    
}


def owner():
    print("\n---AM'S COMPANY---")
    for i in range(5):
        item = input(f"Enter item {i+1}: ").strip().upper()
        storage.append(item)
    print("Items added to storage.")

def dealer():
    print("\n--- DEALER SECTION ---")
    if storage:
        print("Dealer has stored the following items:")
        for item in storage:
            print("-", item)
    else:
        print("I DON'T HAVE THAT ITEM .")

def customer():
    print("\n--- Customer Section ---")
    a = input("To check listed items enter YES/NO: ").strip().upper()  
    if a == "YES":
        print("Available Items:", storage)
    else:
        print("Don't come to this website if you are not interested.")

def buy_item():
    print("\n--- Purchase Section ---")
    item = input("Enter the item you want to buy from the list: ").strip().upper()
    if item in storage:
        name = input("Enter your name: ").strip().title()
        address = input("Enter your address: ").strip()
        price = item_prices.get(item, random.randint(100, 5000))

        storage.remove(item)
        delivered_items.append(item)

        print(f"{item} delivered to {name}!")

        # Generate bill and write to CSV
        bill = [name, address, item, price]
        file_exists = os.path.isfile("bills.csv")

        with open("bills.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Customer Name", "Address", "Product", "Price"])
            writer.writerow(bill)

        print("\n--- Bill Generated ---")
        print(f"Name     : {name}")
        print(f"Address  : {address}")
        print(f"Product  : {item}")
        print(f"Price    : Rs.{price}")
    else:
        print("Invalid selection. Choose only from the listed items.")

def main():
    while True:
        print("\n========== Welcome to AM Logistics ==========")
        print("1. Owner - Add items")
        print("2. Dealer - Store items")
        print("3. Customer - View items")
        print("4. Buy an item")
        print("5. View Delivered Items")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        if choice == 1:
            owner()
        elif choice == 2:
            dealer()
        elif choice == 3:
            customer()
        elif choice == 4:
            buy_item()
        elif choice == 5:
            print("Delivered Items:", delivered_items)
        elif choice == 6:
            print("Exiting Website. Thank you for visiting AM Logistics!")
            break
        else:
            print("WHEN U KNOW THERE ARE 6 OPTIONS CHOOSE FROM THAT ONLY, DON'T PUT YOUR IMAGINARY NUMBER.")

# Run the main function
main()
