import sqlite3
import random

conn = sqlite3.connect('Movie.db')
c = conn.cursor()
Id = 7

def create_movie_table():
    c.execute('CREATE TABLE IF NOT EXISTS movie(name VARCHAR(100) not null, '
              'budget INTEGER, year INTEGER, Duration TIME, Rating VARCHAR(20), Genre VARCHAR(100), Id INTEGER UNIQUE NOT NULL,language VARCHAR(100))')

def create_person_table():
     c.execute('CREATE TABLE IF NOT EXISTS person(name CHAR(100), birthday DATE, id INTEGER UNIQUE)')

def create_distributor_table():
     c.execute('CREATE TABLE IF NOT EXISTS distributor(name CHAR(20), id INTEGER, address varchar(100))')

def create_award_table():
    c.execute('CREATE TABLE IF NOT EXISTS Award(awardType varchar(90),'
              'awardTitle varchar(90), year SMALLINT check(year>1800),'
              'awardeeId INTEGER NOT NULL, movieId   INTEGER,'
              'foreign key(awardeeId) references Person(personId)'
              'on delete no action deferrable initially deferred,' 
              'foreign key(movieId) references Movie(movieId) on delete no action '
              'deferrable initially deferred, primary key(awardType,awardTitle,year))')

def create_distribution_table():
    c.execute("CREATE TABLE IF NOT EXISTS distribution("
               "distributor INTEGER, movie INTEGER,"
               "foreign key(distributor) references distributor(distributerId) deferrable initially deferred,"
               "PRIMARY KEY(distributor,movie),"
               "foreign key(movie) references movie(movieId) deferrable initially deferred )")
    
def create_crew_table():
    c.execute("CREATE TABLE IF NOT EXISTS Crew(crewId INTEGER NOT NULL, isActor INTEGER,"
              "isProducer INTEGER, isDirector INTEGER,"
              "movieCreated INTEGER NOT NULL, foreign key (crewId) references Person(id) "
              "on update cascade on delete no action deferrable initially deferred, foreign key (movieCreated) references Movie(Id)"
              "on update cascade on delete no action deferrable initially deferred, CHECK( (isProducer = 1 OR isDirector = 1 OR isActor = 1)), primary key(crewId,movieCreated));")

def create_awards_set():
    c.execute("INSERT INTO Award(awardType, awardTitle,year,awardeeId,movieId) VALUES (?,?,?,?,?)",
                  ("Oscar","Best Actor in a Leading Role",1995,8,3)) #freeman shawshank
    c.execute("INSERT INTO Award(awardType, awardTitle,year,awardeeId,movieId) VALUES (?,?,?,?,?)",
                  ("Golden Globes","Best Performance by an Actor in a Motion Picture- Drama",1995,8,3)) #freeman shawshank
    c.execute("INSERT INTO Award(awardType, awardTitle,year,awardeeId,movieId) VALUES (?,?,?,?,?)",
                  ("Dallas-Fort Worth Film Critics Association Awards","Best Actor",1995,8,3)) #freeman shawshank
    c.execute("INSERT INTO Award(awardType, awardTitle,year,awardeeId,movieId) VALUES (?,?,?,?,?)",
                  ("Oscar","Best Writing, Screenplay Based on Material Previously Produced",1995,7,3)) #frank shawshank
    c.execute("INSERT INTO Award(awardType, awardTitle,year,awardeeId,movieId) VALUES (?,?,?,?,?)",
                  ("20/20","Best Director",2015,7,3)) #frank shawshank
    c.execute("INSERT INTO Award(awardType, awardTitle,year,awardeeId,movieId) VALUES (?,?,?,?,?)",
                  ("Awards Circuit Community Awards","Best Adapted Screenplay",1994,7,3)) #frank shawshank
    c.execute("INSERT INTO Award(awardType, awardTitle,year,awardeeId,movieId) VALUES (?,?,?,?,?)",
                  ("Chicago Film Critics Association Awards","Best Screenplay",1995,7,3)) #frank shawshank
    c.execute("INSERT INTO Award(awardType, awardTitle,year,awardeeId,movieId) VALUES (?,?,?,?,?)",
                  ("Directors Guild of America","Outstanding Directorial Achievement in Motion Pictures",1995,7,3)) #frank shawshank
    c.execute("INSERT INTO Award(awardType, awardTitle,year,awardeeId,movieId) VALUES (?,?,?,?,?)",
                  ("Oscar","Best Director",1995,9,4)) #robert zem in forrest gump
    c.execute("INSERT INTO Award(awardType, awardTitle,year,awardeeId,movieId) VALUES (?,?,?,?,?)",
                  ("Golden Globe","Best Director-Motion Picture",1995,9,4)) #robert zem in forrest gump
    c.execute("INSERT INTO Award(awardType, awardTitle,year,awardeeId,movieId) VALUES (?,?,?,?,?)",
                  ("Oscar","Best Actor in a leading Role",1995,10,4))#tom hanks in forrest gump
    c.execute("INSERT INTO Award(awardType, awardTitle,year,awardeeId,movieId) VALUES (?,?,?,?,?)",
                  ("Golden Globe","Best Actor",1995,9,4))
    
    
    
