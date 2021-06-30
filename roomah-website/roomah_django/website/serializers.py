from rest_framework import serializers

from .models import House, UserProfile

class HouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = House
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "room",
            "description",
            "price",
            "accommodationtype",
            "get_image",
            "get_thumbnail"
        )

class HousemateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "fullname",
            "get_username",
            # "profilephoto",
            "get_profilephoto",
            "get_profilethumbnail",
            "get_absolute_url",
            "phonenumber",
            "dateofbirth",
            "age",
            "gender",
            "orientation",
            "religion",
            "occupation",
            "HasRoom",
            "pet",
            "bio",
            "preferredgender",
            "preferredorientation",
            "preferredage",
            "preferredreligion",
            "preferredoccupation",
            "preferredlocation",
            "preferredmaxrent",
            "preferredaccommodationtype"
        )
