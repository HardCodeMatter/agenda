from django.shortcuts import render, HttpResponseRedirect
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
        
        return HttpResponseRedirect(f'/profile/{profile.id}')
    else:
        form = ProfileForm()

    return render(request, 'main/profile-create.html', {'form': form})

def profile_list(request):
    profiles = Profile.objects.filter(user_id=request.user.id)

    return render(request, 'main/profile-list.html', {'profiles': profiles})

def profile_view(request, id):
    tasks = Task.objects.filter(profile_id=id)
    profile = Profile.objects.get(id=id)

    return render(request, 'main/profile-view.html', {'tasks': tasks, 'profile': profile})


def task_create(request, id):
    profile = Profile.objects.get(id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            Task.objects.create(
                profile_id=profile.id,
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description')
            )
            
        return HttpResponseRedirect(f'/profile/{id}/')
    else:
        form = TaskForm()

    return render(request, 'main/task-create.html', {'form': form, 'profile': profile})
