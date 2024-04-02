from django.db import models
# so django knows models/db
# from pygments.lexers import get_lexer_by_name
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight

class Dumpling(models.Model): 
  # no need add DumplingId
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=500)
  origin = models.ForeignKey('Origin', on_delete=models.SET_NULL, null=True, default=1, related_name='dumplings')
  # add user info for auth
  # owner = models.ForeignKey('auth.User', related_name='dumplings', on_delete=models.CASCADE)
  # highlighted = models.TextField()
  # create method on dumpling obj so in admin it is it's name vs dumpling object 1
  def __str__(self):
    return self.name + ': ' + self.description
  # for auth?
  # def save(self, *args, **kwargs):

  
class Origin(models.Model):
  country = models.CharField(max_length=60)
  def __str__(self):
    return self.country
  
class Tag(models.Model):
  name = models.CharField(max_length=50)
  dumplings = models.ManyToManyField(Dumpling, related_name='tags')

  def __str__(self):
    return self.name