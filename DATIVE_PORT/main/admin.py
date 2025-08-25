from django.contrib import admin
from .models import Project, ResearchPaper, TeamMember, Service, Testimonial, Message, PricingPackage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'completion_date', 'featured']
    list_filter = ['project_type', 'featured', 'completion_date']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ResearchPaper)
class ResearchPaperAdmin(admin.ModelAdmin):
    list_display = ['title', 'paper_type', 'publication_date', 'is_published']
    list_filter = ['paper_type', 'is_published', 'publication_date']
    search_fields = ['title', 'abstract', 'authors']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'email', 'is_active', 'display_order']
    list_filter = ['is_active', 'position']
    search_fields = ['name', 'position', 'bio']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_company', 'rating', 'is_approved']
    list_filter = ['rating', 'is_approved', 'created_at']
    search_fields = ['client_name', 'content']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status', 'received_date']
    list_filter = ['status', 'service', 'received_date']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['received_date']

@admin.register(PricingPackage)
class PricingPackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'package_type', 'price', 'currency', 'is_featured', 'is_active']
    list_filter = ['package_type', 'is_featured', 'is_active']
    search_fields = ['title', 'features']