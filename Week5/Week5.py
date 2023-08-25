# Write a python program create csv file student.csv(sid,sname,city,contact) using 10 records 
##(in which 5 records input directly and 5 records take input from user). write records into this file.

import csv
p=open('E:\\22BCA245\\student3.csv','w',newline='')
w=csv.writer(p)
header=['sid','sname','city','contact']
w.writerow(header)

#five records input directly.
rows=[[1,'OM','Surat',7835657845],[2,'Sai','Rajasthan',9456745612],[3,'Ram','Mumbai',7465645345],[4,'Amit','Chalthan',5675548454],[5,'Radha','Mp',5464384545]]
w.writerows(rows)

#five records taken input from user. 
l=[]
for i in range(5):
    k=int(input("Enter student id:"))
    i=input("Enter student name:")
    n=input("Enter city:")
    g=int(input("Enter contact number:"))
    list=[k,i,n,g]
    l.append(list)
w.writerows(l)
p.close()

#Read this file using csv module and print it. 
from csv import DictReader
with open('E:\\22BCA245\\student3.csv','r',newline='')as x:
    a=DictReader(x)
    for row in a:
         print(row)
