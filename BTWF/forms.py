from django import forms
from .models import Info
from django.http import HttpResponseRedirect

# class Myform(forms.Form):
#
#     courses = (
#         ('c', 'C'),
#         ('c++', 'C++'),
#         ('c#', 'C#'),
#         ('python', 'PYTHON'),
#         ('java', 'JAVA'),
#     )
#
#     first_name = forms.CharField(max_length=250)
#     last_name = forms.CharField(max_length=250)
#     email = forms.EmailField(null=True)
#     fathers_name = forms.CharField(max_length=250, blank=True)
#     contact_number = forms.IntegerField()
#     dob = forms.DateField()
#     address = forms.CharField(max_length=500, null=True)
#     occupation = forms.CharField(max_length=200, blank=True)
#     course = forms.CharField(max_length=20, choices=courses, default='c')

    # form = Myform(request.POST)
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     obj = Info(first_name=form.cleaned_data['first_name'])
    #     obj = Info(last_name=form.cleaned_data['last_name'])
    #     obj = Info(email=form.cleaned_data['email'])
    #     obj = Info(fathers_name=form.cleaned_data['fathers_name'])
    #     obj = Info(contact_number=form.cleaned_data['contact_number'])
    #     obj = Info(dob=form.cleaned_data['dob'])
    #     obj = Info(address=form.cleaned_data['address'])
    #     obj = Info(occupation=form.cleaned_data['occupation'])
    #     obj = Info(course=form.cleaned_data['course'])
    #     obj.save()
    #     return HttpResponseRedirect('/')

class Myform(forms.ModelForm):

    # courses = (
    #     ('c', 'C'),
    #     ('c++', 'C++'),
    #     ('c#', 'C#'),
    #     ('python', 'PYTHON'),
    #     ('java', 'JAVA'),
    # )
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()
    # fathers_name = forms.CharField()
    # contact_number = forms.IntegerField()
    # dob = forms.DateField()
    # address = forms.CharField()
    # occupation = forms.CharField()
    # course = forms.ChoiceField(choices=courses)

    class Meta:
        model = Info
        fields = '__all__'
