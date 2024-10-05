# Project Name - Backend

## Overview
This is the backend application for the **CBD3354 Assignment 1**. It is built using Flask and provides APIs for user registration, file uploads, and retrieving users and files.

## Features
- API endpoint for user registration
- API endpoint for file uploads
- API endpoints for retrieving lists of users and uploaded files

## Technologies Used
- Python
- Flask
- Flask-CORS
- Google Cloud Storage (for file storage)
- SQL Database

## Getting Started

### Prerequisites
- Python 3.x
- Virtual Environment (optional)
- Required Python packages listed in `requirements.txt`

### Installation
1. Clone the repository:
   ```bash
   git clone <backend-repository-url>
   cd <backend-directory>
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your Google Cloud Storage and ensure your service account JSON is in place.
5. Run the application:
   ```bash
   python app.py
   ```

### Configuration
Update the following environment variables as needed:
- `GCS_BUCKET_NAME`: Your Google Cloud Storage bucket name.
- `SERVICE_ACCOUNT_JSON`: Path to your Google Cloud service account JSON file.

### Usage
1. Start the backend server.
2. Use the provided API endpoints to register users and upload files:
   - `POST /register`: Register a new user
   - `POST /upload`: Upload a file
   - `GET /users`: Retrieve the list of registered users
   - `GET /files`: Retrieve the list of uploaded files

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.
