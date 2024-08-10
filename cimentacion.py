import matplotlib.pyplot as plt
import math

ancho_cimentacion = 3 
largo_cimentacion = 4
Df = 1
peso_unitario_1 = 1.44
peso_unitario_2 = 1.44
angulo_friccion = 23

# Convertir el ángulo a radianes
angulo_friccion_radianes = math.radians(angulo_friccion)
cohesion = 6
factor_seguridad = 3
inclinacion_carga = 0
forma = 'rectangular'

# Calculando los factores de capacidad portante
print('Calculando los Factores de Capacidad de Carga')
Nq = pow(math.e,math.pi*math.tan(angulo_friccion_radianes))*pow(math.tan(math.radians(45 + angulo_friccion/2)),2)
print(f'Nq = {Nq}')
Nc = (1/math.tan(angulo_friccion_radianes))*(Nq - 1)
print(f'Nc = {Nc}')
N_gamma = 2*math.tan(angulo_friccion_radianes)*(Nq + 1)
print(f'Nγ = {N_gamma}')

# Calculando los factores de forma
print('Calculando los Factores de Forma')
if forma =='rectangular':
    Sc = (1 + (Nq/Nc)*(ancho_cimentacion/largo_cimentacion))
    Sq = 1 + (math.tan(angulo_friccion_radianes))*(ancho_cimentacion/largo_cimentacion)
    S_gamma = 1 - 0.4 *(ancho_cimentacion/largo_cimentacion)

elif forma == 'circular':
    Sc = (1 + (Nq/Nc))
    Sq = 1 + (math.tan(angulo_friccion_radianes))
    S_gamma = 0.60

elif forma == 'cuadrado':
    Sc = (1 + (Nq/Nc))
    Sq = 1 + (math.tan(angulo_friccion_radianes))
    S_gamma = 0.60
 
print(f'Sc = {Sc}')
print(f'Sq = {Sq}')
print(f'Sγ = {S_gamma}')

# Calculando los factores de profundidad
print('Calculando los Factores de Profundidad')
d_gamma = 1
if (Df/ancho_cimentacion) <= 1:
    k = Df/ancho_cimentacion
elif (Df/ancho_cimentacion) > 1:  
    k = math.atan(Df/ancho_cimentacion)

dc = 1 + 0.4 * k
dq = 1 + 2 * math.tan(angulo_friccion_radianes) * pow((1 - math.sin(angulo_friccion_radianes)), 2) * k

print(f'dc = {dc}')
print(f'dq = {dq}')
print(f'dγ = {d_gamma}')

# Calculando los factores de inclinación
print('Calculando los Factores de Inclinación')
ic = pow((1 - inclinacion_carga / 90), 2)
iq = pow((1 - inclinacion_carga / 90), 2)
i_gamma = pow((1 - inclinacion_carga / angulo_friccion), 2)

print(f'ic = {ic}')
print(f'iq = {iq}')
print(f'iγ = {i_gamma}')

# Calculamos la capacidad de carga última
qu = round(((cohesion * Nc * Sc * dc * ic + Df * peso_unitario_1 * Nq * Sq * dq * iq + 0.5 * peso_unitario_2 * ancho_cimentacion * N_gamma * S_gamma * d_gamma * i_gamma) / 10), 2)
print(f'La capacidad de carga última: qu = {qu} kg/cm2')

# Calculamos la capacidad admisible
qadm = round((qu / factor_seguridad), 2)
print(f'La capacidad de carga admisible: qamd = {qadm} kg/cm2')

# Calculamos la carga admisible total
Q = round((qadm * ancho_cimentacion * largo_cimentacion), 2)
print(f'La carga admisible: Q = {Q} kg')

# Dibujando nuestra zapata

# Configuración de la figura y los ejes, Crea una nueva figura (fig) y un conjunto de ejes (ax). plt.subplots() es una forma rápida de crear una figura y un único conjunto de ejes.
fig, ax = plt.subplots() 

