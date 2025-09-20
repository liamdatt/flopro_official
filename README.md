# FloPro Official Website

A modern, futuristic Django website for FloPro - Jamaica's premier business automation company.

## 🚀 Features

- **Modern Tech Theme**: Futuristic design with dark backgrounds, glowing effects, and cyberpunk aesthetics
- **Responsive Design**: Mobile-first approach using Bootstrap 5
- **YouTube Video Integration**: Homepage features a prominent video section
- **Social Media Integration**: Links to LinkedIn, YouTube, Twitter, and Instagram
- **Content Management**: Django admin panel for easy content updates
- **Multi-page Layout**: Home, About, Services, Team, and Contact pages

## 🛠️ Tech Stack

- **Backend**: Django 5.2.6
- **Frontend**: Bootstrap 5, Custom CSS, JavaScript
- **Fonts**: Orbitron & Rajdhani (Google Fonts)
- **Icons**: Font Awesome 6
- **Database**: SQLite (development)

## 📁 Project Structure

```
flopro_official/
├── core/                          # Main Django app
│   ├── models.py                  # Database models
│   ├── views.py                   # View functions
│   ├── urls.py                    # URL patterns
│   ├── admin.py                   # Admin configuration
│   ├── templates/core/            # HTML templates
│   │   ├── base.html             # Base template
│   │   ├── home.html             # Homepage
│   │   ├── about.html            # About page
│   │   ├── services.html         # Services page
│   │   ├── team.html             # Team page
│   │   └── contact.html          # Contact page
│   └── static/core/              # Static files
│       ├── css/style.css         # Custom styles
│       └── js/script.js          # Custom JavaScript
├── flopro_offical/               # Django project settings
├── venv/                         # Virtual environment
├── manage.py                     # Django management script
├── populate_data.py              # Data seeding script
└── flopro.txt                    # Business information
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip (Python package manager)

### Installation

1. **Clone the repository** (if applicable) or navigate to the project directory

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django
   # Note: Pillow is commented out in models.py for now
   ```

4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Populate database with sample data:**
   ```bash
   python populate_data.py
   ```

6. **Create superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser and visit:**
   - **Website**: http://127.0.0.1:8000/
   - **Admin Panel**: http://127.0.0.1:8000/admin/ (if superuser created)

## 🎨 Design Features

### Color Scheme
- **Primary**: Electric blue (#00d4ff)
- **Secondary**: Orange/Amber (#ffc107)
- **Background**: Deep space black with gradients
- **Text**: White/light gray with accent colors

### Typography
- **Headers**: Orbitron (futuristic, monospace)
- **Body**: Rajdhani (technical, sans-serif)

### Effects
- Glowing borders and text shadows
- Smooth hover animations
- Parallax scrolling effects
- Gradient backgrounds
- Glass morphism cards

## 📝 Content Management

The website content is managed through Django's admin interface. You can:

- Update company information (name, description, contact details)
- Add/edit team members
- Manage services and their descriptions
- Configure social media links
- Add YouTube video IDs for the homepage

### Admin Access
1. Visit `/admin/`
2. Login with superuser credentials
3. Navigate to the respective sections to update content

## 🔧 Customization

### Adding a YouTube Video
1. Go to Django Admin → Company Information
2. Find the "Youtube video id" field
3. Add the video ID from the YouTube URL (the part after `v=`)

### Social Media Links
1. Go to Django Admin → Social Media
2. Add/update social media platforms
3. Configure URLs and icon classes

### Services & Team
- Use the admin interface to add/edit services and team members
- Set display order for proper sorting
- Toggle active/inactive status

## 🌐 Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure allowed hosts
3. Set up proper static file serving
4. Use a production database (PostgreSQL recommended)
5. Configure environment variables for secrets
6. Set up proper SSL/HTTPS

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is proprietary to FloPro.

## 📞 Support

For support or questions:
- Email: autom8@floproja.com
- Phone: +1 (876) 824-2268
- Address: 161 Constant Spring Road, Kingston 8, Jamaica

---

**Built with ❤️ for FloPro - Automating Jamaica's Future**
