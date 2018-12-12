# myapp/api.py
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from webapp.models import Entry


class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'data'
        authorization = Authorization()
