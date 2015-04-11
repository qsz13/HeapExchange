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


class AccountView(View):
    template_name = "account/account.html"
    classes_number = [i for i in range(1, 12)]
    class_taken = None

    def get(self, request):
        self.class_taken=request.user.profile.timetable
        profile_form = ProfileForm(instance=request.user.profile)
        setting_form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {"profile_form": profile_form, "setting_form": setting_form,
                                                    'classes_number': self.classes_number,
                                                    'class_taken': self.class_taken})


    def post(self, request):
        self.class_taken=request.user.profile.timetable
        profile_form = ProfileForm(instance=request.user.profile)
        setting_form = PasswordChangeForm(request.user)

        if 'profile' in request.POST:
            profile_form = ProfileForm(request.POST, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect("index")
            else:

                return render(request, self.template_name, {"profile_form": profile_form, "setting_form": setting_form,
                                                            'classes_number': self.classes_number,
                                                            'class_taken': self.class_taken})

        elif 'setting' in request.POST:
            setting_form = PasswordChangeForm(user=request.user, data=request.POST)
            if setting_form.is_valid():
                setting_form.save()
                update_session_auth_hash(request, setting_form.user)
                return redirect("index")
            else:
                return render(request, self.template_name, {"profile_form": profile_form, "setting_form": setting_form,
                                                            'classes_number': self.classes_number,
                                                            'class_taken': self.class_taken})

        elif 'time-table' in request.POST:
            table = request.POST['table']
            profile = request.user.profile
            profile.timetable = table
            profile.save()
            self.class_taken = table
            return render(request, self.template_name, {"profile_form": profile_form, "setting_form": setting_form,
                                                            'classes_number': self.classes_number,
                                                            'class_taken': self.class_taken})

