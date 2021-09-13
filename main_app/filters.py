import django_filters
from django_filters import DateFromToRangeFilter, DateRangeFilter, CharFilter, NumberFilter
from django_filters.widgets import RangeWidget
from .models import Hike


class HikeFilter(django_filters.FilterSet):
    class Meta:
        model = Hike
        fields = []

    hike_name = CharFilter(field_name='name', lookup_expr="icontains", label="Name Contains")
    hike_rating = NumberFilter(field_name='hike_rating', label="Hike Rating")
    length = NumberFilter(field_name="length", label="Length of Hike (Miles)")
    elevation_gain = NumberFilter(field_name="elevation_gain", label="Elevation Gain (Feet)")
    hike_date_range = DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}), field_name="hike_date", label="Hike Date Range")
    hike_date_range_dropdown = DateRangeFilter(field_name="hike_date", label="Recent Hikes")

