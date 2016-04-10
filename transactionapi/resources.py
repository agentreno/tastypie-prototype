from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from transactionapi.models import Transaction

class TransactionResource(ModelResource):
	class Meta:
		queryset = Transaction.objects.all()
		resource_name = 'transactions'
		authorization = Authorization()
		always_return_data = True
