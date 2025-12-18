from django.contrib import admin
from django.utils.html import format_html
from .models import Resume, Projects, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image', 'resume', 'projects')
    verbose_name = 'Şəkil'
    verbose_name_plural = 'Şəkillər'


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    
    list_display = ('full_name', 'position', 'age', 'linkedin_short', 'github_short', 'instagram_short', 'facebook_short', 'images_count')
    list_display_links = ('full_name',)
    search_fields = ('full_name', 'position')
    list_filter = ('position',)
    
    fieldsets = (
        ('Əsas Məlumatlar', {
            'fields': ('full_name', 'position', 'age')
        }),
        ('Sosial Media Linkləri', {
            'fields': ('linkedin', 'github', 'instagram', 'facebook'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [ImageInline]
    
    def linkedin_short(self, obj):
        if obj.linkedin:
            return obj.linkedin[:30] + '...' if len(obj.linkedin) > 30 else obj.linkedin
        return '-'
    linkedin_short.short_description = 'LinkedIn'
    
    def github_short(self, obj):
        if obj.github:
            return obj.github[:30] + '...' if len(obj.github) > 30 else obj.github
        return '-'
    github_short.short_description = 'GitHub'
    
    def instagram_short(self, obj):
        if obj.instagram:
            return obj.instagram[:30] + '...' if len(obj.instagram) > 30 else obj.instagram
        return '-'
    instagram_short.short_description = 'Instagram'
    
    def facebook_short(self, obj):
        if obj.facebook:
            return obj.facebook[:30] + '...' if len(obj.facebook) > 30 else obj.facebook
        return '-'
    facebook_short.short_description = 'Facebook'
    
    def images_count(self, obj):
        return obj.images.count()
    images_count.short_description = 'Şəkillər'


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'description_preview', 'technologies_preview', 'site_link_short', 'github_short', 'images_count')
    list_display_links = ('name',)
    search_fields = ('name', 'description', 'technologies')
    list_filter = ('name',)
    
    fieldsets = (
        ('Layihə Məlumatları', {
            'fields': ('name', 'description', 'technologies', 'main_image')
        }),
        ('Linklər', {
            'fields': ('site_link', 'github')
        }),
    )
    
    inlines = [ImageInline]
    
    def description_preview(self, obj):
        if obj.description:
            return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
        return '-'
    description_preview.short_description = 'Təsvir'
    
    def technologies_preview(self, obj):
        if obj.technologies:
            return obj.technologies[:30] + '...' if len(obj.technologies) > 30 else obj.technologies
        return '-'
    technologies_preview.short_description = 'Texnologiyalar'
    
    def site_link_short(self, obj):
        if obj.site_link:
            return obj.site_link[:30] + '...' if len(obj.site_link) > 30 else obj.site_link
        return '-'
    site_link_short.short_description = 'Sayt Linki'
    
    def github_short(self, obj):
        if obj.github:
            return obj.github[:30] + '...' if len(obj.github) > 30 else obj.github
        return '-'
    github_short.short_description = 'GitHub'
    
    def images_count(self, obj):
        return obj.images.count()
    images_count.short_description = 'Şəkillər'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    
    list_display = ('image_preview', 'resume', 'projects', 'created_info')
    list_display_links = ('image_preview',)
    search_fields = ('resume__full_name', 'projects__name')
    list_filter = ('resume', 'projects')
    
    fieldsets = (
        ('Şəkil Məlumatları', {
            'fields': ('image', 'resume', 'projects')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.image.url)
        return '-'
    image_preview.short_description = 'Şəkil'
    
    def created_info(self, obj):
        if obj.id:
            return f'ID: {obj.id}'
        return '-'
    created_info.short_description = 'Məlumat'