def create_distribution_relationship_set():
    c.execute("INSERT INTO distribution(distributor, movie) VALUES (?,?)",
                  (1,1)) #walt - incredibles
    c.execute("INSERT INTO distribution(distributor, movie) VALUES (?,?)",
                  (1,2)) #walt - ralph
    c.execute("INSERT INTO distribution(distributor, movie) VALUES (?,?)",
                  (2,3)) #bros-shaw
    c.execute("INSERT INTO distribution( distributor, movie) VALUES (?,?)",
                  (2,6)) #bros - matrix
    c.execute("INSERT INTO distribution(distributor, movie) VALUES (?,?)",
                  (2,5)) #bros - inception
    c.execute("INSERT INTO distribution(distributor, movie) VALUES (?,?)",
                  (3,4)) #paramount - gump
    c.execute("INSERT INTO distribution(distributor, movie) VALUES (?,?)",
                  (4,3))#columbia - shaw
    c.execute("INSERT INTO distribution(distributor, movie) VALUES (?,?)",
                  (5,7)) #orion - lambs
    c.execute("INSERT INTO distribution(distributor, movie) VALUES (?,?)",
                  (6,6)) #roadshow - matrix
    
    
def create_distributor_set():
    c.execute("INSERT INTO distributor(name, id, address) VALUES (?,?,?)",
                  ("Walt Disney Studios Motion Pictures",1,"500 S Buena Vista St Burbank, CA"))#incredibles,ralph breaks

    c.execute("INSERT INTO distributor(name, id, address) VALUES (?,?,?)",
                  ("Warner Bros",2,"110 Acre Burbank,CA"))  #shawshank redemption,inception,the matrix
    
    c.execute("INSERT INTO distributor(name, id, address) VALUES (?,?,?)",
                  ("Paramount Pictures",3,"5555 Melrose Ave Los Angeles, CA"))#forrest gump
    
    c.execute("INSERT INTO distributor(name, id, address) VALUES (?,?,?)",
                  ("Columbia Pictures",4,"Culver City, CA")) #shawshank

    c.execute("INSERT INTO distributor(name, id, address) VALUES (?,?,?)",
                  ("Orion Pictures",5,"Los Angeles, CA")) #silence of the lambs

    c.execute("INSERT INTO distributor(name, id, address) VALUES (?,?,?)",
                  ("Roadshow Entertainment",6,"Sydney,Austrialia")) #the matrix
    
def create_person_sets():
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Brad Bird","1957-09-24",1)) #director for incredibles 2
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("John Lasseter","1957-01-12",2)) #producer for incredibles 2
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Craig T. Nelson","1944-04-4",3)) #mr.incredibles
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Holly Hunter","1958-03-20",4)) #elastic girl, actor
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Phil Johnston","1971-10-26",5)) #actor + director for ralph breaks internet
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("John C. Reilly","1965-05-24",6)) #ralph in breaks internet, actor
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Frank Darabont","1959-01-28",7)) #director for shawshank redemption
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Morgan Freeman","1937-06-01",8))#actor in shawshank redeption
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Robert Zemeckis","1951-05-14",9))#director for forrest gump
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Tom Hanks","1956-07-09",10)) #actor in forrest gump
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Christopher Nolan","1970-07-30",11)) #director + producerfor inception
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Leonardo DiCaprio","1974-11-11",12)) #actor in inception
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Joseph Gorden-Levitt","1981-02-17",13))#actor in inception
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Lana Wachowski","1965-06-21",14)) #director +producer of the matrix
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Lilly Wachowski","1967-12-29",15))#director +producer of the matrix
    c.execute("INSERT INTO person(name, birthday, id) VALUES (?,?,?)",
                  ("Jonathan Demme","1944-02-22",16))#director for the silence of the lambs
    
    
    
