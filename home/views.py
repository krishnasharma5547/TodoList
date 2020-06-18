from django.shortcuts import render

from home.models import tasks


# Create your views here.
def index(request):
    alertMessage = {'success': False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        ins = tasks(title=title, desc=desc)
        ins.save()
        alertMessage = {'success': True}

    return render(request, 'index.html', alertMessage)


def task(request):
    alltasks = tasks.objects.all()
    taskList = {'list': alltasks}
    return render(request, 'tasks.html', taskList)
