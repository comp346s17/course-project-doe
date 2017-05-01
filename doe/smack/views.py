from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import Profile, ProfileForm
from django.http import JsonResponse

# Create your views here.

# home page, will redirect you to signup page if not signed in
def home(request):
    if request.user.is_authenticated():
        return render(request,'smack/home.html')
    else:
        return redirect('signup')

# login page
def login(request):
    return render(request,'smack/login.html')

# signin page
def signin(request):
    return render(request,'smack/signin.html')

# signup page, creates a new user object that will become a part of a profile, redirects to personalProfile when done
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

# creates a new personalProfile for a user
def personalProfile(request):
    print(request.POST)
    currentProfile = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
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
            if request.user.is_authenticated():
                user = request.user
            profile = Profile.objects.get(user=user)
            profile.dislike.add(profile)
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'smack/personProfile.html',{'form':form})

# displays the proper people for the datingFeed
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
    return render(request, 'smack/feed.html',{'profiles': profiles,'current': profile, 'like':profileLike, 'dislike':profileDislike,'feed':'Dating'})

# displays the proper people for the datingFeed
def friendFeed(request):
    profiles = Profile.objects.all().exclude(user=request.user)
    if request.user.is_authenticated():
        user = request.user
    profile = Profile.objects.get(user=user)
    profileLike = profile.like.all()
    profileDislike = profile.dislike.all()
    return render(request, 'smack/feed.html',{'profiles': profiles,'current': profile, 'like':profileLike, 'dislike':profileDislike, 'feed':'Friend'})

# allows you to edit your profile, will load existing information
def editProfile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile.full_name = form.cleaned_data.get('full_name')
            profile.email = form.cleaned_data.get('email')
            profile.year = form.cleaned_data.get('year')
            profile.major = form.cleaned_data.get('major')
            profile.gender = form.cleaned_data.get('gender')
            profile.sexualOrientation = form.cleaned_data.get('sexualOrientation')
            profile.bio = form.cleaned_data.get('bio')
            profile.idealDate = form.cleaned_data.get('idealDate')
            profile.kagin = form.cleaned_data.get('kagin')
            profile.cafemac = form.cleaned_data.get('cafemac')
            profile.athletes = form.cleaned_data.get('athletes')
            profile.cold = form.cleaned_data.get('cold')
            profile.lookingFor = form.cleaned_data.get('lookingFor')
            profile.friendLookingFor = form.cleaned_data.get('friendLookingFor')
            profile.politics = form.cleaned_data.get('politics')
            profile.aesthetics = form.cleaned_data.get('aesthetics')
            profile.nap = form.cleaned_data.get('nap')
            profile.saturday = form.cleaned_data.get('saturday')
            profile.appSampler = form.cleaned_data.get('appSampler')
            profile.pic = request.FILES['pic']
            total = profile.idealDate+profile.kagin+profile.cafemac+profile.athletes+profile.cold+profile.lookingFor+profile.friendLookingFor+profile.politics+profile.aesthetics+profile.nap+profile.saturday+profile.appSampler
            profile.score = float(total)/12.0
            profile.save()
            return redirect('home')
    else:
        data = {'year':profile.year,'major':profile.major,'gender':profile.gender,'sexualOrientation':profile.sexualOrientation,'bio':profile.bio,'email':profile.email,'idealDate':profile.idealDate,'kagin':profile.kagin,'cafemac':profile.cafemac,'athletes':profile.athletes,'cold':profile.cold,'lookingFor':profile.lookingFor}
        data1 = {'politics':profile.politics,'aesthetics':profile.aesthetics,'nap':profile.nap,'saturday':profile.saturday,'appSampler':profile.appSampler,'friendLookingFor':profile.friendLookingFor,'pic':profile.pic}
        data.update(data1)
        form = ProfileForm(initial=data)
    return render(request, 'smack/editProfile.html', {'form':form})

# allows you to like a profile without refreshing the page
def ajax_like(request):
    profile = Profile.objects.get(user=request.user)
    username = request.GET.get('username', None)
    likedUser = User.objects.get(username=username)
    likedProfile = Profile.objects.get(user=likedUser)
    profile.like.add(likedProfile)
    profile.dislike.remove(likedProfile)
    data = {
        'success' : 'success'
    }
    return JsonResponse(data)

# allows you to dislike a profile without refreshing the page
def ajax_dislike(request):
    profile = Profile.objects.get(user=request.user)
    username = request.GET.get('username', None)
    dislikedUser = User.objects.get(username=username)
    dislikedProfile = Profile.objects.get(user=dislikedUser)
    profile.dislike.add(dislikedProfile)
    profile.like.remove(dislikedProfile)
    data = {
        'success' : 'success'
    }
    return JsonResponse(data)
