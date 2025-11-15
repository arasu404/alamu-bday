
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Wish
from .forms import WishForm
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    # nickname input page
    return render(request, 'index.html')

def cake(request):
    # birthday cake page (you uploaded)
    return render(request, 'birthday-cake.html')

def home(request):
    wishes = Wish.objects.order_by('-created_at')[:50]
    photos = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg']  # put actual files in static/wishes/images/
    context = {
        'wishes': wishes,
        'photos': photos,
        'favorite_song': '/static/wishes/audio/favorite_song.mp3',
    }
    return render(request, 'home.html', context)

def api_wishes(request):
    if request.method == 'GET':
        qs = Wish.objects.order_by('-created_at').values('id','name','message','created_at')
        return JsonResponse(list(qs), safe=False)
    return HttpResponseBadRequest('Invalid method')

@csrf_exempt
def api_add_wish(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                name = data.get('name') or 'Anonymous'
                message = data.get('message','').strip()
            else:
                name = request.POST.get('name') or 'Anonymous'
                message = request.POST.get('message','').strip()
            if not message:
                return HttpResponseBadRequest('Message required')
            w = Wish.objects.create(name=name[:100], message=message)
            return JsonResponse({'id': w.id, 'name': w.name, 'message': w.message, 'created_at': w.created_at.isoformat()})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    return HttpResponseBadRequest('Invalid method')
