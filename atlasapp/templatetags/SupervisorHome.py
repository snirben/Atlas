from django import template
from atlasapp.models import *

register = template.Library()


@register.filter
def avgSteps(gan):
    sumSteps=0
    childGames = Game.objects.all()

    for i in childGames:
        if i.user.gan == gan:
            sumSteps += i.steps
    avgSteps = sumSteps / len(childGames)
    return avgSteps