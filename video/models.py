from django.db import models

# Create your models here.
class video(models.Model):
    id = models.IntegerField(primary_key=True)
    title =models.CharField(max_length=80, blank=False)
    videofile =models.FileField(upload_to='media/')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title + ":" + str(self.videofile)