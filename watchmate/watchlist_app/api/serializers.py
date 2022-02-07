from rest_framework import serializers
# import Movie model to be used in create method
from watchlist_app.models import Movie

# validation function
def name_length(value):
    if len(value) < 2:
        # return exception
        raise serializers.ValidationError("Name is too short")

# if Model is Movie then serializer is MovieSerializer
class MovieSerializer(serializers.Serializer):
    # read only so id cant be edited and generated automatically
    id = serializers.IntegerField(read_only=True)
    # validation with function
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    # to use post request, Crate Instance Method with name def create. Will return validated data to views with structure like in Movie model db
    def create(self,validated_data):
        return Movie.objects.create(**validated_data)

    # to use put request, Crate Instance Method with name def update. instance will carry old values and validated_data will return validated data to views (new value)
    def update(self, instance,validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

# Field Level Validation https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
    # def validate_{obj_name}(self,value)
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         # return exception
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
    def validate_description(self,value):
        if len(value) < 2:
            # return exception
            raise serializers.ValidationError("Description is too short")
        else:
            return value

# Object Level Validation https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description should be different")
        else:
            return data








# '''

# # Python program to demonstrate
# # instance methods
  
  
# class shape:
      
#     # Calling Constructor
#     def __init__(self, edge, color):
#         self.edge = edge
#         self.color = color
          
#     # Instance Method
#     def finEdges(self):
#         return self.edge
          
#     # Instance Method
#     def modifyEdges(self, newedge):
#         self.edge = newedge
          
# # Driver Code
# circle = shape(0, 'red')
# square = shape(4, 'blue')
  
# # Calling Instance Method
# print("No. of edges for circle: "+ str(circle.finEdges()))
  
# # Calling Instance Method
# square.modifyEdges(6)
  
# print("No. of edges for square: "+ str(square.finEdges()))

# # Output

# # No. of edges for circle: 0
# # No. of edges for square: 6

# '''