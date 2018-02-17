from model_graph import graphe_controle

# Programme 2: programme suivant
# 1 : while X <= 0 :
#     then 2 : X := X + 1
# 3 : then : return X



if __name__ == '__main__':
    model = graphe_controle(3)

    # ajout des variables
    model.add_variables(['x'])

    # ajout des aretes de décision
    model.add_arete_decision(1, 2, lambda dic: dic['x'] <= 0)
    model.add_arete_decision(1, 3, lambda dic: dic['x'] > 0)

    # ajout des aretes d'affectation
    model.add_arete_affectation(2, 1, lambda dic: dic.update({'x': dic['x']+1}))

    # print(model.def_function(2))
    # print(model.ref_function(2))
    #
    jeu_test = [{'x': 0}, {'x': 2}]
    # print("Jeu de test : ", jeu_test)
    # print("Toutes les affectations : ", model.toutes_affectations(jeu_test))
    # print("Toutes les décisions : ", model.toutes_affectations(jeu_test))
    print("Toutes les i-boucles : ", model.toutes_boucles(jeu_test, i=2))
    #print("parcours", model.parcours_tous_chemins())
    #print(model.parcours_tous_chemins_pour_solene())
    # print("Toutes les définitions : ", model.toutes_les_def(jeu_test))
    #print("Toutes les utilisations : ", model.toutes_les_utilisations(jeu_test))
   # print(model.parcours_tous_chemins(j=3))
   # print(model.loops())
   # print(model.parcours_tous_chemins_pour_solene())
    #print(model.loop_edges())