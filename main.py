import tkinter as tk
import crapsHandler as cH

window = tk.Tk()
d1, d2 = 0, 0
pot = 0
cash = 1000
point = 0
cashLabel = tk.Label(window, text="")
potLabel = tk.Label(window, text="")

label = tk.Label(window, 
                 font=("times", 250), 
                 fg="black"
                )

def main():
  window.geometry("500x500")
  tk.Button(
    window, 
    text = "roll",
    bd = 5,
    command = rollDice
  ).place(x=400, y=450)
  enterBet()
  displayCash()
  displayPot()

def rollDice():
  # These values indicate dots on the dices.
     # For eg: \u2680 corresponds to 1 dot,
     # \u2681 corresponds to 2 dots etc.
    global point
    d1, d2 = cH.rollDice()

    dice_dots = ['\u2680', '\u2681',
                 '\u2682', '\u2683',
                 '\u2684', '\u2685']
    # Generating random dots on the dices
    label.configure(
        text=f'{dice_dots[d1-1]}{dice_dots[d2-1]}')
    label.pack()

    ans = cH.rollHandler(d1, d2, point)

    if ans == 0:
      lose()
    elif ans == 1:
      win()
    point = ans

def win():
  global cash
  global pot
  cash += pot * 2
  pot = 0
  displayCash()
  displayPot()
    
def lose():
  global pot
  pot = 0
  displayPot()

def addToPot():
   global betEntry
   global pot
   global cash
   betAmount = eval(betEntry.get())
   if betAmount <= cash:
      pot += betAmount
      cash -= betAmount
   else:
      print("shut up poor boy")
   displayCash()
   displayPot()

def enterBet():
   global betEntry
   tk.Button(window, text="Place bet", command=addToPot).place(x=10, y=425)
   betEntry = tk.Entry(window, text = "Bet value: ", font=('calibre',10,'normal'))
   betEntry.focus_set()
   betEntry.place(x=10, y=450)
   
def displayPot():
   global potLabel
   potLabel.destroy()
   text = "Pot: " + str(pot)
   potLabel = tk.Label(window, text=text)
   potLabel.place(x=10, y=10)

def displayCash():
   global cashLabel
   cashLabel.destroy()
   text = "Cash: " + str(cash)
   cashLabel = tk.Label(window, text=text)
   cashLabel.place(x=410, y=10)


if __name__ == "__main__":
  main()
  window.mainloop()