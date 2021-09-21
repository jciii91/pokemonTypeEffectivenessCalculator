from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Type Coverage Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

class Type:
    bug = PhotoImage(file = "bug.gif")
    dark = PhotoImage(file = "dark.gif")
    dragon = PhotoImage(file = "dragon.gif")
    electric = PhotoImage(file = "electric.gif")
    fighting = PhotoImage(file = "fighting.gif")
    fire = PhotoImage(file = "fire.gif")
    flying = PhotoImage(file = "flying.gif")
    ghost = PhotoImage(file = "ghost.gif")
    grass = PhotoImage(file = "grass.gif")
    ground = PhotoImage(file = "ground.gif")
    ice = PhotoImage(file = "ice.gif")
    normal = PhotoImage(file = "normal.gif")
    poison = PhotoImage(file = "poison.gif")
    psychic = PhotoImage(file = "psychic.gif")
    rock = PhotoImage(file = "rock.gif")
    steel = PhotoImage(file = "steel.gif")
    water = PhotoImage(file = "water.gif")
    
    empty = PhotoImage(file = "empty.gif")
    moveSelect = -999
    
    overallEffect = 0
    
    cloneSet = {}
    cloneCount = {}
    cloneColumn = {}

    TypeCount = {
        "bug" : 0,
        "dark" : 0,
        "dragon" : 0,
        "electric" : 0,
        "fighting" : 0,
        "fire" : 0,
        "flying" : 0,
        "ghost" : 0,
        "grass" : 0,
        "ground" : 0,
        "ice" : 0,
        "normal" : 0,
        "poison" : 0,
        "psychic" : 0,
        "rock" : 0,
        "steel" : 0,
        "water" : 0,
        "empty" : 4
        }
        
    TypeList = {
        "bug" : "bug",
        "dark" : "dark",
        "dragon" : "dragon",
        "electric" : "electric",
        "fighting" : "fighting",
        "fire" : "fire",
        "flying" : "flying",
        "ghost" : "ghost",
        "grass" : "grass",
        "ground" : "ground",
        "ice" : "ice",
        "normal" : "normal",
        "poison" : "poison",
        "psychic" : "psychic",
        "rock" : "rock",
        "steel" : "steel",
        "water" : "water"
        }
        
    TypeColumn = {
        "bug" : 5,
        "dark" : 5,
        "dragon" : 5,
        "electric" : 5,
        "fighting" : 5,
        "fire" : 5,
        "flying" : 5,
        "ghost" : 5,
        "grass" : 5,
        "ground" : 5,
        "ice" : 5,
        "normal" : 5,
        "poison" : 5,
        "psychic" : 5,
        "rock" : 5,
        "steel" : 5,
        "water" : 5
        }
        
    MoveSet = {"one" : "empty","two" : "empty","three" : "empty","four" : "empty"}

    def ChangeMoveType(self,arg2,TypeName):
        if (self.moveSelect == 1):
            move1.config(image=arg2)
            self.TypeCount[self.MoveSet["one"]] -= 1
            self.TypeCount[TypeName] += 1
            self.MoveSet["one"] = TypeName
        elif (self.moveSelect == 2):
            move2.config(image=arg2)
            self.TypeCount[self.MoveSet["two"]] -= 1
            self.TypeCount[TypeName] += 1
            self.MoveSet["two"] = TypeName
        elif (self.moveSelect == 3):
            move3.config(image=arg2)
            self.TypeCount[self.MoveSet["three"]] -= 1
            self.TypeCount[TypeName] += 1
            self.MoveSet["three"] = TypeName
        elif (self.moveSelect == 4):
            move4.config(image=arg2)
            self.TypeCount[self.MoveSet["four"]] -= 1
            self.TypeCount[TypeName] += 1
            self.MoveSet["four"] = TypeName
        self.TypeEffectiveness()
        
    def Move1(self):
        self.moveSelect = 1
        
    def Move2(self):
        self.moveSelect = 2
        
    def Move3(self):
        self.moveSelect = 3
        
    def Move4(self):
        self.moveSelect = 4
    
    def TotalEffect(self, whatEffect):
        howEffect = 0
        if (whatEffect == 5):
            howEffect = -3
        elif (whatEffect == 6):
            howEffect = -2
        elif (whatEffect == 7):
            howEffect = 1
        elif (whatEffect == 8):
            howEffect = 2
        self.overallEffect += howEffect
        
    def TypeEffectiveness(self):
        cP = 7
        if (self.TypeColumn["bug"] < 7 and (self.TypeCount["fighting"] > 0 or self.TypeCount["grass"] > 0 or self.TypeCount["ground"] > 0)):
            cP = 6
        if (self.TypeCount["flying"] > 0 or self.TypeCount["fire"] > 0 or self.TypeCount["rock"] > 0):
            cP = 8
        bugColumn.grid(column=cP, row=2)
        self.TypeColumn["bug"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["dark"] < 6 and (self.TypeCount["psychic"] > 0)):
            cP = 5
        if (self.TypeColumn["dark"] < 7 and (self.TypeCount["dark"] > 0 or self.TypeCount["ghost"] > 0)):
            cP = 6
        if (self.TypeCount["bug"] > 0 or self.TypeCount["fighting"] > 0):
            cP = 8
        darkColumn.grid(column=cP, row=3)
        self.TypeColumn["dark"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["dragon"] < 7 and (self.TypeCount["fire"] > 0 or self.TypeCount["water"] > 0 or self.TypeCount["grass"] > 0 or self.TypeCount["electric"] > 0)):
            cP = 6
        if (self.TypeCount["dragon"] > 0 or self.TypeCount["ice"] > 0):
            cP = 8
        dragonColumn.grid(column=cP, row=4)
        self.TypeColumn["dragon"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["electric"] < 7 and (self.TypeCount["flying"] > 0 or self.TypeCount["steel"] > 0 or self.TypeCount["electric"] > 0)):
            cP = 6
        if (self.TypeCount["ground"] > 0):
            cP = 8
        electricColumn.grid(column=cP, row=5)
        self.TypeColumn["electric"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["fighting"] < 7 and (self.TypeCount["rock"] > 0 or self.TypeCount["bug"] > 0 or self.TypeCount["dark"] > 0)):
            cP = 6
        if (self.TypeCount["flying"] > 0 or self.TypeCount["psychic"] > 0):
            cP = 8
        fightingColumn.grid(column=cP, row=6)
        self.TypeColumn["fighting"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["fire"] < 7 and (self.TypeCount["bug"] > 0 or self.TypeCount["steel"] > 0 or self.TypeCount["fire"] > 0 or self.TypeCount["grass"] > 0 or self.TypeCount["ice"] > 0)):
            cP = 6
        if (self.TypeCount["ground"] > 0 or self.TypeCount["rock"] > 0 or self.TypeCount["water"] > 0):
            cP = 8
        fireColumn.grid(column=cP, row=7)
        self.TypeColumn["fire"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["flying"] < 6 and (self.TypeCount["ground"] > 0)):
            cP = 5
        if (self.TypeColumn["flying"] < 7 and (self.TypeCount["bug"] > 0 or self.TypeCount["fighting"] > 0 or self.TypeCount["grass"] > 0)):
            cP = 6
        if (self.TypeCount["electric"] > 0 or self.TypeCount["rock"] > 0 or self.TypeCount["ice"] > 0):
            cP = 8
        flyingColumn.grid(column=cP, row=8)
        self.TypeColumn["flying"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["ghost"] < 6 and (self.TypeCount["normal"] > 0 or self.TypeCount["fighting"] > 0)):
            cP = 5
        if (self.TypeColumn["ghost"] < 7 and (self.TypeCount["bug"] > 0 or self.TypeCount["poison"] > 0)):
            cP = 6
        if (self.TypeCount["dark"] > 0 or self.TypeCount["ghost"] > 0):
            cP = 8
        ghostColumn.grid(column=cP, row=9)
        self.TypeColumn["ghost"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["grass"] < 7 and (self.TypeCount["ground"] > 0 or self.TypeCount["water"] > 0 or self.TypeCount["grass"] > 0 or self.TypeCount["electric"] > 0)):
            cP = 6
        if (self.TypeCount["fire"] > 0 or self.TypeCount["flying"] > 0 or self.TypeCount["bug"] > 0 or self.TypeCount["ice"] > 0 or self.TypeCount["poison"] > 0):
            cP = 8
        grassColumn.grid(column=cP, row=10)
        self.TypeColumn["grass"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["ground"] < 6 and (self.TypeCount["electric"] > 0)):
            cP = 5
        if (self.TypeColumn["ground"] < 7 and (self.TypeCount["poison"] > 0 or self.TypeCount["rock"] > 0)):
            cP = 6
        if (self.TypeCount["water"] > 0 or self.TypeCount["grass"] > 0 or self.TypeCount["ice"] > 0):
            cP = 8
        groundColumn.grid(column=cP, row=11)
        self.TypeColumn["ground"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["ice"] < 7 and (self.TypeCount["ice"] > 0)):
            cP = 6
        if (self.TypeCount["fighting"] > 0 or self.TypeCount["rock"] > 0 or self.TypeCount["steel"] > 0 or self.TypeCount["fire"] > 0):
            cP = 8
        iceColumn.grid(column=cP, row=12)
        self.TypeColumn["ice"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["normal"] < 6 and (self.TypeCount["ghost"] > 0)):
            cP = 5
        if (self.TypeCount["fighting"] > 0):
            cP = 8
        normalColumn.grid(column=cP, row=13)
        self.TypeColumn["normal"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["poison"] < 7 and (self.TypeCount["fighting"] > 0 or self.TypeCount["poison"] > 0 or self.TypeCount["bug"] > 0 or self.TypeCount["grass"] > 0)):
            cP = 6
        if (self.TypeCount["ground"] > 0 or self.TypeCount["psychic"] > 0):
            cP = 8
        poisonColumn.grid(column=cP, row=14)
        self.TypeColumn["poison"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["psychic"] < 7 and (self.TypeCount["fighting"] > 0 or self.TypeCount["psychic"] > 0)):
            cP = 6
        if (self.TypeCount["bug"] > 0 or self.TypeCount["ghost"] > 0 or self.TypeCount["dark"] > 0):
            cP = 8
        psychicColumn.grid(column=cP, row=15)
        self.TypeColumn["psychic"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["rock"] < 7 and (self.TypeCount["normal"] > 0 or self.TypeCount["flying"] > 0 or self.TypeCount["fire"] > 0 or self.TypeCount["poison"] > 0)):
            cP = 6
        if (self.TypeCount["fighting"] > 0 or self.TypeCount["ground"] > 0 or self.TypeCount["steel"] > 0 or self.TypeCount["water"] > 0 or self.TypeCount["grass"] > 0):
            cP = 8
        rockColumn.grid(column=cP, row=16)
        self.TypeColumn["rock"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["steel"] < 6 and (self.TypeCount["poison"] > 0)):
            cP = 5
        if (self.TypeColumn["steel"] < 7 and (self.TypeCount["normal"] > 0 or self.TypeCount["flying"] > 0 or self.TypeCount["rock"] > 0 or self.TypeCount["bug"] > 0 or self.TypeCount["ghost"] > 0 or self.TypeCount["steel"] > 0 or self.TypeCount["grass"] > 0 or self.TypeCount["psychic"] > 0 or self.TypeCount["ice"] > 0 or self.TypeCount["dragon"] > 0 or self.TypeCount["dark"] > 0)):
            cP = 6
        if (self.TypeCount["fighting"] > 0 or self.TypeCount["ground"] > 0 or self.TypeCount["fire"] > 0):
            cP = 8
        steelColumn.grid(column=cP, row=17)
        self.TypeColumn["steel"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.TypeColumn["water"] < 7 and (self.TypeCount["steel"] > 0 or self.TypeCount["water"] > 0 or self.TypeCount["fire"] > 0 or self.TypeCount["ice"] > 0)):
            cP = 6
        if (self.TypeCount["grass"] > 0 or self.TypeCount["electric"] > 0):
            cP = 8
        waterColumn.grid(column=cP, row=18)
        self.TypeColumn["water"] = cP
        self.TotalEffect(cP)
    
    def CloneTypeEffectiveness(self):
        cP = 7
        if (self.cloneColumn["bug"] < 7 and (self.cloneCount["fighting"] > 0 or self.cloneCount["grass"] > 0 or self.cloneCount["ground"] > 0)):
            cP = 6
        if (self.cloneCount["flying"] > 0 or self.cloneCount["fire"] > 0 or self.cloneCount["rock"] > 0):
            cP = 8
        self.cloneColumn["bug"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["dark"] < 6 and (self.cloneCount["psychic"] > 0)):
            cP = 5
        if (self.cloneColumn["dark"] < 7 and (self.cloneCount["dark"] > 0 or self.cloneCount["ghost"] > 0)):
            cP = 6
        if (self.cloneCount["bug"] > 0 or self.cloneCount["fighting"] > 0):
            cP = 8
        self.cloneColumn["dark"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["dragon"] < 7 and (self.cloneCount["fire"] > 0 or self.cloneCount["water"] > 0 or self.cloneCount["grass"] > 0 or self.cloneCount["electric"] > 0)):
            cP = 6
        if (self.cloneCount["dragon"] > 0 or self.cloneCount["ice"] > 0):
            cP = 8
        self.cloneColumn["dragon"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["electric"] < 7 and (self.cloneCount["flying"] > 0 or self.cloneCount["steel"] > 0 or self.cloneCount["electric"] > 0)):
            cP = 6
        if (self.cloneCount["ground"] > 0):
            cP = 8
        self.cloneColumn["electric"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["fighting"] < 7 and (self.cloneCount["rock"] > 0 or self.cloneCount["bug"] > 0 or self.cloneCount["dark"] > 0)):
            cP = 6
        if (self.cloneCount["flying"] > 0 or self.cloneCount["psychic"] > 0):
            cP = 8
        self.cloneColumn["fighting"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["fire"] < 7 and (self.cloneCount["bug"] > 0 or self.cloneCount["steel"] > 0 or self.cloneCount["fire"] > 0 or self.cloneCount["grass"] > 0 or self.cloneCount["ice"] > 0)):
            cP = 6
        if (self.cloneCount["ground"] > 0 or self.cloneCount["rock"] > 0 or self.cloneCount["water"] > 0):
            cP = 8
        self.cloneColumn["fire"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["flying"] < 6 and (self.cloneCount["ground"] > 0)):
            cP = 5
        if (self.cloneColumn["flying"] < 7 and (self.cloneCount["bug"] > 0 or self.cloneCount["fighting"] > 0 or self.cloneCount["grass"] > 0)):
            cP = 6
        if (self.cloneCount["electric"] > 0 or self.cloneCount["rock"] > 0 or self.cloneCount["ice"] > 0):
            cP = 8
        self.cloneColumn["flying"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["ghost"] < 6 and (self.cloneCount["normal"] > 0 or self.cloneCount["fighting"] > 0)):
            cP = 5
        if (self.cloneColumn["ghost"] < 7 and (self.cloneCount["bug"] > 0 or self.cloneCount["poison"] > 0)):
            cP = 6
        if (self.cloneCount["dark"] > 0 or self.cloneCount["ghost"] > 0):
            cP = 8
        self.cloneColumn["ghost"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["grass"] < 7 and (self.cloneCount["ground"] > 0 or self.cloneCount["water"] > 0 or self.cloneCount["grass"] > 0 or self.cloneCount["electric"] > 0)):
            cP = 6
        if (self.cloneCount["fire"] > 0 or self.cloneCount["flying"] > 0 or self.cloneCount["bug"] > 0 or self.cloneCount["ice"] > 0 or self.cloneCount["poison"] > 0):
            cP = 8
        self.cloneColumn["grass"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["ground"] < 6 and (self.cloneCount["electric"] > 0)):
            cP = 5
        if (self.cloneColumn["ground"] < 7 and (self.cloneCount["poison"] > 0 or self.cloneCount["rock"] > 0)):
            cP = 6
        if (self.cloneCount["water"] > 0 or self.cloneCount["grass"] > 0 or self.cloneCount["ice"] > 0):
            cP = 8
        self.cloneColumn["ground"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["ice"] < 7 and (self.cloneCount["ice"] > 0)):
            cP = 6
        if (self.cloneCount["fighting"] > 0 or self.cloneCount["rock"] > 0 or self.cloneCount["steel"] > 0 or self.cloneCount["fire"] > 0):
            cP = 8
        self.cloneColumn["ice"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["normal"] < 6 and (self.cloneCount["ghost"] > 0)):
            cP = 5
        if (self.cloneCount["fighting"] > 0):
            cP = 8
        self.cloneColumn["normal"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["poison"] < 7 and (self.cloneCount["fighting"] > 0 or self.cloneCount["poison"] > 0 or self.cloneCount["bug"] > 0 or self.cloneCount["grass"] > 0)):
            cP = 6
        if (self.cloneCount["ground"] > 0 or self.cloneCount["psychic"] > 0):
            cP = 8
        self.cloneColumn["poison"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["psychic"] < 7 and (self.cloneCount["fighting"] > 0 or self.cloneCount["psychic"] > 0)):
            cP = 6
        if (self.cloneCount["bug"] > 0 or self.cloneCount["ghost"] > 0 or self.cloneCount["dark"] > 0):
            cP = 8
        self.cloneColumn["psychic"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["rock"] < 7 and (self.cloneCount["normal"] > 0 or self.cloneCount["flying"] > 0 or self.cloneCount["fire"] > 0 or self.cloneCount["poison"] > 0)):
            cP = 6
        if (self.cloneCount["fighting"] > 0 or self.cloneCount["ground"] > 0 or self.cloneCount["steel"] > 0 or self.cloneCount["water"] > 0 or self.cloneCount["grass"] > 0):
            cP = 8
        self.cloneColumn["rock"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["steel"] < 6 and (self.cloneCount["poison"] > 0)):
            cP = 5
        if (self.cloneColumn["steel"] < 7 and (self.cloneCount["normal"] > 0 or self.cloneCount["flying"] > 0 or self.cloneCount["rock"] > 0 or self.cloneCount["bug"] > 0 or self.cloneCount["ghost"] > 0 or self.cloneCount["steel"] > 0 or self.cloneCount["grass"] > 0 or self.cloneCount["psychic"] > 0 or self.cloneCount["ice"] > 0 or self.cloneCount["dragon"] > 0 or self.cloneCount["dark"] > 0)):
            cP = 6
        if (self.cloneCount["fighting"] > 0 or self.cloneCount["ground"] > 0 or self.cloneCount["fire"] > 0):
            cP = 8
        self.cloneColumn["steel"] = cP
        self.TotalEffect(cP)
        cP = 7
        if (self.cloneColumn["water"] < 7 and (self.cloneCount["steel"] > 0 or self.cloneCount["water"] > 0 or self.cloneCount["fire"] > 0 or self.cloneCount["ice"] > 0)):
            cP = 6
        if (self.cloneCount["grass"] > 0 or self.cloneCount["electric"] > 0):
            cP = 8
        self.cloneColumn["water"] = cP
        self.TotalEffect(cP)

    def SuggestMove(self):
        holdingEffect = self.overallEffect
        for keys in self.MoveSet:
            self.cloneSet[keys] = self.MoveSet[keys]
        for keys in self.TypeCount:
                self.cloneCount[keys] = self.TypeCount[keys]
        for keys in self.TypeColumn:
                self.cloneColumn[keys] = self.TypeColumn[keys]
        for keys1 in self.cloneSet:
            for keys in self.MoveSet:
                self.cloneSet[keys] = self.MoveSet[keys]
            for keys in self.TypeCount:
                self.cloneCount[keys] = self.TypeCount[keys]
            for keys in self.TypeColumn:
                self.cloneColumn[keys] = self.TypeColumn[keys]
            currentType = self.cloneSet[keys1]
            self.cloneCount[currentType] -= 1
            for keys2 in self.TypeList:
                self.overallEffect = 0
                self.cloneSet[keys1] = self.TypeList[keys2]
                self.cloneCount[keys2] += 1
                self.CloneTypeEffectiveness()
                self.cloneCount[keys2] -= 1
                if (self.overallEffect > holdingEffect):
                    holdingEffect = self.overallEffect
                    suggestedMove1.config(image=getattr(typeClass,self.cloneSet["one"]))
                    suggestedMove2.config(image=getattr(typeClass,self.cloneSet["two"]))
                    suggestedMove3.config(image=getattr(typeClass,self.cloneSet["three"]))
                    suggestedMove4.config(image=getattr(typeClass,self.cloneSet["four"]))
                    

