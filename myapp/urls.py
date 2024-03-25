from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('',views.index,name="index"),
     path('about/', views.about, name='about'),
     path('team/', views.team_view, name='team'),
     path('all-dishes/', views.all_dishes_view, name='all_dishes'),
     path('contact/', views.contact_us, name='contact'),
     path('register/', views.register, name='register'),
     path('login/', views.signin, name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('check_user_exist/', views.check_user_exist, name='check_user_exist'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)