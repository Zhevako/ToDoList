from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    item_list = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = TaskForm()
    context = {
        'item_list': item_list,
        'forms': form,
    }
    return render(request, 'base.html', context)


def remove(request, task_id):
    item = Task.objects.get(id=task_id)
    item.delete()
    return redirect('index')