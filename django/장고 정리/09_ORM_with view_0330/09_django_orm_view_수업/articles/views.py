from django.shortcuts import render, redirect
from .models import Article



# Create your views here.
def index(request):
    # DB에 전체 게시글 조회를 요청하고 쿼리셋을 응답받아 저장
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # print(article)
    context = {
        'article' : article,
    }
    # context - 템플릿에 데이터와 함께 렌더링
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # new에서 보낸 사용자 데이터를 받음
    title = request.POST.get('title')
    content = request.POST.get('content')
   
    # 받은 데이터를 DB에 저장
    # # 1 너무 길어서 탈락
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    # 저장 전에 유효성 검사와 같은 추가 작업을 위해 2번 방법을 택함
    article.save()

    # # 3 탈락 (사용자를 너무 믿음... 저장 전에 확인 해야 함)
    # Article.objects.create(title=title, content=content)

    # 결과 페이지 반환
    # return render (request, 'articles/create.html')

    # # 이동할 주소(URL) 사용자에게 응답
    # return redirect('articles:index')

    # 생성한 글의 단일 조회(detail) 주소(URL)로 이동 응답
    return redirect('articles:detail', article.pk )

def delete(request, pk): # request 사용 안함
    # 삭제할 데이터 조회 (기준=홈페이지에서전달받은 값)
    article = Article.objects.get(pk=pk)
    # 조회한 데이터 삭제
    article.delete()
    # 전체 조회 페이지 이동
    return redirect('articles:index')


def edit(request, pk):
    # 수정할 데이터 조회
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    article.title = request.POST.get('title')
    article.content = request.POST.get('content')

    article.save()
    return redirect('articles:detail', article.pk)