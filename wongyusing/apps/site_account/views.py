from django.shortcuts import render, get_object_or_404
from apps.site_account.models import UserProfile
from apps.site_account.forms import ProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'account/profile.html', {'user': user,'user_profile':user_profile})

@login_required
def profile_update(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():


            user_profile.nickname = form.cleaned_data['nickname']

            user_profile.save()

            return HttpResponseRedirect(reverse('site_account:profile'))
    else:
        default_data = {'nickname': user_profile.nickname}
        form = ProfileForm(default_data)

    return render(request, 'account/profile_update.html', {'form': form, 'user': user,'user_profile':user_profile})
