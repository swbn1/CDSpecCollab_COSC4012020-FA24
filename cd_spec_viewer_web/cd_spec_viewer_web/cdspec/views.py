import datetime

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from cd_spec_viewer_web.cdspec.models import SpecRun
from .forms import CreateForm
from cd_spec_viewer_web.cdspec.util import handle_file_upload, Units
# Create your views here.

#Index View
class IndexView(generic.ListView):
    template_name = "cdspec/index.html"
    context_object_name = 'latest_runs'

    def get_queryset(self):
        return SpecRun.objects.order_by('-upload_date')[:5]
    
#Create View
def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            parsed_dictionary = handle_file_upload(request.FILES['source_file'])  
            #print(parsed_dictionary)   
            model = form.save(commit=False)
            date_time_string = parsed_dictionary['header']['DATE'] + " " + parsed_dictionary['header']['TIME']
            model.run_date = datetime.datetime.strptime(date_time_string, "%y/%m/%d %H:%M:%S")
            model.data = parsed_dictionary['data']
            model.data_points = parsed_dictionary['header']['NPOINTS']
            #Setting all the indexes for later graphing
            model.x_index = parsed_dictionary['indicies'][Units.XUNIT]
            model.degrees_index = parsed_dictionary['indicies'][Units.DEGREES]
            if Units.VOLTAGE in parsed_dictionary['indicies']:
                model.voltage_index = parsed_dictionary['indicies'][Units.VOLTAGE]
            if Units.ABSORBANCE in parsed_dictionary['indicies']:
                model.voltage_index = parsed_dictionary['indicies'][Units.ABSORBANCE]
            model.save()
    else:
        form = CreateForm()
    return render(request, 'cdspec/create.html', {'form': form})

#Singular View
class DetailView(generic.DetailView):
    model = SpecRun
    template_name = 'cdspec/detail.html'




#Graph View

