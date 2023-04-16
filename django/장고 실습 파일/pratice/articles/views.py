from django.shortcuts import render

# Create your views here.
# 특정 기능을 수행하는 view 함수를 만듦
def index(request): # request는 바꿀 순 있지만 다른 이름으로 변경 x 약속임
    return render(request, 'articles/index.html')