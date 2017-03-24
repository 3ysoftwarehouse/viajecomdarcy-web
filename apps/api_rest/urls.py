from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from apps.api_rest import views

schema_view = get_swagger_view(title='VDC API')

urlpatterns = [
 	url('^$', schema_view),
]