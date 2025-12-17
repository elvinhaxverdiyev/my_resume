from django.views import View
from django.shortcuts import render, get_object_or_404

from .models import Resume, Projects

__all__ = [
    'HomeView',
    'ProjectsDetailView'
]

class HomeView(View):
    def get(self, request):
        resume = Resume.objects.first()
        
        projects = Projects.objects.all()

        context = {
            'resume': resume,
            'projects': projects,
        }
        return render(request, 'index.html', context)
    
    
class ProjectsDetailView(View):
    
    def get(self, request, project_id):
        project = get_object_or_404(Projects, id=project_id)
        resume = Resume.objects.first()
        
        technologies_list = []
        if project.technologies:
            technologies_list = [tech.strip() for tech in project.technologies.split(',') if tech.strip()]
        
        context = {
            'project': project,
            'resume': resume,
            'technologies_list': technologies_list,
        }
        return render(request, 'project-detail.html', context)
