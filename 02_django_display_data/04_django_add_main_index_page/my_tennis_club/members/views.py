#  Before :


# from django.shortcuts import render
# from django.http import HttpResponse


# def members(request):
#     return HttpResponse("Hello World !")


# -----------------------------------------
#  After :


# from django.http import HttpResponse
# from django.template import loader


# def members(request):
#     template = loader.get_template('my_first.html')
#     return HttpResponse(template.render())


# ------------------------------------------
# After 2


# from django.http import HttpResponse
# from django.template import loader
# from .models import Member


# def members(request):
#     my_members = Member.objects.all().values()
#     template = loader.get_template('all_members.html')
#     context = {
#         'my_members': my_members
#     }
#     return HttpResponse(template.render(context, request))

# ------------------------------------------
# After 3

# from django.http import HttpResponse
# from django.template import loader
# from .models import Member


# def members(request):
#     my_members = Member.objects.all().values()
#     template = loader.get_template('all_members.html')
#     context = {
#         'my_members': my_members
#     }
#     return HttpResponse(template.render(context, request))


# def details(request, id):
#     my_member = Member.objects.get(id=id)
#     template = loader.get_template('details.html')
#     context = {
#         'my_member': my_member
#     }

#     return HttpResponse(template.render(context, request))


# ------------------------------------------
# After 4

from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    my_members = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'my_members': my_members
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    my_member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'my_member': my_member
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
