from rest_framework.filters import OrderingFilter
from django.db.models.functions import Lower
from django_filters import FilterSet

from store.models import Product


class CaseInsensitiveOrderingFilter(OrderingFilter):
    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        for field in ordering:
            new_ordering = []
            if field.startswith('-'):
                new_ordering.append(Lower(field[1:]).desc())
            else:
                new_ordering.append(Lower(field).asc())
            return queryset.order_by(*new_ordering)
        return queryset


class ClassProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['lte', 'gte', 'range']
        }
