from django.contrib import admin

from .models import BookModel


class BookModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book_title",
        "book_auth",
        "mrp",
    )
    list_display_links = (
        "book_title",
        "book_auth",
    )
    search_fields = (
        "book_title",
        "book_auth",
    )
    list_per_page = 25


admin.site.register(BookModel, BookModelAdmin)
