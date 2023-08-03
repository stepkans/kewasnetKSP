from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views, user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.BASE, name='base'),
    path('', views.HOME, name='home'),
    path('single/course', views.SINGLE_COURSE, name='single_course'),
    path('course', views.course, name='course'),
    path('contact', views.CONTACT_US, name="contact_us"),
    path('about', views.ABOUT_US, name="about_us"),
    path('accounts/register', user_login.REGISTER, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/profile', user_login.PROFILE, name = 'profile'),
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name = 'profile_update'),
    path('pillars', views.PILLARS, name="pillars"),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    