from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializer import PreciosBtcSerializer
from .models import PreciosBtc
import datetime

from Apps.Precios.generador import generarRangoFechas,generarFecha

class PrecioBtcView(ViewSet):

    def list(self, request):

        opcion = request.GET.get('opcion','')
        hora = request.GET.get('hora',0)
        hora=int(hora)

        precios=''
        fechaFormulada=''
        if opcion!='rango' and opcion!='':
            fecha=request.GET.get('fecha','')
            fechaFormulada=generarFecha(opcion,fecha,hora)
            precios=PreciosBtc.objects.filter(fecha__gte=fechaFormulada).order_by('fecha')

        elif opcion=='rango':
            fechaInicial=request.GET.get('fechaInicial','')
            fechaFinal=request.GET.get('fechaFinal','')

            fechasFormuladas=generarRangoFechas(fechaInicial,fechaFinal,hora)
            fInicial=fechasFormuladas[0]
            fFinal=fechasFormuladas[1]
            precios=PreciosBtc.objects.filter(fecha__gte=fInicial).filter(fecha__lte=fFinal).order_by('fecha')
        else:
            precios=PreciosBtc.objects.all()
            
        resultado =PreciosBtcSerializer(precios,many=True)

        return Response(data=resultado.data, status=HTTP_200_OK)

        
        

