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
def customer(request):
 return render(request, 'pages/customer.html')
def membership(request):
 return render(request, 'pages/membership.html')
def shopping(request):
 return render(request, 'pages/shopping.html')
def mypage(request):
 return render(request, 'pages/mypage.html')