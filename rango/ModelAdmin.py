from django.db import models

class PageAdmin(models.Model):
    title = models.CharField(max_length=128)
	category = models.ForeignKey(Category)
    url = models.URLField()

    def __unicode__(self):
        return self.title