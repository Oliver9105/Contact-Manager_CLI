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