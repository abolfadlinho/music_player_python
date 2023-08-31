import random
alldatalist = ["all1","all2","all3","all4","all5", "all6", "all7"]
allalbumslist = ["album1","album2","album3","album4","album5", "album6"]
allartistslist = ["artist1","artist2","artist3","artist4"]
allplaylistslist = ["playlist1","playlist2","playlist3"]
orderedplayed = []
randomplayed = []
previousindex = -1
previousrandomindex = -1


def orderedplayalldata(previousindex):
    print("Ordered element:",alldatalist[previousindex+1])
    orderedplayed.append(alldatalist[previousindex+1])
    if (len(orderedplayed) % len(alldatalist)) == 0:
        previousindex = -1
    else:
        previousindex = previousindex + 1
    return previousindex


def randomplayalldata(randomplayed):
    randomindex = random.randint(0,len(alldatalist)-1)
    while alldatalist[randomindex] in randomplayed:
        randomindex = random.randint(0,len(alldatalist)-1)
    randomplayed.append(alldatalist[randomindex])
    if len(randomplayed) == len(alldatalist):
        lastelement = randomplayed[-1]
        randomplayed = []
        randomplayed.append(lastelement)
    print("Random element:", alldatalist[randomindex])
    return randomplayed


def orderedplayalbums(previousindex):
    print("Ordered element:", allalbumslist[previousindex + 1])
    orderedplayed.append(allalbumslist[previousindex + 1])
    if (len(orderedplayed) % len(allalbumslist)) == 0:
        previousindex = -1
    else:
        previousindex = previousindex + 1
    return previousindex


def randomplayalbums(randomplayed):
    randomindex = random.randint(0, len(allalbumslist) - 1)
    while allalbumslist[randomindex] in randomplayed:
        randomindex = random.randint(0, len(allalbumslist) - 1)
    randomplayed.append(allalbumslist[randomindex])
    if len(randomplayed) == len(allalbumslist):
        lastelement = randomplayed[-1]
        randomplayed = []
        randomplayed.append(lastelement)
    print("Random element:", allalbumslist[randomindex])
    return randomplayed


def orderedplayartists(previousindex):
    print("Ordered element:", allartistslist[previousindex + 1])
    orderedplayed.append(allartistslist[previousindex + 1])
    if (len(orderedplayed) % len(allartistslist)) == 0:
        previousindex = -1
    else:
        previousindex = previousindex + 1
    return previousindex


def randomplayartists(randomplayed):
    randomindex = random.randint(0, len(allartistslist) - 1)
    while allartistslist[randomindex] in randomplayed:
        randomindex = random.randint(0, len(allartistslist) - 1)
    randomplayed.append(allartistslist[randomindex])
    if len(randomplayed) == len(allartistslist):
        lastelement = randomplayed[-1]
        randomplayed = []
        randomplayed.append(lastelement)
    print("Random element:", allartistslist[randomindex])
    return randomplayed


def orderedplayplaylists(previousindex):
    print("Ordered element:", allplaylistslist[previousindex + 1])
    orderedplayed.append(allplaylistslist[previousindex + 1])
    if (len(orderedplayed) % len(allplaylistslist)) == 0:
        previousindex = -1
    else:
        previousindex = previousindex + 1
    return previousindex


def randomplayplaylists(randomplayed):
    randomindex = random.randint(0, len(allplaylistslist) - 1)
    while allplaylistslist[randomindex] in randomplayed:
        randomindex = random.randint(0, len(allplaylistslist) - 1)
    randomplayed.append(allplaylistslist[randomindex])
    if len(randomplayed) == len(allplaylistslist):
        lastelement = randomplayed[-1]
        randomplayed = []
        randomplayed.append(lastelement)
    print("Random element:", allplaylistslist[randomindex])
    return randomplayed


for i in range(len(allplaylistslist)):
    randomplayed = randomplayplaylists(randomplayed)
    previousindex = orderedplayplaylists(previousindex)
    print(randomplayed)
    print(orderedplayed)