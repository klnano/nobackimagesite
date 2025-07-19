from django.http import HttpResponse
from django.shortcuts import render, redirect
from rembg import remove
from PIL import Image
from .forms import DocumentForm
from .models import Document
from django.conf import settings
import os

# Create your views here.

def noback(input_path, output_path):
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        input_image.close()
    except IOError:
        print(f"Error: Cannot open {input_path}")
        return
    
    
    
def index(request):
    form = DocumentForm()
    obj = None
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            latest_doc = Document.objects.latest("id")
            input_path = str(settings.BASE_DIR) + latest_doc.image.url
            output_path = os.path.join(settings.MEDIA_ROOT, "output", "output.png")
            noback(input_path, output_path)
            obj = latest_doc
    else:
        pass
    return render(request, "nobackimage_app/index.html", {
        "form" : form,
        "obj" : obj,
    })  
    
def delete(request):
    output_path = os.path.join(settings.MEDIA_ROOT, "output", "output.png")
    
    if os.path.exists(output_path):
        try:
            os.remove(output_path)
            print("削除成功")
        except Exception as e:
            print("削除エラー:", e)
            
    return redirect("index")