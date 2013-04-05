from tastypie.resources import ModelResource
from formpost.models import *

class PostResource(ModelResource):
	class Meta:
		queryset = uPost.objects.all()
	        resource_name = "post"


