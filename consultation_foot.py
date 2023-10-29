import histoire2foot

# Ici vos fonctions dédiées aux interactions

def info_equipe(liste_equipes):
    boucle = True
    equipe = ""
    while boucle:
        if equipe == "":
            print("Que voulez vous savoir ?")
            print("Donner le nom d'un pays qui a une équipe de football dont vous voulez les informations")
            equipe = input("Donner simplement le nom d'un pays qui a une équipe éxistante : ")
        if equipe in liste_equipes:
            print("Que voulez vous savoir de cette équipe ?")
            print("0 - Revenir en arrière")
            print("1 - Quelle est la date de sa première victoire en match international ?")
            print("2 - Son plus grand nombre de matchs consécutifs sans défaites ?")
            print("3 - Son nombre de victoires, matchs nuls et de défaites")
            choix = input("Veuillez indiquer votre choix (un numéro de choix): ")
            if choix in ["0", "1", "2", "3"]: 
                boucle = False
            else:
                print("!!! Veuillez indiquer un des choix qui vous est proposé !!!")
        else:
            print("!!! Je ne connais pas cette équipe, veuillez indiquez le nom d'une autre équipe qui éxiste !!!")
            equipe = ""
    if choix == "0":
        return None
    else:
        return (equipe, choix)


def info_competition():
    print("Que voulez vous savoir ?")
    print("Donner le nom d'une compétition de football dont vous voulez les informations")
    print("0 - Revenir en arrière")
    competition = input("Donnez le nom d'une compétition qui vous intéresse : ")
    if competition == "0":
        return None
    else:
        return competition


def info_matchs():
    boucle = True
    choix = ""
    ville = ""
    while boucle:
        if choix == "":
            print("Que voulez vous savoir ?")
            print("0 - Revenir en arrière")
            print("1 - Quels sont les matchs qui se sont déroulés dans quelle ville ?")
            print("2 - Quels matchs ont eu le plus écart de buts entre le vainqueur et le perdant ?")
            choix = input("Veuillez indiquer votre choix (un numéro de choix): ")
            if choix in ["0", "1", "2"]:
                if choix == "1":
                    if ville == "":
                        ville = input("Donner le nom d'une ville : ")
                elif choix == "0":
                    choix = None
                boucle = False
            else:
                choix = ""
                print("!!! Veuillez indiquer un des choix qui vous est proposé !!!")
    return (choix, ville)


def affichage_equipe(liste_matchs, equipe, choix):
    if choix == "1":
        date = histoire2foot.premiere_victoire(liste_matchs, equipe)
        if date is None:
            print("L'équipe", equipe, "n'a jamais gagné de matchs")
        else:
            print("L'équipe", equipe, "a gagné son premier match le", date)
    elif choix == "2":
        compte = histoire2foot.nb_matchs_sans_defaites(liste_matchs, equipe)
        print("Le plus grand nombre de victoire sans défaites de l'équipe", equipe, "est de", compte, "matchs sans défaites")
    else:
        resultats = histoire2foot.resultats_equipe(liste_matchs, equipe)
        print("L'équipe", equipe, "a", resultats[0], "victoires, à fait", resultats[1], "matchs nuls et", resultats[2], "défaites")


def affichage_competition(liste_matchs, competition):
    buts_moyens = histoire2foot.nombre_moyen_buts(liste_matchs, competition)
    if buts_moyens == 0:
        print("Soit la compétition est mal orthographié, soit elle n'éxiste pas, soit elle ne compte aucun buts marqués")
    else:
        print("En moyenne, il y a", buts_moyens, "buts marqués par matchs dans la compétition", competition)


