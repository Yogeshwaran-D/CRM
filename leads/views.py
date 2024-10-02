from django.core.mail import send_mail
from django.shortcuts import render,redirect 
from django.urls import reverse
from .models import Leads 
from .forms import LeadModelForm 
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm

class SignupView(CreateView):
    template_name="registration/signup.html"
    form_class=UserCreationForm
    def get_success_url(self) :
        return reverse("login")

class LandingPage(TemplateView):
    template_name="landing.html"

class LeadListView(ListView):
    template_name="leads/leads_list.html"
    queryset=Leads.objects.all() 
    context_object_name="leads"

class LeadDetailView(DetailView):
    template_name="leads/leads_details.html"
    queryset=Leads.objects.all() 
    context_object_name="lead"

class LeadCreateView(CreateView):
    template_name="leads/leads_create.html"
    form_class=LeadModelForm
    def get_success_url(self) :
        return reverse("leads:leads-list")
    def form_valid(self, form):
        send_mail(
            subject="A new lead has been created",
            message="Go to the site to view the new lead",
            from_email="test@gmail.com",
            recipient_list=["test2@gmail.com"]
        )
        return super(LeadCreateView,self).form_valid(form)
    

class LeadsUpdateView(UpdateView):
    template_name="leads/leads_update.html"
    queryset=Leads.objects.all() 
    form_class=LeadModelForm
    context_object_name="lead"
    def get_success_url(self) :
        return reverse("leads:leads-list")
    
class LeadsDeleteView(DeleteView):
    template_name="leads/leads_delete.html"
    queryset=Leads.objects.all() 
    context_object_name="lead"
    def get_success_url(self) :
        return reverse("leads:leads-list")
