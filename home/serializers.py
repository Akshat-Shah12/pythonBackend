from rest_framework import fields, serializers

from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        # fields=['name','age']
        exclude=[]
        # exclude=['name']
        # field='__all__'
    
    def validate(self, data):
        # if data["name"]:
        #     for n in data["name"]:
        #         if n.isdigit():
        #             raise serializers.ValidationError({"error":"Name cannot be numeric"})
                    

        # if data['age']<18:
        #     raise serializers.ValidationError({"error":"age cannot be less than 18"})

        return data