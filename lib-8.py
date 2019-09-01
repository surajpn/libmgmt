import pickle
import os
import sys
list3=[]
list4=[]
list1=[]
list2=[]



def  writestudent():
     bookno=None
     name = raw_input("\nEnter name:")
     admno=input("\nEnter admission no:")
     batch=raw_input("\nEnter batch:")
     list1=[admno,name,batch,bookno]
     list4.append(list1)
     file=open("student.pck","wb")
     pickle.dump(list4,file)
     file.close() 
     print "\n\nNew Student Record Created....."
     

     
 
def  writebook():
     bname=raw_input("\nEnter book name:")
     bno=input("\nEnter book no:")
     bauthor=raw_input("\nEnter book author:")
     fil=open("book.pck","wb")
     list2=[bno,bname,bauthor]
     list3.append(list2)
     pickle.dump(list3,fil)
     fil.close()
     print "\n\nNew Book Record Created....."

def showstudents():
     fil=open("student.pck","rb")
     x=pickle.load(fil)
     l=len(x)
     i=0
     print"\n\t\tAdmno.","\t\tNAME."
     while i<l:
      
      print"\n\t\t",x[i][0],"\t\t",x[i][1]
      i=i+1 
     fil.close()


def showbooks():
     file1=open("book.pck","rb")
     x=pickle.load(file1)
     l=len(x)
     i=0
     print"\n\t\tBookNo.\t\tBookName."
     while i<l:
      
      print"\n\t\t",x[i][0],"\t\t",x[i][1]
      i=i+1 
     file1.close()



def  withdraw():
     no=input("\nEnter book no:")
     ano=input("\nEnter admission no of student:")
     ch=0 
     file=open("student.pck","rb")
     x=pickle.load(file)
     n=len(x)
     i=0
     file1=open("test.pck","wb")
     for i in range(0,n):   
        
           if x[i][0]==ano:
            x[i][3]=no
            pickle.dump(x,file1)
           
            print"\n\n\t\tBook Withdrawed......"
            break
           
            
           else:    
            i=i+1
     
     file.close()
     file1.close()
     os.remove("student.pck")
     os.rename("test.pck","student.pck")

def  returnbook():
     ano=input("\nEnter Admission No:")
     file=open("student.pck","rb")
     y=pickle.load(file)
     i=0
     n=len(y)
     file2=open("test.pck","wb")
     for i in range(0,n):   
        
           if y[i][0]==ano:
            y[i][3]=None
            pickle.dump(y,file2)
            print"\n\n\tBook Returned Successfully...."
            break
           
            
           else:    
            i=i+1
     
     file.close()
     file2.close()
     os.remove("student.pck")
     os.rename("test.pck","student.pck")

os.system('clear')
p=input("\n\n\t\t\t ENTER PASSWORD....: ")
file5=open("password.pck","rb")
password=pickle.load(file5) 
if p==password:    
 ch='y'
 while ch=='y':
  os.system('clear')
  print"\n\n\t\t\tM A I N M E N U "
  print"\n\t\t1.ADD STUDENT\n\t\t2.ADD BOOK\n\t\t3.WITHDRAW BOOK\n\t\t4.RETURN BOOK\n\t\t5.DISPLAY STUDENTS RECORD\n\t\t6.DISPLAY BOOK RECORD\n\t\t7.EXIT"
  choice=input("\nEnter choice:")

  if   choice==1:
        writestudent()
  elif choice==2:
        writebook()
  elif choice==3:
        withdraw()
  elif choice==4:
        returnbook()
  elif choice==5:
     showstudents()
  elif choice==6:
     showbooks()
  elif choice==7:
     sys.exit()
 
  else :
     print"\nWRONG CHOICE......"
  ch=raw_input("\nContinue(y/n) :")
else:
 print"\n\n\n\n\n\t\t\tThe Password Entered is incorrect....."
