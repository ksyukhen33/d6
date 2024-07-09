from django_filters import FilterSet, DateFilter, ChoiceFilter
from .models import Posts
from django import forms

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostsFilter(FilterSet):
    content_type = ChoiceFilter(field_name='content_type', label= 'Тип публикации', empty_label='Все типы', choices=Posts.CATEGORY_CHOICES)
    date_post = DateFilter(field_name='date_post', lookup_expr='date__gte', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Posts

        fields = {
           # поиск по названию
           'name_post': ['icontains'],
           'postCategory': ['exact'],

       }

class PostsSearch(FilterSet):
   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Posts
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'name_post': ['icontains'],
           'postCategory': ['exact'],
           'date_post': ['gt'],
           'content_type': ['exact'],
       }



