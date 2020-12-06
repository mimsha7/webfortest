from django.urls import path
from webpages.views import home, contact, about, member, group
from . import views

urlpatterns = [
    path('', home),
    path('members/', group, name="group"),
    path('member/<int:id>', member, name="member"),
    path('contact/', contact),
    path('about/', about),

]
