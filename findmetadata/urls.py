from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'findmetadata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$',TemplateView.as_view(template_name='index.html')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('appmetadata.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
