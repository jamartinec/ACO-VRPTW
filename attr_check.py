from funs import *

dataM=readData('Input/solomon_r101.txt')
distM=createDistanceMatrix(dataM)


curr_time=0
curr_pos=27
phi=0.00053

next_item_interest=81

feasable=[]
for loc in range(len(dataM)):
    if curr_time+distM[curr_pos][loc]<=dataM[loc]['due_time'] and loc != curr_pos:
        feasable.append(loc)


txtFile=open('Output/attr_test.txt','w')
txtFile.write('attrFirst')
txtFile.write('\t')
txtFile.write('attr0')
txtFile.write('\t')
txtFile.write('phi')
txtFile.write('\n')    

aDict={}
for feasLoc in feasable:
    distanceToFeasLoc=distM[curr_pos][feasLoc]
    feasLocReadyTime=dataM[feasLoc]['ready_time']
    feasLocDueTime=dataM[feasLoc]['due_time']
    delivery_time=max(curr_time+distanceToFeasLoc,feasLocReadyTime)
    delta_time=delivery_time-curr_time
    attr0=1./(delta_time*(feasLocDueTime-curr_time))
    aDict[feasLoc]=attr0*phi
    
    txtFile.write(str((delta_time*(feasLocDueTime-curr_time))))
    txtFile.write('\t')
    txtFile.write(str(attr0))
    txtFile.write('\t')
    txtFile.write(str(phi))
    txtFile.write('\n')

txtFile.close()

amin=min(aDict.values())

aDict2={}
for item in aDict:
    aDict2[item]=int(aDict[item]/amin)**2





for item in aDict2:
    
    if item==next_item_interest:
        print('*****************')

    print(item,'\tattr:\t',aDict2[item],'\tready t\t',dataM[item]['ready_time'],'\tdist\t',distM[curr_pos][item])

    if item==next_item_interest:
        print('*****************')

print('****')
print('dist to', next_item_interest,'is',distM[curr_pos][next_item_interest])

