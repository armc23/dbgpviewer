from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('filter', views.BootstrapFilterView, name='filter'),
   
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_roo=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_roo=settings.MEDIA_ROOT)