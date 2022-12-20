from django.shortcuts import render, redirect
from .models import Profile, Task
from .forms import ProfileForm, TaskForm


def index(request):
    return render(request, 'main/base.html', {})

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

def profile_list(request):
    profiles = Profile.objects.filter(user_id=request.user.id)

    return render(request, 'main/profile-list.html', {'profiles': profiles})

def profile_view(request, id):
    tasks = Task.objects.filter(profile_id=id)
    profile = Profile.objects.get(id=id)

    context = {
        'tasks': tasks,
        'profile': profile
    }

    return render(request, 'main/profile-view.html', context)


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

    return render(request, 'main/task-create.html', {'form': form, 'profile': profile})

def task_view(request, id):
    task = Task.objects.get(id=id)

    return render(request, 'main/task-view.html', {'task': task})

def task_delete(request, id):
    profile = Profile.objects.get(task=id)
    task = Task.objects.get(id=id)
    task.delete()

    return redirect(f'/profile/{profile.id}')
