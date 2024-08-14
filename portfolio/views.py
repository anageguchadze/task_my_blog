from django.shortcuts import render, redirect

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        return redirect('allgood')
    return render(request, 'portfolio/contact.html')

def allgood_view(request):
    return render(request, 'portfolio/allgood.html')

def projects_view(request):
    projects = [
        {'name': 'TODO app', 'description': 'The coolest TODO aplication'},
        {'name': 'Facebook Clone', 'description': 'Facebook clone aplication'},
        {'name': 'Facebook Clone', 'description': 'Facebook clone aplication'},
        {'name': 'Facebook Clone', 'description': 'Facebook clone aplication'},

    ]
    return render(request, 'portfolio/projects.html', {'projects': projects})