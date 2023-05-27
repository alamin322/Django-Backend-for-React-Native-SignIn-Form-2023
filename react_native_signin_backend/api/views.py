from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from api.serializers import SignInSerializer
from api.models import SignIn

# Create your views here.
@api_view(['GET'])
def home_view(request):
    api_urls = {
        'all_items': '/show',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(data=api_urls)


@api_view(['GET'])
def show_view(request):
	# checking for the parameters from the URL
	if request.query_params:
		items = SignIn.objects.filter(**request.query_params.dict())
	else:
		items = SignIn.objects.all()

	# if there is something in items else raise error
	if items:
		serializer = SignInSerializer(items, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def create_view(request):
    users = SignInSerializer(data=request.data)

    # validating for already existing users
    if SignIn.objects.filter(**request.data).exists():
        raise serializers.ValidationError(detail="This data already exists")
    
    if users.is_valid():
        #users.save()
        #return Response(data=users.data)
        return Response(data={"message" : "User Created"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)