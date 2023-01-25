from rest_framework import serializers
from proapp.models  import productMainModel,productColourModel,productImageModel


class Mainserialize(serializers.Serializer):
    class Meta:
        model=productMainModel
        fields="__all__"
class colourserialize(serializers.Serializer):
    class Meta:
        fields="__all__"

class Imageserialize(serializers.Serializer):
    class Meta:
        fields="__all__"
