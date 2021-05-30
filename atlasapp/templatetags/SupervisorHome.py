from django import template
from atlasapp.models import Game

register = template.Library()


@register.filter
def avgSteps(gan):
    sum_steps = 0
    child_games = Game.objects.all()

    for i in child_games:
        if i.user.gan == gan:
            sum_steps += i.steps
    if len(child_games) == 0:
        return 0
    avg_steps = sum_steps / len(child_games)
    return avg_steps
