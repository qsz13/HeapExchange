import os
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from account.forms import ProfileForm
from post.models import Tag


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
        self.class_taken = request.user.profile.timetable
        profile_form = ProfileForm(instance=request.user.profile)
        setting_form = PasswordChangeForm(request.user)
        tags = request.user.profile.interest_tag.all()
        avatar = request.user.profile.avatar
        return render(request, self.template_name,
                      {"avatar": avatar, "profile_form": profile_form, "setting_form": setting_form,
                       'classes_number': self.classes_number,
                       'class_taken': self.class_taken, 'tags': tags})


    def post(self, request):
        self.class_taken = request.user.profile.timetable
        profile_form = ProfileForm(instance=request.user.profile)
        setting_form = PasswordChangeForm(request.user)
        tags = request.user.profile.interest_tag.all()

        if 'profile' in request.POST:
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect("index")
            else:

                return render(request, self.template_name, {"profile_form": profile_form, "setting_form": setting_form,
                                                            'classes_number': self.classes_number,
                                                            'class_taken': self.class_taken, 'tags': tags})

        elif 'setting' in request.POST:
            setting_form = PasswordChangeForm(user=request.user, data=request.POST)
            if setting_form.is_valid():
                setting_form.save()
                update_session_auth_hash(request, setting_form.user)
                return redirect("index")
            else:
                return render(request, self.template_name, {"profile_form": profile_form, "setting_form": setting_form,
                                                            'classes_number': self.classes_number,
                                                            'class_taken': self.class_taken, 'tags': tags})

        elif 'time-table' in request.POST:
            table = request.POST['table']
            profile = request.user.profile
            profile.timetable = table
            profile.save()
            self.class_taken = table
            return render(request, self.template_name, {"profile_form": profile_form, "setting_form": setting_form,
                                                        'classes_number': self.classes_number,
                                                        'class_taken': self.class_taken, 'tags': tags})

        elif 'interest' in request.POST:
            tags = request.POST.getlist('tags')
            print tags
            for tag in tags:
                t, created = Tag.objects.get_or_create(name=tag.lower())

                request.user.profile.interest_tag.add(t)
            return render(request, self.template_name, {"profile_form": profile_form, "setting_form": setting_form,
                                                        'classes_number': self.classes_number,
                                                        'class_taken': self.class_taken, 'tags': tags})

