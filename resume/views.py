from django.shortcuts import render
from django.contrib import messages
import requests
from .models import (
    Blog,
    Portfolio,
    Testimonial,
    Certificate,
    Skill
)

from django.views import generic

from .forms import ContactForm

class IndexView(generic.TemplateView):    
    template_name = 'resume/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)          

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        # blogs = Blog.objects.filter(is_active=True)
        blogs = requests.get("https://dev.to/api/articles?username=princeibs").json()
        portfolio = Portfolio.objects.filter(is_active=True)
        skills = Skill.objects.all()

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['blogs'] = blogs[:4]
        context['portfolio'] = portfolio[:3]
        context['skills'] = skills

        return context


class ContactView(generic.FormView):
    template_name = 'resume/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you for contacting. We will in touch.')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'resume/portfolio.html'
    context_object_name = 'portfolio'

    def get_queryset(self):        
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'resume/portfolio-detail.html'
    context_object_name = 'project'
    


class BlogView(generic.ListView):
    template_name = 'resume/blog.html'
    blog = requests.get("https://dev.to/api/articles?username=princeibs").json()
    context_object_name = 'blog'

    def get_queryset(self):
        return self.blog


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'resume/blog-detail.html'
    