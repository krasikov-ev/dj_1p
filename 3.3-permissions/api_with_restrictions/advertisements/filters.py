# from django_filters import rest_framework 



from django_filters.rest_framework import FilterSet, CharFilter, DateFromToRangeFilter

from advertisements.models import Advertisement



class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter()
    status = CharFilter(field_name='status', lookup_expr='exact')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
