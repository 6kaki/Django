

from django.contrib import admin
from django.urls import path, include
from myapp import views

#http://127.0.0.1 여기로 접속했을 때 myapp에 있는 views.py로 이동하게 하려면
#http://127.0.0.1/app/ 

#http://127.0.0.1/create/ create를 접속했을 때
#http://127.0.0.1/read/1/ read를 접속했을 때

urlpatterns = [
   path('',views.index), #사용자가 아무것도 없는 주소로 들어왔을 때
   path('create/',views.create), #create라고 뒤에 붙여서 들어왔을 때
   path('read/<id>/',views.read) #변할 수 있는 값은 <id> 꺽새로 묶어준다.
]
