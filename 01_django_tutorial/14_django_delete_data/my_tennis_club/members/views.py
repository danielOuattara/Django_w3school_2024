#  Before :

""" 
from django.shortcuts import render
from django.http import HttpResponse


def members(request):
    return HttpResponse("Hello World !")
 """

# -----------------------------------------
#  After :


from django.http import HttpResponse
from django.template import loader


def members(request):
    template = loader.get_template('my_first.html')
    return HttpResponse(template.render())
