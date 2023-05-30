from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls,name="admin"),
    path('api/',include('api.urls')),
    path('accounts/',include('Accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',include('Site.urls')),
    path('chat/',include('chat.urls'))
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)