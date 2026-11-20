import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Definición de los datos de Streaming (Plataforma, Suscriptores_Millones, Opcion_Gratis, Lanzamiento)
nfx = ['Netflix', 260, False, 2007]
dis = ['Disney+', 150, False, 2019]
spn = ['Spotify', 602, True, 2008]
ytb = ['YouTube Premium', 100, True, 2014]
hbo = ['Max', 95, False, 2020]

# 2. Creamos la lista de listas (conformando la tabla)
listas_streaming = [nfx, dis, spn, ytb, hbo]

# 3. Utilizar pandas para organizar la tabla (DataFrame)
# A cada columna le ponemos nombre acorde a la estructura solicitada
df_streaming = pd.DataFrame(
    listas_streaming,
    columns=['Plataforma', 'Suscriptores_Millones', 'Opcion_Gratis', 'Lanzamiento'],
)
print(df_streaming)

# Guardar en archivo CSV (opcional)
# df_streaming.to_csv("streaming.csv", index=False)

# 4. Crear gráfica de líneas (Eje X: Plataforma, Eje Y: Suscriptores_Millones)
plt.plot(df_streaming['Plataforma'], df_streaming['Suscriptores_Millones'])
plt.title('Gráfica Streaming 1110 - Suscriptores')
plt.xlabel('Plataformas de Streaming')
plt.ylabel('Suscriptores (millones)')
plt.show()

# 5. Crear gráfica de puntos (Scatter)
plt.scatter(df_streaming['Plataforma'], df_streaming['Suscriptores_Millones'])
plt.title('Dispersión Streaming - Suscriptores')
plt.xlabel('Plataformas de Streaming')
plt.ylabel('Suscriptores (millones)')
plt.show()

# 6. Gráfica de barras simple
plt.bar(df_streaming['Plataforma'], df_streaming['Suscriptores_Millones'])
plt.title('Streaming 1110')
plt.xlabel('Las Plataformas')
plt.ylabel('Suscriptores (millones)')
plt.show()

# 7. Ordenar la gráfica de barras de manera descendente
df_streaming_ordenar = df_streaming.sort_values('Suscriptores_Millones', ascending=False)
plt.bar(df_streaming_ordenar['Plataforma'], df_streaming_ordenar['Suscriptores_Millones'])
plt.title('Streaming Ordenadas (Mayor a Menor Suscriptores)')
plt.xlabel('Las Plataformas')
plt.ylabel('Suscriptores (millones)')
plt.show()

# 8. Coloreando la gráfica de barras ordenada
plt.bar(
    df_streaming_ordenar['Plataforma'],
    df_streaming_ordenar['Suscriptores_Millones'],
    color=['b', 'g', 'c', 'm', 'y'],  # Ajustado a 5 colores por las 5 plataformas
)
plt.title('Streaming Ordenadas con Color')
plt.xlabel('Las Plataformas')
plt.ylabel('Suscriptores (millones)')
plt.show()

# 9. Gráfica de pastel (Pie chart)
plt.pie(df_streaming['Suscriptores_Millones'], labels=df_streaming['Plataforma'])
plt.title('Distribución de Suscriptores Streaming')
plt.show()