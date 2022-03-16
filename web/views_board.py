import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django_request_mapping import request_mapping

from web.models import *


@request_mapping("/board")
class BoardView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        context = {}
        try:
            boards = Board.objects.all()
            # 입력 파라미터
            page = request.GET.get('page', '1')  # 페이지
            kw = request.GET.get('kw', '')  # 검색어
            so = request.GET.get('so', 'recent')  # 정렬기준

            # 정렬
            if so == 'read': # 조회수
                question_list = Board.objects.order_by('-read_count')
            else:  # recent(최근순)
                question_list = Board.objects.order_by('-write_date')
            if kw:
                question_list = question_list.filter(
                    Q(title__icontains=kw)  # 제목검색
                ).distinct()


            # 페이징처리
            paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
            page_obj = paginator.get_page(page)

            context = {
                'boards': boards,
                'question_list': page_obj,
                'page': page,
                'kw': kw,
                'so': so
            }
        except:
            print("home error!")
        return render(request,'board.html',context);

    @request_mapping("/<int:pk>/recommend", method="get")
    def recommendBoard(self, request, pk):
        objs = Vote.objects.all()
        member = Member.objects.get(userid=request.session['sessionid'])
        board = Board.objects.get(boardid=pk)
        if objs == None:
            Vote(userid=member, boardid=board).save()
            vote = Vote.objects.get(userid=member, boardid=board)
            vote.vote_count += 1
            vote.save()
        else:
            data = 0
            for item in objs:
                if item.userid == member and item.boardid == board:
                    data += 1
                    continue
            if data == 0:
                Vote(userid=member, boardid=board).save()
                vote = Vote.objects.get(userid=member, boardid=board)
                vote.vote_count += 1
                vote.save()

        return redirect('/board/' + str(pk))

    @request_mapping("/post", method="get")
    def writeBoard(self, request):
        return render(request, 'board_post.html');

    @request_mapping("/postimpl", method="post")
    def postData(self, request):
        try:
            title = request.POST['title']
            content = request.POST['content']
            if title == "" or content == "":
                raise Exception
            member = Member.objects.get(userid=request.session['sessionid'])
            print(title,content)
            board = Board(userid=member,title=title,content=content)
            board.save()
            html = '/board'
        except:
            html = '/board/post'
        return redirect(html);

    @request_mapping("/<int:pk>/", method="get")
    def detailBoard(self, request, pk):
        context = {}
        count = 0
        try:
            board = Board.objects.get(boardid=pk)
            board.read_count += 1
            board.save()
            context['board'] = board

            objs = Vote.objects.all()
            if objs == None:
                count = 0
            else:
                for item in objs:
                    if board == item.boardid:
                        count += item.vote_count
            context['count'] = count
        except:
            print("detailBoard 오류!")
        return render(request, 'board_detail.html', context);

    @request_mapping("/<int:pk>/edit/<int:pk2>", method="get")
    def editBoardView(self, request, pk,pk2):
        board = Board.objects.get(boardid=pk)
        return render(request, 'board_edit.html', {'board': board})

    @request_mapping("/<int:pk>/delete", method="get")
    def delteBoard(self, request, pk):
        board = Board.objects.get(boardid=pk)
        board.delete();
        return redirect('/board/');

    @request_mapping("/<int:pk>/edit/<int:pk2>/impl", method="post")
    def editBoard(self, request, pk,pk2):
        board = Board.objects.get(boardid=pk)
        try:
            if request.method == "POST":
                title = request.POST['title']
                content = request.POST['content']
                if title == "" and content == "":
                    raise Exception
                board.title = title
                board.content = content
                board.save()
                return redirect('/board/')
        except:
            return redirect('/board/' + str(pk) + '/edit/' + str(pk))


