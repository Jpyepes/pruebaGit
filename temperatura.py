listaTemperatura = [20,30,40,50,45,35,76,30]
mediaTemp = 0
for i in range(len(listaTemperatura)):
    mediaTemp = mediaTemp + listaTemperatura[i]
mediaTemp = mediaTemp/len(listaTemperatura)
listaTemperatura.append(mediaTemp)
print(f'Temperatura media: {mediaTemp}')
print(f'Temperatura menor: {min(listaTemperatura)}')
print(f'Temperatura mayor: {max(listaTemperatura)}')

