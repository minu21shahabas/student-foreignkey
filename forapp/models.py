from django.db import models

# Create your models here.
class addcourse(models.Model):
    course_name=models.CharField(max_length=255)
    fees=models.IntegerField()
    def __str__(self):
        return self.course_name
class addstudent(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    address=models.TextField()
    joining_date=models.DateField()
    phone_no=models.IntegerField()
    course=models.ForeignKey(addcourse,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name