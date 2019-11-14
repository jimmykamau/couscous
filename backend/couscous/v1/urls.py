from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

app_name = 'v1'
schema_view = get_swagger_view(title='Couscous')

urlpatterns = [
    path('', schema_view)
]
