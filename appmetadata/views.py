import urllib2
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.generic import FormView, CreateView
from appmetadata.forms import URLInputForm, URLMetaData
from appmetadata.models import AppMetaData
from bs4 import BeautifulSoup

class HomePage(FormView):
    
    template_name_resp = 'response.html'
    template_name = 'index.html'
    form_class = URLInputForm
    success_url= settings.HOMEPAGE_URL
    form_class_resp = URLMetaData
    
    def get_data(self,request):
        return request.POST['url_name']
    
    def get_success_url(self):
        return self.success_url
        
    def meta_description(self,object):
        try:meta=object.find('meta', {'name':'description'})['content']
        except:return []    
        return meta
    
    def meta_keywords(self,object):
        try:meta=object.find('meta',{'name':'keywords'})['content']
        except:return []    
        return meta
    
    def extract_data(self,resp):
        soup = BeautifulSoup(resp)
        seo_data = {'title':soup.find('title').string,
                    'meta_desc': self.meta_description(soup),
                    'meta_key':self.meta_keywords(soup)}
        return seo_data
    
    def form_valid(self, form):
        try:
            req = urllib2.Request(self.get_data(self.request))
            resp = urllib2.urlopen(req)
        except ValueError:
            messages.error(self.request,"URL without protocol is not acceptable.")
            return redirect(self.get_success_url())    
        except urllib2.URLError,e:
            messages.error(self.request,"Given URL is"+" "+str(e.reason))
            return redirect(self.get_success_url())        
        html_resp = resp.read()
        response = self.extract_data(html_resp)
        seo_form = self.form_class_resp(response)
        return render_to_response(self.template_name_resp,{'seo_form':seo_form},context_instance= RequestContext(self.request))

class SaveData(CreateView):
        
    form_class = URLMetaData
    model = AppMetaData
    success_url = settings.HOMEPAGE_URL
    template_name = 'index.html'
