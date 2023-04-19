import math

input1=input("enter the 5g channel bandwith(mhz)")
input2=input("enter the subcarrier spacing :")
input3=input("enter the no mimo layer: ")

x=int(input1)*1000/int(input2)/12

numPRBs=x-4

numPRBs=math.floor(numPRBs)

print("avalable number of PRBs is :" +str(numPRBs))

dlslots =1600
throughput= 977*int(numPRBs)*int(dlslots)*int(input3)/1000/1000

print("max throughtput for this configuration is : " + str(throughput),"Mbps")
