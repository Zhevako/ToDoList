from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages


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


def remove(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()
    messages.info(request, 'Item removed!')
    return redirect('index')