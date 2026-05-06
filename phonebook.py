import json

def load_contacts():
    try:
        with open("contacts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

contacts = load_contacts()

def add_contact():
    print("\n--- Add a Contact ---")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            print(f"\n✗ This number already exists under '{contact['name']}'.")
            return

    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    save_contacts()
    print(f"\n✓ Contact '{name}' added successfully!")

def view_contacts():
    print("\n--- All Contacts ---")
    if len(contacts) == 0:
         print("Your phonebook is empty.")
         return
        
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def remove_contact():
    print("\n--- Remove a Contact ---")
    view_contacts()

    if len(contacts) == 0:
        return

    name = input("\nEnter the name to remove: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print(f"\n✓ Contact '{contact['name']}' removed successfully!")
            return
    save_contacts()
    print(f"\n✗ No contact found with that name.")


def edit_contact():
    print("\n--- Edit a Contact ---")
    view_contacts()

    if len(contacts) == 0:
        return

    name = input("\nEnter the name to edit: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print(f"\nLeave blank to keep the current value.")
            
            new_name = input(f"New name ({contact['name']}): ").strip()
            new_phone = input(f"New phone ({contact['phone']}): ").strip()

            for other in contacts:
                if other["phone"] == new_phone and other != contact:
                    print(f"\n✗ That number already exists under '{other['name']}'.")
                    return

            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone

            print(f"\n✓ Contact updated successfully!")
            return
    save_contacts()
    print(f"\n✗ No contact found with that name.")


def search_contact():
    print("\n--- Search a Contact ---")
    query = input("Enter a name or phone number to search: ").strip().lower()

    results = []

    for contact in contacts:
        if query in contact["name"].lower() or query in contact["phone"]:
            results.append(contact)

    if len(results) == 0:
        print(f"\n✗ No contacts found matching '{query}'.")
        return

    print(f"\nFound {len(results)} result(s):")
    for i, contact in enumerate(results, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")



def show_menu():
    print("\n--- Phone Book ---")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Remove a contact")
    print("4. Edit a contact")
    print("5. Search a contact")
    print("6. Quit")

while True:
    show_menu()
    choice = input("\nChoose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        remove_contact()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")