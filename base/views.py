from django.shortcuts import render, redirect
from django.views import View
from .models import Wish, WishMedia
from django.utils.text import slugify

# Create your views here.


class Home(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, 'index.html')  
    
    def post(request):
        images = request.FILES.getlist('images')
        save_wish = Wish.objects.create(
            name_of_person_being_wished = request.POST['name'],
            mail_of_person_being_wished = request.POST['email'],
            name_of_person_doing_wishing = request.POST['wishmaker_name'],
            wish_message = request.POST['message'],
            date_and_time = request.POST['dateandtime'],
            slug = slugify(request.POST['name'] + ' by ' + request.POST['wishmaker_name']),
        )
        save_wish.save()
        for image in images:
            wish_media = WishMedia.objects.create(
                wish = save_wish,
                photos = image,
                video = request.FILES['video']
            )
            wish_media.save()


class WishPage(View):
    template_name = 'display.html'
    def get(self, request):
        return render(request, 'display.html')  

#     def get(request, slug):
#         wish = Wish.objects.get(slug=slug)

#         context = {'wish':wish}