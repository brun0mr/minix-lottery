import subprocess
import matplotlib.pyplot as plt

numProc = 4
numIo = 10000
numCpu = 1000000

lista = [[],[],[],[]]


for i in range(100):

    useless_cat_call = subprocess.Popen(["./test", str(numProc), str(numIo), str(numCpu)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, errors = useless_cat_call.communicate()
    useless_cat_call.wait()

    #print(errors)
    resultado = output.split()

    lista[0].append(float(resultado[2]))
    lista[1].append(float(resultado[5]))
    lista[2].append(float(resultado[8]))
    lista[3].append(float(resultado[11]))


print(lista[2])
print(min(lista[2]) , " " , max(lista[2]))

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(lista[0], color='magenta', marker='o',mfc='pink' )
#plot1.xticks(range(0,len(lista[0])+1, 1))
axs[0, 0].set_ylabel('tempo(ms)') #set the label for y axis
#axs[0, 0].set_xlabel('index') #set the label for x-axis
axs[0, 0].set_title("CPU 3") #set the title of the graph


axs[0, 1].plot(lista[1], color='magenta', marker='o',mfc='pink' )
#plot2.xticks(range(0,len(lista[1])+1, 1))
axs[0, 1].set_ylabel('tempo(ms)') #set the label for y axis
#axs[0, 1].set_xlabel('index') #set the label for x-axis
axs[0, 1].set_title("CPU 1") #set the title of the graph


axs[1, 0].plot(lista[2], color='magenta', marker='o',mfc='pink' )
#plot3.xticks(range(0,len(lista[2])+1, 1))
axs[1, 0].set_ylabel('tempo(ms)') #set the label for y axis
#axs[1, 0].set_xlabel('index') #set the label for x-axis
axs[1, 0].set_title("IO 0") #set the title of the graph


axs[1, 1].plot(lista[3], color='magenta', marker='o',mfc='pink' )
#plot3.xticks(range(0,len(lista[3])+1, 1))
axs[1, 1].set_ylabel('tempo(ms)') #set the label for y axis
#axs[1, 1].set_xlabel('index') #set the label for x-axis
axs[1, 1].set_title("IO 2") #set the title of the graph

for ax in axs.flat:
    ax.label_outer()

plt.show() #display the graph
plt.savefig("grafico.png")
