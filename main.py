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


# Gettin pokemon's info
tk_image=None
def getInfo():
    global tk_image
    try:
        pokemonInput=pokemonText.get(1.0,"end").strip().lower()
        pokemonName.config(text="Search pokemon!")

        abilityResponse=requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonInput}")
        allAbilities=abilityResponse.json()["abilities"]
        for List in allAbilities:
            for k,v in List.items():
                if k=="ability":
                    print(v["name"])

        imageResponse=requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonInput}")
        imageRaw=imageResponse.json()["sprites"]["front_default"]
        imageData2=requests.get(imageRaw)
        imageData=imageData2.content
        image=Image.open(BytesIO(imageData))
        tk_image = ImageTk.PhotoImage(image)
        showImage(tk_image)
    except requests.exceptions.JSONDecodeError:
        pokemonName.config(text="Enter valid name!")
        showImage(defaultImageTK)

# Showing Images
def showImage(Image):
    imageLabel=tkinter.Label(root,image=Image)
    imageLabel.place(relx=0.5,y=140,anchor="n")


# Search pokemon text
pokemonName=tkinter.Label(text="Search pokemon!", font=("Arial", 10, "normal"))
pokemonName.place(relx=0.5, y=15, anchor="n")

# Gettin pokemon's name
pokemonText=tkinter.Text(height=1, width=20)
pokemonText.place(relx=0.5, y=35, anchor="n")

# Search button
searchButton=tkinter.Button(text="search", width=15, height=1,command=getInfo)
searchButton.place(relx=0.5, y=75, anchor="n")










root.mainloop()