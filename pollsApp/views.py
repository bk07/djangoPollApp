from django.shortcuts import render


# Create your views here.
from pollsApp.forms import HomeForm
from pollsApp.models import Question


def home_view(request):
    home_view = HomeForm
    return render(request, 'home.html', {'form': home_view})


def poll_view(request):
    questions = Question.objects.all()
    email = request.POST.get('email')
    return render(request, 'pollview.html', {'questions': questions, 'email':email})
