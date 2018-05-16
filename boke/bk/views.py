from django.shortcuts import *
from django.http import *
from bk import models as m
from .models import *
from django.template import RequestContext
from django import forms
from django.utils import timezone



# Create your views here.
def zt(request,u_id):
    c = m.News.objects.order_by('changetime')
    a = m.User.objects.all(pk=u_id)
    return render(request,'muban.html',{'c':c,'a':a})

def dt(request,u_id):
    c = m.News.objects.order_by('-changetime')
    a = m.User.objects.all(pk=u_id)
    return render(request,'muban.html',{'c':c,'a':a})

def read(request,u_id):
    a = m.News.objects.all(pk=u_id)
    c = a.read
    c += 1
    a.read = c
    a.save()
    return render(request,'muban.html',{'a':a})

def yyyh(request):
    aa = m.User.objects.all()
    return render(request,'yyyh.html',{'aa':aa})

def muban(request):
    time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
    bb = m.News.objects.all()
    aa = m.User.objects.all()
    return render(request, 'muban.html', {'bb': bb ,'aa': aa},RequestContext(request,{'time':time}))


def wz1(request, aa_id):
    time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
    aa = m.News.objects.get(pk=aa_id)
    return render(request, 'wz1.html', {'aa': aa},RequestContext(request,{'time':time}))


def zj(request, aa_id):
    time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
    if str(aa_id) == '0':
        return render(request, 'zj.html',RequestContext(request,{'time':time}))
    aa = m.News.objects.get(pk=aa_id)
    return render(request, 'zj.html', {'aa': aa},RequestContext(request,{'time':time}))


def xg(request):
    time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
    title = request.POST.get('title', 'title失败')
    content = request.POST.get('content', 'content失败')
    aa_id = request.POST.get('aa_id', '0')
    if aa_id == '0':
        m.News.objects.create(title=title, content=content)
        bb = m.News.objects.all()
        return render(request, 'muban.html', {'bb': bb})
    aa = m.News.objects.get(pk=aa_id)
    aa.title = title
    aa.content = content
    aa.save()
    return render(request, 'wz1.html', {'aa': aa},RequestContext(request,{'time':time}))


# # 注册界面
# def zc(request,user_id):
#     if str(user_id) == '0':
#         return render(request,'zc.html')
#     user = m.User.objects.get(pk=user_id)
#     return render(request, 'zc.html',{'user':user})
#
#
def zccg(request):
    name = request.POST['name']
    pwd = request.POST['pwd']
    gender = request.POST['gender']
    context = {'name': name, 'pwd': pwd, 'gender': gender}
    return render(request, 'zccg.html', context)
# #
# def dl(request):
#     if request.method == 'GET':
#         return render(request,'dl.html')
#     uname = request.POST.get('name','')
#     upwd = request.POST.get('pwd','')
#
#
#     return render(request,'dl.html',{'user':user})


def zjm(request):
    time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
    return render(request,'zjm.html',RequestContext(request,{'time':time}))

#表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

#注册
def zc(request):
    time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('注册成功！！')
    else:
        uf = UserForm()
    return render_to_response('zc.html',{'uf':uf}, RequestContext(request,{'time':time}))

#登陆
def dl(request):
    time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转主界面
                response = HttpResponseRedirect('/bk/muban/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在原地
                return HttpResponseRedirect('/bk/')
    else:
        uf = UserForm()
    return render_to_response('dl.html',{'uf':uf},RequestContext(request,{'time':time}))




def yh(request, aa_id):
    time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
    if str(aa_id) == '0':
        return render(request, 'yh.html', RequestContext(request, {'time': time}))
    aa = m.User.objects.get(pk=aa_id)
    return render(request, 'yh.html', {'aa': aa}, RequestContext(request, {'time': time}))


def yhxg(request):
    time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
    username = request.POST.get('username', 'username失败')
    password = request.POST.get('password', 'password失败')
    age = request.POST.get('age', 'age失败')
    sex = request.POST.get('sex', 'sex失败')
    aa_id = request.POST.get('bb_id', '0')
    if aa_id == '0':
        m.User.objects.create(username=username, password=password, age=age, sex=sex)
        bb = m.User.objects.all()
        return render(request, 'muban.html', {'bb': bb})
    aa = m.User.objects.get(pk=aa_id)
    aa.username = username
    aa.password = password
    aa.age = age
    aa.sex = sex
    aa.save()
    return render(request, 'muban.html', {'aa': aa}, RequestContext(request, {'time': time}))



