from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import TemplateDoesNotExist

# @login_required
def root_page_view(request):
    try:
        return render(request, 'pages/maintenance.html')
    except TemplateDoesNotExist:
        return render(request, 'pages/error.html')


# @login_required
def dynamic_pages_view(request, template_name):
    try:
        return render(request, 'pages/maintenance.html')
        # return render(request, f'pages/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/error.html')
