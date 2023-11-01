#K-Means
import random
n=int(input("Enter Number Of Observations="))
obs=[]
print("\nEnter the Observations:-")
for i in range(n):
    x = int(input("Number "+str(i+1)+"="))
    obs.append(x)
obs.sort()
print("\nObservations=",obs)
k=int(input("\nEnter The Number Of Clusters="))
m=[]
#Finding mean
while len(m) < k:
    x = obs[random.randint(0,n-1)]
    if x not in m:
        m.append(x)    
print("\nInitial Mean=",m)
#Initialising CLuster
c={i:[] for i in range(k)}
m_extra=[]
#Appending to the cluster
for i in range(n):
    m_extra.clear()
    for j in range(k):
        m_extra.append(abs(obs[i] - m[j]))
#Print(m_extra)
    min_val = min(m_extra)
    index = m_extra.index(min_val)
    c[index].append(obs[i])
print("Initial Cluster=",c)
#Finding new mean from cluster
m_new = []
for i in range(k):
    mean = sum(c[i]) // len(c[i])
    m_new.append(mean)

while m != m_new:
    c = {i:[] for i in range(k)}
    for i in range(n):
        m_extra.clear()
        for j in range(k):
            m_extra.append(abs(obs[i] - m_new[j]))
#Print(m_extra)
        min_val = min(m_extra)
        index = m_extra.index(min_val)
        c[index].append(obs[i])   

    print("\nUpdated Mean=",m_new)
    print("Updated Cluster=",c)
#Finding mean
    m.clear()
    m = m_new
    m_new.clear()
    for i in range(k):
        mean = sum(c[i]) // len(c[i])
        m_new.append(mean)  
#Print("test :",m_new,m)
print("\nFinal Mean=",m)
print("Final Cluster=",c)
   
