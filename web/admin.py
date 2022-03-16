from django.contrib import admin
from web.models import *


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('userid', 'pwd', 'name', 'email', 'phone', 'birthday', 'gender', 'checkq', 'checka')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genreid', 'theme')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('movieid', 'genreid', 'poster', 'title',
                    'open_date', 'grade', 'running_time', 'director', 'actor',
                    'open_country', 'trailer', 'summary')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewid', 'userid', 'movieid', 'star')


class BoardAdmin(admin.ModelAdmin):
    list_display = ('boardid', 'userid', 'title', 'content',
                    'write_date', 'update_date', 'read_count')


class VoteAdmin(admin.ModelAdmin):
    list_display = ('voteid', 'userid', 'boardid', 'vote_count')


admin.site.register(Member, MemberAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Vote, VoteAdmin)
