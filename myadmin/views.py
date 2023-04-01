from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    tours = Tour.objects.all()
    loc = Location.objects.all()
    pack = Package.objects.all()
    travel= TravelOffer.objects.all()
    post= RecentPost.objects.all()
    guide= TourGuide.objects.all()
    about= About.objects.all()
    context = {'tours': tours, 'loc': loc, 'pack': pack, 'travel': travel, 'post': post, 'guide': guide, 'about': about}
    if request.method == 'POST':
        if 'submit' in request.POST:
            tour_type = request.POST.get('tour_type')
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            city= request.POST.get('city')
            state= request.POST.get('state')
            budget= request.POST.get('budget')
            query = request.POST.get('query')
            userd = Contact(tour_type=tour_type, name=name, email=email, phone=phone, city=city, state=state, budget=budget, query=query)
            userd.save()
        elif 'submit1' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone= request.POST.get('phone')
            date= request.POST.get('date')
            query= request.POST.get('query')
            used = Enquire(name=name, email=email,phone=phone, date=date, query=query)
            used.save()
    return render(request, 'index.html', context)
