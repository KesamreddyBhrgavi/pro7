from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'wish.html',context=d)


def conditions(request):
    d={'a':30,'b':40,'c':50}
    return render(request,'conditions.html',context=d)

def loop(request):
    d={'name':'ashu'}
    return render(request,'loop.html',d)