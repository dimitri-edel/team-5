import django_filters
from django_filters import rest_framework as filters
from user_profile.models import UserProfile
from datetime import date, timedelta

class UserProfileFilter(filters.FilterSet):
    age_min = django_filters.NumberFilter(method='filter_by_age_min')
    age_max = django_filters.NumberFilter(method='filter_by_age_max')

    class Meta:
        model = UserProfile
        fields = ['age_min', 'age_max', 'country', 'city', 'gender', 'sexual_orientation']

    def filter_by_age_min(self, queryset, name, value):
        today = date.today()
        min_birth_date = today - timedelta(days=int(value) * 365)
        return queryset.filter(birth_date__lte=min_birth_date)

    def filter_by_age_max(self, queryset, name, value):
        today = date.today()
        max_birth_date = today - timedelta(days=int(value) * 365)
        return queryset.filter(birth_date__gte=max_birth_date)
