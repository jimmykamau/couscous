from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

app_name = 'v1'
schema_view = get_swagger_view(title='Couscous')

urlpatterns = [
    path('', schema_view),
    path('debtor/', include('couscous.v1.debtor.urls')),
    path('invoice/', include('couscous.v1.invoice.urls'))
]
