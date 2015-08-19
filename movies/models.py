from django.db import models
from django.conf import settings


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    # Charfield belli bir uzunluktan kucuk stringleri tutar
    description = models.TextField(blank=True)
    # TextField sinirsiz uzunluktaki stringleri tutar
    # blank=True olan field bos birakilabilir demek
    release_date = models.DateField()
    # DateField sadece ay yil ve gun tutar
    director = models.ForeignKey('Person', related_name='movies')
    # ForeignKey baska bir model ile baglanti kurar
    # related_name bu baglanti tersten kullanilirken degisken adina atanir
    # movie_set yerine movies dememiz yeterli olacak artik
    total_score = models.PositiveIntegerField()
    # PositiveIntegerField veritabaninda pozitif tam sayi tutar
    genres = models.ManyToManyField('Genre', related_name='movies')
    scored_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    # ManyToManyField bir model ile baska bir modeli coka cok sekilde baglar
    # image = models.ImageField(null=True)
    # ImageField bir resmin diskte tutulan yerini saklar
    characters = models.ManyToManyField("Character", related_name="movies")


class Person(models.Model):
    GENDERS =[
        ('m', "Male"),
        ('f', "Female"),
        ('o', "Other"),
    ]

    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS)
    # choices 'a atanan liste veritabanina kaydedilebilecek degerleri sinirlar
    is_awarded = models.BooleanField()
    # BooleanField true/false degerleri saklamak icin kullanilir


class Character(models.Model):
    person = models.ForeignKey(Person, related_name="characters")
    name = models.CharField(max_length=255)


class Genre(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, related_name="sub_genres")
    # ForeignKey'deki self model'in kendisini ifade eder
