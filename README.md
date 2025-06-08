# 🌐 ConnectNest

![Built with Django](https://img.shields.io/badge/Built%20with-Django-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Development-blue?style=flat-square)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square)
![License: Undefined](https://img.shields.io/badge/License-Not%20Specified-lightgrey?style=flat-square)

**ConnectNest** is a Django-based social networking web application where users can connect, share posts, manage friendships, and explore content with a simple and clean interface.

---

## 🚀 Features

- 👤 User Registration & Authentication (Custom Model)
- 🤝 Friend Request System
- 📝 Timeline & Post Sharing
- 💬 Like & Comment Support 
- 🔍 AI-Powered Search *(experimental)*
- 🛠 Django Admin Control Panel
---

---

## 📁 Project Structure
ConnectNest/
├── accounts/ # User login, register, and profile logic
├── ai_search/ # AI search integration (placeholder)
├── friendRequest/ # Sending/receiving friend requests
├── timelines/ # Posting and viewing timelines
├── social/ # Project-level settings and routing
├── templates/ # HTML frontend templates
├── static/ # CSS, JS, and images
├── manage.py # Django project entry point
└── requirements.txt # List of Python dependencies



---

## 🛠️ Installation Guide

Follow these steps to run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/mkkotlin/ConnectNest.git
cd ConnectNest

python3 -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Visit: http://127.0.0.1:8000
```


🧪 Testing & Usage
Register a user or login

Try posting to the timeline

Send/accept friend requests

Explore the admin panel at /admin/

---

## 📬 Contributing
Pull requests are welcome! If you’d like to help:

Fork the repo

Create a feature branch (git checkout -b feature/your-feature)

Commit your changes

Push to your fork

Open a pull request 🚀




## 👤 Author
GitHub: @mkkotlin
📬 Feel free to connect for feedback, ideas, or collaboration!



> ✅ **Screenshots**


## 🖼️ Preview

### 🔐 Login Page
![Login Page](screenshots/login_page.png)

### 📝 Register Page
![Register Page](screenshots/register_user.png)

### 👤 Dashboard / Profile Page
![Dashboard or Profile](screenshots/dashboard_or_profile_page.png)

### 🔍 Search & Notifications
![Search and Notification](screenshots/search_and_notofication.png)

### 🧾 Notification Requests
![Notification Requests](screenshots/notification_requests.png)

### 🗨️ Comment Box
![Comment Box](screenshots/comment_box.png)

### 📰 Timeline View
![Timeline Page](screenshots/timeline_page.png)

### ➕ Create Post
![Create Post](screenshots/create_post.png)

### 🔗 Share Feature
![Share Feature](screenshots/share.png)

### 📁 Project Directory Structure
![Project Directory](screenshots/project_directory_or_structures.png)
