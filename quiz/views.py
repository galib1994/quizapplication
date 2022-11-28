from django.shortcuts import render
from .models import User
from django.db.models import Q

# Create your views here.
def index(request):
    data = User.objects.all()
    if request.method == "POST" and 'btnform1' in request.POST:
        search = request.POST.get('search')
        data=User.objects.filter(Q(name__icontains=search) | Q(gender__icontains=search) | Q(discription__icontains=search)|Q(query_image__icontains=search))     
        print(search)
    return render(request, 'quiz/index.html',{'data':data})