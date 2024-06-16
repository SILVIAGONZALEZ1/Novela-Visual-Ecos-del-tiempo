# endings.rpy

"""label finale:
    scene bg time_lab with dissolve
    if choice3 == "confront":
        e "He detenido a Dr. Kronos, pero el futuro aún está en peligro..."
        # Final de enfrentamiento
        jump ending_confront

    elif choice3 == "seek_solution":
        e "Encontré una forma de arreglar la línea temporal sin luchar."
        # Final de búsqueda de solución
        jump ending_solution

label ending_confront:
    scene bg present_city with dissolve
    e "Todo ha vuelto a la normalidad, pero el futuro siempre estará en riesgo."
    s "Buen trabajo, Alex. Pero debemos estar siempre atentos."
    # Final de enfrentamiento
    return

label ending_solution:
    scene bg present_city with dissolve
    e "He restaurado el equilibrio sin luchar. El futuro está a salvo por ahora."
    s "Lo has hecho bien, Alex. El tiempo está en buenas manos."
    # Final de búsqueda de solución
    return"""
    
    # endings.rpy

label finale:
    scene bg time_lab with dissolve
    if choice3 == "confront":
        show alex happy at right
        show sophia happy at left
        e "He detenido a Dr. Kronos, pero el futuro aún está en peligro..."
        # Final de enfrentamiento
        jump ending_confront

    elif choice3 == "seek_solution":
        show alex relieved at right
        show sophia happy at left
        e "Encontré una forma de arreglar la línea temporal sin luchar."
        # Final de búsqueda de solución
        jump ending_solution

label ending_confront:
    scene bg present_city with dissolve
    show alex happy at right
    show sophia happy at left
    e "Todo ha vuelto a la normalidad, pero el futuro siempre estará en riesgo."
    s "Buen trabajo, Alex. Pero debemos estar siempre atentos."
    # Final de enfrentamiento
    return

label ending_solution:
    scene bg present_city with dissolve
    show alex happy at right
    show sophia happy at left
    e "He restaurado el equilibrio sin luchar. El futuro está a salvo por ahora."
    s "Lo has hecho bien, Alex. El tiempo está en buenas manos."
    # Final de búsqueda de solución
    return

