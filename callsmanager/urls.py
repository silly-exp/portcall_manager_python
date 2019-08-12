from django.urls import path

from . import views

app_name = 'callsmanager'
urlpatterns = [
    path('', views.index, name='index'),
    path('calls', views.call_list, name='call_search'),
    path('calls/<int:call_id>', views.call_details, name='call_details'),
#    path('calls/create', views.call_create, name='call_create'),
#    path('calls/<int:call_id>/update', views.call_update, name='call_update'),
    path('calls/<int:call_id>/edit', views.call_edit, name='call_edit'),

]