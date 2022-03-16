import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django_request_mapping import request_mapping

from web.models import *


@request_mapping("/item")
class DescriptionView(View):
    urls = ""

    @request_mapping("/<str:theme>/<str:poster>", method="get")
    def explainMovie(self, request, theme, poster):
        global urls
        urls = poster
        objs = Movie.objects.select_related('genreid');
        movie = Movie.objects.get(poster=poster)
        genre = Genre.objects.get(theme=theme)
        review = Review.objects.select_related('movieid', 'userid');
        rating = ""
        try:
            member = Member.objects.get(userid=request.session['sessionid'])
            for item in review:
                if (item.userid == member) and (item.movieid == movie):
                    print(item.userid)
                    print(item.movieid)
                    rating = item.star

            sum_rating = 0
            count = 0
            for item in review:
                if item.movieid == movie:
                    count += 1
                    sum_rating += item.star
            avg_rating = sum_rating / count

            print("sum : ", sum_rating)
            print("count : ", count)
            print("avg :", avg_rating)

            theme = ""
            if genre.theme == "romance":
                theme = "로맨스"
            elif genre.theme == "fantasy":
                theme = "판타지"
            context = {
                'objs': objs,
                'movie': movie,
                'genre': genre,
                'theme': theme,
                'rating': rating
            };
        except:
            theme = ""
            if genre.theme == "romance":
                theme = "로맨스"
            elif genre.theme == "fantasy":
                theme = "판타지"
            context = {
                'objs': objs,
                'movie': movie,
                'genre': genre,
                'theme': theme,
                'rating': rating
            };
        return render(request, 'movie-item.html', context);

    @request_mapping("/chart", method="get")
    def createChart(self, request):
        global urls
        review = Review.objects.select_related('movieid', 'userid');
        movie = Movie.objects.get(poster=urls)
        data = [];
        content = {};
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        for item in review:
            if item.movieid == movie:
                if item.star == 1:
                    count1 += 1
                elif item.star == 2:
                    count2 += 1
                elif item.star == 3:
                    count3 += 1
                elif item.star == 4:
                    count4 += 1
                elif item.star == 5:
                    count5 += 1
            else:
                pass
        content['type'] = 'column';
        content['colorByPoint'] = True;
        content['data'] = [count1, count2, count3, count4, count5];
        content['showInLegend'] = False;
        data.append(content)
        return HttpResponse(json.dumps(data), content_type='application/json');

    @request_mapping("/<str:theme>/<str:poster>/star", method="get")
    def inputStarValue(self, request, theme, poster):
        movie = Movie.objects.get(poster=poster)
        member = Member.objects.get(userid=request.session['sessionid'])
        rating = request.GET['rating']
        try:
            rev = Review.objects.get(userid=member, movieid=movie)
            rev.star = rating
            rev.save()
            print("별점 새로 업데이트")
            print("리뷰 내 아이디 존재")
        except:
            Review(userid=member, movieid=movie, star=rating).save()
            print("리뷰 내 아이디 존재하지 않아 새로 만들었다!")

        return redirect('/item' + '/' + theme + '/' + poster);
