from rest_framework import serializers

class ContactSerilizer(serializers.Serializer):
    fullname=serializers.CharField()
    email=serializers.EmailField()
    mobile=serializers.CharField()
    message=serializers.CharField()