import random
#population is a 2 dimensional array holding th avlues for each person. Not very effective, could be done better using a class.
population = [[0 for col in range(7)] for row in range(0)]
jobs = ["forager", "waterer", "builder"]

#class used incorrectly, needs to be changed

def job():
        forager = 0
        waterer = 0
        builder = 0
        for i in range(0,len(population)):
                if population[i][5] == 0:
                        forager += 1
                elif population[i][5] == 1:
                        waterer += 1
                elif population[i][5] == 2:
                        builder += 1
        return [forager, waterer, builder]
 
def sex():
        female = 0
        male = 0
        for i in range(0,len(population)):
                if population[i][6] == 0:
                        female += 1
                elif population[i][6] == 1:
                        male += 1
        return [female, male]

def home():                
        housed=0
        for i in range(0,len(population)):
                if population[i][4] == 1:
                        housed+=1
        return housed

#generates a single person in the populaiton that is not one of the last 2
def generatepop(tag):
        s = random.randint(0, 1)    
        a = random.randint(15,45)
        h = 0
        t = 0
        d = random.randint(0,1)
        j = random.randint(0, len(jobs)-1)
        e = 0

        person = [tag, a, h, t, d, j, s, e]
        return person

#generates a single person that is one of the last 2. The reason for this funciton to be seperate is bto insure that there is a male and a female, as well as having all "jobs"
def generatelast(tag):
  s = random.randint(0,1)
  j = random.randint(0,len(jobs)-1)
  #makes sure there is a male and a female
  
  if sex()[1] == 0:
        s = 1
  elif sex()[0] == 0:
        s = 0
  #makes sure that there is one of every job
        
  if job()[0] == 0:
        j = 0
  elif job()[1] == 0:
        j = 1
  elif job()[2] == 0:
        j = 2

  a = random.randint(15,45)
  h = 0
  t = 0
  d = 0
  e = 0
 
  person = [tag, a, h, t, d, j, s, e]
  return person


#set of instructions to create the initial random population and give some data about it. needs to be its own funciton.         
popnum = random.randint(5, 20)
for i in range(0,popnum-2):
  population.append(generatepop(i))
population.append(generatelast(popnum-2))
population.append(generatelast(popnum-1))

print( "Total population:", popnum)
print( "There is/are ",  job()[0], " forager(s)." )
print( "There is/are ", job()[1], " waterer(s)." )
print( "There is/are ", sex()[1], " male(s)." ) 
print( "There is/are ", sex()[0], "female(s)." )

#biomes were part of an idea that was not finished.
biomes = ["regular", "snow", "desert"]
b = random.randint(0, 4)
if b >=3:

        b = 0
print( "Biome is", biomes[b])


if biomes[b] == "snow":

        print( "Watch out, it's cold!")
elif biomes[b] == "desert":

        print( "Watch out, it's hot!" )

#class is used semi-correctly, should still be modified, would be easier with single variables.
class stock():
        foodstock = 0
        waterstock = 0
        domecilestock = 4

#determiens how much food is ofund in a "day"        
def forage():
        f=job()[0]
        if f==0:
            pass
        i = 0
        while i < f:
                pf=10 * random.random()
                if pf>=(10*(1-.29)):
                        stock.foodstock += 3
                else:
                        pass
                i += 1

#determiens how much water is found in a "day"
def water():
        w=job()[1]
        if w==0:
            pass
        i = 0
        while i < w:
                pw=random.randint(0, 10)
                if pw>=(10*(1-.6)):
                        stock.waterstock += 2
                else:
                        pass
                i+=1

#determines how man people are exposed to the elements.
def shelter():
        x=job()[2]
        if x==0:
            pass
        i = 0
        while i < x:
                stock.domecilestock += .5
                i+=1

#allocates all stocks of food and water, and deals wiht hosuing. Housing should be its own funciton.
def live():
        for i in range(0,len(population)):
                if stock.waterstock > 0:
                        stock.waterstock -= 1
                        population[i][3] = 0
                else:
                        population[i][3] += 1
                if stock.foodstock > 0:
                        stock.foodstock -= 1
                        population[i][2] = 0
                else:
                        population[i][2] += 1
                if stock.domecilestock > home():
                        if population[i][4] == 1:
                            population[i][4] = 0
                i+=1
        print( "Water stock is:", stock.waterstock )
        print( "Food stock is:", stock.foodstock )
        print( "Domecile stock is:", stock.domecilestock )

#determines if and who dies on a certain "day"
def kill():
        f=0
        w=0
        d=0
        i = 0
        while f in range(0,len(population)):
                if population[f][2] >= 10:
                        print( population[f][0], "died: hunger.")
                        del population[f]
                else:
                        f+=1
        while w in range(0,len(population)):
                if population[w][3] >= 5:
                        print( population[w][0], "died: thirst.")
                        del population[w]
                else:
                        w+=1
        if i >= 10:
                while d in range(0,len(population)):
                        if population[d][4] == 1:
                                print( "person ", population[d][0], " has died from the elements.")
                                del population[d]
                        else:
                                d+=1
        i += 1

#Ages each person by one "day", no funciton to die of old age yet
def aging():
    for i in range(0,len(population)):
        population[i][1]+=1

#incorrectly used class, needs to be revisited.
class day():
        day=1
        while len(population)>0:
                print( "Day ", day)
                forage()
                water()
                shelter()
                live()
                kill()
                aging()
                day +=1
                print( "Pop size: ", len(population), ".       ", job()[0], " foragers", ". ", job()[1], " waterers", ". ", job()[2], " builders")
    

#runs main function, needs ot be cleaned up.
day()
print( "The population died on day:", day().day-1)


