import csv
from csv import DictReader
from numpy import *

def splitSets(set):
    random.shuffle(set)
    learn_boundary = int(set.shape[0] * 3 / 4)
    return set[:learn_boundary, :], set[learn_boundary:, :]

def loadRatingsMat():
    ratings = loadtxt("ratings.csv", delimiter=";")
    return ratings[:, 1:], ratings.shape[1] - 1

def get_x_y(i, set):
    mask = array(set.shape[1] * [True])
    mask[i] = False
    return set[:, mask], set[:, i]

def loadRatingsAvg(include):
    a = loadRatings()
    ratings = []
    movies = loadMovies()
    i, c = 0,0
    for id, rating in a.items():
        i +=1
        if (include or rating["count"] > 30):
            c+=1
            ratings.append([double(rating["sum"] / rating["count"]), movies[id], rating["count"]])
    if c != 0: print(i,c,i/c)
    return ratings

def loadRatings():
    reader = DictReader(open("ratings.csv", "rt", encoding="utf-8"))
    a = dict()
    for row in reader:
        id = row["movieId"]
        if id in a:
            a[id]["sum"] += float(row["rating"])
            a[id]["count"] += 1
        else:
            a[id] = dict()
            a[id]["sum"] = float(row["rating"])
            a[id]["count"] = 1
    return a

def loadMovies():
    reader = DictReader(open("movies.csv", "rt", encoding="utf-8"))
    movies = dict()
    for row in reader:
        movies[row["movieId"]] = row["title"]
    return movies

def sort(a, col):
    a.sort(key=lambda x: x[col])
    return a[::-1]

def format(x, none_val, decimal_point = None):
    if x is None: return none_val
    if decimal_point is None: return x
    else: return str(x).replace(".",decimal_point)

def write(file, data, none_val, header=None, decimal_point=None):
    with open(file, 'w', newline="\n") as out:
        csv_out = csv.writer(out, delimiter=';')
        if header is not None:
            csv_out.writerow(header)
        for row in data:
            csv_out.writerow(list(format(x,none_val,decimal_point) for x in row))