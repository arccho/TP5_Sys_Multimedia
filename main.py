from prediction import prediction

if __name__ == "__main__":
    # print(prs.readdata('ml-100k/u.data', 943, 1682))
    basicPred = prediction('ml-100k/u.data', 943, 1682)
    basicPred.genMoyenneVotes()
