from django.db import models

DEFAULT_DESCRIPTION = '-no-description-'

# Create your models here.



class PostOwnerType(models.Model):
    """
        Class used to handle post owner's type, as physic or juridical person.
    """
    name = models.CharField(max_length=100, verbose_name='Nume', unique=True)
    description = models.TextField(max_length=1000, verbose_name='Caracteristici', blank=True, null=False, default=DEFAULT_DESCRIPTION)
    
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

     
class PostOwner(models.Model):
    """
        Class used to handle post owners' table within DB.
    """
    name = models.CharField(max_length=100, verbose_name='Nume', unique=True)
    description = models.TextField(max_length=1000, verbose_name='Caracteristici', blank=True, null=False, default=DEFAULT_DESCRIPTION)
    type = models.ForeignKey(PostOwnerType, on_delete=models.CASCADE, related_name='type')
    
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


class PostType(models.Model):
    """
        Class used to manage PostType table within DB. It specifies post's type: hotel, pension, cruise etc...
    """
    name = models.CharField(max_length=100, verbose_name='Nume', unique=True)
    description = models.TextField(max_length=1000, verbose_name='Caracteristici', blank=True, null=False, default=DEFAULT_DESCRIPTION)
    
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


class Post(models.Model):
    """
        Class used to handle Post table within databse.
    """
    owner = models.ForeignKey(PostOwner, verbose_name='Proprietar', on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=100, verbose_name='Nume', unique=True)
    post_type = models.ForeignKey(PostType, on_delete=models.CASCADE, related_name='type')
    description = models.TextField(max_length=1000, verbose_name='Caracteristici', blank=True, null=False, default=DEFAULT_DESCRIPTION)
    address = models.TextField(max_length=250, verbose_name='Contact', blank=True, null=False)
    stars = models.IntegerField(verbose_name='Stele', unique=False, default = 1)
    price = models.CharField(max_length=15, verbose_name='Pret(RON)', unique=False)
    rating = models.FloatField(verbose_name='Rating', unique=False, default=0.0)
    visitors_no = models.IntegerField(verbose_name='Numar de vizitatori', unique=False, default=0)
    posted_on = models.DateTimeField(auto_now_add=True, editable=False, blank=False, null=True)
    
    class Meta:
        ordering = ('name', )
        unique_together = (('name', 'post_type'),)
        
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
     
    
    
    
    