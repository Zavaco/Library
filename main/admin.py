from django.contrib import admin
from .models import Book, AuthorandBook
from .models import LibAdmin, Author, LibUser
# Register your models here.


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(LibUser)
admin.site.register(AuthorandBook)
admin.site.register(LibAdmin)