import datetime
from django.db import models

from django.utils import timezone


class Article(models.Model):
    article_titles = models.CharField("Name of article", max_length=200)
    article_text = models.TextField("Article text")
    pub_date = models.DateTimeField('Date publication')

    def __str__(self):
        return self.article_titles

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("Name author", max_length=50)
    comment_text = models.CharField("Text comment", max_length=200)


    def __str__(self):
        return self.author_name