# Ajustar los límites de los ejes, Establece los límites del eje x de -1 a 5 y los límites del eje y de -1 a 4. Esto define el área visible del gráfico.
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 4)

# Dibujar la zapata como un rectángulo, la coordenada (0.5, 0) es el punto de inicio de dibujo de nuestra zapata, el ancho sera lo que esta alamcenado en ancho_cimentacion y el alto sera 0.5, Linewidth es grosor de linea, edgecolor es color de borde y facecolor es color de dibujo.
# ax.add_patch(rect) añade el rectángulo al gráfico.
rect = plt.Rectangle((0.5, 0), ancho_cimentacion, 0.5, linewidth=1, edgecolor='black', facecolor='gray')
ax.add_patch(rect)

# Dibujar la columna central, la coordenada ((ancho_cimentacion / 2) + 0.25 , 0.5) es el punto de inicio de dibujo de nuestra columna, el ancho sera 0.5 y el alto sera 2, Linewidth es grosor de linea, edgecolor es color de borde y facecolor es color de dibujo.
# ax.add_patch(columna) añade el rectángulo al gráfico.
columna = plt.Rectangle(((ancho_cimentacion / 2) + 0.25 , 0.5), 0.5, 2, linewidth=1, edgecolor='black', facecolor='gray')
ax.add_patch(columna)

# Dibujar la línea azul que indica que la coordenada [-1, ancho_cimentacion + 2] indica que la linea comienza en -1 y termina en ancho_cimentacion + 2 en el eje x, en el eje Y comienza en Df y termina en Df.
plt.plot([-1, ancho_cimentacion + 2], [Df, Df ], 'b-')

# Dibujar la línea roja que indica que la coordenada [-1, ancho_cimentacion + 2] indica que la linea comienza en -1 y termina en ancho_cimentacion + 2 en el eje x, en el eje Y comienza en 0 y termina en 0.
plt.plot([-1, ancho_cimentacion + 2], [0, 0], 'r--')

# Etiquetas y límites del gráfico, en el primer "text" (ancho_cimentacion, 0.7) es la coordenada donde se ubicara nuestro texto, va es el alineamiento vertical del texto y ha es el alineamiento horizontal del texto.
plt.text(ancho_cimentacion, 0.7, f'\u03B3 1 = {peso_unitario_1} Ton/m3', va='center', ha='left')
plt.text(ancho_cimentacion + 0.2, Df + 0.1, 'NT', va='center', ha='left')
plt.text(0, Df/2, f'Df = {Df} m', va='center', ha='right')
plt.text(2, -0.2, f'\u03B3 2 = {peso_unitario_2} Ton/m3', va='center', ha='center')
plt.text(2, -0.4, f'c = {cohesion} Ton/m2', va='center', ha='center')
plt.text(2, -0.6, f'\u03C6 = {angulo_friccion}°', va='center', ha='center')

# Configurar las etiquetas de los ejes y el título del gráfico
ax.set_xlabel('Ancho (m)')
ax.set_ylabel('Altura (m)')
ax.set_title('Vista Frontal de la Zapata')

# Mostrar el gráfico, plt.gca() es una función de Matplotlib que significa "get current axes" (obtener los ejes actuales). Devuelve el objeto de los ejes actuales del gráfico, que luego puede ser modificado. set_aspect() es un método del objeto de los ejes que establece la relación de aspecto de los ejes. equal':Este argumento indica que se debe mantener una relación de aspecto igual. Esto significa que una unidad en el eje x es igual a una unidad en el eje y en términos de longitud visual. Los círculos se verán como círculos y los cuadrados como cuadrados, sin distorsión. adjustable='box': Este argumento indica cómo se debe ajustar la caja de los ejes cuando se cambia la relación de aspecto. En resumen, esta línea de código garantiza que las escalas de los ejes x e y sean iguales, de modo que los objetos en el gráfico no se distorsionen y se mantengan proporcionales
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
