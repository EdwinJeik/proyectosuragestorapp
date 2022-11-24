from django.shortcuts import render
from web.formularios.formularioMedico import FormularioMedico
# Create your views here
# Renderizar es PIntar
def Home(request):
    return render(request, 'index.html')
def Medicos(request):
    #Debo utilizar la clase formularioMedico
    #Creamos asi un objeto
    formulario=FormularioMedico()
    diccionario={
        "formulario": formulario
    }

    #ACTIVAR LA RECEPCION DE DATOS
    if request.method=="POST":
        #Validar si los datos son correctos
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #Capturar los datos
            datos=datosRecibidos.cleaned_data
            print(datos)
    return render (request,'registrosmedicos.html', diccionario)   
