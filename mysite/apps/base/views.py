from django.shortcuts import render

def top(request):
    ctx = {'title': 'サービス名'}
    return render(request, 'base/top.html', ctx)