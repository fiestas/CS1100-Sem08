print("Un niño encuentra en el desvan de su abuelo...")
print("Un baul (1)")
print("Una espada samurai (2)")
Un_baul=1
Una_espada_samurai=2
Primera=int(input("Escriba una opcion:"))
if Primera==1:
        print("Abrirlo con un alicate (1)")
        print("Esperar a su abuelo y preguntarle (2)")
        Abrirlo_con_un_alicate=1
        Esperar_a_su_abuelo_y_preguntarle=2
        Primera1=int(input("Escriba una opcion:"))
        if Primera1==1:
                print("Termina hiriendose la mano y en el hospital.Fin de la historia")
        if Primera1==2:
                print("El abuelo se niega a abrir el baul y lo manda a dormir.Fin de la historia")
if Primera==2:
        print("La espada resplandece y se abre un armario. El niño entra al armario y sale en un bosque encantado. De pronto aparece un guerrero samurai. El niño escapa y regresa al armario, donde un hada le ofrece...")
        print("Volver al pasado (1)")
        print("Quedarse en el bosque (2)")
        Volver_al_pasado=1
        Quedarse_en_el_pasado=2
        Segunda=int(input("Escriba una opcion:"))
        if Segunda==1:
            print("Vuelve al momento en que encuentra el baul y la espada (bucle infinito!)")
        if Segunda==2:
            print("Puede ver a traves de un espejo en el armario, como sus abuelos son atrapados en el baul. Fin de la historia,")

