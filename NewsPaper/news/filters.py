import django_filters
from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter
from .models import Category


class PostFilter(FilterSet):

    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок'
    )

    postCategory = django_filters.ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Категории',
        empty_label='Выберите категорию',
    )

    dateCreation = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='lt',
        label='Дата публикации',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'date'},
        ),
    )





