import numpy

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
