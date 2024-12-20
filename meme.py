import random as r

# Diccionario de términos
meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "XD": "SARCASMO",
    "OBO": "¿Qué es obo?",
    "UWU": "Es alguien bien kawai",
    "WTF": "¡Qué grosero!",
}

# Mostrar las palabras disponibles
print("Palabras disponibles: " + ", ".join(meme_dict.keys()))
word = input('¿Qué palabra quieres conocer? O escribe "SORPRÉNDEME" para elegir una aleatoria: ').upper()

# Buscar y mostrar el significado
if word in meme_dict:
    print("Significado de " + word + ": " + meme_dict[word])
elif word == "SORPRÉNDEME":
    random_word = r.choice(list(meme_dict.keys()))  # Convertimos a lista
    print("La palabra que conocerás hoy es " + random_word + ": " + meme_dict[random_word])
else:
    print("Aún no conozco esa palabra 😥")
