# Sticky Notes Application

## Description
A simple note-taking web application built with Django. Users can create, read, update, and delete personal notes. Supports both authenticated users and a fallback guest user for anonymous note creation.

## Features
* User authentication (login/logout)
* Guest user fallback for anonymous note creation
* CRUD(Create, Read, Update, Delete) operations on notes.
* Admin interface for managing users and notes
* Handles foreign key constraints to prevent deletion errors

## Requirements
* Python 3.8+
* Django 5.2.2 (or compatible)
* SQLite (default) or other Django-supported databases

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
    - [Creating a Note](#creating-a-note)
    - [Updating a Note](#updating-a-note)
    - [Viewing a Note](#viewing-a-note)
    - [Deleting a Note](#deleting-a-note)
3. [Credits](#credits)

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/Duri-Kim/sticky_notes_app.git
    ```
2. Navigate to the project directory:
    ```sh
    cd sticky_notes_app
    ```
3. Create and activate a virtual environment:
    - On **Windows (PowerShell)**:
    ```
    python -m venv atom
    .\atom\Scripts\activate
    ```

    - On **macOS/Linux**:
    ```
    python3 -m venv atom
    source atom/bin/activate
    ```
     
4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
    
5. Apply the migrations to set up the database:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser(admin account):
    ```sh
    python manage.py createsuperuser
    ```
    
6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Access the app:
* User interface http://127.0.0.1:8000/
* Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Creating a Note
1. Click "New Note" on the main page.
2. Fill in the note's title and content.
3. Click "Save" to create the note.

### Updating a Note
1. Navigate to the note you want to update.
2. Click "Edit".
3. Modify the title and/or content.
4. Click "Save" to update the note.

### Viewing a Note
2. Click on the note's title in the note list to see details.

### Deleting a Note
1. Open the note you want to delete.
2. Click the "Delete" button to remove it.

## Credits
Developed by Duri Kim.
