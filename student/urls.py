from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student_list', views.student_list, name='sd'),
    path('detail_view/<student_id>', views.detail_view, name='detail_view'),
    path('RegisterStudent/', views.RegisterStudent, name='RegisterStudent'),
    path('Update/<student_id>', views.UpdateRegisterStudent, name='update'),
    path('Delete/<student_id>', views.Delete, name='delete'),
    path('products/', views.products, name='products'),
    path('jsoncall/',views.jsoncall,name='jsoncall'),
]
