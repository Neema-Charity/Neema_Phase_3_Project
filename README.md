# CONTRACTORY

## AUTHOR
[Neema Charity](https://github.com/Neema-Charity)

## DESCRIPTION
 Constructory is designed to manage the construction process for civil engineering projects efficiently. The system ensures accurate inventory management of materials, supplier coordination, and material allocation to projects. The system is built using Python and SQLite3, featuring a relational database model that includes a one-to-many(1 project can use many materials), and many-to-many(Many materials can be used in many projects) relationships to ensure robust data integrity and efficient querying.

## INSTALLATION AND SETUP
### Prerequisites
1. Python 3.8 or higher
2. SQLite 3 or higher

### Project Structure
|Neema_Phase_3_Project/
    |models/
        |__pycache__/
        |__init__.py
        |base.py
        |conn.py
        |material.py
        |project.py
        |supplier.py

|__init__.py
|app.py
|construction.db
|Pipfile
|Pipfile.lock
|README.md

    
### Installation
1. Clone the repository
2. Install the required modules using pip

### Database Setup
1. Create a new SQLite database file: sqlite3 construction.db
2. Creating Tables by running SQL scripts in the database directory.

### Running the App
1. Run the app: python3 app.py

### Usage
Once the App is running, select the option you want and watch it come to life by seeing the table using VSCode Extension

## LIVE SITE

## TECHNOLOGIES
1. Python3
2. SQLite3
3. CLI

## CONTACT INFORMATION
You can reach out to me through:
- [Github](https://github.com/Neema-Charity)
- [Email](https://mail.google.com/mail)

## LICENSE
MIT license
Copyright (c) 2024.