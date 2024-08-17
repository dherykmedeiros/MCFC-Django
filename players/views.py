from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import PlayerSingUpForm, PlayerProfileForm
from .models import Player
from django.contrib.auth.decorators import login_required



def players_list(request):
    players = Player.objects.all()
    return render(request,'players/players.html',{'players':players})

def signup(request):
    if request.method == 'POST':
        form = PlayerSingUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Criação do objeto Player associado ao usuário
            player = Player.objects.create(
                user=user,
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                date_born=form.cleaned_data.get('date_born'),
                position=form.cleaned_data.get('position'),
                dominant_leg=form.cleaned_data.get('dominant_leg'),
                specialty=form.cleaned_data.get('specialty'),
            )
            
            login(request, user)
            return redirect('players')
    else:
        form = PlayerSingUpForm()
    return render(request, 'players/signup.html', {'form': form})


    


@login_required
def edit_profile(request):
    try:
        player = request.user.player
    except Player.DoesNotExist:
        player = None
    
    if request.method == 'POST':
        form = PlayerProfileForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('players')
    else:
        form = PlayerProfileForm(instance=player)
    
    return render(request, 'players/edit_profile.html', {'form': form})
