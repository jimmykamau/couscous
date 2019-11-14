from django.contrib.auth.models import User

import factory


class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = User
    
    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('ascii_safe_email')
    password = factory.PostGenerationMethodCall(
        'set_password', 'password'
    )
