    # chapter1.rpy


label chapter1:
    scene bg ancient_rome with dissolve
    show sophia happy at left
    s "Estamos en la Antigua Roma. Hay un error histórico que debemos corregir."
    show alex thinking at right
    e "¿Qué debemos hacer?"

    menu:
        "Ayudar a Sophia a corregir el error":
            $ choice1 = "help"
            show sophia normal at left
            show alex normal at right
            jump correct_error

        "Ignorar y explorar solo":
            $ choice1 = "ignore"
            show sophia angry at left
            show alex sad at right
            jump explore_alone

label correct_error:
    s "Gracias, Alex. Juntos podemos arreglar esto."
    show alex happy at right
    e "¿Qué debo hacer?"
    # Continuar la historia aquí...
    jump chapter2

label explore_alone:
    e "Lo siento, Sophia. Tengo que salir de aquí."
    show sophia sad at left
    # Continuar la historia aquí...
    jump chapter2

