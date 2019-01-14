import numpy
import math
import random

def	readdata(file,nbuser,nbfilm):
    res = numpy.ones((nbuser,	nbfilm))
    res = res*-1

    fichier = open(file,	'rU')
    lignes = fichier.readlines()

    cumul = 0
    i = 0
    #	lecture	ligne	a	ligne
    for line in lignes:
        # print(line)
        lineSplit = line.split("\t")
        userid = int(lineSplit[0]) - 1
        filmid = int(lineSplit[1]) - 1
        score = int(lineSplit[2])
        cumul = cumul +score
        i += 1
        # print(str(userid)+"	"+str(filmid)+"	"+str(score))
        res[userid, filmid] = score
    return cumul/i, res

# RMSE random
def calc_rmse_predi_random(nbuser, nbvote, nbfilm, matrice):

    sum_score = 0
    for index_user in range(0, nbuser):
        for index_film in range(0, nbfilm):
            score = matrice[index_user][index_film]
            if score > -1:
                score_random = (random.random() * 4) + 1
                sum_score += pow((score - score_random), 2)
    return math.sqrt(sum_score/ nbvote)

def calc_rmse_predict_basique(moy_notes, nbuser, nbvote, nbfilm, matrice):
    bu = list()
    bi = list()
    Vue_film = numpy.zeros(nbfilm)
    Vue_user = numpy.zeros(nbuser)
    for index_film in range(0, nbfilm):
        nb_vue = 0
        for index_user in range(0, nbuser):
            score = matrice[index_user][index_film]
            if score > -1:
                nb_vue += 1
        Vue_film[index_film] = nb_vue
    #numpy.set_printoptions(threshold=numpy.nan)
    #print(Vue_film)
    for index_user in range(0, nbuser):
        nb_vue = 0
        for index_film in range(0, nbfilm):
            score = matrice[index_user][index_film]
            if score > -1:
                nb_vue += 1
        Vue_user[index_user] = nb_vue

    #######################################

    for index_user in range(0, nbuser):
        sum_rui = 0
        for index_film in range(0, nbfilm):
            score = matrice[index_user][index_film]
            if score > -1:
                sum_rui += score

        bu.append((sum_rui / Vue_user[index_user]) - moy_notes)

    for index_film in range(0, nbfilm):
        sum_rui = 0
        for index_user in range(0, nbuser):
            score = matrice[index_user][index_film]
            if score > -1:
                sum_rui += score
        bi.append(sum_rui / Vue_film[index_film] - moy_notes)

    sum_score = 0
    for index_user in range(0, nbuser):
        for index_film in range(0, nbfilm):
            score = matrice[index_user][index_film]
            if score > -1:
                score_basique = moy_notes + bu[index_user] + bi[index_film]
                sum_score += pow((score - score_basique), 2)
    return math.sqrt(sum_score/ nbvote)

def calc_rmse_predict_voisin(moy_notes, nbuser, nbvote, nbfilm, matrice):
    bu = list()
    bi = list()

    Vue_film = numpy.zeros(nbfilm)
    Vue_user = numpy.zeros(nbuser)
    matR = numpy.zeros((nbuser, nbfilm))

    for index_film in range(0, nbfilm):
        nb_vue = 0
        for index_user in range(0, nbuser):
            score = matrice[index_user][index_film]
            if score > -1:
                nb_vue += 1
        Vue_film[index_film] = nb_vue
    #numpy.set_printoptions(threshold=numpy.nan)
    #print(Vue_film)
    for index_user in range(0, nbuser):
        nb_vue = 0
        for index_film in range(0, nbfilm):
            score = matrice[index_user][index_film]
            if score > -1:
                nb_vue += 1
        Vue_user[index_user] = nb_vue

    #######################################

    for index_user in range(0, nbuser):
        sum_rui = 0
        for index_film in range(0, nbfilm):
            score = matrice[index_user][index_film]
            if score > -1:
                sum_rui += score

        bu.append((sum_rui / Vue_user[index_user]) - moy_notes)

    for index_film in range(0, nbfilm):
        sum_rui = 0
        for index_user in range(0, nbuser):
            score = matrice[index_user][index_film]
            if score > -1:
                sum_rui += score
        bi.append(sum_rui / Vue_film[index_film] - moy_notes)


    # Remplissage de la matrice residuelle
    for i in range(0, nbuser):
        for j in range(0, nbfilm):
            if matrice[i][j] != -1:
                score = matrice[i][j] - (moy_notes + bu[i] + bi[j])
                matR[i][j] = score

    return matR



    ###################################################


    return 0

def compute_nbvote_mean(matrice,nbuser,nbfilm):
    nbvote=0
    cumul = 0

    for i in range(0,nbuser):
        for j in range(0,nbfilm):
            val=matrice[i,j]
            if val != -1:
                nbvote = nbvote+1
                cumul += val
    return nbvote, cumul/nbvote

def calc_similarite_voisinage(i, j, matriceInit, nbuser, nbfilm, mean, nbvote):
    matrice = numpy.ones(nbuser, nbfilm)

    # Remplissage de la matrice residuelle
    for i in range(0, nbuser):
        for j in range(0, nbfilm):
            if matriceInit[i][j] != -1:
                score = matriceInit[i][j] - calc_rmse_predict_basique(mean, nbuser, nbvote, nbfilm, matriceInit)
                matrice[i][j] = score

    


nbuser = 943
nbfilm = 1682
nbvote = 100000

mean, matrice_recommandation = readdata('ml-100k/u.data', nbuser, nbfilm)

print(calc_rmse_predi_random(nbuser, nbvote, nbfilm, matrice_recommandation))
print(calc_rmse_predict_basique(mean, nbuser, nbvote, nbfilm, matrice_recommandation))

print('reducing the number of element by 6')
nbuser_reduit=int(nbuser/6)
nbfilm_reduit=int(nbfilm/6)
matrice_reduit=matrice_recommandation[0:nbuser,0:nbfilm]
nbvote_reduit, mean_reduit = compute_nbvote_mean(matrice_reduit,nbuser_reduit,nbfilm_reduit)

print(calc_rmse_predict_voisin(mean_reduit, nbuser_reduit, nbvote_reduit, nbfilm_reduit, matrice_reduit))
