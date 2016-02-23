from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'findmetadata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$',TemplateView.as_view(template_name='index.html')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('appmetadata.urls')),
]
