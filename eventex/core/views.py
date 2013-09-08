# coding: utf-8

from django.shortcuts import render, redirect


def home(request):
    """ Exibe a home """
    return render(request, 'home.html')