from django.db import models
from django.utils.text import slugify


# Create your models here.


class Article(models.Model):
    article_title = models.CharField(max_length=500)
    article_desc = models.TextField()
    article_content = models.TextField()
    article_slug = models.SlugField()

    def __str__(self):
        return self.article_title

    def save(self, *args, **kwargs):
        self.article_slug = slugify(self.article_title)
        return super(Article, self).save(*args, **kwargs)

class Images(models.Model):
    article = models.ForeignKey(Article, on_delete= models.CASCADE)
    img_url = models.CharField(max_length=500)

    def __str__(self):
        return self.img_url