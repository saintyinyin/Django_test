from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo,PeopleInfo

# Create your views here.
def createbook(request):
    book=BookInfo.objects.create(
        name='abc',
        pub_date='2000-1-1',
        readcount=10
    )
    return HttpResponse('create')