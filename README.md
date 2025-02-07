# Blog WebApp

A full-featured Blog Web Application built with modern web technologies.

## Features

- User Authentication (Login/Signup)
- Create, Read, Update, and Delete (CRUD) blog posts
- User Profile Management
- Responsive and Mobile-Friendly UI
- Rich Text Editor for blog content
- Secure User Sessions
- Admin Dashboard

## Technologies Used

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python (Django)
- **Database:** SQLite
- **Authentication:** Django Authentication System

## App Diagram
![Screenshot 2025-02-01 165849](https://github.com/user-attachments/assets/68171a91-605b-498f-9e73-4f7ccc574b61)



## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- Virtualenv (optional but recommended)

### Steps to Install

1. **Clone the repository:**
   ```sh
   git clone https://github.com/RadadiyaAditya/Blog_WebApp.git
   cd Blog_WebApp
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```sh
   python manage.py migrate  # If using Django
   ```

5. **Run the application:**
   ```sh
   python manage.py runserver  # For Django
   ```

6. Open your browser and go to `http://127.0.0.1:5000/` (Flask) or `http://127.0.0.1:8000/` (Django).

## Usage

- Register a new account or log in with an existing one.
- Create new blog posts with a rich text editor.
- Edit or delete your own blog posts.
- View, like, and comment on blog posts.
- Manage your profile settings.

## Contributing

Contributions are welcome! Follow these steps to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -m 'Add new feature'`)
4. Push to your branch (`git push origin feature-branch`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to reach out:
- **GitHub Issues:** [Create a new issue](https://github.com/RadadiyaAditya/Blog_WebApp/issues)
- **Email:** radadiyaaditya@example.com
