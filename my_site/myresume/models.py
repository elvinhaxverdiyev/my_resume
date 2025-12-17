from django.db import models

class Resume(models.Model):
    full_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Ad, Soyad')
    position = models.CharField(max_length=20, blank=True, null=True, verbose_name='Peşə')
    age = models.PositiveIntegerField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True, verbose_name='Linkedin linki')
    github = models.URLField(blank=True, null=True, verbose_name='Github linki')
    instagram = models.URLField(blank=True, null=True, verbose_name='Instagram linki')
    facebook = models.URLField(blank=True, null=True, verbose_name='Facebook linki')
    
    def __str__(self):
        return self.full_name if self.full_name else "Unnamed Resume"
    
    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'CV-ler'
        
        
        
class Projects(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Layihə adı')
    description = models.TextField(blank=True, null=True, verbose_name='Layihə açıqlaması')
    technologies = models.TextField(blank=True, null=True, verbose_name='Texnologiyalar')
    site_link = models.URLField(blank=True, null=True, verbose_name='Sayt adresi')
    github = models.URLField(blank=True, null=True, verbose_name='Github linki')
    
    def __str__(self):
        return self.name if self.name else "Unnamed Project"

    class Meta:
        verbose_name = 'Layihə'
        verbose_name_plural = 'Layihələr'
        
        
class Image(models.Model):
    resume = models.ForeignKey(Resume, related_name='images', on_delete=models.CASCADE, blank=True, null=True, verbose_name='CV')
    projects = models.ForeignKey(Projects, related_name='images', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Layihə')
    image = models.ImageField(upload_to='images/', verbose_name='Şəkil')
    
    def __str__(self):
        if self.projects:
            return f"{self.projects.name} - Şəkil" if self.projects.name else "Layihə Şəkli"
        elif self.resume:
            return f"{self.resume.full_name} - Şəkil" if self.resume.full_name else "CV Şəkli"
        return "Şəkil"
    
    class Meta:
        verbose_name = 'Şəkil'
        verbose_name_plural = 'Şəkillər'