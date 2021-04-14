from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Location

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    print(images)
    return render(request, 'index.html', {"images":images, 'locations':locations})

def search_results(request):

    if 'search_image' in request.GET and request.GET["search_image"]:
        search_term = request.GET.get("search_image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def single(request,image_id):
    # images = Image.get_image_by_id(image_id)
    title = 'Boom'
    #locations = Location.objects.all()
    # category = Category.get_category_id(id = image_category)
    #image_category = Image.objects.filter(image_category__name = category_name)
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html",{"image":image})

def location_filter(request, image_location):
    locations = Location.objects.all()
    location = Location.objects.filter(name = image_location).first()
    images = Image.objects.filter(img_location = location)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title':title, 'images':images, 'locations':locations, 'location':location})