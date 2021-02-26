import datetime
def generarFecha(opcion,fecha,hora):
    fechaFormulada=''
    if opcion!='rango' and opcion!='all':
        fecha=fecha.split('-')
        dia=int(fecha[2])
        mes=int(fecha[1])
        anio=int(fecha[0])
        if opcion=="ultimas24Hrs":
            if dia==1:
                if mes%2==1:
                    if mes==1:
                        anio-=1
                    elif mes==3:
                        dia=28
                    else:
                        dia=30
                else:
                    dia=31
            else:
                dia-=1
                
        elif opcion=="semana":
            diasMesPar=30
            diasMesImpar=31

            if mes%2==1 and dia<=7:
                if mes==3:
                    diasMesPar=28
                    mes-=1
                elif mes==1:
                    mes=12
                    anio-=1
                dia=dia-7+diasMesPar
                
            elif mes%2==0 and dia<=7:
                dia=dia-7+diasMesImPar
                mes-=1
            else:
                dia=dia-7

        elif opcion=="mes":
            if mes==1:
                anio-=1
                mes=12
            else:
                if dia>28 and mes==3:
                    dia=28
                mes-=1
                
        elif opcion=="anio":
            anio-=1

        fechaFormulada=datetime.datetime(anio,mes,dia,hora,0,0,0)
        
    return fechaFormulada

def generarRangoFechas(fechaInicial,fechaFinal,hora):
    fechas=[]
    fecha1=fechaInicial.split('-')
    dia1=int(fecha1[2])
    mes1=int(fecha1[1])
    anio1=int(fecha1[0])

    fecha2=fechaFinal.split('-')
    dia2=int(fecha2[2])
    mes2=int(fecha2[1])
    anio2=int(fecha2[0])

    fechaInicial=datetime.datetime(anio1,mes1,dia1,hora,0,0,0)
    fechaFinal=datetime.datetime(anio2,mes2,dia2,hora,0,0,0)
    fechas.append(fechaInicial)
    fechas.append(fechaFinal)
    return fechas
    