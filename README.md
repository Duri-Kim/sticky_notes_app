# Sticky Notes Application

## Description
The Sticky Notes application is a web-based platform that allows users to create, update, view, and delete notes and posts. This project is developed using Django, a high-level Python web framework. Learning this aspect of coding is important as it provides hands-on experience with web development, handling user input, and interacting with a database.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
    - [Creating a Note](#creating-a-note)
    - [Updating a Note](#updating-a-note)
    - [Viewing a Note](#viewing-a-note)
    - [Deleting a Note](#deleting-a-note)
    - [Creating a Post](#creating-a-post)
    - [Updating a Post](#updating-a-post)
    - [Viewing a Post](#viewing-a-post)
    - [Deleting a Post](#deleting-a-post)
3. [Credits](#credits)

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/Duri-Kim/sticky_notes_app.git
    ```
2. Navigate to the project directory:
    ```sh
    cd sticky_notes
    ```
3. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```
4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
5. Apply the migrations to set up the database:
    ```sh
    python manage.py migrate
    ```
6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

### Creating a Note
1. Navigate to the home page: `http://127.0.0.1:8000/`
2. Click on "New Note".
3. Fill in the title and content of the note and click "Save".

### Updating a Note
1. Navigate to the note you want to update: `http://127.0.0.1:8000/note/<note_id>/`
2. Click on "Edit".
3. Update the title and content of the note and click "Save".

### Viewing a Note
1. Navigate to the home page: `http://127.0.0.1:8000/`
2. Click on the title of the note you want to view.

### Deleting a Note
1. Navigate to the note you want to delete: `http://127.0.0.1:8000/note/<note_id>/`
2. Click on "Delete".

### Creating a Post
1. Navigate to the Bulletin Board: `http://127.0.0.1:8000/posts/`
2. Click on "New Post".
3. Fill in the title and content of the post and click "Save".

### Updating a Post
1. Navigate to the post you want to update: `http://127.0.0.1:8000/post/<post_id>/`
2. Click on "Edit".
3. Update the title and content of the post and click "Save".

### Viewing a Post
1. Navigate to the Bulletin Board: `http://127.0.0.1:8000/posts/`
2. Click on the title of the post you want to view.

### Deleting a Post
1. Navigate to the post you want to delete: `http://127.0.0.1:8000/post/<post_id>/`
2. Click on "Delete".

## Credits
This application was developed by [Duri Kim](https://github.com/Duri-Kim).
