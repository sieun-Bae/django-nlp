from django.contrib import admin
from django.urls import path

import blog.views
from report.views import reportMain

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.index, name='index'),
    path('reportMain/', reportMain, name='reportMain'),
]
