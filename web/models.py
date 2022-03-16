import datetime

from django.db import models


# Create your models here.
class Member(models.Model):
    userid = models.CharField(max_length=20, primary_key=True)
    pwd = models.CharField(max_length=10)
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=13, null=True)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    checkq = models.CharField(max_length=20, default='')
    checka = models.CharField(max_length=20, default='')

    class Meta:
        db_table = 'db_member'


class Genre(models.Model):
    genreid = models.AutoField(primary_key=True)
    theme = models.CharField(max_length=30)

    class Meta:
        db_table = 'db_genre'


class Movie(models.Model):
    movieid = models.AutoField(primary_key=True)
    genreid = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movie_genreid')
    poster = models.CharField(max_length=500)
    title = models.CharField(max_length=50)
    open_date = models.CharField(max_length=10)
    grade = models.IntegerField()
    running_time = models.IntegerField()
    director = models.CharField(max_length=30)
    actor = models.CharField(max_length=200)
    open_country = models.CharField(max_length=20)
    trailer = models.CharField(max_length=500, null=True)
    summary = models.CharField(max_length=2000)

    class Meta:
        db_table = 'db_movie'


class Review(models.Model):
    reviewid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='review_userid')
    movieid = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='review_movieid', null=True)
    star = models.IntegerField(default=0)

    class Meta:
        db_table = 'db_review'


class Board(models.Model):
    boardid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='board_userid')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    write_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    read_count = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'db_board'


class Vote(models.Model):
    voteid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='vote_userid')
    boardid = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='vote_boardid')
    vote_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'db_vote'
