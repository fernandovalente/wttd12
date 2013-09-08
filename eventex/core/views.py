# coding: utf-8

from django.shortcuts import render, redirect


def home(request):
    """ Exibe a home com form para encurtar a URL """
    return render(request, 'home.html')