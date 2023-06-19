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
    path('prefixes', views.prefixes, name='prefixes'),
    path('update_prefixes/<prefix_id>', views.update_prefixes, name='update-prefixes'),
    path('add_prefix', views.add_prefix, name='add-prefix'),
    path('delete_prefix/<prefix_id>', views.delete_prefix, name='delete-prefix'),
    path('sites', views.sites, name='sites'),
    path('update_sites/<site_id>', views.update_sites, name='update-sites'),
    path('add_site', views.add_sites, name='add-sites'),
    path('delete_sites/<site_id>', views.delete_sites, name='delete-sites'),
   
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_roo=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_roo=settings.MEDIA_ROOT)