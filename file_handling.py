#NOTE BOOK FILE
def main_function():
    print("Discription of the app \n>>>use only integers(0-9) to select the options \n>>>Understand the concept")
    print("""1)for creating a new file \n2)for opening a exsisting file\n3)know about programers\n4)close program""")
    while(1):
        input_option=int(input("select the option from the above content=="))
        if input_option==1:
            open_new_file()#function to open file
        elif input_option==2:
             ex_file_options()#function of exsisting file
        elif input_option==3:
            about_us()
        elif input_option==4:
              break
        else:
                 print('the input you have given is not in the options \n please enter in a only 1 or 2')

def ex_file_options():
    print("Discription of the app \n>>>use only integers(0-9) to select the options \n>>>Understand the concept \n>>>enter 0 for more information ")
    print('''1)show files used last time\n
             2)rename the file \n
             3)update the file details \n
             4)copy duplicate of that file \n
             5)clear the text data in the file \n
             6)delete the file \n
             7)to find no of words duplicates in text file\n
             0)return to back menu ''')
    input_option=int(input("select the option from the above content=="))
    if input_option==1:
        show_files()
    elif input_option==2:
        file_name=input("enter the file name you want to rename==")
        rename_file(file_name)
    elif input_option==3:
        file_name=input("enter the file name you want to update==")
        update_file(file_name)
    elif input_option==4:
        file_name=input("enter the file name you want to copy a duplicate==")
        copy_file(file_name)
    elif input_option==5:
        file_name=input("enter the file name you want to clear data==")
        clear_data_file(file_name)
    elif input_option==6:
        file_name=input("enter the file name you want to delete==")
        delete_file(file_name)
    elif input_option==7:
        file_name=input("enter the file name ==")
        count_of_words_in_file(file_name)
    elif input_option==0:
        return


def file_list():
    import os
    path = 'C:/Users/patik/OneDrive/Desktop/'
    files=[]
    for r,d,f in os.walk(path):
            for item in f:
                if item[-4:]=='.txt' or item[-4:]=='.csv' or item[-4:]=='.bak':
                    files.append(os.path.join(r, item))
            for i in files:
                print( i )


def open_new_file():
      import datetime
      from datetime import date,time,timedelta
      import time
      file_name=input("enter the file name==")
      file_type=input("""enter the type \n
                    NOTE>>>>>>BY default it is text 
                   1)text file \n
                   2)csv file \n
                   enter option==""")
      if file_type==2:
               file=open(file_name+".csv", "a+")
               file_time=ctime(path.getmtime(file_name))
               file_list.append("{}.csv  ---- {}".format(file_name,file_time))
               print("write by comma for the next box in csv")
               file.append("enter the content==\n")
      else:
               file=open(file_name+".txt", "w+")
               n=1
               for i in range(n):
                   file.write(input("enter the content==\n"))
                   n=n+1
               file.close()
               file=open("{}.txt".format(file_name),"r")
               a=file.readlines()
               print(a)
               file.close()


def show_files():
        print(file_list())
        return


def update_file(file_name):
                     n=int(input('enter no of lines to update=='))
                     for i in range(n):
                         file=open(file_name+'txt','a')
                         file.write(input('enter the content==\n'),end="\n")
                         if i==n-1:
                             file.close()
                     file=open(file_name+".txt",'r')
                     print(file.read())
                     file.close()
                     
               
def path_file():
	import os
	from os import path
	paths=path.realpath(file_name)
	return paths


def time_file(file_name):
        import os
        from os import path
        import datetime
        from datetime import date,time,timedelta
        import time
        time=datetime.datetime.fromtimestamp(path.getmtime(file_name+".txt"))
        return time


def rename_file(file_name):
        import os
        import shutil
        from os import path
        dst=input("enter the new nameof the file==")
        if path.exists(file_name+".txt"):
            scr=path.realpath(file_name+".txt")
            os.rename(file_name+".txt",dst+".txt")
        else:
            print("no path found")
        return


def copy_file(file_name):
    import os
    import shutil
    from os import path
    if path.exists(file_name+".txt"):
        scr=path.realpath(file_name+".txt")
        head,tail=path.split(scr)
        dst=scr+".bak"
        shutil.copy(scr,dst)
        shutil.copystat(scr,dst)
        ex_file_options()


def clear_data_file(file_name):
        file=open(file_name+".txt","w")
        file.write("")
        file.close()
        file=open(file_name+".txt","r")
        print(file.read())
        file.close()
        ex_file_options()


def delete_file(file_name):
        import os
        if os.path.exists(file_name+".txt"):
               os.remove(file_name+".txt")
               print("succesfully deleted")
               ex_file_options()
        else:
               print("file do not exist")
               ex_file_options()

def count_of_words_in_file(file_name):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    file_contents=open(file_name+'.txt','r')
    file_contents=file_contents.read()
    file_contents=file_contents.lower()
    for i in punctuations:
        file_contents=file_contents.replace(i, "")
    words=file_contents.split()
    alpha_words=[]
    not_alpha=[]
    result={}
    for word in words:
        if word.isalpha() == True:
            alpha_words.append(word)
        elif word.isalpha()== False:
            not_alpha.append(word)
    for word in alpha_words :
        result[word]=alpha_words.count(word)
    for key in result.keys():
        print( '{}={}'.format(key,result[key]))
    file_contents.close()

def about_us():
    print("PYTHON PROJECT\nEEE--B\nROLLNO        NAME     \n19121A02A2    M.SRI CHARITHA\n19121A0277    K.RAKESH\n19121A02B6    N.NIKHILA\n19121A0296    K.VENKATAGANESH\n19121A02D6    P.KARUNAKAR RAO    ")


print(main_function())
