from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Task
from .forms import ProfileForm, TaskForm


def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
    else:
        user = None

    return render(request, 'main/base.html', {'user': user})

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
    tasks = Task.objects.filter(profile_id=id).order_by('-date_created')
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

        return redirect(f'/profile/{id}')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'main/profile_update.html', context)


@login_required
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

@login_required
def task_view(request, id):
    task = Task.objects.get(id=id)

    return render(request, 'main/task-view.html', {'task': task})

@login_required
def task_delete(request, id):
    profile = Profile.objects.get(task=id)
    task = Task.objects.get(id=id)
    task.delete()

    return redirect(f'/profile/{profile.id}')

@login_required
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

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'main/task-update.html', context)
