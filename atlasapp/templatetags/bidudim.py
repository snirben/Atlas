from django import template
from atlasapp.models import User

register = template.Library()


@register.filter
def activateornot(gan):
    users = User.objects.filter(gan=gan, covid=True).count()
    if users > 0:
        return 'לא פעיל'
    return 'פעיל'

@register.filter
def percentofcovid(gan):
    allusers = User.objects.filter(gan=gan).count()
    covidusers = User.objects.filter(gan=gan, covid=True).count()
    percentofcovid = (covidusers/allusers)*100
    return percentofcovid
