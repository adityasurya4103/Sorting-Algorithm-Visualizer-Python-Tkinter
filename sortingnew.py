#Import the required Libraries
from tkinter import *
import tkinter as tk
import random
import time



#accepting value:

#n =int(input("Enter Total Number of Elements:    ")) 

#Function to swap two bars that will be animated
def swap(pos_0, pos_1):

    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21-bar11, 0)
    canvas.move(pos_1, bar12-bar22, 0)

    
worker = None 

#Insertion Sort
def _insertion_sort():
    global barList
    global lengthList

    for i in range(len(lengthList)):
        cursor = lengthList[i]
        cursorBar = barList[i]
        pos = i

        while pos > 0 and lengthList[pos - 1] > cursor:
            lengthList[pos] = lengthList[pos - 1]
            barList[pos], barList[pos - 1] = barList[pos - 1], barList[pos]
            swap(barList[pos],barList[pos-1])   
            yield                                      
            pos -= 1                                   

        lengthList[pos] = cursor
        barList[pos] = cursorBar
        swap(barList[pos],cursorBar)


#Bubble Sort
def _bubble_sort():
    global barList
    global lengthList
    
    for i in range(len(lengthList) - 1):
        for j in range(len(lengthList) - i - 1):
            if(lengthList[j] > lengthList[j + 1]):
                lengthList[j] , lengthList[j + 1] = lengthList[j + 1] , lengthList[j]
                barList[j], barList[j + 1] = barList[j + 1] , barList[j]
                swap(barList[j + 1] , barList[j])
                yield        
           

#Selection Sort            
def _selection_sort():
    global barList    
    global lengthList

    for i in range(len(lengthList)):
        min = i
        time.sleep(0.5)
        for j in range(i + 1 ,len(lengthList)):
            if(lengthList[j] < lengthList[min]):
                min = j
        lengthList[min], lengthList[i] = lengthList[i] ,lengthList[min]
        barList[min] , barList[i] = barList[i] , barList[min]

        swap(barList[min] , barList[i])
        
        yield
    

#Triggering Fuctions

def insertion_sort():     
    global worker
    worker = _insertion_sort()
    animate()

def selection_sort():     
    global worker
    worker = _selection_sort()
    animate()

def bubble_sort():     
    global worker
    worker = _bubble_sort()
    animate()    



#Animation Function
def animate():      
    global worker
    if worker is not None:
        try:
            next(worker)
            window.after(10, animate)    
        except StopIteration:            
            worker = None
        finally:
            window.after_cancel(animate) 


#Generator function for generating data
def generate():
    global barList
    global lengthList
    canvas.delete('all')
    barstart = 5
    barend = 15
    barList = []
    lengthList = []

    #Creating a rectangle
    for bar in range(0, (number)):
        randomY = random.randint(1, 360)
        bar = canvas.create_rectangle(barstart, randomY, barend, 365, fill='yellow')
        barList.append(bar)
        barstart += 10
        barend += 10

    #Getting length of the bar and appending into length list
    for bar in barList:
        bar = canvas.coords(bar)
        length = bar[3] - bar[1]
        lengthList.append(length)

    #Maximum is colored Red
    #Minimum is colored Black
    for i in range(len(lengthList)-1):
        if lengthList[i] == min(lengthList):
            canvas.itemconfig(barList[i], fill='red')
        elif lengthList[i] == max(lengthList):
            canvas.itemconfig(barList[i], fill='black')


#for Accepting total number of Inputs
def Accept_value():
   global number
   t1=int(a.get())
   number = t1



#Main Code(Driver Code)


root = Tk()
# specify size of window.
root.geometry("700x350")
# Create text widget and specify size.
T = Text(root, height = 5, width = 52,bg = "yellow")
# Create label
l = Label(root, text = "SORTING ALGORITHM VISUALIZER")
l.config(font =("Courier", 14))

Fact = """MINI PROJECT 
          Group Members are :-
          ADITYA SURYAWANSHI
          MIHIR SONAWANE"""


# Create an Exit button.
b2 = Button(root, text = "NEXT",
			command = root.destroy)

l.pack()
T.pack()
b2.pack()

# Insert The Fact.
T.insert(tk.END, Fact)
root.mainloop()

#ACCEPT NUMBER OF Input
win = tk.Tk()
win.geometry("700x350")
# Create an Entry widget
a=Entry(win, width=35)
a.pack()
Button(win, text="Enter number of Display BARS from", command=Accept_value).pack()
Button(win, text="Next", command=win.destroy).pack()

win.mainloop()




#Making a window using the Tk widget
window = tk.Tk()
window.title('Sorting Visualizer')
window.geometry('1000x450')


#Making a Canvas within the window to display contents
canvas = tk.Canvas(window, width='1000', height='400')
canvas.grid(column=0,row=0, columnspan = 50)

#Buttons
insert = tk.Button(window, text='Insertion Sort', command=insertion_sort)
select = tk.Button(window, text='Selection Sort', command=selection_sort)
bubble = tk.Button(window, text='Bubble Sort', command=bubble_sort)
shuf = tk.Button(window, text='Shuffle', command=generate)
insert.grid(column=1,row=1)
select.grid(column=2,row=1)
bubble.grid(column=3,row=1)
shuf.grid(column=0, row=1)

generate()
window.mainloop()




