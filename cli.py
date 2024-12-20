def add_contact():
    name = input("Enter contact name: ").strip()
    phone_number = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    Contact.add_contact(name, phone_number, email) 
    print("Contact added successfully.")


def list_contacts():
    contacts = Contact.get_all_contacts()
    print("Contacts:")
    for contact in contacts:
        contact_id, name, phone_number, email = contact
        print(f"ID: {contact_id} | Name: {name} | Phone: {phone_number} | Email: {email}")

# cli.py
def search_contact_by_id():
    contacts = Contact.get_all_contacts()
    if not contacts:
        print("No contacts available.")
        return 

    print("Select a contact to search by ID:")
    for contact in contacts:
        print(f"ID: {contact['id']} | Name: {contact['name']}")

    try:
        contact_id = int(input("Enter the contact ID: ").strip())
        selected_contact = Contact.find_contact_by_id(contact_id)
        if selected_contact:
            print(f"ID: {selected_contact['id']} | Name: {selected_contact['name']} | Phone: {selected_contact['phone_number']} | Email: {selected_contact['email']}")
        else:
            print("Invalid contact ID.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# cli.py
def search_contact_by_id(): 
    # (Code for search_contact_by_id() is already included in the previous commit)
    pass

# cli.py
def delete_contact():
    try:
        contact_id = int(input("Enter contact ID to delete: ").strip())
        Contact.delete_contact(contact_id)
        print("Contact deleted successfully.")
    except ValueError:
        print("Invalid ID format. Please enter a number.")


def assign_contact_to_group():
    try:
        # List all available contacts
        contacts = Contact.get_all_contacts()
        if not contacts:
            print("No contacts available.")
            return

        print("\nSelect a contact to assign to a group:")
        for contact in contacts:
            print(f"ID: {contact[0]} | Name: {contact[1]}")

        contact_id = int(input("Enter the contact ID to assign: ").strip())

        # List all groups
        groups = Group.get_all_groups()
        if not groups:
            print("No groups available.")
            return

        print("\nSelect a group to assign the contact:")
        for group in groups:
            print(f"ID: {group[0]} | Name: {group[1]}")

        group_id = int(input("Enter the group ID to assign to: ").strip())

        # Assign the contact to the selected group
        ContactGroup.assign_contact_to_group(contact_id, group_id) 
        print(f"Contact ID {contact_id} has been assigned to group '{group[1]}'.")

    except ValueError:
        print("Invalid input. Please enter a number.")

# cli.py
def main():
    ContactGroup.create_table()
    Group.create_table()
    Contact.create_table()

    while True:
        print("Contact Manager")
        print("================")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Search Contacts")
        print("4. Delete Contact")
        print("5. Assign Contact to Group")
        print("6. Add Group")
        print("7. List Groups")
        print("8. Delete Group")
        print("9. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            search_choice = input("\nSearch Contacts by:\n1. ID\n2. Group\nEnter your choice (1/2): ")
            if search_choice == "1":
                search_contact_by_id()
            elif search_choice == "2":
                search_contact_by_group()
            else:
                print("Invalid choice.")
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            assign_contact_to_group()
        elif choice == "6":
            add_group()
        elif choice == "7":
            list_groups()
        elif choice == "8":
            delete_group()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")  

if __name__ == "__main__":
    main()