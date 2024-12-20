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