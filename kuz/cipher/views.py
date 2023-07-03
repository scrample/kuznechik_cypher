from binascii import unhexlify
from django.shortcuts import render, redirect
# Create your views here.
from .forms import UploadImg
from .GOSTCRYPTO import *
import os
from .models import *
from .STUDENTKUZ import *


def cipher(request):
    if request.method == 'POST':
        form = UploadImg(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            current_dir = os.getcwd()
            pathSourse = current_dir + "/media/" + str(img_obj.original_img)
            cipher_path = current_dir + "/media/encode/{}.PNG".format(str(img_obj.title))
            pathDec = current_dir + "/media/decode/{}.PNG".format(str(img_obj.title))
            
            data = form.cleaned_data
            key = data['key']
            if img_obj.alg_var == 'GOSTCRYPTO':
                enc = ENC_ECB(pathSourse, key, cipher_path)
                dec = DEC_ECB(cipher_path, key, pathDec)
            if img_obj.alg_var == 'STUDENT':
                key = unhexlify(key)
                # #ENC BLOCK
                input_values = get_img_data(pathSourse)
                encrypted_values = execute(lambda block: encrypt_block(block, key), input_values[2])
                save_img_enc(input_values[0], input_values[1], encrypted_values, cipher_path)


                # #DEC BLOCK
                input_values = get_img_data(cipher_path)
                decrypted_values = execute(lambda block: decrypt_block(block, key), input_values[2])
                save_img_dec(input_values[0], input_values[1], decrypted_values, pathDec)

            
            return redirect('home')
            
    else:
        form = UploadImg()
            
    return render(request, 'cipher/cipher.html', {'form': form})
    


def index(request):
    images = Image_file.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'cipher/test.html', context=context)