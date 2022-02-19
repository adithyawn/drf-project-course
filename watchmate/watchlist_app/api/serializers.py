from rest_framework import serializers
# import Movie model to be used in create method
from watchlist_app.models import Watchlist, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        # fields = "__all__"
        # using exclude watchlist if doesnt want to input watchlist
        # The `exclude` option must be a list or tuple. Got str. Put comma so it will not be string
        exclude = ('watchlist',)

class WatchlistSerializer(serializers.ModelSerializer):

    # show nested one to many relationship from movies { reviews. Read Only true means it can't be inputed from movie, can only be inputed automatically when give rating (from rating input / model)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Watchlist
        fields = "__all__"


    # object to get field
    def get_len_name(self,object):
        length = len(object.name)
        return length

    # validation method
    def validate_name(self,data):
        if len(data) < 2:
            # return exception
            raise serializers.ValidationError("Name is too short")
        else:
            return data    

class StreamPlatformSerializer(serializers.ModelSerializer):
    # Nested Serializer One to Many {"id":..,"name":..,"about":..,"website":.., "watchlist": { [ {"id" : 1 } , {"id" : 2 }, ...] } }
    # create new field show what movies platform has. watchlist name is important because we have defined in models => platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    # many=True because watchlist has many items (array) \

    # All key in movie showed
    # watchlist = WatchlistSerializer(many=True,read_only=True)

    # If want to constrain what key is showed in watchlist and it's String
    # https://www.django-rest-framework.org/api-guide/relations/#serializer-relations
    
    # watchlist = serializers.StringRelatedField(many=True)
    #  {"id":..,"name":..,"about":..,"website":.., "watchlist": ["The Avengers","The Mandalorian"] }

    # If want to show only primary key in watchlist
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #  {"id":..,"name":..,"about":..,"website":.., "watchlist": [1,2] }

    # If want to show hyperlink directly in watchlist
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        # view_name refer to name in urls
        view_name='movie-detail',
        # Could not resolve URL for hyperlinked relationship using view name "movie-details". You may have failed to include the related model in your API, or incorrectly configured the `lookup_field` attribute on this field.
        lookup_field='pk'
    )
    #  {"id":..,"name":..,"about":..,"website":.., "watchlist": ['http://.../1','http://.../2'] }

    #return str refer to models 
    def __str__(self):
        return self.title
        



    
    class Meta:
        model = StreamPlatform
        fields = "__all__"














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