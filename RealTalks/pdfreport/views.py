from datetime import date

from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .utils import render_to_pdf
from xhtml2pdf.config.httpconfig import httpConfig
import tempfile
from .models import Customer
httpConfig.save_keys('nosslcheck', True)

# Create your views here.

def render_pdf_view(request):
    template_path = 'report.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def generate_pdf(request):
    """Generate pdf."""
    # Model data
    people = Customer.objects.all().order_by('name')

    # Rendered
    html_string = render_to_string('report2.html', {'people': people})
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response





class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': date.today(),
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('report2.html', data)
        return HttpResponse(pdf, content_type='application/pdf')