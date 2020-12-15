from django.contrib import admin
from django.urls import path

from report import views as report_views
from blog import views as blogs_views
from contact import views as contact_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogs_views.index, name='home'),
    path('post/', blogs_views.post, name='post'),
    #path('create/', blogs_views.create, name='create'),
    path('report/', report_views.report, name='report'),
    path('contact/', contact_views.contact, name='contact'),
    #path('contact/', contact_views.check_contact, name='contact')
]
