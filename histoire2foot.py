"""Fichier source de la SAE 1.01 partie 1
    Historique des matchs de football internationaux
    """

# ---------------------------------------------------------------------------------------------
# Exemples de données pour vous aider à faire des tests
# ---------------------------------------------------------------------------------------------
    
# exemples de matchs de foot
match1 = ('2021-06-28', 'France', 'Switzerland', 3, 3, 'UEFA Euro', 'Bucharest', 'Romania', True)
match2 = ('1998-07-12', 'France', 'Brazil', 3, 0, 'FIFA World Cup', 'Saint-Denis', 'France', False)
match3 = ('1978-04-05', 'Germany', 'Brazil', 0, 1, 'Friendly', 'Hamburg', 'Germany', False)

# exemples de listes de matchs de foot
liste1 = [('1970-04-08', 'France', 'Bulgaria', 1, 1, 'Friendly', 'Rouen', 'France', False), 
        ('1970-04-28', 'France', 'Romania', 2, 0, 'Friendly', 'Reims', 'France', False), 
        ('1970-09-05', 'France', 'Czechoslovakia', 3, 0, 'Friendly', 'Nice', 'France', False), 
        ('1970-11-11', 'France', 'Norway', 3, 1, 'UEFA Euro qualification', 'Lyon', 'France', False)
        ]
liste2 = [('1901-03-09', 'England', 'Northern Ireland', 3, 0, 'British Championship', 'Southampton', 'England', False), 
        ('1901-03-18', 'England', 'Wales', 6, 0, 'British Championship', 'Newcastle', 'England', False), 
        ('1901-03-30', 'England', 'Scotland', 2, 2, 'British Championship', 'London', 'England', False), 
        ('1902-05-03', 'England', 'Scotland', 2, 2, 'British Championship', 'Birmingham', 'England', False), 
        ('1903-02-14', 'England', 'Northern Ireland', 4, 0, 'British Championship', 'Wolverhampton', 'England', False), 
        ('1903-03-02', 'England', 'Wales', 2, 1, 'British Championship', 'Portsmouth', 'England', False), 
        ('1903-04-04', 'England', 'Scotland', 1, 2, 'British Championship', 'Sheffield', 'England', False), 
        ('1905-02-25', 'England', 'Northern Ireland', 1, 1, 'British Championship', 'Middlesbrough', 'England', False), 
        ('1905-03-27', 'England', 'Wales', 3, 1, 'British Championship', 'Liverpool', 'England', False), 
        ('1905-04-01', 'England', 'Scotland', 1, 0, 'British Championship', 'London', 'England', False), 
        ('1907-02-16', 'England', 'Northern Ireland', 1, 0, 'British Championship', 'Liverpool', 'England', False), 
        ('1907-03-18', 'England', 'Wales', 1, 1, 'British Championship', 'London', 'England', False), 
        ('1907-04-06', 'England', 'Scotland', 1, 1, 'British Championship', 'Newcastle', 'England', False), 
        ('1909-02-13', 'England', 'Northern Ireland', 4, 0, 'British Championship', 'Bradford', 'England', False), 
        ('1909-03-15', 'England', 'Wales', 2, 0, 'British Championship', 'Nottingham', 'England', False), 
        ('1909-04-03', 'England', 'Scotland', 2, 0, 'British Championship', 'London', 'England', False)
        ]
liste3 = [('1901-03-30', 'Belgium', 'France', 1, 2, 'Friendly', 'Bruxelles', 'Belgium', False),
        ('1901-03-30', 'England', 'Scotland', 2, 2, 'British Championship', 'London', 'England', False),
        ('1903-04-04', 'Brazil', 'Argentina', 3, 0, 'Friendly', 'Sao Paulo', 'Brazil', False),
        ('1903-04-04', 'England', 'Scotland', 1, 2, 'British Championship', 'Sheffield', 'England', False), 
        ('1970-09-05', 'France', 'Czechoslovakia', 3, 0, 'Friendly', 'Nice', 'France', False), 
        ('1970-11-11', 'France', 'Norway', 3, 1, 'UEFA Euro qualification', 'Lyon', 'France', False)
        ]
