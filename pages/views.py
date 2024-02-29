from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import HttpResponseRedirect
from django import forms
from .models import User

class HomePageView(TemplateView): 
    template_name = 'pages/home.html'

class UserIndexView(View): 
    template_name = 'users/index.html' 

    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Users - Perfume Online Store" 
        viewData["subtitle"] =  "List of users" 
        viewData["users"] = User.objects.all( )

        return render(request, self.template_name, viewData) 
    
class UserShowView(View): 
    template_name = 'users/show.html' 

    def get(self, request, id): 
        try: 
            user_id = int(id)
            if user_id < 1:
                raise ValueError("User id must be 1 or greater")
            user = get_object_or_404(User, pk=user_id)
        
        except:
            return HttpResponseRedirect(reverse('home'))
        
        viewData = {}
        user = get_object_or_404(User, pk=user_id)
        viewData["title"] = user.name + " - Perfume Online Store" 
        viewData["subtitle"] =  user.name + " - User information" 
        viewData["user"] = user

        return render(request, self.template_name, viewData)
    
class UserForm(forms.ModelForm):
    name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    email_address = forms.CharField(required=True)
    country = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['name', 'address', 'email_address', 'country']


class UserCreateView(View):
    template_name = 'users/create.html'

    def get(self, request):
        form = UserForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('created'))

        else:
            viewData = {}
            viewData["title"] = "Create user"
            viewData["form"] = form
            return render(request, self.template_name, viewData)

class UserCreatedPageView(TemplateView): 
    template_name = 'users/created.html'

class UserListView(ListView): 
    model = User 
    template_name = 'user_list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['name'] = 'Users - Perfume Online Store' 
        context['email_address'] = 'List of users' 

        return context 

class DeleteUserView(View):
    def post(self, request, id):
        user_id = int(id)
        user = User.objects.get(id=user_id)
        user.delete()

        return redirect('index')