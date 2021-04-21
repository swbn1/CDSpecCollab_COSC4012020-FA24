import datetime

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.contrib import messages

from cdspec.models import SpecRun
from .forms import CreateForm, EditForm
from cdspec.util import handle_file_upload, Units, graph_format

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
            #Setting the x/y header names
            if "XUNITS" in parsed_dictionary['header']: 
                model.x_units = parsed_dictionary['header']['XUNITS']
            if "YUNITS" in parsed_dictionary['header']:
                model.y_units = parsed_dictionary['header']['YUNITS']
            if "Y2UNITS" in parsed_dictionary['header']:
                model.y2_units = parsed_dictionary['header']['Y2UNITS']
            if "Y3UNITS" in parsed_dictionary['header']:
                model.y3_units = parsed_dictionary['header']['Y3UNITS']
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
    #Send the model and all of the data points (presented as a list of x, list of y, list of y2, list of y3) to the corresponding template
    return render(request, 'cdspec/detail.html', {'specrun': model, 'x': graph_format(model.data, 0), 'y': graph_format(model.data, 1), 'y2': graph_format(model.data, 2),
    'y3': (graph_format(model.data, 3) if model.y3_units is not None else None), "pk": pk})

#Multi View
def multi(request, pks):
    proteins = []
    for pk in pks.split('/')[:-1]:
        proteins.append(get_object_or_404(SpecRun, pk=pk))

    #check if the models have the same units
    x_units = proteins[0].x_units
    y_units = proteins[0].y_units
    y2_units = proteins[0].y2_units
    y3_units = proteins[0].y3_units
    for protein in proteins:
        if protein.x_units != x_units or protein.y_units != y_units or protein.y2_units != y2_units or protein.y3_units != y3_units:
            messages.info(request, 'Multi-graph failed: graphs have different axes')
            return HttpResponseRedirect('/')

    #Send the models and all of the data points (presented as a list of x, list of y, list of y2, list of y3) to the corresponding template
    output_object = [];
    for protein in proteins:
        output_object.append({'run_title' : protein.run_title, 'model' : protein, 'x' : graph_format(protein.data, 0), 'y' : graph_format(protein.data, 1), 'y2' : graph_format(protein.data, 2),
        'y3' : (graph_format(protein.data, 3) if protein.y3_units is not None else None)});

    return render(request, 'cdspec/multi.html', {'proteins': output_object, 'pks': pks, 'first': proteins[0]})

# Table List View
class SpecRunJson(BaseDatatableView):
    model = SpecRun
    
#Delete view
@require_http_methods(["POST"])
def delete(request, pk): 
    # fetch the object related to passed id 
    obj = get_object_or_404(SpecRun, id = pk) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/") 
  