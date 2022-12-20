from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Task
from .forms import ProfileForm, TaskForm


def index(request):
    return render(request, 'main/base.html', {})

@login_required
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            profile = Profile.objects.create(
                title=form.cleaned_data['title'],
                user_id=request.user.id
            )
        
        return redirect(f'/profile/{profile.id}')
    else:
        form = ProfileForm()

    return render(request, 'main/profile-create.html', {'form': form})

@login_required
def profile_list(request):
    profiles = Profile.objects.filter(user_id=request.user.id)

    return render(request, 'main/profile-list.html', {'profiles': profiles})

@login_required
def profile_view(request, id):
    tasks = Task.objects.filter(profile_id=id)
    profile = Profile.objects.get(id=id)

    context = {
        'tasks': tasks,
        'profile': profile
    }

    return render(request, 'main/profile-view.html', context)

@login_required
def profile_delete(request, id):
    profile = Profile.objects.get(id=id)
    profile.delete()

    return redirect(f'/profile/')

@login_required
def profile_update(request, id):
    profile = Profile.objects.get(id=id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

        return redirect(f'/profile/')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'main/profile_update.html', {'form': form})


def task_create(request, id):
    profile = Profile.objects.get(id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = Task.objects.create(
                profile_id=profile.id,
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description')
            )
            
        return redirect(f'/profile/{profile.id}')
    else:
        form = TaskForm()

    context = {
        'form': form, 
        'profile': profile
    }

    return render(request, 'main/task-create.html', context)

def task_view(request, id):
    task = Task.objects.get(id=id)

    return render(request, 'main/task-view.html', {'task': task})

def task_delete(request, id):
    profile = Profile.objects.get(task=id)
    task = Task.objects.get(id=id)
    task.delete()

    return redirect(f'/profile/{profile.id}')

def task_update(request, id):
    task = Task.objects.get(id=id)
    profile = Profile.objects.get(task=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

        return redirect(f'/profile/{profile.id}')
    else:
        form = TaskForm(instance=task)

    return render(request, 'main/task-update.html', {'form': form})
