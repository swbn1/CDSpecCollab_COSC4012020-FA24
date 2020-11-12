import datetime

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from cd_spec_viewer_web.cdspec.models import SpecRun
from .forms import CreateForm, EditForm
from cd_spec_viewer_web.cdspec.util import handle_file_upload, Units, graph_format

# Create your views here.

#Index View, a list of last ten objects
class IndexView(generic.ListView):
    template_name = "cdspec/index.html"
    context_object_name = 'latest_runs'

    def get_queryset(self):
        return SpecRun.objects.order_by('-upload_date')[:10]

#Edit view, allows the editing of existing objects
def edit(request, pk):
    #The post statement is the form submit handler. 
    if request.method == 'POST':
        #We first recreate the form object using the request objects.
        form = EditForm(request.POST, instance=get_object_or_404(SpecRun, pk=pk))
        #As long as the form is valid, we proceed to parsing.
        if form.is_valid():
            model = form.save()
            return HttpResponseRedirect(reverse('cdspec:detail', args=(model.id,)))
    else:
        form = EditForm(instance=get_object_or_404(SpecRun, pk=pk))
    return render(request, 'cdspec/edit.html', {'form': form, 'pk':pk})


#Create View, allows the creation of new objects
def create(request):
    #The post statement is the form submit handler. 
    if request.method == 'POST':
        #We first recreate the form object using the request objects.
        form = CreateForm(request.POST, request.FILES)
        #As long as the form is valid, we proceed to parsing.
        if form.is_valid():
            #We parse the file into three dictionaries, header, data and indicies all within parsed_dictionary
            parsed_dictionary = handle_file_upload(request.FILES['source_file'])  
            #We then save the form but don't commit to db yet
            model = form.save(commit=False)
            #We add all the model's fields that are from the parsed dictionary
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
                model.absorbance_index = parsed_dictionary['indicies'][Units.ABSORBANCE]
            
            #print(molar_ellipticity_calculation(parsed_dictionary['data'], model.pathlength, model.protein_concentration, model.number_of_amino_acids, model.degrees_index))
            #Then save the model to the db, here we can return a different view, maybe redirect.
            model.save()
            return HttpResponseRedirect(reverse('cdspec:detail', args=(model.id,)))
    else:
        form = CreateForm()
    return render(request, 'cdspec/create.html', {'form': form,})

#Singular View w/ graph
def detail(request, pk):
    model = get_object_or_404(SpecRun, pk=pk)
    x_array = graph_format(model.data, model.x_index)
    y_array = graph_format(model.data, model.degrees_index)
    
    return render(request, 'cdspec/detail.html', {'specrun': model, "x": x_array, "y": y_array})




#Multi View
def multi(request, pks):
    proteins = []
    for pk in pks.split('/')[:-1]:
        proteins.append(get_object_or_404(SpecRun, pk=pk))
    return HttpResponse(proteins)


