from django.shortcuts import render
#from rest_framework import Mainserialize, colourserialize, Imageserialize
from rest_framework.response  import Response
from rest_framework.decorators import api_view
from .models import productMainModel,productColourModel,productImageModel
from proapp.serialize import Mainserialize,colourserialize,Imageserialize
@api_view(['GET'])
def multiplemodels(request):
    main=productMainModel.objects.all()
    colour=productColourModel.objects.all()
    image=productImageModel.objects.all()
    Mainserializeobj=Mainserialize(main,many=True)
    colourserializeobj=colourserialize(colour,many=True)
    Imageserializeobj=Imageserialize(image,many=True)
    ResultModel=Mainserializeobj.data+colourserializeobj.data+Imageserializeobj.data
    return Response(ResultModel)
