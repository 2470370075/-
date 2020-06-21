from django.shortcuts import HttpResponse,render,redirect
from django.http import JsonResponse
from .models import Userinfo
from .models import Book
from .models import Publish
from app01 import models
from django.contrib import auth
from geetest import GeetestLib


def require(func):
    def inner(request,*args,**kwargs):
        cook=request.session.get('login')
        print('cook:',cook)
        if cook:
            return func(request,*args,**kwargs)
        else:
            url=request.path_info
            return redirect('/login/?next={}'.format(url))
    return inner


def login(request):
    if request.method=="GET":
        return render(request,'denglu.html')
    if request.method == "POST":
        if request.POST.get('email')=='WJX@qq.com' and request.POST.get('password')=='123':
            url=request.GET.get('next')
            if url:
                ret=redirect(url)
            else:
                ret=redirect('/book/')
            request.session['login'] = True
            request.session.set_expiry(0)                    #设置超时时间为60秒，删除cookie不删除session，需要request.session.clear_expired()来删除服务器的session
            return ret
        else:
            return render(request,'denglu.html',{'error':'用户名或密码错误'})


def logout(request):
    ret=redirect('/login')
    request.session.flush()
    return ret

@require
def author(request):
    author=models.Author.objects.all()
    return render(request,'author.html/',{'author':author})


def addauthor(request):
    if request.method=='GET':
        ret = Book.objects.all()
        haha='gaha'
        return render(request, 'addauthor.html/', {'books': ret,'haha':haha})
    if request.method == 'POST':
        author_name=request.POST.get('author_name')
        author_books=request.POST.getlist('books')
        new_author=models.Author.objects.create(name=author_name)
        new_author.book.set(author_books)
        return redirect('/author/')

def deleteauthor(request):
    author_id=request.GET.get('id')
    models.Author.objects.get(id=author_id).delete()
    return redirect('/author/')

def editauthor(request):
    if request.method=='GET':
        author_id=request.GET.get('id')
        ret=models.Author.objects.get(id=author_id)
        books=Book.objects.all()
        return render(request,'editauthor.html',{'edit_author':ret,'books':books})

    if request.method == 'POST':
        author_name=request.POST.get('author_name')
        author_book=request.POST.getlist('books')
        author_id = request.POST.get('author_id')
        ret = models.Author.objects.get(id=author_id)
        ret.name=author_name
        ret.book.set(author_book)
        return redirect('/author/')



def editbook(request):
    if request.method=='GET':
        id1=request.GET.get('id')
        ret=Book.objects.get(id=id1)
        pub=Publish.objects.all()
        return render(request,'editbook.html/',{'edit_book':ret,'publish':pub})
    if request.method=='POST':
        edit_publish_name=request.POST.get('publisher')
        edit_book_name=request.POST.get('bookname')
        edit_book_id=request.POST.get('id')

        publish=Publish.objects.get(id=edit_publish_name)
        edit_book=Book.objects.all().get(id=edit_book_id)

        edit_book.pid_id=publish.id
        edit_book.name=edit_book_name
        edit_book.save()
        return redirect('/book/')



@require
def book(request):
    import mypage
    page=request.GET.get('page')
    ret=Book.objects.all()
    ex=mypage.Mypage(page,ret)
    html=ex.html()
    ret=ex.lastret
    return render(request,'book.html',{'book':ret,'author':author,'html':html})


def addbook(request):
    if request.method=='GET':
        ret = Publish.objects.all()
        return render(request,'addbook.html',{'publish':ret,'error':''})
    if request.method == 'POST':
        bookname=request.POST.get('book')
        if bookname:
            publishname = request.POST.get('publisher')
            ret = Book.objects.all()
            ret.create(name=bookname,pid_id=publishname)
            return redirect('/book/')
        else:
            ret = Publish.objects.all()
            return render(request, 'addbook.html', {'publish': ret,'error':'书籍不能为空!!!'})

def deletebook(request):
    if request.method=='GET':
        id=request.GET.get('id')
        Book.objects.get(id=id).delete()
        return redirect('/book/')
    else:
        return HttpResponse('出错了')




from  django import forms
from  django.forms import widgets
from  django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class Regform(forms.Form):
    name=forms.CharField(label='用户名:',max_length=15,min_length=5,
                         widget=widgets.TextInput(attrs={'class': 'form-control'}),
                         error_messages={'max_length':'用户名最多15位',
                                         'min_length':'用户名必少5位',
                                         'required':'用户名不能为空'})
    password=forms.CharField(label='密码:',max_length=15,min_length=5,
                        widget=widgets.PasswordInput(attrs={'class':'form-control'}),
                        error_messages = {'max_length': '密码最多15位',
                                          'min_length': '密码最少5位',
                                          'required': '密码不能为空'})
    password2 = forms.CharField(label='确认密码:', max_length=15, min_length=5,
                               widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
                               error_messages={'max_length': '密码最多15位',
                                               'min_length': '密码最少5位',
                                               'required': '密码不能为空'})
    phone=forms.CharField(label='手机号:',
                          validators=[RegexValidator(r'^[1][3-8][0-9]{9}$', '不是手机号'),],
                          widget=widgets.TextInput(attrs={'class': 'form-control'}),
                          error_messages = {'required': '用户名不能为空'}
                          )
    city=forms.ChoiceField(label='城市：',
                           choices=models.City.objects.all().values_list('id','name'),
                           initial=1,
                           widget=forms.widgets.Select,
                           error_messages={'required': '城镇不能为空'}
                           )
    #
    # def clean(self):
    #     password1=self.cleaned_data.get('password')
    #     password2=self.cleaned_data.get('password2')
    #     if password1!=password2:
    #         self.add_error('password2', ValidationError('两次密码不一致'),)
    #         raise ValidationError('两次密码不一致')
    #     return self.cleaned_data

    def clean_name(self):
        value=self.cleaned_data.get('name')
        ret=models.Us.objects.all().values_list('name')
        if (value,) in list(ret):
            raise ValidationError('用户名已存在')
        return value

    def clean_password2(self):
        value=self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if value!=password2:
            raise ValidationError('密码不一致')
        return value


def registe(request):
    form=Regform()
    if request.method=='POST':
        form=Regform(request.POST)
        if form.is_valid():
            name=request.POST.get('name',None)
            password=request.POST.get('password',None)
            ret=models.Us.objects.all()
            ret.create(name=name,password=password)
            return HttpResponse('注册成功！')
        else:
            pass
    return render(request,'registe.html/',{'form':form,})


VALID_CODE = ""
pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"


def get_geetest(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)


def login2(request):
    # if request.is_ajax():  # 如果是AJAX请求
    if request.method == "POST":
        print('psoe')
        # 初始化一个给AJAX返回的数据
        ret = {"status": 0, "msg": ""}
        # 从提交过来的数据中 取到用户名和密码
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # 获取极验 滑动验证码相关的参数
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]
        print(1)
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            print(2)
            # 验证码正确
            # 利用auth模块做用户名和密码的校验
            user = auth.authenticate(username=username, password=pwd)
            if user:
                # 用户名密码正确
                # 给用户做登录
                print(3)
                auth.login(request, user)
                ret["msg"] = "/book/"
            else:
                # 用户名密码错误
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误！"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"

        return JsonResponse(ret)
    return render(request, "login.html")

