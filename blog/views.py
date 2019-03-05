from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse, request
from django.shortcuts import render


# Create your views here.
from django.template.defaultfilters import title

from blog.models import BlogPost


def home(reqeust):
    blogarchives = BlogPost.objects.all().order_by('-timestamp')
    context = { 'blogarchives': blogarchives }

    return render(reqeust, 'lightlog-index.html',context)

def detail(reqeust,id):

    archive = BlogPost.objects.get(id=id)

    context = {'archive': archive}
    return render(reqeust, 'detail.html',context)


'''
def getpost(reqeust):

    title=reqeust.POST['title'],
    body = reqeust.POST['body'],
    timestamp = datetime.now(),
    context = {'title':title,'body':body,'timestamp':timestamp,}
    return render(reqeust,'getpost.html',context) 
'''
def create(reqeust):

    if request.method == 'POST':
        BlogPost(
        title = reqeust.POST['title'],
        body1 = reqeust.POST['body'],
        timestamp = datetime.now(),
            ).save()
    return render(reqeust, 'archive.html')

def getpost(reqeust):

    return render(reqeust,'getpost.html')
def archive(reqeust):
    title = reqeust.POST['title'],
    body = reqeust.POST['body'],
    timestamp = datetime.now(),
    context = {'title': title, 'body': body, 'timestamp': timestamp, }
    return render(reqeust, 'archive.html', context)
