from django.db.models import Avg, Max, Min, Sum
from django.shortcuts import render

from cities.models import City
from regions.models import Region


def index(request):
    context = {
        'total_cities':
            City.objects.count(),

        'total_regions':
            Region.objects.count(),

        'countries':
            City.objects
            .values_list('country', flat=True)
            .distinct()
            .order_by('country'),

        'region_types':
            Region.objects
            .values_list('region_type', flat=True)
            .distinct(),

        'city_types': [
            choice[0]
            for choice
            in City._meta
            .get_field('city_type')
            .choices
        ],
    }

    return render(
        request,
        'dashboard/index.html',
        context
    )

def analytics(request):
    city_queryset = City.objects.all()

    city_stats = {
        'total_cities':
            city_queryset.count(),

        'total_population':
            city_queryset.aggregate(
                value=Sum('population')
            )['value'] or 0,

        'avg_population':
            city_queryset.aggregate(
                value=Avg('population')
            )['value'] or 0,

        'max_population':
            city_queryset.aggregate(
                value=Max('population')
            )['value'] or 0,

        'min_population':
            city_queryset.aggregate(
                value=Min('population')
            )['value'] or 0,

        'avg_area':
            city_queryset.aggregate(
                value=Avg('urban_area_km2')
            )['value'] or 0,
    }

    region_queryset = Region.objects.all()

    region_stats = {
        'total_regions':
            region_queryset.count(),

        'total_population':
            region_queryset.aggregate(
                value=Sum('total_population')
            )['value'] or 0,

        'avg_population':
            region_queryset.aggregate(
                value=Avg('total_population')
            )['value'] or 0,

        'max_population':
            region_queryset.aggregate(
                value=Max('total_population')
            )['value'] or 0,

        'min_population':
            region_queryset.aggregate(
                value=Min('total_population')
            )['value'] or 0,

        'avg_area':
            region_queryset.aggregate(
                value=Avg('area_km2')
            )['value'] or 0,

        'avg_gdp_per_capita':
            region_queryset.aggregate(
                value=Avg('gdp_per_capita')
            )['value'] or 0,
    }

    context = {
        'city_stats': city_stats,
        'region_stats': region_stats,
    }

    return render(
        request,
        'dashboard/analytics.html',
        context
    )