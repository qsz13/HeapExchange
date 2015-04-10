from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from account.forms import ProfileForm
from account.models import Profile


class SignUpView(View):
    template_name = "account/sign_up.html"

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=form.clean_password2())
            login(request, new_user)
            return redirect("index")
        else:
            return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = "account/log_in.html"

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = AuthenticationForm(None, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.user.is_staff:
                return redirect("heap_admin")
            else:
                return redirect("index")
        else:
            print form.error_messages
            return render(request, self.template_name, {'form': form})


class ProfileView(View):
    template_name = "account/profile.html"

    def get(self, request):
        form = ProfileForm()
        return render(request, self.template_name, {"form": form})


class SettingView(View):
    template_name = "account/setting.html"

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("index")
        else:
            return render(request, self.template_name, {'form': form})



class AccountView(View):
    template_name = "account/account.html"

    def get(self, request):

        profile_form = ProfileForm()
        setting_form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {"profile_form": profile_form, "setting_form":setting_form})

