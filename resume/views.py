from django.shortcuts import render
from django.contrib import messages
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
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        skills = Skill.objects.all()

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['blogs'] = blogs
        context['portfolio'] = portfolio
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
    paginated_by = 10

    def get_queryset(self):
        data = super().get_queryset().filter(is_active=True)
        return data


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'resume/portfolio-detail.html'


class BlogView(generic.ListView):
    model = Blog
    template_name = 'resume/blog.html'
    paginated_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'resume/blog-detail.html'
    