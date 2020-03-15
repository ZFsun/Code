from django.shortcuts import render
from django.views import generic


# Create your views here.


class index(generic.ListView):
    template_name = 'datademo/index.html'
    context_object_name = 'index_list'

    def get_queryset_cache_key(self):
        """
        子类重写.获得queryset的缓存key
        """
        raise NotImplementedError()

    def get_queryset_data(self):
        """
        子类重写.获取queryset的数据
        """
        raise NotImplementedError()

    def get_queryset(self):
        return 'test'
