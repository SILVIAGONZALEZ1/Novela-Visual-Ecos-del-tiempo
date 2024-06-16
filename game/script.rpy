# script.rpy
# Personajes
# Importa Ren'Py

define e = Character('Alex', color="#02ac66") 

define s = Character('Sophia', color="#c82a54")

define k = Character('Dr. Kronos', color="#8c4966")

# Define las imágenes de los personajes y los fondos
image bg present_city = "images/present_city.jpg"
image bg ancient_rome = "images/ancient_rome.jpg"
image bg medieval_castle = "images/medieval_castle.jpg"
image bg future_dystopia = "images/future_dystopia.jpg"
image bg time_lab = "images/time_lab.jpg"
image bg museum = "images/museum.jpg"

image alex normal = "images/alex_normal.png"
image alex happy = "images/alex_happy.png"
image alex sad = "images/alex_sad.png"
image alex determined = "images/alex_determined.png"
image alex thinking = "images/alex_thinking.png"
image alex shocked = "images/alex_shocked.png"
image alex relieved = "images/alex_relieved.png"


image sophia normal = "images/sophia_normal.png"
image sophia happy = "images/sophia_happy.png"
image sophia angry = "images/sophia_angry.png"
image sophia sad = "images/sophia_sad.png"
image sophia worried = "images/sophia_worried.png"
image sophia determined = "images/sophia_determined.png"

image kronos normal = "images/kronos_normal.png"
image kronos evil = "images/kronos_evil.png"
image kronos thinking = "images/kronos_thinking.png"
image kronos angry = "images/kronos_angry.png"

# Inicio del juego

# script.rpy

label start:
     # Reproduce música de fondo en bucle
    play music "audio/background_music.ogg" loop
    scene bg present_city
    show alex normal at left
    e "¡Hola! Soy Alex. No creerías lo que descubrí hoy..."

    # Cambiar a una expresión feliz de Alex
    scene bg museum
    show alex happy at left
    e "¡Esto es increíble!"

    # Descubrimiento del artefacto
    scene bg museum
    show alex normal at right
    e "Esto parece un artefacto antiguo. ¿Qué es esta inscripción?"
    e "¡Oh no, está haciendo algo extraño!"

    # Primer viaje en el tiempo
    scene bg ancient_rome
    show alex sad at right
    e "¿Dónde estoy? Esto parece... ¡Roma Antigua!"

    # Encontrando a Sophia
    show sophia normal at left
    s "¡Hola, extraño! ¿Estás perdido?"
    show alex happy at right
    e "No te lo creerías, pero creo que viajé en el tiempo..."

    jump chapter1
