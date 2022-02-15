from classe_codiqr import codiqr

txt = input("Entra el contingut: ")
if len(txt) == 0:
    print("El codi QR ha de tenir contingut (text, URL,...)")
else:
    arxiu_logo = input("Entra la ruta a l'arxiu del logo (buit sense logo): ")
    color = input("Entra el color (per defecte Black, en anglès!): ")
    if len(color) == 0:
        color = "Black"
    arxiu_qr = input("Entra la ruta a l'arxiu a generar (buit per codiqr.png): ")
    if len(arxiu_qr) == 0:
        arxiu_qr = "codiqr.png"
    qr = codiqr(txt,arxiu_qr,arxiu_logo,color)
    qr.generarqr()
