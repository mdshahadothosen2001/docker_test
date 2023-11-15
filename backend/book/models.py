from django.db import models


class BookModel(models.Model):
    book_title = models.CharField(max_length=100)
    book_auth = models.CharField(max_length=100)
    mrp = models.IntegerField(null=True, default=True)

    def __str__(self):
        return self.book_title
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        db_table = "book"
