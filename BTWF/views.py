from django.shortcuts import render
from django.http import HttpResponse
from .models import Info
from .forms import *
from django.views import generic
from django.core.urlresolvers import *

# Create your views here.
# def all_data(request):
#     data = Info.objects.all()
#     return render(request,'list.html',{'data':data})

class all_data(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'data'
    url = reverse_lazy('home')

    def get_queryset(self):
        return Info.objects.all()

def form_page(request):
    if request.method == "POST":
        form = Myform(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # form = Info(first_name=form.cleaned_data['first_name'])
            # form = Info(last_name=form.cleaned_data['last_name'])
            # form = Info(email=form.cleaned_data['email'])
            # form = Info(fathers_name=form.cleaned_data['fathers_name'])
            # form = Info(contact_number=form.cleaned_data['contact_number'])
            # form = Info(dob=form.cleaned_data['dob'])
            # form = Info(address=form.cleaned_data['address'])
            # form = Info(occupation=form.cleaned_data['occupation'])
            # form = Info(course=form.cleaned_data['course'])
            form.save()
            return HttpResponseRedirect('/home')
        else:
            print(form)
            return HttpResponseRedirect('/home')
    else:
        form = Myform()
        return render(request,'form.html',{'form':form})

def edit(request,id):
    if request.method == "POST":
        form = Myform(request.POST)
        if form.is_valid():
            form = Info.objects.get(pk=id)
            form = Myform(request.POST,instance=form)
            form.save()
            return HttpResponseRedirect('/home')
    else:
        obj = Info.objects.get(id=id)
        form = Myform(instance=obj)
        #return render(request,'firstApp/edit.html',{'obj':obj})
        return render(request,'form.html', {'form': form,'id':id})
def delete(request,data_id):
    obj= Info.objects.filter(id=data_id)
    obj.delete()
    return HttpResponseRedirect('/home')