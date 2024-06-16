# chapter3.rpy

"""label chapter3:
    scene bg future_dystopia with dissolve
    e "¿Qué ha pasado aquí? Este futuro está devastado."
    s "Dr. Kronos ha estado manipulando la línea temporal. Debemos detenerlo."

    # Enfrentamiento con Dr. Kronos
    show kronos normal at right
    k "No puedes detenerme, Alex. El tiempo está bajo mi control."

    menu:
        "Enfrentar a Dr. Kronos":
            $ choice3 = "confront"
            jump confront_kronos

        "Buscar otra solución":
            $ choice3 = "seek_solution"
            jump seek_solution

label confront_kronos:
    e "¡No dejaré que destruyas el tiempo!"
    # Continuar la historia aquí...
    jump finale

label seek_solution:
    e "Debe haber otra forma de arreglar esto..."
    # Continuar la historia aquí...
    jump finale"""
    
    
    # chapter3.rpy

label chapter3:
    scene bg future_dystopia with dissolve
    show alex shocked at right
    e "¿Qué ha pasado aquí? Este futuro está devastado."
    show sophia worried at left
    s "Dr. Kronos ha estado manipulando la línea temporal. Debemos detenerlo."

    # Enfrentamiento con Dr. Kronos
    show kronos evil at right
    k "No puedes detenerme, Alex. El tiempo está bajo mi control."

    menu:
        "Enfrentar a Dr. Kronos":
            $ choice3 = "confront"
            show alex determined at right
            jump confront_kronos

        "Buscar otra solución":
            $ choice3 = "seek_solution"
            show alex thinking at right
            jump seek_solution

label confront_kronos:
    e "¡No dejaré que destruyas el tiempo!"
    show kronos angry at right
    # Continuar la historia aquí...
    jump finale

label seek_solution:
    e "Debe haber otra forma de arreglar esto..."
    show sophia hopeful at left
    # Continuar la historia aquí...
    jump finale