typeClass = Type()

ttk.Label(mainframe, text="Move Set").grid(column=1, row=1, columnspan=2, sticky=(W))

move1 = ttk.Button(mainframe, image=typeClass.empty, command=typeClass.Move1)
move1.grid(column=1, row=2)
move2 = ttk.Button(mainframe, image=typeClass.empty, command=typeClass.Move2)
move2.grid(column=2, row=2)
move3 = ttk.Button(mainframe, image=typeClass.empty, command=typeClass.Move3)
move3.grid(column=1, row=3)
move4 = ttk.Button(mainframe, image=typeClass.empty, command=typeClass.Move4)
move4.grid(column=2, row=3)


ttk.Label(mainframe, text="No Effect").grid(column=5, row=1)
ttk.Label(mainframe, text="Not Very Effective").grid(column=6, row=1)
ttk.Label(mainframe, text="Effective").grid(column=7, row=1)
ttk.Label(mainframe, text="Super Effective").grid(column=8, row=1)

ttk.Label(mainframe, image=typeClass.empty).grid(column=1, row=4)

ttk.Button(mainframe, image=typeClass.bug, command=lambda: typeClass.ChangeMoveType(typeClass.bug,"bug")).grid(column=1, row=5)
ttk.Button(mainframe, image=typeClass.dark, command=lambda: typeClass.ChangeMoveType(typeClass.dark,"dark")).grid(column=2, row=5)
ttk.Button(mainframe, image=typeClass.dragon, command=lambda: typeClass.ChangeMoveType(typeClass.dragon,"dragon")).grid(column=3, row=5)
ttk.Button(mainframe, image=typeClass.electric, command=lambda: typeClass.ChangeMoveType(typeClass.electric,"electric")).grid(column=4, row=5)

