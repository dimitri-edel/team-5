from django_filters import rest_framework as filters
from .models import UserProfile

class UserProfileFilter(filters.FilterSet):
    min_age = filters.NumberFilter(field_name='birth_date', lookup_expr='lte', method='filter_by_min_age')
    max_age = filters.NumberFilter(field_name='birth_date', lookup_expr='gte', method='filter_by_max_age')

    class Meta:
        model = UserProfile
        fields = ['country', 'city', 'gender', 'sexual_orientation']

    def filter_by_min_age(self, queryset, name, value):
        from datetime import date
        today = date.today()
        min_birth_date = today.replace(year=today.year - value)
        return queryset.filter(birth_date__lte=min_birth_date)

    def filter_by_max_age(self, queryset, name, value):
        from datetime import date
        today = date.today()
        max_birth_date = today.replace(year=today.year - value)
        return queryset.filter(birth_date__gte=max_birth_date)
