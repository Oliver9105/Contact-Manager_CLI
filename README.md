# Contact Manager CLI

## Introduction

Contact Manager CLI is a simple command-line application built to manage contacts. The application allows users to add, list, search, update, delete, and organize contacts into groups. It uses an SQLite database to persist data and provides a seamless experience for managing personal or professional contacts from the command line.

## Features

- **Add Contact**: Add a new contact to the database with details such as name, phone number, and email. - **List Contacts**: View all the contacts stored in the database.
- **Search Contacts**: Search for contacts by ID or by the groups they belong to.
- **Delete Contact**: Remove a contact from the database by ID.
- **Assign Contact to Group**: Assign a contact to a specific group.
- **Add Group**: Create new groups for organizing contacts.
- **List Groups**: View all groups created in the system.
- **Delete Group**: Delete a group from the database.

## Requirements

Before running the application, make sure you have the following installed on your system:

- **Python 3.8.13**
- **SQLite** (or use Python's built-in SQLite support)

## Installation

1. **Clone the repository**:

   ``sh
`git clone git@github.com:Oliver9105/Contact-Manager_CLI.git`

   ```

   ```

2. **Navigate into the project directory**:

   ``sh
 `cd contact-manager-cli`

   ```

   ```

3. **Install dependencies**:

   ``sh
 `pipenv install`

   ```

   ```

4. **Activate the virtual environment**:

   ``sh
`pipenv shell`

   ```

   ```

5. Run the application:
   ``sh
`python cli.py`
   ```

   ```

## Usage

1. Run the application:
   ``sh
`python3 cli.py`
   ```

   ```

```plaintext
Contact Manager
================
1. Add Contact
2. List Contacts
3. Search Contacts
4. Delete Contact
5. Assign Contact to Group
6. Add Group
7. List Groups
8. Delete Group
9. Quit
```

2. Follow the on-screen instructions to interact with the Contact Manager.

## Example Scenarios

### Adding a Contact

```plaintext
Enter your choice: 1
Enter contact name: John Doe
Enter phone number: 123-456-7890
Enter email: johndoe@email.com
Contact John Doe added successfully!
```

### Listing Contacts

```markdown
Enter choice: 2
Contacts:
ID: 1 | Name: Alice Johnson | Phone: 123-456-7890 | Email: alice.johnson@email.com | Groups: Family
ID: 2 | Name: Bob Smith | Phone: 234-567-8901 | Email: bob.smith@email.com | Groups: Friends, Work
ID: 3 | Name: Carol | Phone: 345-678-9012 | Email: carol@email.com | Groups: Family
ID: 4 | Name: Kamau | Phone: 456-235-000 | Email: kamau@email.com | Groups: Gym
ID: 5 | Name: John Doe | Phone: 123-456-7700 | Email: johndoe@email.com | Groups: Family, Work, Gym
ID: 7 | Name: Jane Doe | Phone: 234-567-888 | Email: janedoe@email.com | Groups: Family, Friends
```

### Assigning a Contact to a Group

```plaintext
Enter your choice: 5
Enter contact ID to assign to group: 1
Enter group name to assign: Family
Contact John Doe assigned to group Family.
```

### Searching Contacts

#select option 3 and the cli prompts you to choose between :

#option1: `search by contact id`
#option2: `search by groups`

```plaintext
Contact Manager
================
1. Add Contact
2. List Contacts
3. Search Contacts
4. Delete Contact
5. Assign Contact to Group
6. Add Group
7. List Groups
8. Delete Group
9. Quit

Enter your choice: 3

Search Contacts by:
1. ID
2. Group
Enter your choice (1/2): 2

Select a group to search contacts:
ID: 1 | Name: Family
ID: 2 | Name: Friends
ID: 3 | Name: Work
ID: 4 | Name: Gym

Enter the group ID: 4

Contacts in group Gym:
ID: 4 | Name: Kamau | Phone: 456-235-000 | Email: kamau@email.com
ID: 5 | Name: John Doe | Phone: 123-456-7700 | Email: johndoe@email.com


Search Contacts by:
 1. ID
 2. Group
Enter your choice (1/2): 1

Select a contact to search by ID:
ID: 1 | Name: Alice Johnson
ID: 2 | Name: Bob Smith
ID: 3 | Name: Carol
ID: 4 | Name: Kamau
ID: 5 | Name: John Doe
ID: 7 | Name: Jane Doe

Enter the contact ID: 2

ID: 2 | Name: Bob Smith | Phone: 234-567-8901 | Email: bob.smith@email.com | Groups: Friends, Work
```

### List Groups from the main menu.

1. This option displays a list of all groups, along with their IDs, for easy reference.
2. IDs are helpful when assigning contacts or deleting groups.

```plaintext
Enter your choice: 7
Groups:
ID: 1 | Name: Family
ID: 2 | Name: Friends
ID: 3 | Name: Work
ID: 4 | Name: Gym
ID: 5 | Name: Classmates
```

### Deleting a Group

1.  Select Delete Group from the main menu.
2.  Enter the name of the group you want to delete.

```plaintext
Enter your choice: 8
Enter group name to delete: Classmates
Group deleted successfully!
```

### Listing Groups

Select List Groups from the main menu.

```plaintext
Enter your choice: 7
Groups:
ID: 1 | Name: Family
ID: 2 | Name: Friends
ID: 3 | Name: Work
ID: 4 | Name: Gym
ID: 5 | Name: Classmate
```

# Database Schema

### Contacts Table

    id: INTEGER, primary key

    name: TEXT

    phone_number: TEXT

    email: TEXT

### Groups Table

    id: INTEGER, primary key

    name: TEXT

### ContactGroups Table

    contact_id: INTEGER, foreign key (contacts.id)

    group_id: INTEGER, foreign key (groups.id)

# Technologies

### Primary Technologies:

    Python: The core programming language used to develop the application.

    SQLite: A lightweight and embedded relational database used to store contact and group data.

### Supporting Technologies:

    Pipenv: A tool for managing project dependencies, creating virtual environments, and ensuring reproducibility.

    Git: For version control, tracking changes, and collaborating with others.

### Support and Contact Details

If you have any questions, suggestions, or need assistance, please contact:

    Email:Olivercher1000@gmail.com

License

MIT License © 2024 Oliver (Oliver9105)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
