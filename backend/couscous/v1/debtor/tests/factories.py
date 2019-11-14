import couscous.v1.debtor.models as debtor_models
import couscous.v1.tests.factories as couscous_factories
import factory


class DebtorFactory(factory.DjangoModelFactory):

    class Meta:
        model = debtor_models.Debtor
    
    created_by = factory.SubFactory(couscous_factories.UserFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('ascii_safe_email')
    iban = factory.Faker('iban')
