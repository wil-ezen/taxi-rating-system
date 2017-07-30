from django.http import HttpResponse
from .models import Taxi

def index(request):
    taxi_list = Taxi.objects.order_by('overall_rating')[:5]
    output = ', '.join([str(t.overall_rating) for t in taxi_list])
    return HttpResponse(output)