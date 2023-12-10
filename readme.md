# Simple Note REST API Project

This project is a simple RESTful API for managing notes, built with Django Rest Framework. It includes token-based authentication for secure access.

## Features

- **Create, Read, Update, Delete (CRUD) Operations**: Perform basic CRUD operations on notes.
- **Token Authentication**: Secure your API with token-based authentication.
- **Django Rest Framework**: Utilizes the power of DRF for building robust APIs.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python
- Pipenv (optional but recommended for virtual environment management)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MoeAlm/simple-note-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd djangoProject
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

### Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Access the API at `http://localhost:8000/` in your browser or using a tool like [curl](https://curl.se/) or [Postman](https://www.postman.com/).

3. Obtain an authentication token by sending a POST request to `http://localhost:8000/api/token/` with your credentials.

4. Include the obtained token in the Authorization header for subsequent requests:

    ```bash
    curl -H "Authorization: Token YOUR_TOKEN_HERE" http://localhost:8000/api/notes/
    ```

## API Endpoints

- **List Notes**: `GET /api/notes/`
- **Create Note**: `POST /api/notes/`
- **Retrieve Note**: `GET /api/notes/{note_id}/`
- **Update Note**: `PUT /api/notes/{note_id}/`
- **Delete Note**: `DELETE /api/notes/{note_id}/`

For token authentication, use the `Authorization` header with the value `Token YOUR_TOKEN_HERE` in your requests.

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Your feedback is highly appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
