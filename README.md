# 🌐 ConnectNest

![Built with Django](https://img.shields.io/badge/Built%20with-Django-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Development-blue?style=flat-square)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square)
![License: Undefined](https://img.shields.io/badge/License-Not%20Specified-lightgrey?style=flat-square)

**ConnectNest** is a Django-based social networking web application where users can connect, share posts, manage friendships, and explore content with a simple and clean interface.

---

## 🖼️ Preview

> *Screenshots coming soon!*

You can include:
- 📸 Homepage screenshot  
- 👥 Friend request UI  
- 📝 Timeline post example  
- ⚙️ Admin dashboard

---

## 🚀 Features

- 👤 User Registration & Authentication
- 🤝 Friend Request System
- 📝 Timeline & Post Sharing
- 💬 Like & Comment Support *(coming soon)*
- 🔍 AI-Powered Search *(experimental)*
- 🛠 Django Admin Control Panel

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

##📬 Contributing
Pull requests are welcome! If you’d like to help:

Fork the repo

Create a feature branch (git checkout -b feature/your-feature)

Commit your changes

Push to your fork

Open a pull request 🚀
---


##📄 License
⚠️ No license specified yet.
For public use and contributions, it's recommended to add an MIT License or similar.
---

##👤 Author
GitHub: @mkkotlin
📬 Feel free to connect for feedback, ideas, or collaboration!



> ✅ **Next Step Suggestion**: Add a `preview.png` or screenshots inside a `/screenshots/` folder and update the README with actual image paths like:

```markdown
![Homepage Preview](screenshots/home.png)