ttk.Button(mainframe, image=typeClass.fighting, command=lambda: typeClass.ChangeMoveType(typeClass.fighting,"fighting")).grid(column=1, row=6)
ttk.Button(mainframe, image=typeClass.fire, command=lambda: typeClass.ChangeMoveType(typeClass.fire,"fire")).grid(column=2, row=6)
ttk.Button(mainframe, image=typeClass.flying, command=lambda: typeClass.ChangeMoveType(typeClass.flying,"flying")).grid(column=3, row=6)
ttk.Button(mainframe, image=typeClass.ghost, command=lambda: typeClass.ChangeMoveType(typeClass.ghost,"ghost")).grid(column=4, row=6)

ttk.Button(mainframe, image=typeClass.grass, command=lambda: typeClass.ChangeMoveType(typeClass.grass,"grass")).grid(column=1, row=7)
ttk.Button(mainframe, image=typeClass.ground, command=lambda: typeClass.ChangeMoveType(typeClass.ground,"ground")).grid(column=2, row=7)
ttk.Button(mainframe, image=typeClass.ice, command=lambda: typeClass.ChangeMoveType(typeClass.ice,"ice")).grid(column=3, row=7)
ttk.Button(mainframe, image=typeClass.normal, command=lambda: typeClass.ChangeMoveType(typeClass.normal,"normal")).grid(column=4, row=7)

