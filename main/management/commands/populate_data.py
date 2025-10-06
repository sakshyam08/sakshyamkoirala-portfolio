from django.core.management.base import BaseCommand
from main.models import PersonalInfo, Skill, Project, Education


class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **options):
        # Create Personal Info
        personal_info, created = PersonalInfo.objects.get_or_create(
            name="Sakshyam Koirala",
            defaults={
                'title': 'Computer Science Student',
                'tagline': 'Passionate about technology and innovation',
                'bio': 'I am a dedicated Computer Science student with a passion for technology, cybersecurity, and web development. I enjoy exploring new technologies and building innovative solutions that make a difference.',
                'email': 'sakshyam@example.com',
                'location': 'Nepal',
                'linkedin_url': 'https://linkedin.com/in/sakshyam-koirala',
                'github_url': 'https://github.com/sakshyam-koirala',
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created Personal Info'))
        else:
            self.stdout.write(self.style.WARNING('Personal Info already exists'))

        # Create Skills
        skills_data = [
            {'name': 'Graphic Designing', 'category': 'design', 'proficiency': 85, 'icon': 'fas fa-paint-brush'},
            {'name': 'Networking', 'category': 'networking', 'proficiency': 80, 'icon': 'fas fa-network-wired'},
            {'name': 'Linux', 'category': 'system', 'proficiency': 75, 'icon': 'fab fa-linux'},
            {'name': 'Python', 'category': 'programming', 'proficiency': 90, 'icon': 'fab fa-python'},
            {'name': 'Django', 'category': 'programming', 'proficiency': 85, 'icon': 'fab fa-django'},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created skill: {skill.name}'))

        # Create Projects
        projects_data = [
            {
                'title': 'Portfolio Website',
                'description': 'A responsive portfolio website built with Django and Bootstrap, featuring dark/light mode and smooth animations. This project showcases modern web development practices and clean design principles.',
                'short_description': 'A responsive portfolio website with dark/light mode and smooth animations.',
                'tech_stack': 'Django, Bootstrap, JavaScript, HTML, CSS',
                'github_url': 'https://github.com/sakshyam-koirala/portfolio',
                'live_url': 'https://sakshyam-portfolio.herokuapp.com',
                'featured': True,
            },
            {
                'title': 'Security Dashboard',
                'description': 'A cybersecurity monitoring dashboard for network security analysis and threat detection. Built with Python and Django, this tool helps organizations monitor their network security in real-time.',
                'short_description': 'A cybersecurity monitoring dashboard for network security analysis.',
                'tech_stack': 'Python, Django, Linux, Network Security',
                'github_url': 'https://github.com/sakshyam-koirala/security-dashboard',
                'live_url': 'https://security-dashboard.herokuapp.com',
                'featured': True,
            },
            {
                'title': 'Network Monitor',
                'description': 'A network monitoring tool built with Python for real-time network analysis and performance tracking. This application helps network administrators monitor network health and performance.',
                'short_description': 'A network monitoring tool for real-time network analysis.',
                'tech_stack': 'Python, Networking, Linux, System Administration',
                'github_url': 'https://github.com/sakshyam-koirala/network-monitor',
                'live_url': 'https://network-monitor.herokuapp.com',
                'featured': False,
            },
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created project: {project.title}'))

        # Create Education
        education_data = {
            'degree': 'Bachelor of Computer Science',
            'institution': 'University Name',
            'field_of_study': 'Computer Science',
            'start_year': 2022,
            'end_year': 2026,
            'description': 'Pursuing a comprehensive Computer Science degree with focus on software development, cybersecurity, and network administration. Coursework includes data structures, algorithms, database systems, computer networks, and cybersecurity fundamentals.',
            'current': True,
        }
        
        education, created = Education.objects.get_or_create(
            degree=education_data['degree'],
            institution=education_data['institution'],
            defaults=education_data
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created education: {education.degree}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated database with initial data!'))