# Django Multilingual FAQ System

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Dummy Data](#dummy-data)
- [Testing](#testing)
- [Contribution Guidelines](#contribution-guidelines)
- [Submission Guidelines](#submission-guidelines)
- [License](#license)

## Introduction
The **Django Multilingual FAQ System** is a web application that allows users to manage FAQs with multi-language support. It uses Google Translate for automated translations and provides a REST API to fetch and manage FAQs. The application is optimized for performance with caching using Redis.

## Features
- Create, update, and delete FAQs with WYSIWYG editor support.
- Automated multi-language translation (e.g., English, Hindi, Bengali).
- REST API with language-based query parameters.
- Caching mechanism using Redis for faster performance.
- Admin panel for managing FAQs.
- PEP8-compliant code and unit tests.

## Technologies Used
- **Backend**: Django 5.1.5
- **Database**: SQLite (default, can be changed)
- **Caching**: Redis
- **WYSIWYG Editor**: django-ckeditor
- **Translation**: googletrans API
- **Testing**: pytest

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/multilingual-faq.git
cd multilingual-faq
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Redis
- Install Redis:
  ```bash
  sudo apt update
  sudo apt install redis
  ```
- Start Redis:
  ```bash
  sudo service redis-server start
  ```
- Verify Redis:
  ```bash
  redis-cli ping
  ```
  Expected response: `PONG`

### 5. Migrate Database
```bash
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

### 7. Access the Application
Open your browser and visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

### Adding Dummy Data
Use the Django shell to add dummy FAQs:
```bash
python manage.py shell
```
```python
from faq.models import FAQ
FAQ.objects.create(
    question="What is Django?",
    answer="Django is a high-level Python web framework.",
    language="en"
)
```
Alternatively, load dummy data from fixtures:
```bash
python manage.py loaddata faq/fixtures/faqs.json
```

## API Endpoints

### 1. List All FAQs
- **URL**: `/api/faqs/`
- **Method**: GET
- **Query Parameters**: `?lang=<language_code>` (e.g., `en`, `hi`, `bn`)
- **Response Example**:
  ```json
  [
      {
          "question": "What is Django?",
          "answer": "Django is a high-level Python web framework."
      }
  ]
  ```

### 2. Create a New FAQ
- **URL**: `/api/faqs/`
- **Method**: POST
- **Payload Example**:
  ```json
  {
      "question": "What is Django ORM?",
      "answer": "Django ORM is an abstraction layer for databases.",
      "language": "en"
  }
  ```

### 3. Update an FAQ
- **URL**: `/api/faqs/<id>/`
- **Method**: PUT
- **Payload Example**:
  ```json
  {
      "question": "Updated Question?",
      "answer": "Updated Answer.",
      "language": "en"
  }
  ```

### 4. Delete an FAQ
- **URL**: `/api/faqs/<id>/`
- **Method**: DELETE

## Dummy Data
Example data for testing:
```json
[
  {
    "question": "What is Django?",
    "answer": "Django is a high-level Python web framework.",
    "language": "en"
  },
  {
    "question": "How to install Django?",
    "answer": "Use pip: pip install django.",
    "language": "en"
  }
]
```

## Testing
### Run Tests
- **Install pytest**:
  ```bash
  pip install pytest
  ```
- **Run Tests**:
  ```bash
  pytest
  ```

### Code Coverage
- Generate a code coverage report:
  ```bash
  pytest --cov=faq
  ```

## Contribution Guidelines
- Follow PEP8 guidelines for Python code.
- Use meaningful commit messages (e.g., `feat: Add multilingual support`).
- Submit a pull request with a detailed description of changes.

## Submission Guidelines
### Steps to Submit Your Solution
1. Attempt the assignment and complete your solution.
2. Open an issue in this repository with the relevant tag (backend or frontend, depending on the test you're applying for).
3. Once done, tag `@theakshaydhiman` in the issue, and we will review your code.
4. Include the link to your GitHub repository, which must be publicly accessible.

### Repository Requirements
Ensure your repository contains a detailed README with:
- Installation steps
- API usage examples
- Any additional notes or instructions

Use Git for version control, with meaningful commit messages.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

