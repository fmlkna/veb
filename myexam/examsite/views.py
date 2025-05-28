from django.shortcuts import render
from .models import akexam

def akexam_view(request):
    exams = akexam.objects.filter(is_public=True)
    
    if not exams.exists():
        exams = None 

    context = {
        'fio': 'Анастасия Корышева',  
        'group': '241-671',         
        'exams': exams
    }
    return render(request, 'examsite/akexam.html', context)