def crew_table_entry():
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (1, 0,0,1,1)) #brad bird = only director of incredibles 2
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (2, 0,1,0,1)) # john lasseter producer for incredibles 2
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (3, 1,0,0,1)) #craig mr.incredibles
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (4, 1,0,0,1)) #elastic girl
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (5, 1,0,1,2)) # phil johnston - actor and director for ralph
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (6, 1,0,0,2)) # john c. actor in ralph
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (7, 0,0,1,3)) #frank director for shaw
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (8, 1,0,0,3))#morgan freeman actor in shaw
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (9, 0,0,1,4)) # robert zem. director for forrest gump
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (10, 1,0,0,4)) #actor for forrest gump
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (14, 0,1,1,6)) #lana director and producer of matrix
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (15, 0,1,1,6)) #lana director and producer of matrix
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (11, 0,1,1,5)) #christopher director + producer for inception
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (12, 1,0,0,5))#dicaprio actor for inception
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (13, 1,0,0,5))#joseph gordon-levitt actor for inception
    c.execute("INSERT INTO Crew(crewId,isActor,isProducer,isDirector,movieCreated) VALUES (?,?,?,?,?)",
                  (16, 0,0,1,7))#jonathan demme- director for silence of the lambs

    
    
    
def movie_table_entry():
    
    c.execute("INSERT INTO movie (name, budget, year,Duration,Rating,Genre,Id,language) VALUES (?,?,?,?,?,?,?,?)",
                  ("Incredibles 2", 200, 2018,'1:58','PG','Animation,Action,Adventure',1,'English')) #budget is in millions
    c.execute("INSERT INTO movie (name, budget, year,Duration,Rating,Genre,Id,language) VALUES (?,?,?,?,?,?,?,?)",
                  ("Ralph Breaks the Internet", 175, 2018,'1:52','PG','Animation,Comedy,Adventure',2,'English'))
    c.execute("INSERT INTO movie (name, budget, year,Duration,Rating,Genre,Id,language) VALUES (?,?,?,?,?,?,?,?)",
                  ("The Shawshank Redemption", 25, 1994,'2:22','R','Drama',3,'English'))
    c.execute("INSERT INTO movie (name, budget, year,Duration,Rating,Genre,Id,language) VALUES (?,?,?,?,?,?,?,?)",
                  ("Forrest Gump", 55, 1994,'2:22','PG-13','Drama,Romance',4,'English'))
    c.execute("INSERT INTO movie (name, budget, year,Duration,Rating,Genre,Id,language) VALUES (?,?,?,?,?,?,?,?)",
                  ("Inception", 55, 2010,'2:28','PG-13','Action,Adventure,Sci-Fi',5,'English'))
    c.execute("INSERT INTO movie (name, budget, year,Duration,Rating,Genre,Id,language) VALUES (?,?,?,?,?,?,?,?)",
                  ("The Matrix", 63, 1999,'2:16','R','Action,Sci-Fi',6,'English'))
    c.execute("INSERT INTO movie (name, budget, year,Duration,Rating,Genre,Id,language) VALUES (?,?,?,?,?,?,?,?)",
                  ("The Silence of the Lambs", 19, 1991,'1:58','R','Crime,Drama,Thriller',7,'English'))


def getId():
    global Id
    Id+=1
    return Id

def viewMoviesAlpha():
    c.execute('SELECT name,budget,year,Duration,Rating,Genre FROM movie ORDER BY name')
    data = c.description
    d = "";
    for i in data:
        d = d + i[0] +"\t"
    d = d + '\n'
    data = c.fetchall()

    for i in data:
        for k in range(0,len(i)):
            d = d +str(i[k]) +'\t'
        d = d +'\n'

    #print(d)
    return d

def findMoviesBy(person):
    command = "SELECT M.name,M.budget,M.year,M.rating,M.Genre,M.language FROM movie M, Crew C, person P "
    command = command + "WHERE P.name = \"" +person +"\" AND C.crewId = P.id AND C.movieCreated = M.Id"
    c.execute(command)
    data = c.description
    d = "";
    for i in data:
        d = d + i[0] +"\t"
    d = d + '\n'
    data = c.fetchall()

    for i in data:
        for k in range(0,len(i)):
            d = d +str(i[k]) +'\t'
        d = d +'\n'

    #print(d)
    return d

def selectYear(year):
    c.execute('SELECT name,budget,year,Duration,Rating,Genre FROM movie WHERE year = ?', (year,))

    data = c.description
    d = "";
    for i in data:
        d = d + i[0] +"\t"
    d = d + '\n'
    data = c.fetchall()

    for i in data:
        for k in range(0,len(i)):
            d = d +str(i[k]) +'\t'
        d = d +'\n'

    #print(d)
    return d

def findGenre(genre):
    command = "SELECT name,budget,year,Duration,Rating,Genre FROM movie WHERE Genre LIKE \"%"+ genre + "%\""
    c.execute(command)
    data = c.description
    d = "";
    for i in data:
        d = d + i[0] +"\t"
    d = d + '\n'
    data = c.fetchall()

    for i in data:
        for k in range(0,len(i)):
            d = d +str(i[k]) +'\t'
        d = d +'\n'

    #print(d)
    return d

