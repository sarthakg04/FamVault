# views.py
from django.shortcuts import render
from .models import Folder, File

def file_manager(request):
    folders = Folder.objects.all()
    folder_structure = []
    for folder in folders:
        files = File.objects.filter(folder=folder)
        file_names = [file.name for file in files]
        folder_structure.append({'name': folder.name, 'files': file_names})
    return render(request, 'file_manager.html', {'folders': folder_structure})


def directory_structure(request):
    paths = []
    with open('path_list.txt', 'r') as file:
        for line in file:
            paths.append(line.strip())
    return render(request, 'directory_structure.html', {'paths': paths})
