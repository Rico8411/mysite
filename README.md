# Django Blog

This project is a simple blog built with the Django framework, allowing you to publish and manage blog posts easily.

## Features
- Create, edit, and delete blog posts
- List view and detail page for each post
- View counter for each post
- Admin panel for managing posts
- Responsive design using Bootstrap

## Prerequisites
- Python 3.8+
- Django 5.1+

## Setup & Usage
1. Install dependencies (if needed):
   ```bash
   pip install django
   ```
2. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```
4. Access the site:
   - Home: http://localhost:8000/
   - Blog: http://localhost:8000/blog/
   - Admin: http://localhost:8000/admin/

## Create Superuser
To access the admin panel:
```bash
python manage.py createsuperuser
```

## Project Structure
- `blog/` : Blog application
- `website/` : Main website pages (home, about, contact)
- `templates/` : HTML templates
- `statics/` : Static files (CSS, JS, images)

## License
This project is licensed under the MIT License.

