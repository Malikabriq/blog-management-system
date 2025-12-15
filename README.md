Blog Management System

A modern, easy-to-use personal blog platform built with FastAPI and PostgreSQL. This project allows you to create, manage, and publish articles, with a clean separation between guest and admin sections.

Features
Guest Section

View all published blog articles.

Read full articles with publication dates.

Responsive and user-friendly interface.

Admin Section

Create, edit, and delete blog articles.

Secure authentication for admins.

Easy-to-manage backend powered by FastAPI.

Technologies Used

Backend: Python, FastAPI

Database: PostgreSQL, SQLAlchemy

Authentication: JWT / OAuth (if implemented)

Frontend (optional): HTML/CSS/JavaScript or a templating engine

Version Control: Git & GitHub

Installation

Clone the repository:

git clone https://github.com/Malikabriq/blog-management-system.git
cd blog-management-system


Create a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows:

.\venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Set up environment variables:

Create a .env file in the project root:

DATABASE_URL=postgresql://username:password@localhost/blog_db
SECRET_KEY=your_secret_key


Run database migrations (if using Alembic):

alembic upgrade head


Start the server:

uvicorn main:app --reload

Usage

Visit http://127.0.0.1:8000 to view the blog as a guest.

Visit /admin to log in and manage articles.

Contributing

Fork the repository.

Create a new branch: git checkout -b feature/YourFeature.

Make your changes and commit: git commit -m "Add some feature".

Push to your branch: git push origin feature/YourFeature.

Open a Pull Request.

License

This project is licensed under the MIT License.

Contact

GitHub: MalikAbriq
Email: mrabriq756@gmail.com
Project Page url :https://roadmap.sh/projects/personal-blog