def affichage_matchs(liste_matchs, choix, ville):
    if choix == "1":
        liste_ville = histoire2foot.matchs_ville(liste_matchs, ville)
        if liste_ville == []:
            print("Il n'y a aucun match qui ne s'est déroulé dans la ville de", ville)
        else:
            print("Les matchs s'étant déroulé à", ville, "sont : ")
            for match in liste_ville:
                ligne = match[1] + " à marquer " + str(match[3]) + " buts face à " + match[2] + " qui a marquer " + str(match[4]) + " buts"
                print(ligne)
    else:
        match_spect = histoire2foot.matchs_spectaculaires(liste_matchs)
        if len(match_spect) == 1:
            match = match_spect[0]
            print("Le match le plus spectaculaire est celui s'étant dérouler à", match[6], "en", match[7], 
              "avec un score de", match[3], "pour", match[1], "et de", match[4], "pour", match[2])
        else:
            for match in match_spect:
                print("L'un des matchs les plus spectaculaires est celui s'étant dérouler à", match[6], "en", match[7], 
              "avec un score de", match[3], "pour", match[1], "et de", match[4], "pour", match[2])


# ici votre programme principal
def programme_principal():
    barre = "".ljust(42, "#")
    vide = "#".ljust(40) + "#"
    print(barre)
    print(vide)
    print("# Bienvenue en quoi puis-je vous aider ? #")
    print(vide)
    print(barre, "\n")
     #  Partie chargement d'un fichier csv
    print("Avez vous un fichier csv que vous voulez exploiter en parliculier ? Si non, une liste de matchs par défaut sera utilisée (cela peut prendre un certains temps)")
    particu_csv = ""
    while particu_csv.upper() not in ["Y", "N"]:
        particu_csv = input("Y/N : ")
    if particu_csv.upper() == "Y":
        boucle = True
        while boucle:
            nom_csv = input("Donner le nom de votre fichier csv (avec extension) soit 0 si vous avez changé d'avis: ")
            if nom_csv == "0":
                particu_csv = "N"
                boucle = False
            else:
                try:
                    liste_matchs = histoire2foot.charger_matchs(nom_csv)
                    if histoire2foot.liste_matchs_correct(liste_matchs) and histoire2foot.est_bien_trie(liste_matchs):
                        boucle = False
                    else:
                        print("Votre fichier a un problème, soit les matchs ne respectent pas le format nécessaire pour être utiliser, soit ils ne sont pas triés dans un ordre croissant celon leur date")
                except:
                    print("Veuillez donner le nom d'un fichier csv qui existe sans oublier l'extension")
    if particu_csv.upper() == "N":
        liste1 = histoire2foot.charger_matchs("histoire1.csv")
        liste2 = histoire2foot.charger_matchs("histoire2.csv")
        liste3 = histoire2foot.charger_matchs("histoire3.csv")
        fusion = histoire2foot.fusionner_matchs(liste1, liste2)
        liste_matchs = histoire2foot.fusionner_matchs(fusion, liste3)
     #  Partie de tout ce qui va être menu de choix et questions
    boucle = True
    saisie = ""
    while boucle:
        if saisie == "":
            print(vide.strip("#") + "\n" + barre + "\n" + vide.strip("#"))
            print( "MENU", "\n", "Quelles types d'information voulez vous avoir ?")
            print("0 - Met fin au processus")
            print("1 - Informations en rapport avec un équipe")
            print("2 - Le nombre de but moyen par matchs dans une compétition")
            print("3 - Informations en rapport avec les matchs en général")
            saisie = input("Veuillez indiquer votre choix (un numéro de choix): ")
        if saisie == "0":
            boucle = False
        elif saisie == "1":
            liste_equipe = histoire2foot.liste_equipes(liste_matchs)
            resultats = info_equipe(liste_equipe)
            if resultats is not None:
                affichage_equipe(liste_matchs, resultats[0], resultats[1])
        elif saisie == "2":
            resultats = info_competition()
            if resultats is not None:
                affichage_competition(liste_matchs, resultats)
        elif saisie == "3":
            resultats = info_matchs()
            choix = resultats[0]
            ville = resultats[1]
            if choix is not None:
                affichage_matchs(liste_matchs, choix, ville)
        else:
            print("!!! Veuillez indiquer un des choix qui vous est proposé !!!")
        if saisie != "0":
            print("Voulez vous continuer a utilisé ce programme ?")
            continuer = input("Y/N : ")
            if continuer.upper() == "Y":
                saisie = ""
            else:
                saisie = "0"
    print("Merci d'avoir utiliser mon programme, en espérant qu'il vous ait plut et à bientôt")


if __name__ == "__main__":
    programme_principal()