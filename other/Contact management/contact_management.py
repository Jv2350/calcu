import json

contacts = []


def load_contacts(filename="contacts.json"):
    global contacts
    try:
        with open(filename, "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []


def save_contacts(filename="contacts.json"):
    with open(filename, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(store_name, phone_number, email, address):
    contact_id = len(contacts) + 1
    contacts.append(
        {
            "id": contact_id,
            "store_name": store_name,
            "phone_number": phone_number,
            "email": email,
            "address": address,
        }
    )
    save_contacts()


def view_contacts():
    for contact in contacts:
        print(
            f"ID: {contact['id']}, Store Name: {contact['store_name']}, Phone Number: {contact['phone_number']}"
        )


def search_contact(query):
    results = [
        contact
        for contact in contacts
        if query.lower() in contact["store_name"].lower()
        or query in contact["phone_number"]
    ]
    for contact in results:
        print(
            f"ID: {contact['id']}, Store Name: {contact['store_name']}, Phone Number: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}"
        )


def update_contact(contact_id, store_name, phone_number, email, address):
    for contact in contacts:
        if contact["id"] == contact_id:
            contact["store_name"] = store_name
            contact["phone_number"] = phone_number
            contact["email"] = email
            contact["address"] = address
            break
    save_contacts()


def delete_contact(contact_id):
    global contacts
    contacts = [contact for contact in contacts if contact["id"] != contact_id]
    save_contacts()


def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            store_name = input("Enter store name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(store_name, phone_number, email, address)
            print("Contact added successfully.")

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            query = input("Enter store name or phone number to search: ")
            search_contact(query)

        elif choice == "4":
            contact_id = int(input("Enter contact ID to update: "))
            store_name = input("Enter new store name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            update_contact(contact_id, store_name, phone_number, email, address)
            print("Contact updated successfully.")

        elif choice == "5":
            contact_id = int(input("Enter contact ID to delete: "))
            delete_contact(contact_id)
            print("Contact deleted successfully.")

        elif choice == "6":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


load_contacts()

if __name__ == "__main__":
    main()
