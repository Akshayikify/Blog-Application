from django.contrib import admin
from django.urls import path,include
from blog_app import views as blog_views
from django.contrib.auth import views as auth
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog_app.urls')),
    path('login/',blog_views.Login,name='login'),
    path('register/',blog_views.register,name='register'),
    path('logout/',auth.LogoutView.as_view(template_name='index.html'),name='logout'),
]
