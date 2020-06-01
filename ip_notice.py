rd=[]

with open ('ip_nc_27-5.txt' ,'r') as f :
    for i in range(250):
        x = f.readline().split(" ")
        print (str(i)+'--'+x[0])
        if x[0] not in rd :
            rd.append(x[0])
        next

# with open ('25-51.txt' ,'r') as f :
#     for i in range(250):
#         x = f.readline().split(" ")
#         print (str(i)+'--'+x[0])
#         if x[0] not in rd :
#             rd.append(x[0])
#         next

with open ('mis/ip_nc_all.txt','a') as fw :
    for i in rd:
        fw.write(i+'\n')