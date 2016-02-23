from django.conf.urls import url
from appmetadata import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'findmetadata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$',views.HomePage.as_view(),name='home_page'),
    url(r'^save-data/$',views.SaveData.as_view(),name='save_page'),
]
