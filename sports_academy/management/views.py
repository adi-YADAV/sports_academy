from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import PlayerForm, CoachLoginForm
from .models import Player
from .forms import PlayerRegistrationForm
# Coach login view
def coach_login(request):
    if request.method == 'POST':
        form = CoachLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CoachLoginForm()
    return render(request, 'management/login.html', {'form': form})

@login_required
def player_registration(request):
    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page, list page, or elsewhere
    else:
        form = PlayerRegistrationForm()

    return render(request, 'management/player_registration.html', {'form': form})

@login_required
def update_player(request, player_id):
    player = Player.objects.get(id=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'management/update_player.html', {'form': form})

@login_required
def player_list(request):
    players = Player.objects.filter(coach=request.user)
    return render(request, 'management/player_list.html', {'players': players})

# Coach logout view
def coach_logout(request):
    logout(request)
    return redirect('coach_login')


def coach_logout(request):
    logout(request)
    return redirect('coach_login')

