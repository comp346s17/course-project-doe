from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from smack import views as smack_views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'smack/login.html'}, name='login'),
    url(r'^logout/$',auth_views.logout, {'next_page': 'home'}, name='logout'),
    url(r'^signin/$',smack_views.signin,name='signin'),
    url(r'^$', smack_views.home, name='home'),
    url(r'^signup/$', smack_views.signup, name='signup'),
    url(r'^personalProfile/$', smack_views.personalProfile, name='personalProfile'),
    url(r'^datingFeed/$', smack_views.datingFeed, name='datingFeed'),
    url(r'^friendFeed/$', smack_views.friendFeed, name='friendFeed'),
    url(r'^editProfile/$', smack_views.editProfile, name='editProfile'),
    url(r'^ajax/ajax_like/$', smack_views.ajax_like, name='ajax_like'),
    url(r'^ajax/ajax_dislike/$', smack_views.ajax_dislike, name='ajax_dislike'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
