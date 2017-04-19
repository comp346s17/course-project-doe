from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import Profile, ProfileForm

# Create your views here.

def home(request):
    if request.user.is_authenticated():
        return render(request,'smack/home.html')
    else:
        return redirect('signin')

def login(request):
    return render(request,'smack/login.html')

def signin(request):
    return render(request,'smack/signin.html')

def signup(request):
    if request.method == 'POST':
        userForm = UserCreationForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            username = userForm.cleaned_data.get('username')
            raw_password = userForm.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('personalProfile')
    else:
        userForm = UserCreationForm()
    return render(request, 'smack/signup.html', {'form': userForm})

def personalProfile(request):
    print(request.POST)
    currentProfile = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            year = form.cleaned_data.get('year')
            major = form.cleaned_data.get('major')
            gender = form.cleaned_data.get('gender')
            sexualOrientation = form.cleaned_data.get('sexualOrientation')
            bio = form.cleaned_data.get('bio')
            idealDate = form.cleaned_data.get('idealDate')
            kagin = form.cleaned_data.get('kagin')
            cafemac = form.cleaned_data.get('cafemac')
            athletes = form.cleaned_data.get('athletes')
            cold = form.cleaned_data.get('cold')
            lookingFor = form.cleaned_data.get('lookingFor')
            friendLookingFor = form.cleaned_data.get('friendLookingFor')
            politics = form.cleaned_data.get('politics')
            aesthetics = form.cleaned_data.get('aesthetics')
            nap = form.cleaned_data.get('nap')
            saturday = form.cleaned_data.get('saturday')
            appSampler = form.cleaned_data.get('appSampler')
            pic = request.FILES['pic']
            total = idealDate+kagin+cafemac+athletes+cold+lookingFor+friendLookingFor+politics+aesthetics+nap+saturday+appSampler
            score = float(total)/12.0
            Profile.objects.create(user=currentProfile,year=year,major=major,gender=gender,sexualOrientation=sexualOrientation,bio=bio,idealDate=idealDate,kagin=kagin,cafemac=cafemac,athletes=athletes,cold=cold,lookingFor=lookingFor,friendLookingFor=friendLookingFor,politics=politics,aesthetics=aesthetics,nap=nap,appSampler=appSampler,saturday=saturday,score=score,pic=pic)
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'smack/personProfile.html',{'form':form})

def datingFeed(request):
    profiles = Profile.objects.all().exclude(user=request.user)
    if request.user.is_authenticated():
        user = request.user
    profile = Profile.objects.get(user=user)
    profileLike = profile.like.all()
    profileDislike = profile.dislike.all()
    if profile.sexualOrientation=='men' and profile.gender=='female':
        profiles = Profile.objects.filter(gender='male').exclude(sexualOrientation='men')
    elif profile.sexualOrientation=='women' and profile.gender=='male':
        profiles = Profile.objects.filter(gender='female').exclude(sexualOrientation='women')
    elif profile.sexualOrientation=='men' and profile.gender=='male' :
        profiles = Profile.objects.filter(gender='male').exclude(sexualOrientation='women')
    elif profile.sexualOrientation=='women' and profile.gender=='female' :
        profiles = Profile.objects.filter(gender='female').exclude(sexualOrientation='men')
    print(profileLike)
    print(profileDislike)
    return render(request, 'smack/feed.html',{'profiles': profiles,'current': profile, 'like':profileLike, 'dislike':profileDislike})

def friendFeed(request):
    profiles = Profile.objects.all().exclude(user=request.user)
    if request.user.is_authenticated():
        user = request.user
    profile = Profile.objects.get(user=user)
    profileLike = profile.like.all()
    profileDislike = profile.dislike.all()
    return render(request, 'smack/feed.html',{'profiles': profiles,'current': profile, 'like':profileLike, 'dislike':profileDislike})
