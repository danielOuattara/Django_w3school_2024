

from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q


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


def testing(request):

    # all members:
    members = Member.objects.all().values()

    # filter
    emil = Member.objects.filter(first_name='Emil').values()

    # filter AND
    refsnes = Member.objects.filter(last_name='Refsnes', id=2).values()

    # filter OR using pipe |
    email_or_tobias_1 = Member.objects.filter(first_name='Emil').values(
    ) | Member.objects.filter(first_name='Tobias').values()

    # filter OR using Q class
    email_or_tobias_2 = Member.objects.filter(
        Q(first_name='Emil') | Q(first_name='Tobias')).values()

    # Field Lookups Syntax

    field_lookup_data = Member.objects.filter(
        first_name__startswith='L').values()

    template = loader.get_template('template.html')

    context = {
        'members': members,
        'emil': emil,
        'refsnes': refsnes,
        'email_or_tobias_1': email_or_tobias_1,
        'email_or_tobias_2': email_or_tobias_2,
        'field_lookup_data': field_lookup_data,
    }

    return HttpResponse(template.render(context, request))
