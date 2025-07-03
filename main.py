import requests
import tkinter
from PIL import Image, ImageTk
from io import BytesIO


root = tkinter.Tk()
def getScreen():
    window_width = 350
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.title("Pokemon")
getScreen()

# Question Mark
defaultImage=Image.open("default.png")
defaultImage=defaultImage.resize((60,60))
defaultImageTK=ImageTk.PhotoImage(defaultImage)


#Getting pokemon's image
def getImage(pokemonInput):
    imageResponse = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonInput}")
    imageRaw = imageResponse.json()["sprites"]["front_default"]
    imageData2 = requests.get(imageRaw)
    imageData = imageData2.content
    image = Image.open(BytesIO(imageData))
    tk_image = ImageTk.PhotoImage(image)
    showImage(tk_image)

#Getting pokemon's ability
abilityList=[]
def getAbility(pokemonInput):
    global abilityList
    abilityList = []
    abilityResponse = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonInput}")
    allAbilities = abilityResponse.json()["abilities"]
    for List in allAbilities:
        for k, v in List.items():
            if k == "ability":
                abilityList.append(v["name"])

#Getting pokemon's stats
statsList={}
def getStats(pokemonInput):
    global statsList
    statsList = {}
    statsResponse=requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonInput}")
    allStats=statsResponse.json()["stats"]
    for List in allStats:
        statName=List["stat"]
        statsList[statName["name"]]=List["base_stat"]

#Getting pokemon's types
typeList=[]
def getTypes(pokemonInput):
    global typeList
    typeList = []
    typeResponse=requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonInput}")
    allTypes=typeResponse.json()["types"]
    for List in allTypes:
        typeName=List["type"]
        typeList.append(typeName["name"])

#Gettin pokemons's height and weight
physicalAttributesList={}
def getPhysicalAttributes(pokemonInput):
    global physicalAttributesList
    physicalAttributesList = {}
    phyresponse=requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonInput}")
    heigt=phyresponse.json()["height"]
    weight=phyresponse.json()["weight"]
    physicalAttributesList["height"]=heigt
    physicalAttributesList["weight"]=weight


# Getting pokemon's all info
tk_image=None
def getInfo():
    global tk_image
    try:
        pokemonInput=pokemonText.get(1.0,"end").strip().lower()
        pokemonName.config(text="Search pokemon!")
        getStats(pokemonInput)
        getTypes(pokemonInput)
        getAbility(pokemonInput)
        getImage(pokemonInput)
        getPhysicalAttributes(pokemonInput)
        changeValues()
    except requests.exceptions.JSONDecodeError:
        pokemonName.config(text="Enter valid name!")



# Showing Images
imageLabel = tkinter.Label(root, image=defaultImageTK)
def showImage(img):
    imageLabel.config(image=img)
    imageLabel.place(relx=0.5, y=130, anchor="n")
    imageLabel.image = img


# Search pokemon text
pokemonName=tkinter.Label(text="Search pokemon!", font=("Arial", 10, "normal"))
pokemonName.place(relx=0.5, y=15, anchor="n")

# Gettin pokemon's name
pokemonText=tkinter.Text(height=1, width=20)
pokemonText.place(relx=0.5, y=35, anchor="n")

# Search button
searchButton=tkinter.Button(text="search", width=15, height=1,command=getInfo)
searchButton.place(relx=0.5, y=75, anchor="n")


#stats text
pokemonStats=tkinter.Label(text="Stats", font=("Arial", 12, "bold"))
pokemonStats.place(x=30,y=200)

hpLabel=tkinter.Label(text=f"Hp: ?", font=("Arial", 12, "normal"))
hpLabel.place(x=12,y=230)

attackLabel=tkinter.Label(text=f"Attack: ?", font=("Arial", 12, "normal"))
attackLabel.place(x=12,y=260)

speedLabel=tkinter.Label(text=f"Speed: ?", font=("Arial", 12, "normal"))
speedLabel.place(x=12,y=290)

defenseLabel=tkinter.Label(text=f"Defense: ?", font=("Arial", 12, "normal"))
defenseLabel.place(x=12,y=320)


#Physical text
pokemonpy=tkinter.Label(text="Physical", font=("Arial", 12, "bold"))
pokemonpy.place(x=30,y=380)

weightLabel=tkinter.Label(text=f"Weight: ?", font=("Arial", 12, "normal"))
weightLabel.place(x=12,y=410)

heightLabel=tkinter.Label(text=f"Height: ?", font=("Arial", 12, "normal"))
heightLabel.place(x=12,y=440)


#Type text
typeLabel=tkinter.Label(text="Type", font=("Arial", 12, "bold"))
typeLabel.place(x=245,y=197)

typesLabel=tkinter.Label(text="Type: ?", font=("Arial", 12, "normal"))
typesLabel.place(x=227,y=230)

typesLabel2=tkinter.Label(font=("Arial", 12, "normal"))

#ability
abilityText=tkinter.Label(text="Ability", font=("Arial", 12, "bold"))
abilityText.place(x=245, y=380)

abilityLabel=tkinter.Label(text="Ability: ?", font=("Arial", 12, "normal"))
abilityLabel.place(x=227, y=410)

abilityLabel2=tkinter.Label(font=("Arial", 12, "normal"))


def changeValues():
    global abilityList
    global statsList
    global physicalAttributesList
    global typeList
    global typesLabel2
    global abilityLabel2

    hpLabel.config(text=f"Hp: {statsList['hp']}")
    attackLabel.config(text=f"Attack: {statsList['attack']}")
    speedLabel.config(text=f"Speed: {statsList['speed']}")
    defenseLabel.config(text=f"Defense: {statsList['defense']}")

    weightLabel.config(text=f"Weight: {physicalAttributesList['weight']}")
    heightLabel.config(text=f"Height: {physicalAttributesList['height']}")


    if len(typeList)==2:
        typesLabel.config(text=typeList[0])
        typesLabel2.config(text=typeList[1])
        typesLabel2.place(x=227,y=260)
    else:
        typesLabel.config(text=typeList[0])
        typesLabel2.place_forget()

    if len(abilityList)==2:
        abilityLabel.config(text=abilityList[0])
        abilityLabel2.config(text=abilityList[1])
        abilityLabel2.place(x=227, y=440)
    else:
        abilityLabel.config(text=abilityList[0])
        abilityLabel2.place_forget()



root.mainloop()