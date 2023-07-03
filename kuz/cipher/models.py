from django.db import models
from datetime import datetime


# Create your models here.
class Image_file(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name')
    original_img = models.ImageField(upload_to='image' , verbose_name='Original')
    enc_img = models.ImageField(upload_to='encode', verbose_name='Encrypted')
    dec_img = models.ImageField(upload_to='decode', verbose_name='Decrypted')
    key = models.CharField(max_length=255, verbose_name='Key')
    CHOICES = (
        ("GOSTCRYPTO","GOSTCRYPTO"),
        ("STUDENT","STUDENT")
    )
    alg_var = models.CharField(max_length=255, choices = CHOICES)
    date_upload = models.DateTimeField(default=datetime.now, blank=True)


    def save(self):
        if self.original_img:
            self.enc_img = "encode/{}.PNG".format(str(self.title))
            self.dec_img = "decode/{}.PNG".format(str(self.title))
        return super(Image_file, self).save()