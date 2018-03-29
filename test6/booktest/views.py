#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import *
def index(request):
    return render(request,'booktest/index.html')

def pro(request):
    prolist = AreaInfo.objects.filter(parea__isnull=True)
    list = []
    #[[1,'北京'],[2,'天津'],......]
    for item in prolist:
        list.append([item.id,item.title])#[1,'北京']
    return JsonResponse({'data':list})

def city(request,id):
    citylist = AreaInfo.objects.filter(parea_id=id)
    list = []
    for item in citylist:
    #[{id:1,title:'北京'},{id:2,title:'天津'},......]
        list.append({'id':item.id,'title':item.title})
    return JsonResponse({'data':list})

#自定义编辑器
def htmlEditor(request):
    return render(request,'booktest/htmlEditor.html')

def htmlEditorHandle(request):
    html = request.POST['hcontent']
    # test1 = Test1.objects.get(pk=1)
    # test1.hcontent = html
    # test1.save()
    test1 = Test1()
    test1.hcontent = html
    test1.save()
    context = {'content':html}
    return render(request,'booktest/htmlShow.html',context)