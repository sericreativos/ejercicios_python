#variables forzozas 
tasaAnual=0.2090
plazo=36
monto=float(input("Introduce el monto: "))
tasaAnualConIva=tasaAnual*1.16
TasaMensualSinIva=tasaAnual/12
TasaMensualConIva=tasaAnualConIva/12
interes=monto*TasaMensualSinIva
iva=interes*.16
pagoMensual=(monto*TasaMensualConIva)/(1-(1+TasaMensualConIva)**-36)
capital=pagoMensual-interes-iva
pagoCliente=capital+interes+iva
saldoInsoluto=monto-capital
#nuevas variables
j=1
mes=60


print("Plazo: ", plazo)
print("Monto: ", monto)
print("Tasa anual: ", tasaAnual)
print("Tasa anual con Iva: ", tasaAnualConIva)
print("Tasa Mensual Sin Iva: ", TasaMensualSinIva)
print("Tasa Mensual Con Iva: ", TasaMensualConIva)


while(j<=plazo):
    print("Numero de mes: ", j, "Saldo Insoluto:", saldoInsoluto, "Pago mensual: ", pagoMensual, "Capital: ", capital, "Intereses: ", interes, "IVA: ", iva)
    saldoInsoluto = saldoInsoluto-capital
    interes=saldoInsoluto*TasaMensualSinIva
    capital=pagoMensual-interes-iva
    iva=interes*0.16
    j += 1





