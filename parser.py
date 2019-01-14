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

def calc_rmse_predict_basique(moy_notes, nbuser, nbfilm, matrice):

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

    sum_score = 0
    for index_user in range(0, nbuser):
        for index_film in range(0, nbfilm):

            sum_rui = 0
            # calcul bu
            for index in range(0, nbfilm):
                score = matrice[index_user][index]
                if score > -1:
                    sum_rui += score
            bu = (sum_rui/Vue_user[index_user]) - moy_notes

            sum_rui = 0
            # calcul bi
            for index in range(0, nbuser):
                score = matrice[index][index_film]
                if score > -1:
                    sum_rui += score
            bi = (sum_rui/Vue_film[index_film]) - moy_notes






nbuser = 943
nbfilm = 1682
nbvote = 100000

mean, matrice_recommandation = readdata('ml-100k/u.data', nbuser, nbfilm)

print(calc_rmse_predi_random(nbuser, nbvote, nbfilm, matrice_recommandation))
calc_rmse_predict_basique(mean, nbuser, nbfilm, matrice_recommandation)
