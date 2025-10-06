# Sakshyam Koirala - Professional Portfolio Website

A modern, responsive portfolio website built with Django and Bootstrap, featuring a LinkedIn-inspired design with dark/light mode toggle.

## 🚀 Features

- **Modern LinkedIn-style Design**: Clean, professional layout with smooth animations
- **Dark/Light Mode Toggle**: Seamless theme switching with persistent preferences
- **Fully Responsive**: Mobile-friendly design that works on all devices
- **Interactive Sections**: 
  - Hero section with animated typing effect
  - About section with professional summary
  - Skills showcase with animated badges
  - Featured projects with hover effects
  - Education timeline
  - Contact form with validation
- **Smooth Animations**: Scroll-triggered animations and hover effects
- **Contact Form**: Functional contact form with email notifications
- **SEO Optimized**: Clean URLs and meta tags

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5.3.2, HTML5, CSS3, JavaScript
- **Database**: SQLite (development)
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Inter)

## 📁 Project Structure

```
PROTFOLIO/
├── manage.py
├── requirements.txt
├── README.md
├── portfolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── main/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── management/
│       └── commands/
│           └── populate_data.py
├── templates/
│   ├── base.html
│   └── main/
│       └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd PROTFOLIO
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Populate initial data**
   ```bash
   python manage.py populate_data
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Open your browser**
   Navigate to `http://127.0.0.1:8000/`

## 🎨 Customization

### Personal Information
Update your personal information in the Django admin panel or by running the `populate_data` command.

### Skills
Add or modify skills in the admin panel at `/admin/main/skill/`

### Projects
Manage your projects in the admin panel at `/admin/main/project/`

### Styling
- Modify `static/css/style.css` for custom styling
- Update color scheme by changing CSS variables in the `:root` selector
- Add custom animations in `static/js/script.js`

## 📱 Responsive Design

The website is fully responsive and optimized for:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (320px - 767px)

## 🌙 Dark/Light Mode

The theme toggle automatically saves user preferences in localStorage and applies the selected theme across all pages.

## 📧 Contact Form

The contact form includes:
- Client-side validation
- Server-side validation
- Email notifications (configure SMTP settings in production)
- Success/error messages

## 🚀 Deployment

### Production Settings

1. **Update settings.py**
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

2. **Configure email settings**
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'your-smtp-server.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@domain.com'
   EMAIL_HOST_PASSWORD = 'your-password'
   DEFAULT_FROM_EMAIL = 'your-email@domain.com'
   ```

3. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

### Popular Deployment Platforms

- **Heroku**: Add `Procfile` and `runtime.txt`
- **DigitalOcean**: Use App Platform or Droplets
- **AWS**: Deploy on EC2 or Elastic Beanstalk
- **Vercel**: Use Django deployment guide

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Sakshyam Koirala**
- Email: sakshyam@example.com
- LinkedIn: [Sakshyam Koirala](https://linkedin.com/in/sakshyam-koirala)
- GitHub: [sakshyam-koirala](https://github.com/sakshyam-koirala)

## 🙏 Acknowledgments

- Bootstrap for the responsive framework
- Font Awesome for the icons
- Google Fonts for the typography
- Django community for the excellent framework

---

**Note**: Remember to update the contact information, social media links, and project details with your actual information before deploying.