

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


def testing(request):  # <-- New !
    template = loader.get_template('template.html')
    members = Member.objects.all().values()
    context = {
        # 'greeting': 1,
        'greeting': 2,
        # 'greeting': 3,
        'day': 'Friday',
        'fruits': ['Apple', 'Banana', 'Cherry'],
        'x': ['Apple', 'Banana', 'Cherry'],
        'y': ['Apple', 'Banana', 'Cherry'],
        'cars': [
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964',
            }],
        'members': members
    }

    return HttpResponse(template.render(context, request))
