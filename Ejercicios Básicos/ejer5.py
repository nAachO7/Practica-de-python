while(True):
    h= float(input("Cuantas horas al dia trabaja usted: "))
    if (h>24):
        print("No es posible que trabaje mas de 24 horas al dia \nVuelva a intentar")
    else:
        break

while(True):
    c= float(input("Cuanto se le paga por hora: "))
    if (c<0):
        print("No es posible introducir numeros negativos")
    else:
        break
print(f"Usted gana: {h*c}Bs en un dia")