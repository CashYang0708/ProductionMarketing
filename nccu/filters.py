from .models import Customer
import django_filters
 
 
class CustomerFilter(django_filters.FilterSet):
 
    class Meta:
        model = Customer
        fields = '__all__'