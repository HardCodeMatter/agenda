from django.shortcuts import render, HttpResponseRedirect
from .models import Profile
from .forms import ProfileForm


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
