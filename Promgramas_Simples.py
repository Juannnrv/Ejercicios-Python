import math

M_pequeno = 47 
M_grande = 67  
rho = 1.038  
c = 3.7  
K = 5.4e-3  
Tw = 100  

To = float(input("Ingrese la temperatura original del huevo (en °C): "))

tamanio_huevo = input("¿El huevo es pequeño o grande? (P/G): ")
if tamanio_huevo.upper() == 'P':
    M = M_pequeno
else:
    M = M_grande

Ty = 70  
t = (M**(2/3) * c * rho**(1/3) * K * math.pi**2) / (4 * math.pi / 3)**(2/3) * math.log(0.76 * (To - Tw) / (Ty - Tw))

print("El tiempo necesario para alcanzar la temperatura máxima de la yema es de {:.2f} segundos.".format(t))

