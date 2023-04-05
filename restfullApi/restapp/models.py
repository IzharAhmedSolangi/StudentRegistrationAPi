from django.db import models



class student(models.Model):
    rollnum = models.CharField(max_length=20 , primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    email_token = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    age = models.IntegerField()
    is_email_varified = models.BooleanField(default=False)
    password = models.CharField(max_length=20)



    

class course(models.Model):
    course_Id = models.CharField(max_length=50 , primary_key=True)
    duration = models.IntegerField()
    fees = models.IntegerField()


class enrolled(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    student = models.ForeignKey(student , on_delete=models.CASCADE)
    total_amount_paid = models.IntegerField()
    






