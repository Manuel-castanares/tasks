from django.conf.urls import url 
from tasks import views 
 
urlpatterns = [ 
    url(r'^api/tasks$', views.tasks_list),
]

