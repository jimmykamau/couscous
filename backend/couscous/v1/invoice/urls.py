from django.urls import include, path


import couscous.v1.invoice.views as invoice_views

urlpatterns = [
    path(
        '',
        invoice_views.ListInvoiceView.as_view(),
        name='list-invoices'
    )
]
