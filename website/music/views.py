from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from music.models import Album,Song
from django.template import loader

# Create your views here.
""" def index(request):
    return HttpResponse("<h1> This is the music app homepage</h1>") """

""" def index(request):
    all_albums = Album.objects.all()
    html = '' 
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html) """

""" def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums' : all_albums
    } #store data in context (dictionary) and send them to the template
    return HttpResponse(template.render(context,request)) """

def index(request):
    all_albums = Album.objects.all()
    template = 'music/index.html'
    context = {
        'all_albums' : all_albums,
    } #store data in context (dictionary) and send them to the template
    return render(request,template,context)

""" def detail(request, album_id):
    return HttpResponse("<h2>Detail for Album id : " + str(album_id) + "</h2>") """

def detail(request, album_id):
    template = 'music/detail.html'
    """  try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist") """
    album = get_object_or_404(Album,pk=album_id)
    return render(request,template,{ 'album' : album})

def favorite(request, album_id):
    album = get_object_or_404(Album,pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html',{
             'album' : album,
             'error_message' : "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,'music/detail.html',{ 'album' : album})