from django.conf.urls import url, include
from simplemooc.core import views


urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^contact/',views.contact, name='contact'),
]
