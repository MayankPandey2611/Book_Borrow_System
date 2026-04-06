📚 Book Borrow System
A modern web-based Library Management System built with Django that allows students to browse, borrow, and suggest books, with a dedicated admin panel for managing the library.
🔗 Live Demo: https://book-borrow-system-6.onrender.com/

✨ Features
👨‍🎓 Student

Register and log in securely
Browse all available books with cover images
Issue / borrow a book with a single click
Suggest new books via the contact/suggestion form

🛠️ Admin

Dedicated admin login portal
Add, update, or remove books
Manage borrowing records and students


🖥️ Tech Stack
LayerTechnologyBackendPython, DjangoFrontendHTML, CSSDatabaseSQLite (dev) / PostgreSQL (prod)DeploymentRender

🚀 Getting Started
Prerequisites

Python 3.x
pip

Installation
bash# 1. Clone the repository
git clone https://github.com/MayankPandey2611/Book_Borrow_System.git
cd Book_Borrow_System/library_management

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (admin)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

📁 Project Structure
Book_Borrow_System/
└── library_management/
    ├── library_management/   # Project settings & URLs
    ├── <app>/                # Core app (models, views, templates)
    ├── static/
    │   └── images/
    │       └── book_images/  # Book cover images
    ├── templates/            # HTML templates
    ├── manage.py
    ├── requirements.txt
    └── Procfile              # For Render deployment

🔗 Key Routes
URLDescription/Home page — browse all books/student-register/Student sign-up/student-login/Student sign-in/admin-login/Admin login portal/borrow/<id>/Issue / borrow a specific book

☁️ Deployment
This project is deployed on Render using a Procfile.
To deploy your own instance:

Push your code to GitHub.
Create a new Web Service on Render and connect your repository.
Set the build command to pip install -r requirements.txt.
Set the start command to gunicorn library_management.wsgi.
Add any required environment variables (e.g., SECRET_KEY, DEBUG, DATABASE_URL).


📬 Book Suggestion
Users can suggest new books directly from the home page using the Suggest Books form, which collects the user's name, email, contact, and message.

🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

👤 Author
Mayank Pandey
GitHub: @MayankPandey2611

📄 License
This project is open source and available under the MIT License.
