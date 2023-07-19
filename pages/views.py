from django.shortcuts import render
def mainpage(request):
 return render(request, 'pages/mainpage.html')
def company(request):
 return render(request, 'pages/company_info.html')
def context(request):
 return render(request, 'pages/context_list.html')