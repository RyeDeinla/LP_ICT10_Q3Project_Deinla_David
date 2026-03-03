from pyscript import document

def player_loop(event):

    players = ["Riri", 
            "Seb", 
            "Christian", 
            "Cassy", 
            "Steph", 
            "Joaquin", 
            "Marcus", 
            "Andrew", 
            "Rye", 
            "John Rony",
            "Amber", 
            "Cheska", 
            "Atashya", 
            "Ava", 
            "Shanti", 
            "John Ken", 
            "Megan",
            "Noleen",
            "Carmen",
            "Jasie",
            "Brooke",
            "Gabe",
            "Yumi",
            "Lucas",
            "Eyl",
            "Art"]
    
    playerlist = document.getElementById("playerlist")

    playerlist.innerHTML = ""

    # Loop
    for player in players:
        playerlist.innerHTML += f"<li>{player}</li>"