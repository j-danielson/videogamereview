from django.shortcuts import render, get_object_or_404
from .forms import VideoGameForm, ReviewForm
from reviewapp.forms import VideoGameForm
from .models import Videogame, Vgreview
from django.contrib.auth.decorators import login_required 
from django.db.models import Avg, Sum

# Create your views here.
def index(request):
    return render(request, 'reviewapp/index.html')

def videogames(request):
    videogame_list=Videogame.objects.all()
    return render(request, 'reviewapp/videogames.html', {'videogame_list': videogame_list})

def videogamedetail(request, id):
    videogamedetail=get_object_or_404(Videogame, pk=id)
    review_list=Vgreview.objects.filter(vgid=id)
    review_count=Vgreview.objects.filter(vgid=id).count()
    review_average=Vgreview.objects.filter(vgid=id).aggregate(Avg('Rating'))['Rating__avg'] or 0.0
    context={
        'videogamedetail' : videogamedetail,
        'review_list' : review_list,
        'review_count' : review_count,
        'review_average' : review_average,
    }
    return render(request, 'reviewapp/videogamedetail.html', context=context)

def vgreview(request, id):
    vgreview=get_object_or_404(Vgreview, pk=id)
    return render(request, 'reviewapp/videogamereview.html', {'vgreview' : vgreview})

@login_required
def addvideogame(request):
    form=VideoGameForm

    if request.method=='POST':
        form=VideoGameForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=VideoGameForm()
    else:
        form=VideoGameForm()
    return render(request, 'reviewapp/addvideogame.html', {'form' : form})

@login_required
def addreview(request, id):
    form=ReviewForm

    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm(initial={'vgid' : id})
    return render(request, 'reviewapp/addreview.html', {'form' : form})

def loginmessage(request):
    return render(request, 'reviewapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'reviewapp/logoutmessage.html')