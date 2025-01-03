from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, choices=(('F','F'),('M','M'),), blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=255,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/') # cria pasta com subpasta ano e mes
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        db_column='id_category'
    )
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_column='id_owner'
    )

    # retorna as informações para exibir na tabela admin
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
