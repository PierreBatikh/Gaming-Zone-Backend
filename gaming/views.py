from django.shortcuts import redirect, render
from .models import Submitter, Pro, Newbie

# Create your views here.
def index(request):
    return render(request, 'index.html')

def newbie(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        age = request.POST.get('Age')
        platform = request.POST.get('Platform')
        fav_game = request.POST.get('Favourite Game')
        genre = request.POST.get('Genre')
        submitter = Submitter.objects.create(name=name, age=age)
        submitter.save()
        new = Newbie.objects.create(platform=platform, fav_game=fav_game, genre=genre, submitter=submitter)
        new.save()
        return redirect('thanks')
    return render(request, 'newbie.html')


def pro(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        age = request.POST.get('Age')
        platform = request.POST.get('Platform')
        # here should add a check for the option, to make sure it's valid
        fav_game = request.POST.get('Favourite Game')
        genre = request.POST.get('Genre')
        game_art_style = request.POST.get('Style')
        clash_royal = request.POST.get('Clash Royale')
        hollow_knight = request.POST.get('Hollow Knight: Silksong')
        rdr2 = request.POST.get('RDR2')
        submitter = Submitter.objects.create(name=name, age=age)
        submitter.save()
        pro = Pro.objects.create(
            platform=platform, fav_game=fav_game, genre=genre, game_art_style=game_art_style,
            clash_royal=clash_royal, hollow_knight=hollow_knight, rdr2=rdr2, submitter=submitter)
        pro.save()
        return redirect('thanks')
    return render(request, 'pro.html')

def thanks(request):
    return render(request, 'thanks.html')


