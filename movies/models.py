from django.db import models
from django.conf import settings


class Movie(models.Model):
    title = models.CharField(max_length=255)
    # CharField belli bir uzunluktan kucuk stringleri tutar
    description = models.TextField(blank=True)
    # TextField sinirsiz uzunluktaki stringleri tutar
    # blank=True olan field bos birakilabilir demek
    release_date = models.DateField(null=True, blank=True)
    # DateField sadece ay yil ve gun tutar
    director = models.ForeignKey('Person', related_name='directed_movies')
    # ForeignKey baska bir model ile baglanti kurar
    # related_name bu baglanti tersten kullanilirken degisken adina atanir
    # movie_set yerine movies dememiz yeterli olacak artik
    total_score = models.PositiveIntegerField(default=0)
    # PositiveIntegerField veritabaninda pozitif tam sayi tutar
    genres = models.ManyToManyField('Genre', related_name='movies', blank=True)
    scored_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    # ManyToManyField bir model ile baska bir modeli coka cok sekilde baglar
    image = models.URLField(blank=True)
    # URLField bir url saklamak icin kul1lanilir
    characters = models.ManyToManyField("Character", related_name="movies", blank=True)

    def __str__(self):
        return self.title

    def avg_score(self):
        if not self.scored_users.count():
            return 0
        return self.total_score / self.scored_users.count()

    def genres_verbose(self):
        return ', '.join(self.genres.values_list('name', flat=True))


class Person(models.Model):
    GENDERS = [
        ('m', "Male"),
        ('f', "Female"),
        ('o', "Other"),
    ]

    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS)
    # choices 'a atanan liste veritabanina kaydedilebilecek degerleri sinirlar
    is_awarded = models.BooleanField(default=False)
    # BooleanField true/false degerleri saklamak icin kullanilir

    def __str__(self):
        return self.name


class Character(models.Model):
    person = models.ForeignKey(Person, related_name="characters")
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = (
            ('person', 'name'),
        )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, related_name="sub_genres")
    # ForeignKey'deki self model'in kendisini ifade eder

    def __str__(self):
        return self.name
