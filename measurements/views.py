from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect

from measurements.models import Patient
from measurements.forms import PatientForm

def patient(request,slug):
    single_patient = get_object_or_404(Patient, pk=slug)
    t = loader.get_template('measurements/patient.html')
    context_dict = {'single_patient':single_patient,
    }
    # for patient in latest_patients:
    #     patient.url = encode_url(patient.patient_name)
    c = Context(context_dict)
    return HttpResponse(t.render(c))

def patients(request):
    all_patients = Patient.objects.all().order_by('-modified_date')
    t = loader.get_template('measurements/patients.html')
    context_dict = {'all_patients':all_patients,
    }
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def encode_url(url):
    return url.replace(' ','_')

def add_patient(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            # patient_name = request.POST['patient_name']
            # a=Patient.objects.get(id=a_id)

            patient_id = Patient.objects.latest('id').id
            return redirect(patient,slug=patient_id)
            #print patient_form
            #return redirect(success)
        else:
            print form.errors
    else:
        form = PatientForm()
    return render_to_response('measurements/add_patient.html', {'form': form}, context)

def success(request):
    print "HOLAA"
