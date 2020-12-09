from django.shortcuts import render
import folium


def home_page(request):
    context = {}
    return render(request, 'home_page.html', context)


def about_us_page(request):
    m = folium.Map(width=1150, height=500, location=(35.761572, 51.394657), zoom_start=14)
    folium.Marker(location=(35.761572, 51.394657), icon=folium.Icon(color='red'), popup='Online Shop').add_to(m)
    m = m._repr_html_()
    context = {
        'map': m
    }
    return render(request, 'about_us.html', context)
