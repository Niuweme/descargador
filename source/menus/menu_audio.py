import descargar_audio
def menu_audio():
    while(True):
        URL_audio = input("inserte el URL del audio que desa descargar")
        print("Elija una opcion:")
        print("1. descargar audio en MP3")
        print("2. descargar audio en WEBM")
        print("3. salir")
        opcion_DA = int(input())
        if opcion_DA == 1:
            Descargar_audio_MP3(URL_audio)
        elif opcion_DA == 2:
            Descargar_audio_WEBM(URL_audio)
        elif opcion_DA == 3:
            return
        else:
            print("esta opcion no es valida, acuañema")