from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse

from app02 import form

def registe(request):
    reform=form.Reform()
    if request.method=='POST':
        ret={'status':0,'msg':''}
        reform=form.Reform(request.POST)
        if reform.is_valid():
            ret['msg']="/xiaomi/"
            return JsonResponse(ret)
        else:
            ret['status']=1
            ret['msg']=reform.errors
            return JsonResponse(ret)
    return render(request,'registe2.html',{'reform':reform})


def fileup(request):
    if request.method=='POST':
        file=request.FILES.get('file')
        with open(file.name,'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
    return render(request,'fileup.html')


def ajax(request):
    return render(request,'ajax.html')

def ajaxadd(request):
    i1=int(request.GET.get('i1'))
    i2=int(request.GET.get('i2'))
    ret=i1+i2
    return HttpResponse(ret)

import time
def ajaxmany(request):
    time.sleep(3)
    print('ok')
    src="/static/121550umjsc788wwgb877g.jpg"
    return HttpResponse(src)



