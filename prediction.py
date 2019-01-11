from parser import readdata

class prediction:
    def __init__(self, file, nbUsers, nbFilms):
        self.r = 0
        self.N = nbUsers
        self.M = nbFilms
        self.moyVotes = 0

        self.res = readdata(file, self.N, self.M)
        print(self.res)


    def genMoyenneVotes(self):
        moyenne = 0
        nbValues = 0

        for boucleY in range (0, self.N):
            for boucleX in range (0, self.M):
                value = self.res[boucleX, boucleY]

                if value is not -1:
                    moyenne = value
                    nbValues += 1

        self.moyNotes = moyenne / nbValues
        print(self.moyNotes)