ttk.Button(mainframe, image=typeClass.poison, command=lambda: typeClass.ChangeMoveType(typeClass.poison,"poison")).grid(column=1, row=8)
ttk.Button(mainframe, image=typeClass.psychic, command=lambda: typeClass.ChangeMoveType(typeClass.psychic,"psychic")).grid(column=2, row=8)
ttk.Button(mainframe, image=typeClass.rock, command=lambda: typeClass.ChangeMoveType(typeClass.rock,"rock")).grid(column=3, row=8)
ttk.Button(mainframe, image=typeClass.steel, command=lambda: typeClass.ChangeMoveType(typeClass.steel,"steel")).grid(column=4, row=8)

ttk.Button(mainframe, image=typeClass.water, command=lambda: typeClass.ChangeMoveType(typeClass.water,"water")).grid(column=1, row=9)

ttk.Label(mainframe, image=typeClass.empty).grid(column=1, row=10)

ttk.Label(mainframe, text="Suggested Move Set").grid(column=1, row=11, columnspan=3, sticky=(W))

suggestedMove1 = ttk.Button(mainframe, image=typeClass.empty)
suggestedMove1.grid(column=1, row=12)
suggestedMove2 = ttk.Button(mainframe, image=typeClass.empty)
suggestedMove2.grid(column=2, row=12)
suggestedMove3 = ttk.Button(mainframe, image=typeClass.empty)
suggestedMove3.grid(column=1, row=13)
suggestedMove4 = ttk.Button(mainframe, image=typeClass.empty)
suggestedMove4.grid(column=2, row=13)

