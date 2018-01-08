##  converting measures

print()
print('* * * MEASUREMENTS CONVERTER * * *')
print()


measure= int(input('Choose the measure 1 - length, 2 - volume, 3 - mass: '))

print()

## length
m=1
sm=0.01*m
km=1000*m
inch=0.0254*m
ft=0.305*m
mi=1609*m

## volumes
l=1
ml=0.001*l
m3=1000*l
fo=0.03*l
pt=0.57*l
gal=3.79*l

## weights

kg=1
g=0.001*kg
mg=0.000001*kg
oz=0.02835*kg
lb=0.49*kg
st=6.35*kg



if measure == 1:
    print('+-----------------------+\n|sm | m |km |in |ft |mi |\n-------------------------\n| 1 | 2 | 3 | 4 | 5 | 6 |\n+-----------------------+')
    print()
    len1=int(input("convert from: "))
    len2=int(input("convert to: "))
    val= float(input("value: ")) 
    print('_____________________')
    
    ## sm to...
    if len1== 1:
        if len2== 1:
            val= val/1
            print(val)
        elif len2== 2:
            val= val*sm/m
            print(val)
        elif len2== 3:
            val= val*sm/km
            print(val)
        elif len2== 4:
            val= val*sm/inch
            print(val)
        elif len2== 5:
            val= val*sm/ft
            print(val)
        elif len2== 6:
            val= val*sm/mi
            print(val)
        else:
            print('ERROR')
    ## m to...
    elif len1== 2:
        if len2== 1:
            val= val/sm
            print(val)
        elif len2== 2:
            val= val/1
            print(val)
        elif len2== 3:
            val= val*m/km
            print(val)
        elif len2== 4:
            val= val*m/inch
            print(val)
        elif len2== 5:
            val= val*m/ft
            print(val)
        elif len2== 6:
            val= val*m/mi
            print(val)
        else:
            print('ERROR')  
            
    ## km to...
    elif len1== 3:
        if len2== 1:
            val= val*km/sm
            print(val)
        elif len2== 2:
            val= val*km/m
            print(val)
        elif len2== 3:
            val= val/1
            print(val)
        elif len2== 4:
            val= val*km/inch
            print(val)
        elif len2== 5:
            val= val*km/ft
            print(val)
        elif len2== 6:
            val= val*km/mi
            print(val)
        else:
            print('ERROR') 
            
    ## inch to...
    elif len1== 4:
        if len2== 1:
            val= val*inch/sm
            print(val)
        elif len2== 2:
            val= val*inch/m
            print(val)
        elif len2== 3:
            val= val*inch/km
            print(val)
        elif len2== 4:
            val= val/1
            print(val)
        elif len2== 5:
            val= val*inch/ft
            print(val)
        elif len2== 6:
            val= val*inch/mi
            print(val)
        else:
            print('ERROR')  
            
    ## feet to...
    elif len1== 5:
        if len2== 1:
            val= val*ft/sm
            print(val)
        elif len2== 2:
            val= val*ft/m
            print(val)
        elif len2== 3:
            val= val*ft/km
            print(val)
        elif len2== 4:
            val= val*ft/inch
            print(val)
        elif len2== 5:
            val= val/1
            print(val)
        elif len2== 6:
            val= val*ft/mi
            print(val)
        else:
            print('ERROR') 
                    
    ## mile to...
    elif len1== 6:
        if len2== 1:
            val= val*mi/sm
            print(val)
        elif len2== 2:
            val= val*mi/m
            print(val)
        elif len2== 3:
            val= val*mi/km
            print(val)
        elif len2== 4:
            val= val*mi/inch
            print(val)
        elif len2== 5:
            val= val*mi/ft
            print(val)
        elif len2== 6:
            val= val/1
            print(val)
        else:
            print('ERROR')                     
                    
