import django_filters
from django_filters import DateTimeFilter, CharFilter, NumberFilter
from django_filters.filters import OrderingFilter
from .models import Hike


class HikeFilter(django_filters.FilterSet):
    class Meta:
        model = Hike
        fields = ["name", "hike_rating", "created_at"]

    hike_name = CharFilter(field_name='name', lookup_expr="icontains")
    hike_rating = NumberFilter(field_name='hike_rating')
    created_at = DateTimeFilter(field_name='created_at')

    # o = OrderingFilter(
    #     fields=(
    #         ('name'),
    #         ('hike_rating'),
    #         ('created_at'),
    #     ),

    #     field_labels={
    #         'name': 'Hike Name',
    #         'hike_rating': 'Hike Rating',
    #         'created_at': 'Date Posted'
    #     }
    # )




# def sort_hikes(request):
#     alphabetical_hikes ={
#         "hikes" : Hike.objects.all().order_by('-name')
#     }
#     return render(request,'profile.html', context=alphabetical_hikes)

# def sort_hikes(request):
#     alphabetical_hikes ={
#         "hikes" : Hike.objects.all().order_by('-name')
#     }
#     return render(request,'profile.html', context=alphabetical_hikes)


