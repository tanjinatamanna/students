from django.shortcuts import render, redirect, get_object_or_404
from .forms import CVForm
from .models import CV
from django.template.loader import get_template
from django.http import HttpResponse
from io import BytesIO

try:
    from xhtml2pdf import pisa
    XHTML2PDF_AVAILABLE = True
except Exception:
    XHTML2PDF_AVAILABLE = False

def home(request):
    return render(request, 'cvbuilder/home.html')

def cv_create(request):
    form = CVForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        cv = form.save()
        return render(request, 'cvbuilder/cv_preview.html', {'cv': cv})
    return render(request, 'cvbuilder/cv_form.html', {'form': form})

def cv_list(request):
    cvs = CV.objects.order_by('-created_at')
    return render(request, 'cvbuilder/cv_preview.html', {'cvs': cvs})

def cv_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    return render(request, 'cvbuilder/cv_preview.html', {'cv': cv})

def download_cv(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    if XHTML2PDF_AVAILABLE:
        template = get_template('cvbuilder/cv_download.html')
        html = template.render({'cv': cv})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{cv.full_name}_CV.pdf"'
        pisa.CreatePDF(html, dest=response)
        return response
    else:
        return render(request, 'cvbuilder/cv_download.html', {'cv': cv})


