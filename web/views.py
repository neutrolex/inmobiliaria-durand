from django.shortcuts import render

def home(request):
    """
    Renderiza la Landing Page de la empresa.
    """
    return render(request, 'web/index.html')

def contacto(request):
    """
    Maneja el formulario de contacto web.
    """
    if request.method == 'POST':
        # TODO: Implementar envío de correo o registro en BD
        return render(request, 'web/contacto.html', {'mensaje_enviado': True})
    return render(request, 'web/contacto.html')