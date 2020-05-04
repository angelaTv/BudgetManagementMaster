from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from accounts.forms import UserCreationForm, UserLoginForm
from accounts.models import Users


class CreateUser(TemplateView):
    template_name = "accounts/register.html"
    model_name = Users
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = {}
        context["form"] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print("inside registration post")
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "created", 'status': 200})


class LoginView(TemplateView):
    template_name = "accounts/login.html"
    # template_name = "accounts/log.html"
    model_name = Users
    form_class = UserLoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = {}
        context["form"] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print("inside login")
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            qs = Users.objects.get(username=username)

            if (qs.username == username) & (qs.password == password):
                request.session['username'] = username
            return JsonResponse({"message": "loginSuccess", 'status': 200})
        else:
            return JsonResponse({"message": "loginFail", 'status': 204})


class Userprofile(TemplateView):
    def get(self, request, *args, **kwargs):
        qs = Users.objects.filter(username=request.session['username'])
        context = {}
        context["qs"] = qs
        return render(request, "accounts/userprofile.html", context)



class Logout(TemplateView):
    def get(self, request, *args, **kwargs):
        print(request.session["username"])
        del request.session["username"]
        print('logged out')
        return redirect('index')
