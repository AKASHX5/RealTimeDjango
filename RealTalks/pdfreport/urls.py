from django.contrib import admin
from django.urls import path,include
from .views import render_pdf_view,GeneratePdf, generate_pdf
urlpatterns = [
    path('pdf', render_pdf_view,name='pdf'),
    path('newpdf', generate_pdf, name='pdf'),
    path('new', GeneratePdf.as_view(),name='pdf'),
]
