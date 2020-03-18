from django.db import models

# Create your models here.
class category(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=100)
    #subcategory=models.CharField(max_length=100)
    def __str__(self):
        return self.cname

class product(models.Model):
    pid= models.AutoField(primary_key=True)
    logoname= models.CharField(max_length=200)
    category= models.ForeignKey(category, on_delete=models.CASCADE)
    price= models.FloatField(max_length=1000,default=0.0)
    companyname=models.CharField(max_length=200)

    def __str__(self):
        return self.companyname

class logoinfo(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,default="")
    img=models.ImageField(upload_to='upload/',default="dummy.jpg")
    category= models.ForeignKey(category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title 

class client(models.Model):
    name=models.CharField(max_length=255,default="")
    email=models.CharField(max_length=255,default="")
    contact=models.IntegerField()
    message=models.TextField()
    logoid=models.IntegerField(default=0)

    def __str__(self):
        return self.email