liste4 = [('1978-03-19', 'Argentina', 'Peru', 2, 1, 'Copa Ramón Castilla', 'Buenos Aires', 'Argentina', False), 
        ('1978-03-29', 'Argentina', 'Bulgaria', 3, 1, 'Friendly', 'Buenos Aires', 'Argentina', False), 
        ('1978-04-05', 'Argentina', 'Romania', 2, 0, 'Friendly', 'Buenos Aires', 'Argentina', False), 
        ('1978-05-03', 'Argentina', 'Uruguay', 3, 0, 'Friendly', 'Buenos Aires', 'Argentina', False), 
        ('1978-06-01', 'Germany', 'Poland', 0, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-02', 'Argentina', 'Hungary', 2, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', False), 
        ('1978-06-02', 'France', 'Italy', 1, 2, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-02', 'Mexico', 'Tunisia', 1, 3, 'FIFA World Cup', 'Rosario', 'Argentina', True), 
        ('1978-06-03', 'Austria', 'Spain', 2, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-03', 'Brazil', 'Sweden', 1, 1, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-03', 'Iran', 'Netherlands', 0, 3, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-03', 'Peru', 'Scotland', 3, 1, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-06', 'Argentina', 'France', 2, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', False), 
        ('1978-06-06', 'Germany', 'Mexico', 6, 0, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-06', 'Hungary', 'Italy', 1, 3, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-06', 'Poland', 'Tunisia', 1, 0, 'FIFA World Cup', 'Rosario', 'Argentina', True), 
        ('1978-06-07', 'Austria', 'Sweden', 1, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-07', 'Brazil', 'Spain', 0, 0, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-07', 'Iran', 'Scotland', 1, 1, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-07', 'Netherlands', 'Peru', 0, 0, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-10', 'Argentina', 'Italy', 0, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', False), 
        ('1978-06-10', 'France', 'Hungary', 3, 1, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-10', 'Germany', 'Poland', 1, 3, 'FIFA World Cup', 'Rosario', 'Argentina', True), 
        ('1978-06-11', 'Austria', 'Brazil', 0, 1, 'FIFA World Cup', 'Mar del Plata', 'Argentina', True), 
        ('1978-06-11', 'Iran', 'Peru', 1, 4, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-11', 'Netherlands', 'Scotland', 2, 3, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-11', 'Spain', 'Sweden', 1, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-14', 'Argentina', 'Poland', 2, 0, 'FIFA World Cup', 'Rosario', 'Argentina', False), 
        ('1978-06-14', 'Austria', 'Netherlands', 1, 5, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-14', 'Brazil', 'Peru', 3, 0, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-14', 'Germany', 'Italy', 0, 0, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-18', 'Argentina', 'Brazil', 0, 0, 'FIFA World Cup', 'Rosario', 'Argentina', False), 
        ('1978-06-18', 'Austria', 'Italy', 0, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-18', 'Germany', 'Netherlands', 2, 2, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-18', 'Peru', 'Poland', 0, 1, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-21', 'Argentina', 'Peru', 6, 0, 'FIFA World Cup', 'Rosario', 'Argentina', False), 
        ('1978-06-21', 'Austria', 'Germany', 3, 2, 'FIFA World Cup', 'Córdoba', 'Argentina', True), 
        ('1978-06-21', 'Brazil', 'Poland', 3, 1, 'FIFA World Cup', 'Mendoza', 'Argentina', True), 
        ('1978-06-21', 'Italy', 'Netherlands', 1, 2, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-24', 'Brazil', 'Italy', 2, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', True), 
        ('1978-06-25', 'Argentina', 'Netherlands', 3, 1, 'FIFA World Cup', 'Buenos Aires', 'Argentina', False)
]

# -----------------------------------------------------------------------------------------------------
# listes des fonctions à implémenter
# -----------------------------------------------------------------------------------------------------

# Fonctions à implémenter dont les tests sont fournis


def match_correct(match):
    """renvoie si le match rentré en paramètre respecte le format de match

    Args:
        match (tuple): tuple que l'on va tester s'il correspond au bon format

    Returns:
        bool: True si le match respect le format, False s'il ne le fait pas
    """
    if type(match) == tuple and len(match) == 9: #  Test si match est un tuple et qu'il contient 9 éléments
        match_format = (str, str, str, int, int, str, str, str, bool) #  Tuple contentant le type aux quels doivent appartenir les éléments pour respecter le format
        for indice in range(len(match)):
            if type(match[indice]) != match_format[indice]: #  Test si les éléments sont du bon type
                return False
         #  Test si la date respecte le format de la date comme il doit être enregistrer
        date = match[0]
        if not (date[4] == "-" and date[7] == "-"):
            if not (date[0:3] in "0123456789" and date[5:6] in "0123456789" and date[8:9] in "0123456789"):
                return False
         #  Test si l'occurence est correcte, si le match se passe réelement en terrain neutre
        if match[8]:
            if match[7] in match[1:2]:
                return False
        else:
            if not match[7] in match[1:2]:
                return False
        return True #  Si tout est bon, on renvoie True
    return False


def liste_matchs_correct(liste_matchs):
    """Permet de tester si une liste de matchs respecte le format de match utiliser

    Args:
        liste_matchs (list): liste de matchs

    Returns:
        bool: True si la liste de match respecte le format, False si ce n'est pas le cas
    """
    for match in liste_matchs: #  Test pour chaque élément de liste_matchs
        if not match_correct(match): #  Si un match ne respecte pas le format, on renvoie False
            return False
    return True


def equipe_gagnante(match):
    """retourne le nom de l'équipe qui a gagné le match. Si c'est un match nul on retourne None

    Args:
        match (tuple): un match

    Returns:
        str: le nom de l'équipe gagnante (ou None si match nul)
    """
    gagnant = None
    if match[3] != match[4]:
        if match[3] > match[4]:
            gagnant = match[1]
        else:
            gagnant = match[2]
    return gagnant


def victoire_a_domicile(match):
    """indique si le match correspond à une victoire à domicile

    Args:
        match (tuple): un match

    Returns:
        bool: True si l'équipe qui gagne gagne à domicile, False si ce n'est pas le cas
    """
    return equipe_gagnante(match) == match[7]


def nb_buts_marques(match):
    """indique le nombre total de buts marqués lors de ce match

    Args:
        match (tuple): un match

    Returns:
        int: le nombre de buts du match, None si le match ne respecte pas le format de match
    """
    buts = match[3] + match[4]
    return buts


def matchs_ville(liste_matchs, ville):
    """retourne la liste des matchs qui se sont déroulés dans une ville donnée
    
    Args:
        liste_matchs (list): une liste de matchs
        ville (str): le nom d'une ville

    Returns:
        list: la liste des matchs qui se sont déroulé dans la ville ville    
    """
    liste_ville = []
    for match in liste_matchs:
        if match[6] == ville:
            liste_ville.append(match)
    return liste_ville


def nombre_moyen_buts(liste_matchs, nom_competition):
    """retourne le nombre moyen de buts marqués par match pour une compétition donnée

    Args:
        liste_matchs (list): une liste de matchs
        nom_competition (str): le nom d'une compétition
    
    Returns:
        float: le nombre moyen de buts par match pour la compétition
    """
    nb_competition = 0
    total_buts = 0
    moyenne = 0
    for match in liste_matchs:
        if match[5].lower() == nom_competition.lower():
            nb_competition += 1
            total_buts += nb_buts_marques(match)
    if nb_competition != 0:
        moyenne = total_buts / nb_competition
    return moyenne


def est_bien_trie(liste_matchs):
    """vérifie si une liste de matchs est bien trié dans l'ordre chronologique
       puis pour les matchs se déroulant le même jour, dans l'ordre alphabétique
       des équipes locales

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        bool: True si la liste est bien triée et False sinon
    """
    for indice in range(1, len(liste_matchs)):
        if liste_matchs[indice-1][0] > liste_matchs[indice][0]:
            return False
        if liste_matchs[indice-1][0] == liste_matchs[indice][0]:
            if liste_matchs[indice-1][1] > liste_matchs[indice][1]:
                return False
    return True


def compare_matchs(match1, match2):
    """Compare deux matchs pour savoir lequel doit apparaitre en premier dans une liste quand on fusionne deux listes

    Args:
        match1 (tuple): match issue de la liste de matchs 1
        match2 (tuple): match issue de la liste de matchs 2

    Returns:
        tuple: renvoie le tuple du match qui doit apparaître en premier, si les deux sont égaux on renvoie un tuple contenant les deux matchs
    """    
    resultat = (match1, match2)
    if match1 != match2:
        if match1[0] < match2[0]:
            resultat = match1
        elif match1[0] > match2[0]:
            resultat = match2
        elif match1[1] < match2[1]:
            resultat = match1
        elif match1[1] > match2[1]:
            resultat = match2
        elif match1[2] < match2[2]:
            resultat = match1
        elif match1[2] > match2[2]:
            resultat = match2
        elif match1[3] < match2[3]:
            resultat = match1
        elif match1[3] > match2[3]:
            resultat = match2
        elif match1[4] < match2[4]:
            resultat = match1
        elif match1[4] > match2[4]:
            resultat = match2
        elif match1[5] < match2[5]:
            resultat = match1
        elif match1[5] > match2[5]:
            resultat = match2
        elif match1[6] < match2[6]:
            resultat = match1
        elif match1[6] > match2[6]:
            resultat = match2
        elif match1[7] < match2[7]:
            resultat = match1
        elif match1[7] > match2[7]:
            resultat = match2
        elif match1[8] < match2[8]:
            resultat = match1
        else:
            resultat = match2
    return resultat


def fusionner_matchs(liste_matchs1, liste_matchs2):
    """Fusionne deux listes de matchs triées sans doublons en une liste triée sans doublon
    sachant qu'un même match peut être présent dans les deux listes

    Args:
        liste_matchs1 (list): la première liste de matchs
        liste_matchs2 (list): la seconde liste de matchs

    Returns:
        list: la liste triée sans doublon comportant tous les matchs de liste_matchs1 et liste_matchs2
    """
    indice1 = 0
    indice2 = 0
    liste_matchs = []
    while indice1 < len(liste_matchs1) and indice2 < len(liste_matchs2):  # Parcours les deux listes tant qu'une des deux listes n'est pas entièrement parcouru
        match1 = liste_matchs1[indice1]
        match2 = liste_matchs2[indice2]
        test = compare_matchs(match1, match2)
        if test == (match1, match2):
                liste_matchs.append(match1)  # Dans ce cas on ajoute la ligne et on incrémente de 1 les deux indides
                indice1 += 1
                indice2 += 1
        elif test == liste_matchs1[indice1]:  # Si le match de la liste 1 c'est dérouler avant le match de la liste 2
            liste_matchs.append(liste_matchs1[indice1])
            indice1 += 1
        else:
            liste_matchs.append(liste_matchs2[indice2])
            indice2 += 1
    if indice1 == len(liste_matchs1):
        for indice in range(indice2, len(liste_matchs2)):
            if liste_matchs2[indice] not in liste_matchs:
                liste_matchs.append(liste_matchs2[indice])
    else:
        for indice in range(indice1, len(liste_matchs1)):
            if liste_matchs1[indice] not in liste_matchs:
                liste_matchs.append(liste_matchs1[indice])
    return liste_matchs


def resultats_equipe(liste_matchs, equipe):
    """donne le nombre de victoire, de matchs nuls et de défaites pour une équipe donnée

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        tuple: un triplet d'entiers contenant le nombre de victoires, nuls et défaites de l'équipe
    """
    victoires = 0
    nuls = 0
    defaites = 0
    for match in liste_matchs:
        if match[1] == equipe:  # Vérifie que l'équipe donnée est l'equipe qui reçois
            if match[3] == match[4]:  # Vérifie si le match est nul
                nuls += 1
            elif match[3] > match[4]:  # Vérifie que le nombre de buts de l'équipe qui reçois est supérieur à l'équipe accueilli
                victoires += 1
            else:
                defaites += 1
        elif match[2] == equipe:  # Vérifie que l'équipe donnée est l'equipe qui est accueilli
            if match[3] == match[4]:  # Vérifie si le match est nul
                nuls += 1
            elif match[3] < match[4]:  # Vérifie que le nombre de buts de l'équipe qui est accueilli est supérieur à l'équipe reçois
                victoires += 1
            else:
                defaites += 1
    return (victoires, nuls, defaites)


def plus_gros_scores(liste_matchs):
    """retourne la liste des matchs pour lesquels l'écart de buts entre le vainqueur et le perdant est le plus grand

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des matchs avec le plus grand écart entre vainqueur et perdant
    """
    liste_gros_scores = []
    gros_score = 0
    for match in liste_matchs:
        if match[3] != match[4]:
            if match[3] > match[4]:  # Permet de connaître le score du match
                score = match[3] - match[4]
            else:
                score = match[4] - match[3]
            if score > gros_score:  # test si le score du match est plus gros que le plus gros score acutel
                liste_gros_scores = [match]
                gros_score = score
            elif score == gros_score:  # Si le score du match actuel est égal au plus gros score, alors on l'ajoute à la liste des plus gros scores
                liste_gros_scores.append(match)
    return liste_gros_scores


def liste_equipes(liste_matchs):
    """retourne la liste des équipes qui ont participé aux matchs de la liste
    Attention on ne veut voir apparaitre le nom de chaque équipe qu'une seule fois

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: une liste de str contenant le noms des équipes ayant jouer des matchs
    """
    liste_equipes = []
    for match in liste_matchs:
        if match[1] not in liste_equipes:
            liste_equipes.append(match[1])
        if match[2] not in liste_equipes:
            liste_equipes.append(match[2])
    return liste_equipes


def premiere_victoire(liste_matchs, equipe):
    """retourne la date de la première victoire de l'equipe. Si l'equipe n'a jamais gagné de match on retourne None

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        str: la date de la première victoire de l'equipe, None si l'équipe n'a gagné aucun match
    """
    for match in liste_matchs:
        gagnant = equipe_gagnante(match)
        if gagnant == equipe:
            return match[0]
    return None


def matchs_equipe(liste_matchs, equipe):
    """renvoie la liste des matchs auquels une équipe à participer

    Args:
        liste_matchs (list): liste de matchs
        equipe (str): nom d'une équipe

    Returns:
        list: liste de matchs auquels l'équipe à participer
    """    
    liste_matchs_equipe = []
    for match in liste_matchs:
        if match[1] == equipe or match[2] == equipe:
            liste_matchs_equipe.append(match)
    return liste_matchs_equipe


def nb_matchs_sans_defaites(liste_matchs, equipe):
    """retourne le plus grand nombre de matchs consécutifs sans défaite pour une equipe donnée.

    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        int: le plus grand nombre de matchs consécutifs sans défaite du pays nom_pays
    """
    liste_matchs_equipe = matchs_equipe(liste_matchs, equipe)
    victory_streak = 0
    best_victory_streak = 0
    for match in liste_matchs_equipe:
        gagnant = equipe_gagnante(match)
        if gagnant == equipe or gagnant is None:
            victory_streak += 1
        else:
            if victory_streak > best_victory_streak:
                best_victory_streak = victory_streak
                victory_streak = 0
    if victory_streak > best_victory_streak:
        best_victory_streak = victory_streak
    return best_victory_streak


def charger_matchs(nom_fichier):
    """charge un fichier de matchs donné au format CSV en une liste de matchs

    Args:
        nom_fichier (str): nom du fichier CSV contenant les matchs

    Returns:
        list: la liste des matchs du fichier
    """
    fichier = open(nom_fichier, "r")
    fichier.readline()
    liste_matchs = []
    for ligne in fichier:
        champ = ligne.split(",")
        champ[8] = champ[8] == "True"
        match = (champ[0], champ[1], champ[2], int(champ[3]), int(champ[4]), champ[5], champ[6], champ[7], champ[8])
        liste_matchs.append(match)
    fichier.close()
    return liste_matchs


def sauver_matchs(liste_matchs,nom_fichier):
    """sauvegarde dans un fichier au format CSV une liste de matchs

    Args:
        liste_matchs (list): la liste des matchs à sauvegarder
        nom_fichier (str): nom du fichier CSV

    Returns:
        None: cette fonction ne retourne rien
    """
    fichier = open(nom_fichier, "w")
    fichier.write("date,home_team,away_team,home_score,away_score,tournament,city,country,neutral\n")
    for match in liste_matchs:
        ligne = match[0] + "," + match[1] + "," + match[2] + "," + str(match[3]) + "," + str(match[4]) + "," + match[5] + "," + match[6] + "," + match[7] + "," + str(match[8]) + "\n"
        fichier.write(ligne)
    fichier.close()


# Fonctions à implémenter dont il faut également implémenter les tests


def plus_victoires_que_defaites(liste_matchs, equipe):
    """vérifie si une équipe donnée a obtenu plus de victoires que de défaites
    Args:
        liste_matchs (list): une liste de matchs
        equipe (str): le nom d'une équipe (pays)

    Returns:
        bool: True si l'equipe a obtenu plus de victoires que de défaites
    """
    resultats = resultats_equipe(liste_matchs, equipe)
    return resultats[0] > resultats[2] #  resultats[0] = nombre de victoires et resultats[2] = nombre de défaites


def matchs_spectaculaires(liste_matchs):
    """retourne la liste des matchs les plus spectaculaires, c'est à dire les
    matchs dont le nombre total de buts marqués est le plus grand

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des matchs les plus spectaculaires
    """
    liste_spectaculaires = []
    nb_buts_max = 0
    for match in liste_matchs:
        nb_buts = nb_buts_marques(match)
        if nb_buts > nb_buts_max:
            liste_spectaculaires = [match]
            nb_buts_max = nb_buts
        elif nb_buts == nb_buts_max:
            liste_spectaculaires.append(match)
    return liste_spectaculaires


def meilleures_equipes(liste_matchs):
    """retourne la liste des équipes de la liste qui ont le plus petit nombre de defaites

    Args:
        liste_matchs (list): une liste de matchs

    Returns:
        list: la liste des équipes qui ont le plus petit nombre de defaites
    """
    liste_des_equipes = liste_equipes(liste_matchs)
    liste_defaites = []
    for equipe in liste_des_equipes:
        resultats = resultats_equipe(liste_matchs, equipe)
        liste_defaites.append(resultats[2])
    liste_mini_defaites = []
    nb_defaites_mini = liste_defaites[0]
    for indice in range(len(liste_defaites)):
        nb_defaites = liste_defaites[indice]
        equipe = liste_des_equipes[indice]
        if nb_defaites == nb_defaites_mini:
            liste_mini_defaites.append(equipe)
        elif nb_defaites < nb_defaites_mini:
            liste_mini_defaites = [equipe]
            nb_defaites_mini = nb_defaites
    return liste_mini_defaites
