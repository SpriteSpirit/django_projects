from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import StudentListView, contact, StudentCreateView, StudentUpdateView, StudentDetailView, \
    StudentDeleteView, toggle_activity

app_name = MainConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('contact/', cache_page(60)(contact), name='contact'),
    path('create/', StudentCreateView.as_view(), name='create_student'),
    path('edit/<int:pk>', StudentUpdateView.as_view(), name='update_student'),
    path('view/<int:pk>', StudentDetailView.as_view(), name='view_student'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='delete_student'),
    path('activity/<int:pk>', toggle_activity, name='toggle_activity'),
]
