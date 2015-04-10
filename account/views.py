from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from account.models import Profile


class SignUpView(View):
    template_name = "account/sign_up.html"

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=form.clean_password2())
            login(request, new_user)
            return redirect("index")
        else:
            return render(request, self.template_name, {'form':form})



class LoginView(View):
    template_name = "account/log_in.html"

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = AuthenticationForm(None, request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect("index")
        else:
            print form.error_messages
            return render(request, self.template_name,{'form':form})


class ProfileView(TemplateView):
    template_name = "account/profile.html"

    # def get(self, request):
    #     pass