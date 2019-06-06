from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

from django.db.models import Q

from .models import Bunk
from django.contrib.auth.models import User
from django.utils import timezone
# Create your views here.

def index(request):
    latest_bunks = Bunk.objects.order_by('-time')[:10]
    context = {'latest_bunks': latest_bunks}
    return render(request, 'bunk/index.html', context)

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    bunks_between_users = Bunk.objects.order_by('-time').filter(
                            Q(from_user=user) | Q(to_user=user))
    recent_bunks = bunks_between_users[:10]

    bunk_score = 0
    positive_bunk_score = bunks_between_users.filter(from_user=user).count()
    negative_bunk_score = bunks_between_users.filter(to_user=user).count()
    bunk_score = positive_bunk_score - negative_bunk_score
    context = {
        'profile_user' : user,
        'recent_bunks' : recent_bunks,
        'bunk_score' : bunk_score,
        'total_bunks' : positive_bunk_score
    }
    return render(request, 'bunk/profile.html', context)

@login_required
def bunk(request):
    to_user = get_object_or_404(User, pk=request.POST['to_user'])
    from_user = get_object_or_404(User, pk=request.POST['from_user'])
    new_bunk = Bunk(from_user=from_user, to_user=to_user)
    new_bunk.save()
    print(context)
    messages.success(request, "Successfully bunked %s!" % (from_user.first_name))
    return HttpResponseRedirect('/')

def logout(request, **kwargs):
    auth_logout(request, **kwargs)
    return HttpResponseRedirect('/')
