from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Project(models.Model):
    PROJECT_TYPES = (
        ('web', 'Web Development'),
        ('mobile', 'Mobile App'),
        ('ai', 'AI/ML'),
        ('network', 'Network Solutions'),
        ('research', 'Research Project'),
        ('other', 'Other'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    completion_date = models.DateField()
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    technologies_used = models.CharField(max_length=300, help_text="Comma-separated list of technologies")
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-completion_date']

class ResearchPaper(models.Model):
    PAPER_TYPES = (
        ('academic', 'Academic Research'),
        ('commercial', 'Commercial Research'),
        ('technical', 'Technical Paper'),
    )
    
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    paper_type = models.CharField(max_length=20, choices=PAPER_TYPES)
    authors = models.CharField(max_length=300, help_text="Comma-separated list of authors")
    publication_date = models.DateField()
    journal_or_conference = models.CharField(max_length=200, blank=True, null=True)
    document = models.FileField(upload_to='research_papers/', blank=True, null=True)
    external_link = models.URLField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publication_date']

class TeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    join_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    
    # Social media links
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.position}"
    
    class Meta:
        ordering = ['display_order', 'name']

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="CSS class for the icon (e.g., fas fa-code)")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['display_order']

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100, blank=True, null=True)
    client_company = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Testimonial from {self.client_name}"
    
    class Meta:
        ordering = ['-created_at']

class Message(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
        ('archived', 'Archived'),
    )
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    received_date = models.DateTimeField(auto_now_add=True)
    replied_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-received_date']

class PricingPackage(models.Model):
    PACKAGE_TYPES = (
        ('development', 'Development'),
        ('research', 'Research'),
        ('network', 'Network'),
    )
    
    title = models.CharField(max_length=100)
    package_type = models.CharField(max_length=20, choices=PACKAGE_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='TZS')
    period = models.CharField(max_length=20, default='project', help_text="e.g., project, month, etc.")
    features = models.TextField(help_text="One feature per line")
    is_featured = models.BooleanField(default=False)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def get_features_list(self):
        return self.features.split('\n')
    
    def __str__(self):
        return f"{self.title} - {self.price} {self.currency}"
    
    class Meta:
        ordering = ['package_type', 'display_order']