# Contact Manager CLI

## Introduction

Contact Manager CLI is a simple command-line application built to manage contacts. The application allows users to add, list, search, update, delete, and organize contacts into groups. It uses an SQLite database to persist data and provides a seamless experience for managing personal or professional contacts from the command line.

## Features

1. _Add Contact_: Add a new contact to the database with details such as name, phone number, and email.
2. _List Contacts_: View all the contacts stored in the database.
3. _Search Contacts_: Search for contacts by ID or by the groups they belong to.
4. _Delete Contact_: Remove a contact from the database by ID.
5. _Assign Contact to Group_: Assign a contact to a specific group.
6. _Add Group_: Create new groups for organizing contacts.
7. _List Groups_: View all groups created in the system.
8. _Delete Group_: Delete a group from the database.

## Requirements

Before running the application, make sure you have the following installed on your system:

- Python 3.8.13
- SQLite (or use Python's built-in SQLite support)

## Installation

1. _Clone the repository_:
   sh
   git clone git@github.com:Oliver9105/Contact-Manager_CLI.git
2. ### Navigate into the project directory\\:

   sh
   cd contact-manager-cli

3. ### Install dependencies

   sh
   pipenv install

4. ### Activate the virtual environment

   pipenv shell

5. ### Run the application
   sh
   python cli.py

## Usage

1. Run the application:
   sh
   python3 cli.py
2. Follow the on-screen instructions to interact with the Contact Manager.

# Example

### Adding a Contact

markdown
Enter your choice: 1
Enter contact name: John Doe
Enter phone number: 123-456-7890
Enter email: johndoe@email.com
Contact John Doe added successfully! -->

### Listing Contacts

markdown
Enter your choice: 2 Contacts: ID: 1 | Name: John Doe | Phone: 123-456-7890 | Email: johndoe@email.com | Groups: No

### Assigning a Contact to a Group

markdown
Enter your choice: 5
Enter contact ID to assign to group: 1
Enter group name to assign: Family
Contact John Doe assigned to group Family.

## Database Schema

### Contacts Table

- id: INTEGER, primary key
- name: TEXT
- phone_number: TEXT
- email: TEXT

### Groups Table

- id: INTEGER, primary key
- name: TEXT

### ContactGroups Table

- contact_id: INTEGER, foreign key (contacts.id)
- group_id: INTEGER, foreign key (groups.id)

## Technologies

### Primary Technologies:

- _Python_: The core programming language used to develop the application.
- _SQLite_: A lightweight and embedded relational database used to store contact and group data.

### Supporting Technologies:

- _Pipenv_: A tool for managing project dependencies, creating virtual environments, and ensuring reproducibility.
- _Git_: For version control, tracking changes, and collaborating with others.

## Support and Contact Details

If you have any questions, suggestions, or need assistance, please contact:

- <span style="color:blue">Email: Olivercher1000@gmail.com</span>

## License

_MIT License © 2024 Oliver (Oliver9105)_

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