def findPerson(name):
    command = "SELECT * FROM person WHERE name =\""+name+"\""
    c.execute(command)
    data = c.description
    d = "";
    for i in data:
        d = d + i[0] +"\t"
    d = d + '\n'
    data = c.fetchall()

    for i in data:
        for k in range(0,len(i)):
            d = d +str(i[k]) +'\t'
        d = d +'\n'

    #print(d)
    return d


    
def findMoviesDistributedBy(distributor):
    command = "SELECT M.name FROM movie M, distribution D, distributor d "
    command = command + "WHERE D.name = \"" +distributor +"\" AND D.id = d.distributor AND d.movie = M.Id"
    c.execute(command)
    data = c.description
    d = "";
    for i in data:
        d = d + i[0] +"\t"
    d = d + '\n'
    data = c.fetchall()

    for i in data:
        for k in range(0,len(i)):
            d = d +str(i[k]) +'\t'
        d = d +'\n'

    #print(d)
    return d



def everythingAboutMovie(name):
    c.execute('SELECT name,budget,year,Duration,Rating,Genre FROM movie WHERE name = ?', (name,))
    data = c.description
    d = "";
    for i in data:
        d = d + i[0] +"\t"
    d = d + '\n'
    data = c.fetchall()

    for i in data:
        for k in range(0,len(i)):
            d = d +str(i[k]) +'\t'
        d = d +'\n'

    #print(d)
    return d

def findDistributorsForMovie(movie):
    command = "SELECT d.name, d.address FROM movie M, distribution D, distributor d "
    command = command + "WHERE M.name = \"" +movie +"\" AND D.id = d.distributor AND d.movie = M.Id"
    c.execute(command)
    data = c.description
    d = "";
    for i in data:
        d = d + i[0] +"\t"
    d = d + '\n'
    data = c.fetchall()

    for i in data:
        for k in range(0,len(i)):
            d = d +str(i[k]) +'\t'
        d = d +'\n'

    #print(d)
    return d

def bothActorAndDirector():
    command = "SELECT DISTINCT P.name FROM Crew C, person P "
    command = command + "WHERE C.crewId = P.id AND C.isActor = 1 AND C.isDirector =1"
    
    c.execute(command)
    data = c.description
    d = ""
    for i in data:
        d = d + i[0] +"\t"
    d = d + '\n'
    data = c.fetchall()
    
    for i in data:
        for k in range(0,len(i)):
            d = d +str(i[k]) +'\t'
        d = d +'\n'

    #print(d)
    return d



def findCrewForMovie(movie):
    command = "SELECT P.name,P.birthday FROM movie M, Crew C, person P "
    command = command + "WHERE M.name = \"" +movie +"\" AND C.crewId = P.id AND C.movieCreated = M.Id"

    c.execute(command)
    data = c.description
    d = ""
    for i in data:
        d = d + i[0] +"\t"
    d = d + '\n'
    data = c.fetchall()
    
    for i in data:
        for k in range(0,len(i)):
            d = d +str(i[k]) +'\t'
        d = d +'\n'

    #print(d)
    return d

def findAwardsBy(person):
    command = "SELECT A.awardType, A.awardTitle, A.year, M.name FROM movie M, Award A, person P "
    command = command + "WHERE P.name = \"" +person +"\" AND A.awardeeId = P.id AND M.Id = A.movieId"
    c.execute(command)
    data = c.description
    d = "";
    for i in data:
        d = d + i[0] +"\t"
    d = d + '\n'
    data = c.fetchall()

    for i in data:
        for k in range(0,len(i)):
            d = d +str(i[k]) +'\t'
        d = d +'\n'

    #print(d)
    return d

def insertMovie(name, budget, year, Duration, Rating, Genre, language):
    statement = "SELECT name FROM movie WHERE name=\"" +name +"\" AND year=\"" +year +"\" AND budget = \"" +budget +"\""
    c.execute(statement)
    result = c.fetchall()
    if(len(result)>0):
        return False
    c.execute("INSERT INTO movie (name, budget, year,Duration,Rating,Genre,Id,language) VALUES (?,?,?,?,?,?,?,?)",
                      (name, budget, year,Duration,Rating,Genre,getId(),language)) #budget is in millions
    conn.commit()
    if(c.rowcount!=1):
        return False
    return True
    



def createTables():
    create_movie_table()
    create_person_table()
    movie_table_entry()
    create_person_sets()
    create_crew_table()
    crew_table_entry()
    create_distribution_table()
    create_distributor_table()
    create_distributor_set()
    create_distribution_relationship_set()
    create_award_table()
    create_awards_set()
    conn.commit()
 


#createTables()
#ratingOfMovie("Incredibles 2")
#everythingAboutMovie("Incredibles 2")

#findGenre("Animation")
#selectYear(2018)
#bothActorAndDirector()
#findMoviesBy("Morgan Freeman")
#findAwardsBy("Morgan Freeman")
#c.close()
#conn.close()
