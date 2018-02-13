from django.db import models



# Create your models here.
class Info(models.Model):
    courses = (
        ('c', 'C'),
        ('C++', 'C++'),
        ('C#', 'C#'),
        ('PYTHON', 'PYTHON'),
        ('JAVA', 'JAVA'),
    )

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(null=True)
    fathers_name = models.CharField(max_length=250,blank=True)
    contact_number = models.IntegerField()
    dob = models.DateField()
    address = models.CharField(max_length=500,null=True)
    occupation = models.CharField(max_length=200,blank=True)
    course = models.CharField(max_length=20,choices=courses,default='c')
    def __str__(self):
        return self.first_name+'-'+self.last_name