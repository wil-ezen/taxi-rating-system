from django.http import HttpResponse
from django.template import loader
from .models import Taxi


def index(request):
    submitted_number_plate = request.POST['submitted_number_plate']
    # This could return multiple number plates if the entry is not complete
    submitted_number_plate_list = Taxi.objects.filter(number_plate__startswith=submitted_number_plate)
    if not submitted_number_plate_list:
        submitted_number_plate_rating = 0.0
    else:
        submitted_number_plate_rating = submitted_number_plate_list[0].overall_rating
    template = loader.get_template('taxi/index.html')
    # submitted_number_plate = 'Default string'
    context = {
        'submitted_number_plate': submitted_number_plate,
        'submitted_number_plate_rating': submitted_number_plate_rating
    }
    return HttpResponse(template.render(context, request))


# def details(request):
#     return HttpResponse('HELLO FROM DETAILS!!!!')


# def details(request, submitted_number_plate):
#     return HttpResponse('Details for %s:' % submitted_number_plate)
