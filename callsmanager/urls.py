from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calls', views.call_list, name='call_search'),
    path('calls/<int:call_id>', views.call_details, name='call_details'),

]