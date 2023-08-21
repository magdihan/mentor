from django.db import models
from django.utils import timezone


from users.models import User

# Create your models here.

class Cotegory(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
    
class Subcotegory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Cotegory, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
    

class Ads(models.Model):
    LEARN = 'Хочу научиться'
    TEACH = "Могу научить"
    TYPE_OF_ADS =[
    (LEARN,'Хочу научиться'),
    (TEACH,"Могу научить")
]
    
    
    subcategory = models.ForeignKey(Subcotegory, on_delete=models.CASCADE,null=True, blank=True,related_name='ads') 
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="images/ads/", default="images.jpg")
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ads',null=True, blank=True)
    type = models.CharField(max_length=100, choices=TYPE_OF_ADS, default=LEARN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Ads"
        verbose_name_plural = "Ads"