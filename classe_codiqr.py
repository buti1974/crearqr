import qrcode
import os
from PIL import Image
# Cal tenir els paquets Pillow i qrcode
# pip install Pillow
# pip install qrcode

# Classe per per generar codis QR. 
# Amés del contingut se li pot passar el nom de l'arxiu a generar,
# un arxiu amb unaimatge de logo, el color i l'amplada del logo
# Si l'amplada del logo es gran, pot ser que el codi QR no funcioni 
class codiqr:

    def __init__(self,text = "", arxiu = "codiqr.png", 
            logo = "", color = "Black", amplada_logo = 50):
        # només assignem logo si existeix
        if (len(logo) > 0) and not os.path.isfile(logo):
                self.__arxiu_logo = ""
                print("L'arxiu de logo no existeix")
        else:
            self.__arxiu_logo = logo
        self.__arxiu_qr = arxiu
        self.__contingut = text
        self.__color = color
        self.__logo_max_width = amplada_logo

    def setcontingut(self, text):
        self.__contingut = text

    def setcolor(self, color):
        self.__color = color

    def setamplada_logo(self, amplada_logo):
        self.__logo_max_width = amplada_logo

    def setlogo(self, logo):
        #només assignem logo si existeix
        if (len(logo) > 0) and not os.path.isfile(logo):
                self.__arxiu = ""
                print("L'arxiu de logo no existeix")
        else:
            self.__arxiu = logo

    def setarxiu_qr(self, arxiu):
        self.__arxiu_qr = arxiu

    def generarqr(self,arxiu="codiqr.png"):
        codiqr = qrcode.QRCode(
            error_correction = qrcode.constants.ERROR_CORRECT_H)
        # afegim el contingut
        codiqr.add_data(self.__contingut) 
        # codifiquem contingut
        codiqr.make()
        # creem el codi QR sense imatge
        imatge_qr = codiqr.make_image(fill_color = self.__color, 
            back_color="white").convert('RGB')
        if len(self.__arxiu_logo) == 0:
            # si no hi ha logo guardem la imatge del codi QR
            imatge_qr.save(self.__arxiu_qr)
        else:
            # si hi ha logo l'inserim
            logo = Image.open(self.__arxiu_logo)
            width , height = logo.size
            logo = logo.resize((self.__logo_max_width,height*
                self.__logo_max_width//width))
            # calculem la posició del logo
            pos = ((imatge_qr.size[0] - logo.size[0]) // 2,
                (imatge_qr.size[1] - logo.size[1]) // 2)
            imatge_qr.paste(logo, pos)            
            # guardem la imatge del codi QR
            imatge_qr.save(self.__arxiu_qr)
        print("S'ha generat el codi QR a " + self.__arxiu_qr)            
        