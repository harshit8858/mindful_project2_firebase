from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^home/', home, name='home'),

]
