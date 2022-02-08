from rest_framework import serializers
# import Movie model to be used in create method
from watchlist_app.models import Movie

# If dont want to declare variable / field again (reuse from Movie model (from watchlist_app.models import Movie)) can use (serializers.ModelSerializer). It's diffent with (serializers.Serializer)
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = "__all__"
        # If want spesific field. It will only show {"id":1,"name":TEST} without desc and active. If you post name, desc automaticaly will be "" and active will be true
        # fields = ['id','name']

        # Also can use exclude so it will be same like fields= ['id','name']. But fields must be empty / deleted
        exclude = ['description','active']

    # validation method
    def validate_name(self,data):
        if len(data) < 2:
            # return exception
            raise serializers.ValidationError("Name is too short")
        else:
            return data    

# '''
# # validation function
# def name_length(data):
#     if len(data) < 2:
#         # return exception
#         raise serializers.ValidationError("Name is too short")

# # if Model is Movie then serializer is MovieSerializer
# class MovieSerializer(serializers.Serializer):
#     # read only so id cant be edited and generated automatically. read_only, validators are Core Arguments https://www.django-rest-framework.org/api-guide/fields/#core-arguments
#     # Serializer fields (Ex: IntegerField, CharField, EmailField etc.. ) handle converting between primitive values and internal datatypes. They also deal with validating input values, as well as retrieving and setting the values from their parent objects. 
#     # Note: The serializer fields are declared in fields.py, but by convention you should import them using from rest_framework import serializers and refer to fields as serializers.<FieldName>.

#     id = serializers.IntegerField(read_only=True)
#     # validation with function
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     # to use post request, Crate Instance Method with name def create. Will return validated data to views with structure like in Movie model db
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)

#     # to use put request, Crate Instance Method with name def update. instance will carry old values and validated_data will return validated data to views (new value)
#     def update(self, instance,validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

# # Field Level Validation https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
#     # def validate_{obj_name}(self,data)
#     # def validate_name(self,data):
#     #     if len(data) < 2:
#     #         # return exception
#     #         raise serializers.ValidationError("Name is too short")
#     #     else:
#     #         return data
#     def validate_description(self,data):
#         if len(data) < 2:
#             # return exception
#             raise serializers.ValidationError("Description is too short")
#         else:
#             return data

# # Object Level Validation https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should be different")
#         else:
#             return data

# '''






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