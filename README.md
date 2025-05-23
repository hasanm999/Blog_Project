# Blog_Project

A simple blog application built with the Django framework. Users can register, log in, create and delete their own posts. User management (adding/removing users) is handled exclusively by the site admin.

## Features

- User registration and login
- Create, view, and delete personal blog posts
- Admin-only user management
- Built with Django
- API integration planned for future updates

## Getting Started

### Prerequisites

- Python (preferably version 3.10 or later)
- pip (Python package installer)

### Installation

1. Clone the repository:

   `bash
   git clone https://github.com/hasanm999/Blog_Project.git
   cd Blog_Project

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install the dependencies:

pip install -r requirements.txt


4. Apply migrations and set up the database:

python manage.py migrate


5. Run the development server:

python manage.py runserver


6. Access the admin panel:

Create a superuser:

python manage.py createsuperuser

Admin panel URL: http://127.0.0.1:8000/admin/




Development Status

The project is currently under active development on the develop branch. API functionality and other features are planned for future updates.


Contributions

Contributions are welcome! Feel free to open issues or submit a pull request.
