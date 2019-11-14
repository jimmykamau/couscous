from django.urls import include, path

import couscous.v1.debtor.views as debtor_views

urlpatterns = [
    path(
        '',
        debtor_views.ListDebtorView.as_view(),
        name='list-debtors'
    )
]
