from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    chais = ChaiVarity.objects.all()
    data = {"title": "Home Page", "chai_data": chais}
    return render(request, "home.html", data)


def detail_chai_page(request, chai_id):

    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    data = {"title": "Chai Detail Page", "chai_data": chai}
    return render(request, "detail_chai.html", data)
