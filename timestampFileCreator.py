from datetime import datetime
currenttime=datetime.now()
timestamp = currenttime.strftime("%Y-%m-%d_%H%M%S")
FILE_NAME=("topmovies-"+timestamp)



topMovies = open(FILE_NAME,"w+")
num=5
for i in range(1, 11):
    print(num, 'x', i, '=', num*i,file=topMovies)
topMovies.close