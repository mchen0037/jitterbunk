from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db.models import Q
from .models import Bunk, User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your views here.

def index(request):
    latest_bunks = Bunk.objects.order_by('-time')[:10]
    context = {'latest_bunks': latest_bunks}
    return render(request, 'bunk/index.html', context)

def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    recent_bunks = Bunk.objects.order_by('-time').filter(
                        Q(from_user=user) | Q(to_user=user)
                        )[0:10]

    bunk_score = 0
    positive_bunk_score = Bunk.objects.filter(from_user=user).count()
    negative_bunk_score = Bunk.objects.filter(to_user=user).count()
    bunk_score = positive_bunk_score - negative_bunk_score
    context = {
        'user' : user,
        'recent_bunks' : recent_bunks,
        'bunk_score' : bunk_score,
        'total_bunks' : positive_bunk_score
    }
    return render(request, 'bunk/profile.html', context)

def bunk(request):
    to_user = User.objects.filter(pk=request.POST['to_user'])[0]
    from_user = User.objects.filter(pk=request.POST['from_user'])[0]
    new_bunk = Bunk(from_user=from_user, to_user=to_user, time=timezone.now())
    new_bunk.save()
    context = {
        'just_bunked' : to_user
    }
    return HttpResponseRedirect('/', context)
