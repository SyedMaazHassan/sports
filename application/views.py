from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
import json
from csv import reader
import sqlite3
import os
import numpy as np
import pandas as pd
import sklearn
from sklearn.feature_extraction import text  
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.svm import SVC
import seaborn as sns
import base64
from io import BytesIO
from matplotlib.figure import Figure





# main page function

def index(request):
    context = {}

    all_leagues = league.objects.all()

    for i in all_leagues:
        i.make_url_name()

    context['all_leagues'] = all_leagues

        # generat_graph() is a function to calculate confusion matrix and plot

    return render(request, 'index.html', context)


def per_league(request, leagueName):
    context = {}
    new_name = leagueName.replace("-", " ")

    particular_league = league.objects.get(league_name=new_name)

    context['LEAGUE'] = particular_league

    if division.objects.filter(parent_league=particular_league).exists():
        context['DIVISIONS'] = division.objects.filter(parent_league=particular_league)

    
    return render(request, 'leagues.html', context)





# function for signup


def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        dob = request.POST['dob']
        pic = request.FILES['image']
        context = {
            "name":name,
            "email":email,
            "pass1":pass1,
            "pass2":pass2,
            "dob":dob,
            "pic":pic
        }
        if pass1==pass2:
            if User.objects.filter(username=email).exists():
                print("Email already taken")
                messages.info(request, "Entered email already in use!")
                context['border'] = "email"
                return render(request, "signup.html", context)

            user = User.objects.create_user(username=email, email=dob, first_name=name, password=pass1, last_name=pic)
            user.save()

            save_img = profile_pics(id=request.user.id, user_img=pic)
            save_img.save()


            return redirect("login")
        else:
            messages.info(request, "Your pasword doesn't match!")
            context['border'] = "password"
            return render(request, "signup.html", context)



    return render(request, "signup.html")




# function for login

def login(request):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Incorrect login details!")
            return redirect("login")
    else:
        return render(request, "login.html")


# function for logout

def logout(request):
    auth.logout(request)
    return redirect("index")


def add_team(request):
    if request.method == 'POST':
        team_logo = request.FILES['image']
        team_name = request.POST['team_name']

        representative_pic = request.FILES['image2']
        representative_name = request.POST['rep_name']

        coach_pic = request.FILES['image3']
        coach_name = request.POST['coach_name']

        print('team_logo', team_logo)
        print('team_name', team_name)
        print()
        print('representative_pic', representative_pic)
        print('representative_name', representative_name)
        print()
        print('coach_pic', coach_pic)
        print('coach_name', coach_name)

        new_team = team(
            team_logo = team_logo, 
            team_name = team_name, 
            team_captain = request.user,
            representative_name = representative_name,
            representative_pic = representative_pic,
            coach_name = coach_name,
            coach_pic = coach_pic
        )

        new_team.save()

    return redirect("profile")

def add_player(request):
    if request.method == 'POST':
        team_id = int(request.POST['team_id'])
        player_image = request.FILES['profile']
        player_name = request.POST['player_name']
        player_phone = request.POST['phone']
        player_dob = request.POST['dob']


        print('team_id', team_id)
        print('player_image', player_image)
        print('player_name', player_name)
        print('player_phone', player_phone)
        print('player_dob', player_dob)

        new_player = player(
            parent_team = team.objects.get(id = team_id),
            player_img = player_image,
            player_name = player_name,
            player_phone = player_phone,
            player_dob = player_dob
        )

        new_player.save()

    return redirect("profile")


def profile(request):
    context = {}

    if not request.user.is_authenticated:
        return redirect("index")

    if team.objects.filter(team_captain=request.user).exists():
        empty_teams = []
        all_teams = team.objects.filter(team_captain=request.user)

        for i in all_teams:
            i.get_players()
            empty_teams.append(i)

        context['TEAMS'] = empty_teams
        
    return render(request, 'profile.html', context)