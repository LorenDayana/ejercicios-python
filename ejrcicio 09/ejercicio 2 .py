contador1=0
contador2=0
contador3=0
contador4=0

#calificaciones 10 estudiantes 
estudiante1=int(input("digite la calificacion del estudiante"))
estudiante2=int(input("digite la calificacion del estudiante"))
estudiante3=int(input("digite la calificacion del estudiante"))
estudiante4=int(input("digite la calificacion del estudiante"))
estudiante5=int(input("digite la calificacion del estudiante"))
estudiante6=int(input("digite la calificacion del estudiante"))
estudiante7=int(input("digite la calificacion del estudiante"))
estudiante8=int(input("digite la calificacion del estudiante"))
estudiante9=int(input("digite la calificacion del estudiante"))
estudiante10=int(input("digite la calificacion del estudiante"))

#analisis

if estudiante1 > 80:
    contador1 += 1
elif estudiante1 > 70 and estudiante1 < 80:
    contador2 += 1
elif estudiante1 > 50 and estudiante1 < 70:
    contador3 += 1
elif estudiante1 < 50:
    contador4 += 1 
  
if estudiante2 > 80:
    contador1 += 1
elif estudiante2 > 70 and estudiante2 < 80:
    contador2 += 1
elif estudiante2 > 50 and estudiante2 < 70:
    contador3 += 1
elif estudiante2 < 50:
    contador4 += 1 
       
if estudiante3 > 80:
    contador1 += 1
elif estudiante3 > 70 and estudiante3 < 80:
    contador2 += 1
elif estudiante3 > 50 and estudiante3 < 70:
    contador3 += 1
elif estudiante3 < 50:
    contador4 += 1 
       
if estudiante4 > 80:
    contador1 += 1
elif estudiante4 > 70 and estudiante4 < 80:
    contador2 += 1
elif estudiante4 > 50 and estudiante4 < 70:
    contador3 += 1
elif estudiante4 < 50:
    contador4 += 1 
       
if estudiante5 > 80:
    contador1 += 1
elif estudiante5 > 70 and estudiante5 < 80:
    contador2 += 1
elif estudiante5 > 50 and estudiante5 < 70:
    contador3 += 1
elif estudiante5 < 50:
    contador4 += 1
        
if estudiante6 > 80:
    contador1 += 1
elif estudiante6 > 70 and estudiante6 < 80:
    contador2 += 1
elif estudiante6 > 50 and estudiante6 < 70:
    contador3 += 1
elif estudiante6 < 50:
    contador4 += 1
        
if estudiante7 > 80:
    contador1 += 1
elif estudiante7 > 70 and estudiante7 < 80:
    contador2 += 1
elif estudiante7 > 50 and estudiante7 < 70:
    contador3 += 1
elif estudiante7 < 50:
    contador4 += 1
        
if estudiante8 > 80:
    contador1 += 1
elif estudiante8 > 70 and estudiante8 < 80:
    contador2 += 1
elif estudiante8 > 50 and estudiante8 < 70:
    contador3 += 1
elif estudiante8 < 50:
    contador4 += 1
        
if estudiante9 > 80:
    contador1 += 1
elif estudiante9 > 70 and estudiante9 < 80:
    contador2 += 1
elif estudiante9 > 50 and estudiante9 < 70:
    contador3 += 1
elif estudiante9 < 50:
    contador4 += 1  
      
if estudiante10 > 80:
    contador1 += 1
elif estudiante10 > 70 and estudiante10 < 80:
    contador2 += 1
elif estudiante10 > 50 and estudiante10 < 70:
    contador3 += 1
elif estudiante10 < 50:
    contador4 += 1    
    
print(f"{contador1} sacaron una calificacion mayor a 80")
print(f"{contador2} sacaron una calificacion mayor a 70 menor a 80")
print(f"{contador3} sacaron una calificacion mayor a 50 meor a 70")
print(f"{contador4} sacaron una calificacion menor a 50")


