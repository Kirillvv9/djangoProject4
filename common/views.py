from datetime import datetime
from random import randrange
from django.shortcuts import render

from django.views import View
from django.http import HttpResponse


class CurrentDateView(View):
   def get(self, request):
       html = f"{datetime.now()}"
       return HttpResponse(html)


class CurrentRandomView(View):
   def get(self, request):
       random_number = randrange(0, 100, 1)

       return HttpResponse(random_number)

class CurrentHelloView(View):
   def get(self, request):
       fraz = "Hello World"
       return HttpResponse(fraz)

class IndexView(View):
   def get(self, request):
       return render(request, 'common/index.html')

