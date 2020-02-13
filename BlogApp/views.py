from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import writing
from .forms import writing_post


# Create your views here.
def home(request):
    write = writing.objects #쿼리셋
    #블로그 모든 글들을 대상으로
    writing_list = writing.objects.all()
    #블로그 객체 세개를 한 페이지로 자르기
    paginator = Paginator(writing_list,3)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해준다
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'writings':write, 'posts':posts} )

def detail(request, writing_id):
    writing_detail = get_object_or_404(writing, pk=writing_id)
    return render(request, 'detail.html', {'write_detail':writing_detail})

#new.html 띄워주는 역할
def new(request):
    return render(request, 'new.html')

#입력받은 내용 DB에 넣어주는 함수
def create(request):
    qs = writing() # 클래스 객체 생성
    qs.title = request.GET['title']
    qs.text = request.GET['text']
    qs.pub_date = timezone.datetime.now()
    qs.save()
    #redirect... 위에꺼 다 처리하고 URL로 넘겨주세요
    return redirect('/writing/'+str(qs.id))

def writingpost(request):
    # 1. 입력된 내용 처리하는 기능 -> POST
    if request.method == 'POST':
        form = writing_post(request.POST)
        if form.is_valid():
            #갖고오는데 아직 저장은 하지 말아봐
            post = form.save(commit=False)
            #타임존 현재시간으로 넣어주기
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
            
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = writing_post()
        return render(request,'new.html',{'form':form})