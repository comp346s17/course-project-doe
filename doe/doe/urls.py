"""doe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from smack import views as smack_views
from django.conf.urls.static import static

from django.conf import settings

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
