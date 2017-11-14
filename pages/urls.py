from django.conf.urls import url 

# Import Views
from . import views

app_name = 'pages'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
