from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import bataskabupaten
from django.core.serializers import serialize

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


def home(request):
    #count = User.objects.count()
    #all_lists = Kecamatan.objects.all().order_by('kodeKec')
    return render(request, 'home.html', {
        #'count': count,
        #'all_lists': all_lists,
    })

def BataskabupatenData(request):
    kabupaten = serialize('geojson', bataskabupaten.objects.all())
    return HttpResponse(kabupaten, content_type='json')
