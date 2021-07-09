from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.core.files import File
from django.db import connection
import os
from pathlib import Path
from django.db import connections

# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent

# Save Media Files Manually


def save_media(name, files):
    with open(f"data/{str(name)}/{str(files)}", "wb") as img:
        myfile = File(img)
        for i in files:
            myfile.write(i)
        img.close()
        myfile.close()


def home(request):
    form = TreeLeafForm()
    if request.method == 'POST':
        data = request.POST
        file = request.FILES
        name = data['name']
        files = file['files']
        image = 'webcam.jpg'
        cursor = connections['default'].cursor()
        cursor.execute(
            f'''INSERT INTO main_TreeLeaf(name, files, image) VALUES('{name}', '{name}/{files}', '{name}/{image}');''')
        PATH = os.path.join(BASE_DIR, f"data/{str(name)}")
        Path(PATH).mkdir(parents=True, exist_ok=True)
        save_media(name, files)

    return render(request, 'home.html', locals())


@ csrf_exempt
def saveimage(request):
    name = request.GET['name']
    files = request.FILES['webcam']
    PATH = os.path.join(BASE_DIR, f"data/{name}/")
    Path(PATH).mkdir(parents=True, exist_ok=True)
    save_media(name, files)
    return HttpResponse('Success')


def viewall(request):
    data = TreeLeaf.objects.all()
    return render(request, 'all.html', locals())
