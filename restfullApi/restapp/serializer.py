from rest_framework import serializers
from .models import student , course , enrolled


class studentSeriaizer(serializers.ModelSerializer):
    class Meta :
        model = student
        fields = ['rollnum' , 'name' , 'email','department' , 'age','password']


class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = ['course_Id','duration','fees']

class enrolledSerializer(serializers.ModelSerializer):
    class Meta:
        model = enrolled
        fields = ['course' , 'student' , 'total_amount_paid']