ttk.Button(mainframe, text="Calculate", command=typeClass.SuggestMove).grid(column=1, row=14, columnspan=2)

bugColumn = ttk.Label(mainframe, image=typeClass.bug)
bugColumn.grid(column=typeClass.TypeColumn["bug"], row=2)
darkColumn = ttk.Label(mainframe, image=typeClass.dark)
darkColumn.grid(column=typeClass.TypeColumn["dark"], row=3)
dragonColumn = ttk.Label(mainframe, image=typeClass.dragon)
dragonColumn.grid(column=typeClass.TypeColumn["dragon"], row=4)
electricColumn = ttk.Label(mainframe, image=typeClass.electric)
electricColumn.grid(column=typeClass.TypeColumn["electric"], row=5)
fightingColumn = ttk.Label(mainframe, image=typeClass.fighting)
fightingColumn.grid(column=typeClass.TypeColumn["fighting"], row=6)
fireColumn = ttk.Label(mainframe, image=typeClass.fire)
fireColumn.grid(column=typeClass.TypeColumn["fire"], row=7)
flyingColumn = ttk.Label(mainframe, image=typeClass.flying)
flyingColumn.grid(column=typeClass.TypeColumn["flying"], row=8)
ghostColumn = ttk.Label(mainframe, image=typeClass.ghost)
ghostColumn.grid(column=typeClass.TypeColumn["ghost"], row=9)
grassColumn = ttk.Label(mainframe, image=typeClass.grass)
grassColumn.grid(column=typeClass.TypeColumn["grass"], row=10)
groundColumn = ttk.Label(mainframe, image=typeClass.ground)
groundColumn.grid(column=typeClass.TypeColumn["ground"], row=11)
iceColumn = ttk.Label(mainframe, image=typeClass.ice)
iceColumn.grid(column=typeClass.TypeColumn["ice"], row=12)
normalColumn = ttk.Label(mainframe, image=typeClass.normal)
normalColumn.grid(column=typeClass.TypeColumn["normal"], row=13)
poisonColumn = ttk.Label(mainframe, image=typeClass.poison)
poisonColumn.grid(column=typeClass.TypeColumn["poison"], row=14)
psychicColumn = ttk.Label(mainframe, image=typeClass.psychic)
psychicColumn.grid(column=typeClass.TypeColumn["psychic"], row=15)
rockColumn = ttk.Label(mainframe, image=typeClass.rock)
rockColumn.grid(column=typeClass.TypeColumn["rock"], row=16)
steelColumn = ttk.Label(mainframe, image=typeClass.steel)
steelColumn.grid(column=typeClass.TypeColumn["steel"], row=17)
waterColumn = ttk.Label(mainframe, image=typeClass.water)
waterColumn.grid(column=typeClass.TypeColumn["water"], row=18)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
#
root.mainloop()