from django.shortcuts import render

ToDoList = [
    {"name": "Fill up car", "completed": True},
    {"name": "Complete class homeworks", "completed": False},
    {"name": "Contact project group", "completed": False},
    {"name": "Read the study guide", "completed": True},
    {"name": "Attend meeting", "completed": False},
]

# Create your views here.
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def home(request):
    return render(request, "home.html", {"ToDoList": ToDoList})