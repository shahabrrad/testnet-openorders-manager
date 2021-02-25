from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("hello")

    context = {
        'title' : 'latest order',
        'orderlist' : [{'title': "one" , 'body': "body one"} , {'title': "two" , 'body': "body two"}]
    }

    return render(request , "order/index.html" , context)