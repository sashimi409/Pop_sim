import random
population = [[0 for col in range(7)] for row in range(0)]
job = ["forager", "waterer", "builder"]

class check:
        def job(self):
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
         
        def sex(self):
                female = 0
                male = 0
                for i in range(0,len(population)):
                        if population[i][6] == 0:
                                female += 1
                        elif population[i][6] == 1:
                                male += 1
                return [female, male]

        def home(self):                
                housed=0
                for i in range(0,len(population)):
                        if population[i][4] == 1:
                                housed+=1
                return housed

def generatepop(tag):
        s = random.randint(0, 1)    
        a = random.randint(15,45)
        h = 0
        t = 0
        d = random.randint(0,1)
        j = random.randint(0, len(job)-1)
        e = 0

        person = [tag, a, h, t, d, j, s, e]
        return person

def generatelast(tag):
  s = random.randint(0,1)
  j = random.randint(0,len(job)-1)
  if check().sex()[1] == 0:
        s = 1
  if check().sex()[0] == 0:
        s = 0
  if check().job()[0] == 0:
        j = 0
  if check().job()[1] == 0:
        j = 1
  if check().job()[2] == 0:
        j = 2
  a = random.randint(15,45)
  h = 0
  t = 0
  d = 0
  e = 0
 
  person = [tag, a, h, t, d, j, s, e]
  return person
         
popnum = random.randint(5, 20)
for i in range(0,popnum-2):
  population.append(generatepop(i))
population.append(generatelast(popnum-2))
population.append(generatelast(popnum-1))

print "Total population:", popnum
print "There is/are ",  check().job()[0], " forager(s)."
print "There is/are ", check().job()[1], " waterer(s)."
print "There is/are ", check().sex()[1], " male(s)."
print "There is/are ", check().sex()[0], "female(s)."

biomes = ["regular", "snow", "desert"]
b = random.randint(0, 4)
if b >=3:

        b = 0
print "Biome is", biomes[b]


if biomes[b] == "snow":

        print "Watch out, it's cold!"
elif biomes[b] == "desert":

        print "Watch out, it's hot!"

class stock():
        foodstock = 0
        waterstock = 0
        domecilestock = 4
        
def forage():
        f=check().job()[0]
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

def water():
        w=check().job()[1]
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

def shelter():
        x=check().job()[2]
        if x==0:
            pass
        i = 0
        while i < x:
                stock.domecilestock += .5
                i+=1

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
                if stock.domecilestock > check.home:
                        if population[i][4] == 1:
                            population[i][4] = 0
                i+=1
        print "Water stock is:", stock.waterstock
        print "Food stock is:", stock.foodstock
        print "Domecile stock is:", stock.domecilestock
extday = 0

def kill():
        f=0
        w=0
        d=0
        i = 0
        while f in range(0,len(population)):
                if population[f][2] >= 10:
                        print population[f][0], "died: hunger."
                        del population[f]
                else:
                        f+=1
        while w in range(0,len(population)):
                if population[w][3] >= 5:
                        print population[w][0], "died: thirst."
                        del population[w]
                else:
                        w+=1
        if i >= 10:
                while d in range(0,len(population)):
                        if population[d][4] == 1:
                                print "person ", population[d][0], " has died from the elements."
                                del population[d]
                        else:
                                d+=1
        i += 1


def aging():
    for i in range(0,len(population)):
        population[i][1]+=1

class day():
        day=1
        while len(population)>0:
                print "Day ", day
                forage()
                water()
                shelter()
                live()
                kill()
                aging()
                day +=1
                print "Pop size: ", len(population), ".       ", check().job()[0], " foragers", ". ", check().job()[1], " waterers", ". ", check().job()[2], " builders"
    

day()
print "The population died on day:", day().day-1

asdf = raw_input("Press any key to exit.")

