from django.db import models

# Create your models here.

class PostType(models.Model)
    """
        Class used to manage PostType table within DB. It specifies post's type: hotel, pension, cruise etc...
    """
    name = models.CharField(max_length=100, verbose_name='Name', unique=True)
    
    class Meta:
        ordering = ('name', )
    
    def __str__(self):
        """
            Method to specify what to print in print function.
        """
        return str(self.name)
    
    def __unicode__(self):
        """
            Method to specify what to print in print function for older or funny versions of Python.
        """
        return str(self.name)


class Post(models.Models):
    """
        Class used to handle Post table within databse.
    """
    name = models.CharField(max_length=100, verbose_name='Name', unique=True)
    post_type = models.ForeignKey(PostType, on_delete=models.CASCADE, related_name='type')
    description = models.TextField(max_length=1000, verbose_name='Description', blank=True, null=False)
    address = models.TextField(max_length=250, verbose_name='Address', blank=True, null=False)
    stars = models.CharField(max_length=10, verbose_name='Stars', unique=True)
    rating = models.CharField(max_length=10, verbose_name='Rating', unique=True)
    visitors_no = models.CharField(max_length=10, verbose_name='Number of visitors', unique=True)
    posted_on = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    
    class Meta:
        ordering = ('name', )
        unique_together = (('name', 'type'),)
        
    def __str__(self):
        """
            Method to specify what to print in print function.
        """
        return str(self.name)
    
    def __unicode__(self):
        """
            Method to specify what to print in print function for older or funny versions of Python.
        """
        return str(self.name)
        
    
    
    