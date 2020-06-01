rd = []
with open ('mis/tcp2.txt' ,'r') as f :
    for i in range(119):
        x = f.readline().split(" ")
        print (str(i)+'--'+x[0])
        if x[0] not in rd :
            rd.append(x[0])
        next

with open ('mis/tcp.txt' ,'r') as f :
    for i in range(119):
        x = f.readline().split(" ")
        print (str(i)+'--'+x[0])
        if x[0] not in rd :
            rd.append(x[0])
        next

with open ('25-5.txt' ,'r') as f :
    for i in range(119):
        x = f.readline().split(" ")
        print (str(i)+'--'+x[0])
        if x[0] not in rd :
            rd.append(x[0])
        next

with open ('ip_nc_25.txt','a') as fw :
    for i in rd:
        fw.write(i+'\n')       
