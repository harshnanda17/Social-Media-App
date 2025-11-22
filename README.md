<img width="1366" height="768" alt="Screenshot 2025-11-22 114231" src="https://github.com/user-attachments/assets/1a86cafb-3337-4610-8bc2-0f7c8815e471" />


# Talkify - Social Media Application

A modern Django-based social media web application that enables users to connect, share content, and interact with each other in real-time.

## 📋 Features

- **User Authentication**: Secure user registration and login system
- **User Profiles**: Create and customize user profiles with profile pictures
- **Posts & Feeds**: Share posts, view news feeds, and explore content from other users
- **User Search**: Search and discover other users in the application
- **Profile Management**: Edit profile information and upload profile images
- **Real-time Video Streaming**: Integrated Agora RTC for video calls and live streaming
- **Responsive Design**: Mobile-friendly UI built with modern CSS and JavaScript
- **Dark Sidebar**: Professional dark-themed sidebar navigation

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3, JavaScript
- **Video Technology**: Agora RTC (v4.24.0 and v4.8.0)
- **Server**: Django Development Server / WSGI

## 📁 Project Structure

```
Talkify/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── media/                   # User uploaded files
├── static/
│   ├── assets/              # JavaScript libraries (Agora RTC)
│   ├── CSS/                 # Stylesheets
│   ├── images/              # Image storage (posts, profiles)
│   ├── js/                  # JavaScript files
│   └── style/               # Additional styling
├── templates/               # HTML templates
│   ├── main.html
│   ├── profile.html
│   ├── room.html            # Video room
│   ├── lobby.html           # Video lobby
│   ├── explore.html
│   ├── search.html
│   ├── edit_profile.html
│   ├── signup.html
│   ├── loginn.html
│   └── ...
├── Talkify/                 # Main Django app
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── userauth/                # User authentication app
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    └── migrations/
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Social-Media-App
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   cd Talkify
   python manage.py migrate
   ```

5. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main app: `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

## 📝 Usage

### User Registration & Login
- Sign up with email and password
- Login to access the application
- View and edit your profile

### Creating Posts
- Navigate to the main feed
- Create a new post with text content
- Upload post images
- Share with the community

### Discovering Users
- Use the search feature to find other users
- View user profiles
- Explore content from the platform

### Video Streaming
- Access the lobby to start a video room
- Join existing rooms
- Real-time video/audio communication with other users

## 🎨 Customization

### Sidebar Color
To change the sidebar color, edit `static/CSS/app.css`:
```css
.sidebar {
    background-color: #2c3e50;  /* Change this hex color */
    height: 100vh;
    color: white;
}
```

### Styling
- Main styles: `static/CSS/main.css`
- App-specific styles: `static/CSS/app.css`

## 🔧 Configuration

Edit `Talkify/settings.py` to configure:
- Database settings
- Installed apps
- Static files location
- Media files location
- Allowed hosts
- Debug mode

## 📦 Dependencies

See `requirements.txt` for all project dependencies. Key packages include:
- Django
- Pillow (image processing)
- And other supporting libraries

## 🗄️ Database

The application uses SQLite for development. To use a different database (PostgreSQL, MySQL, etc.), update the `DATABASES` configuration in `settings.py`.

## 🚀 Deployment

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Use a production database (PostgreSQL recommended)
4. Set up environment variables for sensitive data
5. Use Gunicorn or similar WSGI server
6. Configure static files serving
7. Set up SSL/HTTPS

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Commit with clear messages
5. Push to the branch
6. Create a pull request

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👤 Author

Created by harshnanda17

## 📞 Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

## 🎯 Future Enhancements

- [ ] Direct messaging between users
- [ ] Post likes and comments
- [ ] Notifications system
- [ ] User following/followers
- [ ] Stories feature
- [ ] Advanced search filters
- [ ] Analytics dashboard
- [ ] Mobile app version

---

**Last Updated**: November 2025