elif measure == 2:
    print('+-----------------------------+\n|ml | l |m3 |fl.oz |pint |gal |\n-------------------------------\n| 1 | 2 | 3 |  4   |  5  |  6 |\n+-----------------------------+')
    print()
    vol1=int(input("convert from: "))
    vol2=int(input("convert to: "))
    val= float(input("value: "))
    print('_____________________')

    
    ## ml to...
    if vol1== 1:
        if vol2== 1:
            val= val/1
            print(val)
        elif vol2== 2:
            val= val*ml/l
            print(val)
        elif vol2== 3:
            val= val*ml/m3
            print(val)
        elif vol2== 4:
            val= val*ml/fo
            print(val)
        elif vol2== 5:
            val= val*ml/pt
            print(val)
        elif vol2== 6:
            val= val*ml/gal
            print(val)
        else:
            print('ERROR')
    ## l to...
    elif vol1== 2:
        if vol2== 1:
            val= val*l/ml
            print(val)
        elif vol2== 2:
            val= val/1
            print(val)
        elif vol2== 3:
            val= val*l/m3
            print(val)
        elif vol2== 4:
            val= val*l/fo
            print(val)
        elif vol2== 5:
            val= val*l/pt
            print(val)
        elif vol2== 6:
            val= val*l/gal
            print(val)
        else:
            print('ERROR')
    ## m3 to...
    elif vol1== 3:
        if vol2== 1:
            val= val*m3/ml
            print(val)
        elif vol2== 2:
            val= val*m3/l
            print(val)
        elif vol2== 3:
            val= val/1
            print(val)
        elif vol2== 4:
            val= val*m3/fo
            print(val)
        elif vol2== 5:
            val= val*m3/pt
            print(val)
        elif vol2== 6:
            val= val*m3/gal
            print(val)
        else:
            print('ERROR')
            
    ## fl.oz to...
    elif vol1== 4:
        if vol2== 1:
            val= val*fo/ml
            print(val)
        elif vol2== 2:
            val= val*fo/l
            print(val)
        elif vol2== 3:
            val= val*fo/m3
            print(val)
        elif vol2== 4:
            val= val*fo/fo
            print(val)
        elif vol2== 5:
            val= val*fo/pt
            print(val)
        elif vol2== 6:
            val= val*fo/gal
            print(val)
        else:
            print('ERROR')
                
    ## pint to...
    elif vol1== 5:
        if vol2== 1:
            val= val*pt/ml
            print(val)
        elif vol2== 2:
            val= val*pt/l
            print(val)
        elif vol2== 3:
            val= val*pt/m3
            print(val)
        elif vol2== 4:
            val= val*pt/fo
            print(val)
        elif vol2== 5:
            val= val*pt/pt
            print(val)
        elif vol2== 6:
            val= val*pt/gal
            print(val)
        else:
            print('ERROR')
            
    ## gallons to...
    elif vol1== 6:
        if vol2== 1:
            val= val*gal/ml
            print(val)
        elif vol2== 2:
            val= val*gal/l
            print(val)
        elif vol2== 3:
            val= val*gal/m3
            print(val)
        elif vol2== 4:
            val= val*gal/fo
            print(val)
        elif vol2== 5:
            val= val*gal/pt
            print(val)
        elif vol2== 6:
            val= val*gal/gal
            print(val)
        else:
            print('ERROR')
                  
elif measure == 3:
    print('+-----------------------+\n|mg | g |kg |oz |lb |st |\n-------------------------\n| 1 | 2 | 3 | 4 | 5 | 6 |\n+-----------------------+')
    print()
    m1=int(input("convert from: "))
    m2=int(input("convert to: "))
    val= float(input("value: "))
    print('_____________________')
    
    ## milligramms to...
    if m1== 1:
        if m2== 1:
            val= val*mg/mg
            print(val)
        elif m2== 2:
            val= val*mg/g
            print(val)
        elif m2== 3:
            val= val*mg/kg
            print(val)
        elif m2== 4:
            val= val*mg/oz
            print(val)
        elif m2== 5:
            val= val*mg/lb
            print(val)
        elif m2== 6:
            val= val*mg/st
            print(val)
        else:
            print('ERROR')
            
    ## gramms to...
    elif m1== 2:
        if m2== 1:
            val= val*g/mg
            print(val)
        elif m2== 2:
            val= val*g/g
            print(val)
        elif m2== 3:
            val= val*g/kg
            print(val)
        elif m2== 4:
            val= val*g/oz
            print(val)
        elif m2== 5:
            val= val*g/lb
            print(val)
        elif m2== 6:
            val= val*g/st
            print(val)
        else:
            print('ERROR')
                    
    ## kilogramms to...
    elif m1== 3:
        if m2== 1:
            val= val*kg/mg
            print(val)
        elif m2== 2:
            val= val*kg/g
            print(val)
        elif m2== 3:
            val= val*kg/kg
            print(val)
        elif m2== 4:
            val= val*kg/oz
            print(val)
        elif m2== 5:
            val= val*kg/lb
            print(val)
        elif m2== 6:
            val= val*kg/st
            print(val)
        else:
            print('ERROR')             
                            
    ## ozz to...
    elif m1== 4:
        if m2== 1:
            val= val*oz/mg
            print(val)
        elif m2== 2:
            val= val*oz/g
            print(val)
        elif m2== 3:
            val= val*oz/kg
            print(val)
        elif m2== 4:
            val= val*oz/oz
            print(val)
        elif m2== 5:
            val= val*oz/lb
            print(val)
        elif m2== 6:
            val= val*oz/st
            print(val)
        else:
            print('ERROR')
                                    
    ## pounds to...
    elif m1== 5:
        if m2== 1:
            val= val*lb/mg
            print(val)
        elif m2== 2:
            val= val*lb/g
            print(val)
        elif m2== 3:
            val= val*lb/kg
            print(val)
        elif m2== 4:
            val= val*lb/oz
            print(val)
        elif m2== 5:
            val= val*lb/lb
            print(val)
        elif m2== 6:
            val= val*lb/st
            print(val)
        else:
            print('ERROR') 
    ## stones to...
    elif m1== 6:
        if m2== 1:
            val= val*st/mg
            print(val)
        elif m2== 2:
            val= val*st/g
            print(val)
        elif m2== 3:
            val= val*st/kg
            print(val)
        elif m2== 4:
            val= val*st/oz
            print(val)
        elif m2== 5:
            val= val*st/lb
            print(val)
        elif m2== 6:
            val= val*st/st
            print(val)
        else:
            print('ERROR')                                                
else: 
    print ("ERROR")
print('_____________________')

from os import system
system("pause")