# Sticky Notes Application

This is a Django-based web application for creating, updating, and managing notes and posts. Each note and post is associated with a user, providing a personalized experience.

## Features

- User authentication
- Create, update, and delete notes
- Create, update, and delete posts
- Detailed views for notes and posts
- List views for all notes and posts

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.8 or later.
- You have installed Django 3.1 or later.
- You have a basic understanding of Django and Python.

## Installation

To install this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/sticky-notes.git
    ```

2. Navigate to the project directory:

    ```bash
    cd sticky-notes
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Log in using the superuser credentials you created.
3. Create, update, and delete notes and posts from the web interface.

## Project Structure

- `views.py`: Contains all the view functions for handling requests and rendering templates.
- `models.py`: Defines the data models for notes and posts.
- `forms.py`: Contains form classes for creating and updating notes and posts.
- `urls.py`: Maps URL patterns to view functions.
- `templates/`: Contains HTML templates for rendering the web pages.
- `static/`: Contains static files such as CSS and JavaScript.
- `tests.py`: Contains test cases for models and views.
