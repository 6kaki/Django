from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request): #첫번째 파라미터: 객체
    return HttpResponse('Welcome!') #home에 객체를 return

def create(request):
    return HttpResponse('Create!')

def read(request,id):
    return HttpResponse('Read!' + ' '+id) #받아온 id값을 화면에 표시해준다.