from rest_framework import serializers
from rest_api.models import Post,Student
#serializer
#ModelSerializer

# 1. using normal serializer
class PostSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=50)
    author=serializers.CharField(max_length=50)
    email=serializers.EmailField(default='')

#create and returns a new post instance given the validated data.
    def create(self,validated_data):
        return Post.objects.create(validated_data)

# Update and return an existing `Post` instance, given the validated data.

    def update(self,instance,validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.author=validated_data.get('author',instance.author)
        instance.email=validated_data.get('email',instance.email)
        instance.save()
        return instance
    
# 2. Using ModelSerializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #to take all fields
        fields = "__all__"
        # to take specific columns
        #fields= ['rollno','name','wclass']