import time as t
import matplotlib.pyplot as plt

word = "aaa"
print("Write 5 times following word. We have three rounds:", word)
counter = 0 


osx = [1,2,3]
legend = ["1","2","3"]
osy = []


for a in range(3):
    start_time = t.time()
    print("Round:",a+1)
    for x in range(5):
        w = input("type a word->  ")
        if w != word:
            counter+=1
    print("Mistakes done:",counter)
    counter = 0
    osy.append(t.time()-start_time)
    
plt.title("Time in quick typing")
plt.plot(osx,osy)
plt.xticks(osx,legend)
plt.ylabel("Time")
plt.xlabel("Rounds")
plt.show()

