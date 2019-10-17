from django.contrib import admin
from django.urls import path
from django.views import generic
from core import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/posts/', views.posts_list, name='posts_list'),
    path('api/v1/posts/<int:pk>', views.post_details, name='post_details'),
    path('', generic.TemplateView.as_view(template_name='index.html'))
]
