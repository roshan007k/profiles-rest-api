from rest_framework import serializers
from restbasic import  models
class HelloSerializer(serializers.Serializer):

    name=serializers.CharField(max_length=15)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.UserProfile
        fields=('name','email','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self,validated_data):
        """Create new user"""
        user=models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.ProfileFeedItem
        fields='__all__'
        extra_kwargs={'user_profile':{'read_only':True}}

