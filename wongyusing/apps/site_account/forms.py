from django import forms
from apps.site_account.models import UserProfile


class ProfileForm(forms.Form):

    nickname = forms.CharField(label='Nickname', max_length=50, required=False)



class SignupForm(forms.Form):

    def signup(self, request, user):
        user_profile = UserProfile()
        user_profile.user = user
        user.save()
        user_profile.save()
