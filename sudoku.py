"""
Arthor : Darren
Sudoku
Edit1 : Oct 7  6   pm -  6.45pm Do the basic structure
Edit2 :        9.30pm - 12.30pm Show the map and set the game up
Edit3 : Oct 8 10   am - 11.15am get user input and show on the map
Edit4 :        2   pm -  2.30pm ''
Edit5 :        6   pm -  9.20pm get user input to delete and some refinement, critical issue found in remove number function, fix later :/
Edit6 :       10   pm - 10.40pm fixed the issue after a midnight snack """
import time

line = "  +-+-+-+-+-+-+-+-+-+"
conv = lambda i : i or " "
numb = ["1.","2.","3.","4.","5.","6.","7.","8.","9."]
num = ["1","2","3","4","5","6","7","8","9"]

def get_block(slot):
    row = int(slot[0])-1
    col = ord(slot[1].lower()) - 96 - 1
    return((row//3)*3 + col//3)

def print_space():
    print("")
    print("-------------------------------")
    print("")
    
class Sudoku:
    def __init__(self):
        self.row = [None,None,None,None,None,None,None,None,None]
        self.col = [None,None,None,None,None,None,None,None,None]
        self.block = [None,None,None,None,None,None,None,None,None]
        self.occupied = 0

    def print_sudoku(self):
        print("   A B C D E F G H I")
        for i in range(9):
            print(line)
            res = [conv(j) for j in self.row[i].present]
            print(numb[i],*res,sep = "|",end="|\n")

        print(line)

    def insert(self,slot,ans):
        ans = int(ans)
        row = int(slot[0])-1
        col = ord(slot[1].lower()) - 96 - 1
        block = get_block(slot)
        if ans not in self.row[row].numlist:
            if ans not in self.col[col].numlist:
                if ans not in self.block[block].numlist:
                    self.row[row].numlist.append(ans)
                    self.col[col].numlist.append(ans)
                    self.block[block].numlist.append(ans)
                    self.row[row].present[col] = ans
                    self.occupied += 1
                else:
                    print("Invalid input. There is same number in the same block")
            else:
                print("Invalid input. There is same number in the same column")
        else:
            print("Invalid input. There is same number in the same row")

    def remove(self,slot):
        row = int(slot[0])-1
        col = ord(slot[1].lower()) - 96 - 1
        block = get_block(slot)
        number = 0
        if self.row[row].attr[col].locked == False:
##            print(self.row[row].present[col])
            if self.row[row].present[col] != None:
                number = self.row[row].present[col]
                self.row[row].present[col] = None
##                print(self.row[row].numlist)
                self.row[row].numlist.remove(int(ans))
                self.col[col].numlist.remove(int(ans))
                self.block[block].numlist.remove(int(ans))
                self.occupied -= 1
                print("Delete successfully")
            else:
                print("The slot is already empty")
                time.sleep(1.5)
        else:
            print()
            print("This is the initial slot that cannot be removed")
            print()
            time.sleep(1.5)
        

    def set_game(self,game_map):
        for i in range(len(self.row)):
            self.row[i] = Num()
            for j in range(9):
                if game_map[j+(9*i)] != None:
                    self.row[i].numlist.append(game_map[j+(9*i)])
                    self.row[i].attr[j].locked = True
                    self.occupied += 1
                self.row[i].present.append(game_map[j+(9*i)])
                

        for i in range(len(self.col)):
            self.col[i] = Num()
            for j in range(9):
                if game_map[j*9 + i] != None:
                    self.col[i].numlist.append(game_map[j*9 + i])
                self.col[i].present.append(game_map[j*9 + i])
                                    
        for i in range(len(self.block)):
            self.block[i] = Num()
            for j in range(3):
                for k in range(3):
                    if i//3 == 0:
                        if game_map[k + j*9 + i*3] != None:
                            self.block[i].numlist.append(game_map[k + j*9 + i*3])
                        self.block[i].present.append(game_map[k + j*9 + i*3])
                    elif i//3 == 1:
                        if game_map[k + j*9 + i%3*3 + 27] != None:
                            self.block[i].numlist.append(game_map[k + j*9 + i%3*3 + 27])
                        self.block[i].present.append(game_map[k + j*9 + i%3*3 + 27])
                    else:
                        if game_map[k + j*9 + i%3*3 + 54] != None:
                            self.block[i].numlist.append(game_map[k + j*9 + i%3*3 + 54])
                        self.block[i].present.append(game_map[k + j*9 + i%3*3 + 54])
                            
                        
class Num:
    def __init__(self):
        self.numlist = []
        self.present = []
        self.attr = [Slot(),Slot(),Slot(),Slot(),Slot(),Slot(),Slot(),Slot(),Slot()]


class Slot:
    def __init__(self):
        self.locked = False
    

game_map = [1,2,3,4,5,6,7,8,9,
            4,5,7,1,8,9,2,3,6,
            6,8,9,2,3,7,1,4,5,
            8,1,5,3,6,2,9,7,4,
            2,7,4,None,9,None,6,5,3,
            3,9,6,5,7,4,8,1,2,
            5,4,2,6,1,8,3,9,7,
            7,6,1,9,4,5,5,2,8,
            9,3,8,7,2,5,4,6,1]

game_map = [None,None,6,None,3,9,None,1,None,
            2,9,None,1,4,None,7,None,3,
            None,None,None,8,None,None,9,None,None,
            1,5,4,None,9,None,None,8,None,
            8,7,None,None,None,None,4,None,None,
            None,6,None,4,None,8,None,2,1,
            None,2,None,None,8,None,6,3,5,
            4,3,7,2,6,None,None,9,None,
            6,8,None,None,None,None,2,7,None]

sudoku = Sudoku()
sudoku.set_game(game_map)

sudoku.print_sudoku()

while (sudoku.occupied < 81):
    while True:
        slot = input("Enter the slot you want to insert a number, type '/' infront to delete a number instead\n(E.g:1A,/G7): ")
        if len(slot) >=2 and len(slot) <=3:
            if len(slot) == 2:             #if input is length of 2
                if (ord(slot[0]) - 49 >= 0) and (ord(slot[0]) - 49 <= 8):
                    if (ord(slot[1]) - 97 >= 0) and (ord(slot[1]) - 97 <= 8):
                        break
                    else:
                        print("Invalid. Try Again")
                        print_space()
                        continue
                elif (ord(slot[0]) - 49 >= 48) and (ord(slot[0]) - 49 <= 56):
                    slot = slot[::-1]
                    if (ord(slot[0]) - 49 >= 0) and (ord(slot[0]) - 49 <= 8):
                        if (ord(slot[1]) - 97 >= 0) and (ord(slot[1]) - 97 <= 8):
                            break
                        else:
                            print("Invalid. Try Again")
                            print_space()
                            continue
                    else:
                        print("Invalid. Try Again")
                        print_space()
                else:
                    print("Invalid. Try Again")
                    print_space()
                    continue

                
            elif len(slot) == 3:      #if input is length of 3
                if slot[0] == "/":      #if first letter is "/"
                    if (ord(slot[1]) - 49 >= 0) and (ord(slot[1]) - 49 <= 8):
                        if (ord(slot[2]) - 97 >= 0) and (ord(slot[2]) - 97 <= 8):
                            break
                        else:
                            print("Invalid. Try Again")
                            print_space()
                            continue
                    elif (ord(slot[1]) - 49 >= 48) and (ord(slot[1]) - 49 <= 56):
                        slot = slot[:1] + slot[-1:0:-1]
                        if (ord(slot[1]) - 49 >= 0) and (ord(slot[1]) - 49 <= 8):
                            if (ord(slot[2]) - 97 >= 0) and (ord(slot[2]) - 97 <= 8):
                                break
                            else:
                                print("Invalid. Try Again")
                                print_space()
                                continue
                        else:
                            print("Invalid. Try Again")
                            print_space()
                    else:
                        print("Invalid. Try Again")
                        print_space()
                        continue
                else:
                    print("Invalid. Try Again")
                    print_space()

        else:   #other length is invalid
            print("Invalid. Try Again")
            print_space()
            continue
            
##    print(slot)         
    if slot[0] == "/":
        sudoku.remove(slot[1:])
    else:
        while True:
            ans = input("Enter the number: ")
            if len(ans) == 1:
                if ans in num:
                    break
                else:
                    print("Invalid number")
                    print_space()
                    continue
            else:
                print("Invalid number")
                print_space()
                continue
                    
        
        sudoku.insert(slot,ans)
        
    print_space()
    sudoku.print_sudoku()

print("You Won")
    
        
