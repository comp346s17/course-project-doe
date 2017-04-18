from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your models here.

YEAR = [
('FY','First Year'),
('SO','Sophomore'),
('JR','Junior'),
('SR','Senior'),
]
GENDER = [
('male','Male'),
('female','Female'),
('other','Other'),
]
SEXORIENT = [
('men','Men'),
('women','Women'),
('bisexual','Bisexual'),
('other','Other')
]
IDEALDATE = [
(1,'Long walk on the beach'),
(5,'Cuddle in front of the fireplace with a glass of wine'),
(10,'Not really a date person'),
]
KAGIN = [
(1,'Not really my scene'),
(5,'I\'ll give it a try, but the pregame will probably be more fun'),
(10,'Lets do this thing.'),
]
CAFEMAC = [
(1,'North'),
(4,'East'),
(6,'West'),
(10,'South'),
]
ATHLETES = [
(1,'Can\'t stand them'),
(5,'They\'re alright'),
(10,'I love them')
]
COLD = [
(1,'I love it'),
(4,'It\'s not so bad'),
(6, 'Not my favorite'),
(10, 'Minnesota is hell on Earth'),
]
LOOKINGFOR = [
(1,'Something a little more serious'),
(4,'Unsure'),
(7,'Repeated hookup'),
(10,'One night stand')
]
POLITICS = [
(1,'Alt-Left'),
(4,'Fairly Left'),
(6,'Moderate'),
(10,'Mac GOP'),
]
AESTHETICS = [
(1,'Pear'),
(3,'Grapefruit'),
(5,'Melon'),
(8,'Banana'),
(10,'Pineapple'),
]
NAP = [
(1,'Alone in my room'),
(5,'The library'),
(10,'Anywhere')
]
SATURDAY = [
(1,'Attended a lecture'),
(5,'Went out with friends'),
(10,'I don\'t remember'),
]
APPSAMPLER = [
(1,'Fries'),
(5,'Mozzarella Sticks'),
(10, 'Jalapeno Poppers'),
]
FRIENDLOOKINGFOR = [
(1,'A good friend'),
(4,'Unsure'),
(7,'Hang out occasionally'),
(10,'High five when drunk')
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    year = models.CharField(max_length=10, choices=YEAR)
    major = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER)
    sexualOrientation = models.CharField(max_length=20, choices=SEXORIENT)
    bio = models.TextField()

    # data
    idealDate = models.IntegerField(choices=IDEALDATE)
    kagin = models.IntegerField(choices=KAGIN)
    cafemac = models.IntegerField(choices=CAFEMAC)
    athletes = models.IntegerField(choices=ATHLETES)
    cold = models.IntegerField(choices=COLD)
    lookingFor = models.IntegerField(choices=LOOKINGFOR)
    politics = models.IntegerField(choices=POLITICS)
    aesthetics = models.IntegerField(choices=AESTHETICS)
    nap = models.IntegerField(choices=NAP)
    saturday = models.IntegerField(choices=SATURDAY)
    appSampler = models.IntegerField(choices=APPSAMPLER)
    friendLookingFor = models.IntegerField(choices=FRIENDLOOKINGFOR)
    score = models.FloatField()

class ProfileForm(forms.Form):
    year = forms.ChoiceField(label='What year are you?',required=False,choices=YEAR)
    major = forms.CharField(label='What is your intended major?',required=False,max_length=100)
    gender = forms.ChoiceField(label='What is your gender?',required=False,choices=GENDER)
    sexualOrientation = forms.ChoiceField(label='What gender do you prefer?',required=False,choices=SEXORIENT)
    bio = forms.CharField(label='Tell us a little about yourself',max_length=200)
    idealDate = forms.ChoiceField(label='What is your ideal date?',required=False,choices=IDEALDATE,widget=forms.Select())
    kagin = forms.ChoiceField(label='There\'s a Kagin tonight, what are you thinking?',required=False,choices=KAGIN,widget=forms.Select())
    cafemac = forms.ChoiceField(label='What\'s your favorite station at Cafe Mac?',required=False,choices=CAFEMAC,widget=forms.Select())
    athletes = forms.ChoiceField(label='How do you feel about athletes?',required=False,choices=ATHLETES,widget=forms.Select())
    cold = forms.ChoiceField(label='How do you feel about the cold?',required=False,choices=COLD,widget=forms.Select())
    lookingFor = forms.ChoiceField(label='What are you looking for in a partner?',required=False,choices=LOOKINGFOR,widget=forms.Select())
    friendLookingFor = forms.ChoiceField(label='What are you looking for in a friend?',required=False,choices=FRIENDLOOKINGFOR,widget=forms.Select())
    politics = forms.ChoiceField(label='Where do your politics fall?',required=False,choices=POLITICS,widget=forms.Select())
    aesthetics = forms.ChoiceField(label='Which fruit do you find most aesthetically pleasing?',required=False,choices=AESTHETICS,widget=forms.Select())
    nap = forms.ChoiceField(label='Where is your favorite spot to nap?',required=False,choices=NAP,widget=forms.Select())
    saturday = forms.ChoiceField(label='What did you do on Saturday night?',required=False,choices=SATURDAY,widget=forms.Select())
    appSampler = forms.ChoiceField(label='What is your favorite thing to get in the app sampler?',required=False,choices=APPSAMPLER,widget=forms.Select())
