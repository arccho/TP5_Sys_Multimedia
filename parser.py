import numpy
import math
import random

def	readdata(file,nbuser,nbfilm):
    res = numpy.ones((nbuser,	nbfilm))
    res = res*-1

    fichier = open(file,	'rU')
    lignes = fichier.readlines()

    #	lecture	ligne	a	ligne
    for line in lignes:
        # print(line)
        lineSplit = line.split("\t")
        userid = int(lineSplit[0]) - 1
        filmid = int(lineSplit[1]) - 1
        score = int(lineSplit[2])
        # print(str(userid)+"	"+str(filmid)+"	"+str(score))
        res[userid, filmid] = score
    return res

def predict_random(nbuser, nbfilm):
    res = numpy.zeros((nbuser, nbfilm))
    for user in range(nbuser):
        for film in range(nbfilm):
            res[user][film] = (numpy.random.random()*4)+1
    return res

# RMSE 1
def calc_rmse_predi_random(nbuser, nbvote, nbfilm, matrice):
    score_random = (random.random() * 4) + 1
    sum_core = 0
    for index_user in range(0, nbuser):
        for index_film in range(0, nbfilm):
            score = matrice[index_user][index_film]
            if score > -1:
                sum_core += pow((score - score_random), 2)
    return math.sqrt(sum_core/ nbvote)

nbuser = 943
nbfilm = 1682
nbvote = 100000

matrice_recommandation = readdata('ml-100k/u.data', nbuser, nbfilm)
matrice_predict_rand = predict_random(nbuser, nbfilm)
#print(matrice_recommandation)
#print(matrice_predict_rand)
print(calc_rmse_predi_random(nbuser, nbvote, nbfilm, matrice_recommandation))