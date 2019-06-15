from enum import Enum

from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    class Meta:
        verbose_name = 'Customer: Customer'

    class CustomerType(Enum):
        def as_tuple(self):
            return self.value, str(self)

        @classmethod
        def choices(cls):
            return[x.as_tuple() for x in list(cls)]

        CUSTOMER_TYPE_PERSON = 1
        CUSTOMER_TYPE_COMPANY = 2

    class ConstractType(Enum):
        def as_tuple(self):
            return self.value, str(self)

        @classmethod
        def choices(cls):
            return[x.as_tuple() for x in list(cls)]

        CONTRACT_TYPE_CTPS = 1
        CONTRACT_TYPE_CNPJ = 2

    name = models.CharField(max_length=128)
    active = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    customer_type = models.IntegerField(choices=CustomerType.choices(), blank=True, null=True)
    customer_document = models.TextField(null=True, blank=True)
    name = models.TextField()
    email = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    contract_type = models.IntegerField(choices=ConstractType.choices(), blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Customer #{}: {}'.format(self.id, self.name)
