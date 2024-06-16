# chapter2.rpy

"""label chapter2:
    scene bg medieval_castle with dissolve
    e "Este lugar... parece un castillo medieval."
    s "Aquí debemos detener un conflicto que cambiará el curso de la historia."

    menu:
        "Intervenir en la batalla":
            $ choice2 = "intervene"
            jump intervene_battle

        "No intervenir":
            $ choice2 = "no_intervene"
            jump do_not_intervene

label intervene_battle:
    s "¡Buena elección, Alex! Podemos evitar una catástrofe."
    e "Espero que esto funcione..."
    # Continuar la historia aquí...
    jump chapter3

label do_not_intervene:
    s "Está bien, Alex. Tal vez es mejor no interferir."
    e "Sí, no quiero causar más problemas."
    # Continuar la historia aquí...
    jump chapter3"""
    
    
    # chapter2.rpy

label chapter2:
    scene bg medieval_castle with dissolve
    show alex thinking at right
    e "Este lugar... parece un castillo medieval."
    show sophia normal at left
    s "Aquí debemos detener un conflicto que cambiará el curso de la historia."

    menu:
        "Intervenir en la batalla":
            $ choice2 = "intervene"
            show sophia determined at left
            show alex determined at right
            jump intervene_battle

        "No intervenir":
            $ choice2 = "no_intervene"
            show sophia sad at left
            show alex sad at right
            jump do_not_intervene

label intervene_battle:
    s "¡Buena elección, Alex! Podemos evitar una catástrofe."
    show alex happy at right
    e "Espero que esto funcione..."
    # Continuar la historia aquí...
    jump chapter3

label do_not_intervene:
    s "Está bien, Alex. Tal vez es mejor no interferir."
    show alex sad at right
    e "Sí, no quiero causar más problemas."
    # Continuar la historia aquí...
    jump chapter3

