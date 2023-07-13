from django.shortcuts import render
def mainpage(request):
 return render(request, 'pages/mainpage.html')
def company(request):
 return render(request, 'pages/company_info.html')
def homepage(request):
 return render(request, 'pages/homepage.html')
def login(request):
 return render(request, 'pages/login.html')
def find(request):
 return render(request, 'pages/find.html')
def custmer(request):
 return render(request, 'pages/custmer.html')