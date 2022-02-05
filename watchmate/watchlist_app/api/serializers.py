from rest_framework import serializers

# if Model is Movie then serializer is MovieSerializer
class MovieSerializer(serializers.Serializer):
    # read only so id cant be edited and generated automatically
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()


# AttributeError: Got AttributeError when attempting to get a value for field `name` on serializer `MovieSerializer`.
# The serializer field might be named incorrectly and not match any attribute or key on the `QuerySet` instance.
# Original exception text was: 'QuerySet' object has no attribute 'name'.
# Do one thing, delete current values for the movie from the admin and re-add them.
# This error is occurring due to multiple values in response when only 1 was requested.