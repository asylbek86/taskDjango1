from django.db import models



class Post_club(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описания')
    image = models.ImageField(upload_to="")
    created_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True)


    def __str__(self):
        return self.name