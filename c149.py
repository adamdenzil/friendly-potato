from tkinter import*

import random

root=Tk()

root.title("lucky friend wheel")
root.geometry("241x245")

list_friends=["james","sata","jhones carl bosken","melon"]
print(list_friends)

def alone():
 random_no=random.randint(0,3)
 print(random_no)
 random_lucky_friend=list_friends[random_no]    
 print("your lucky friend that you have never met before is:" + random_lucky_friend)   
btn=Button(root,text="who is you lucky friend that you have never met before",command=alone)
btn.place(relx=0.5, rely=0.5, anchor=CENTER) 

  
root.mainloop()