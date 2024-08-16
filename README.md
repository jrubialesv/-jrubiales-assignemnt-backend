# Cooking Recipes Web App - Backend

This repository contains the backend API for the Cooking Recipes Web App. The backend is built using Flask, a lightweight Python web framework, and provides RESTful endpoints for managing recipes, user accounts, and other core functionalities of the application.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Architecture](#architecture)
- [Files and Directories](#files-and-directories)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About the Project

The backend API serves as the core of the Cooking Recipes Web App, handling all the business logic, data processing, and database interactions. It ensures that users can create, read, update, and delete recipes, as well as manage their accounts and preferences.

## Features

- **User Authentication**: Secure user authentication and authorization using JWT tokens.
- **Recipe Management**: Endpoints for creating, updating, deleting, and retrieving recipes.
- **Search Functionality**: Search recipes by name, ingredients, or other attributes.
- **User Profiles**: Manage user profiles, including saving favorite recipes and viewing cooking history.
- **Database Integration**: Uses SQLAlchemy ORM for database interactions, supporting SQLite, PostgreSQL, and other databases.

## Architecture

The backend follows a modular structure with clearly defined layers:

- **Routes**: Define the API endpoints and handle HTTP requests.
- **Models**: Represent the database schema using SQLAlchemy models.
- **Services**: Contain the business logic for processing data and interacting with models.
- **Tests**: Include unit and functional tests to ensure the correctness of the API.

## Files and Directories

- **`config.py`**: Configuration file for setting environment variables and application settings.
- **`run.py`**: The entry point for starting the Flask application.
- **`recipes_api/`**: Contains the core API code, including routes, models, and services.
  - **`routes.py`**: Defines the API endpoints and the logic for handling requests.
  - **`models.py`**: Defines the SQLAlchemy models, which map to the database tables.
  - **`__init__.py`**: Initializes the Flask app, sets up the database connection, and registers routes.
- **`tests/`**: Contains test cases for the API.
  - **`unit/`**: Unit tests for individual functions and models.
  - **`functional/`**: Functional tests that simulate API requests and verify end-to-end functionality.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your_username/cooking-recipes-web-app-backend.git
    ```
2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Set environment variables** in `config.py`:
    - `FLASK_ENV`: Set to `development` for local development.
    - `DATABASE_URL`: The URL of your database (e.g., `sqlite:///recipes.db` for SQLite).
    - `SECRET_KEY`: A secret key for securing sessions and JWT tokens.

2. **Initialize the database**:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

## Usage

Run the Flask application locally:
```bash
python run.py

The API will be accessible at http://localhost:5000.

API Documentation

Here are the main API endpoints provided by the backend:

	•	User Authentication:
	•	POST /auth/register: Register a new user.
	•	POST /auth/login: Authenticate an existing user and retrieve a JWT token.
	•	Recipe Management:
	•	GET /recipes: Retrieve a list of all recipes.
	•	POST /recipes: Create a new recipe (requires authentication).
	•	GET /recipes/<id>: Retrieve details of a specific recipe by ID.
	•	PUT /recipes/<id>: Update a specific recipe by ID (requires authentication).
	•	DELETE /recipes/<id>: Delete a specific recipe by ID (requires authentication).
	•	User Profiles:
	•	GET /users/me: Retrieve the authenticated user’s profile.
	•	PUT /users/me: Update the authenticated user’s profile.

Testing

The backend includes a suite of unit and functional tests to ensure the correctness of the codebase. To run the tests:

	1.	Install testing dependencies:

pip install -r requirements-dev.txt


	2.	Run the tests:

pytest



Test coverage reports are generated automatically during the testing process.

Deployment

To deploy the backend in a production environment, follow these steps:

	1.	Set up your production environment by configuring the appropriate environment variables:
	•	Ensure FLASK_ENV is set to production.
	•	Set DATABASE_URL to your production database’s URL.
	•	Configure a secure SECRET_KEY.
	2.	Use a WSGI server like Gunicorn to run the application:

gunicorn run:app


	3.	Deploy to a cloud service such as AWS, Azure, or Google Cloud, ensuring the necessary infrastructure (e.g., database, storage) is set up and connected to the application.

Contributing

Contributions to improve the backend are welcome. To contribute, please fork the repository and submit a pull request. Ensure that all new code is covered by tests and passes existing tests.

	1.	Fork the repository and create your feature branch (git checkout -b feature/AmazingFeature).
	2.	Commit your changes (git commit -m 'Add some AmazingFeature').
	3.	Push to the branch (git push origin feature/AmazingFeature).
	4.	Open a Pull Request to the main branch.

License

Distributed under the MIT License. See LICENSE for more information.

Contact

Juan J. Rubiales - [jrubialesv@gmail.com](mailto:jrubialesv@gmail.com)

Project Frontend Link: [https://github.com/jrubialesv/cooking-recipes-web-app-frontend](https://github.com/jrubialesv/cooking-recipes-web-app-frontend)
Project Backend Link: [https://github.com/jrubialesv/cooking-recipes-web-app-backend](https://github.com/jrubialesv/cooking-recipes-web-app-backend)
Project IaC Link: [https://github.com/jrubialesv/cooking-recipes-web-app-iac](https://github.com/jrubialesv/cooking-recipes-web-app-iac)
