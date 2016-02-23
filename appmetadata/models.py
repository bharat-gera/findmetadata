from django.db import models
from django.utils.translation import ugettext_lazy as _
class AppMetaData(models.Model):
    
    title = models.TextField(_("Title"),max_length=500,
                              blank = True, help_text = 'Title of  your URL')
    
    meta_desc = models.TextField(_("Meta Description"),max_length=1500,
                                 blank=True,help_text='Meta Description')
    
    meta_key = models.TextField(_("Meta Keywords"),max_length=1500,
                                 blank=True,help_text='Meta Keywords')
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Meta data'
        verbose_name_plural = 'Meta data'