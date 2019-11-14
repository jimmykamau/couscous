import couscous.v1.debtor.tests.factories as debtor_factories
import couscous.v1.invoice.models as invoice_models
import factory
import factory.fuzzy


class InvoiceFactory(factory.DjangoModelFactory):

    class Meta:
        model = invoice_models.Invoice
    
    debtor = factory.SubFactory(debtor_factories.DebtorFactory)
    status = factory.fuzzy.FuzzyChoice(
        invoice_models.Invoice.INVOICE_STATUS_CHOICES,
        getter=lambda c: c[0]
    )
    amount = factory.Faker('random_int', min=0, max=10000)
    due_date = factory.Faker('date_object')
