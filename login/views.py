from django.shortcuts import render

from login import models  # 导入models文件

# Create your views here.
from django.shortcuts import HttpResponse
user_list = []

def index(request):
    #return HttpResponse("Hello,dongbao")
    return render(request,"index.html")

def login(request):
    # return HttpResponse("Hello,dongbao")
    return render(request, "login.html")

def loginCheck(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        #temp={'user':username,'pwd':password}
        #user_list.append(temp)
        # 将数据保存到数据库
        models.UserInfo.objects.create(user=username, pwd=password)
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html',{'data':user_list})