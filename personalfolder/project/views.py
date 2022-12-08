""" from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html") """
from django.shortcuts import render, redirect
from django.views import View
from .models import Project
from django.http import HttpResponse

# Create your views here.
class IndexView(View):
    def get(self, request):
        projects = Project.objects.all()
        context = {
            "projects":projects
        }
        print(context)
        return render(request, "index.html", context)

class Inner(View):
    def get(self, request):
        return render(request, "inner.html")

    def post(self, request):
        photo = request.POST['photo']
        title = request.POST['title']
        description = request.POST['description']
        tags = request.POST['tags']
        url = request.POST['url']
        print(title)
        if not photo == '' and not photo == None:
            project = Project(photo=photo, title=title, description=description, url=url, tags=tags)
            project.save()
            return redirect("index")
        return HttpResponse("No se han insertado datos")