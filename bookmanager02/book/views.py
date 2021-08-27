from collections import namedtuple
from django.http.response import HttpResponse
from django.shortcuts import render
from book.models import BookInfo,PeopleInfo

# Create your views here.
def index(request):
    # here add insert/delete/update/select
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse('index')



# insert data method 1
book=BookInfo(
    name='Django', 
    pub_date='1931-4-24',
    readcount=0,
    commentcount=0,
    is_delete=0
    )

book.save()

# insert data method 2
BookInfo.objects.create(    
    name='Django2', 
    pub_date='1931-4-25',
    readcount=0,
    commentcount=0,
    is_delete=0
)


# update method 1
book = BookInfo.objects.get(id=6)
book.name = "manage"
book.save()

# update method 2
BookInfo.objects.filter(id=6).update(name="show show")


# drop method 1
# physical(here use this) or logical
book=BookInfo.objects.get(id=6)
book.delete()

# drop method 2
BookInfo.objects.filter(id=5).delete()

# get one record
try:
    book=BookInfo.objects.get(id=6)
except BookInfo.DoesNotExist:
    print('record not exist')

# get all records
books=BookInfo.objects.all()

# filter(属性名__运算符=值)
books = BookInfo.objects.filter(name__contains='湖')
books = BookInfo.objects.filter(name__endswith='部')
books = BookInfo.objects.filter(name__isnull=True)
books = BookInfo.objects.filter(id__in=(1,3,5))
books = BookInfo.objects.filter(pub_date__year=1980)
# exclude(属性名__运算符=值)
books = BookInfo.objects.exclude(id=3)
# get(属性名__运算符=值) or get(属性名=值)
book=BookInfo.objects.get(id=6)
book=BookInfo.objects.get(pk=6)


################# F Objects ##################
from django.db.models import F

# usage : 2 properties compare
# <model>.objects.filter(属性名__运算符=F('第二个属性名'))
books = BookInfo.objects.filter(readcount__gte=F('commentcount'))


# and
books = BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
books = BookInfo.objects.filter(readcount__gt=20,id__lt=3)

################# Q Objects ##################
from django.db.models import Q

# or <model>.objects.filter(Q(属性名__运算符=值)|Q()|...)
# and <model>.objects.filter(Q(属性名__运算符=值)&Q()&...)
# not <model>.objects.filter(~Q(属性名__运算符=值))
books = BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))


#############aggregate#############
from django.db.models import Sum, Max, Min, Avg, Count
# <model>.objects.aggregate(xxx(column_name))
readct = BookInfo.objects.aggregate(Sum('readcount'))


#############sort##############
books.order_by('name')
books.order_by('-name')



################### two tables operations ###############
# query all people whose book is 1
book = BookInfo.objects.get(id=1)
peoples = book.peopleinfo_set.all()

# query book that people is 1
person = PeopleInfo.objects.get(id=1)
book  = person.book


##################关联过滤查询#####################
# 查询图书，图书人物为郭靖
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
BookInfo.objects.filter(peopleinfo__name='郭靖')

# 查询图书，要求图书中人物描述包含“八”
BookInfo.objects.filter(peopleinfo__description__contains='八')