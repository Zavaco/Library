from django.db import models


# Create your models here.


class Book(models.Model):
    book_title = models.CharField(max_length=100, null=True)
    published_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Author(models.Model):
    author_name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class AuthorandBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.book_title

    class Meta:
        verbose_name = 'Author and Book'
        verbose_name_plural = 'Authors and Books'


class LibUser(models.Model):
    user_name = models.CharField(null=True, max_length=100)
    user_status = models.BooleanField(default=True)
    user_image = models.ImageField(upload_to='customer', null=True, blank=True)
    book_info = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(null=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class LibAdmin(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(LibUser, on_delete=models.CASCADE, null=True, blank=True)
    take_date = models.DateField(null=True, blank=True)
    give_date = models.DateField(null=True, blank=True)
    book_status = models.BooleanField(null=True, default='True')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.user_name

    class Meta:
        verbose_name = 'Library_Admin'
        verbose_name_plural = 'Library_Admins'
