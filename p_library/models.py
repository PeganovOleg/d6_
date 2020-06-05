from django.db import models

  
  
class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):  
       # return self.full_name
        return "{}, {}".format(self.full_name,self.birth_year)

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    redaction = models.ForeignKey('Redaction', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    my_friend= models.ForeignKey('Friend', on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='media', blank=True, help_text='150x150px', verbose_name='Ссылка картинки')
    #blank=True, upload_to='images/blog/%Y/%m/%d', help_text='150x150px', verbose_name='Ссылка картинки'
    def image_img(self):
        if self.images:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.images.url))
        else:
            return '(Нет изображения)'
        image_img.short_description = 'Картинка'
        image_img.allow_tags = True

    def __str__(self):
        return self.title

class Redaction(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Friend(models.Model):
    friend_name = models.TextField()
    phone       = models.TextField(default='******')
    id = models.SmallIntegerField(primary_key='True')
    def __str__(self):
        return self.friend_name        