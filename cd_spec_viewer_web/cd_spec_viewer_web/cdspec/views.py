import datetime

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from cd_spec_viewer_web.cdspec.models import SpecRun
from .forms import CreateForm
from cd_spec_viewer_web.cdspec.util import handle_file_upload
# Create your views here.

class IndexView(generic.ListView):
    template_name = "cdspec/index.html"
    context_object_name = 'latest_runs'

    def get_queryset(self):
        return SpecRun.objects.order_by('-upload_date')[:5]
    
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
            model.save()
    else:
        form = CreateForm()
    return render(request, 'cdspec/create.html', {'form': form})








#Upload

#List View

#Graph View

