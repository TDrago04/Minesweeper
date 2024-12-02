from game import Game
from board import Board


file = open("settings.ini", "r")


#   default settings:
#   - size = (30, 30)
#   - prob = .15
#   - screenSize = (900, 900)




size = (25, 25) # lower -> less pieces 
prob = .15  #higher (prob -> 1) = more bombs
screenSize = (900, 900) # change resolution here!!!

for i in range(0, 3):
    s = file.readline()
    if (i== 0):
        size = (int(s.split(" = ")[1].strip("\n").split(",")[0]), int(s.split(" = ")[1].strip("\n").split(",")[1]))
    if (i==1):
        prob = float(s.split(" = ")[1].strip("\n"))
    if (i==2):
        screenSize = (int(s.split(" = ")[1].strip("\n").split(",")[0]), int(s.split(" = ")[1].strip("\n").split(",")[1]))
        

board = Board(size, prob)

game = Game(board, size, prob, screenSize)
game.run()

file.close()

            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠚⠉⠉⠉⠉⠑⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⡘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢂⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣀⣀⣀⣤⣠⡄⣤⣄⡶⣤⣤⣤⡠⣄⣠⣀⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢄⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⢀⣀⣤⣤⣴⣦⣿⣾⣿⣾⣯⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣾⣿⣿⣿⣿⣾⣽⣿⣿⣿⣿⣿⣿⣿⣶⢶⣦⣤⣤⣀⡀⠑⢄⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀⢀⡴⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣽⣶⣄⠱⡀⠀
            # ⠀⠀⠀⠀⠀⢀⡎⢀⡤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⡷⢹⠀
            # ⠀⠀⠀⠀⠀⢺⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⢁⡇
            # ⠀⠀⠀⠀⠀⠸⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠾⣁⠞⠀
            # ⠀⠀⠀⠀⠀⠀⢣⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⢋⡩⠤⠖⠁⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠉⠢⢍⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⡿⢿⣿⣿⣿⣿⣿⡇⡴⠒⠊⠁⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣻⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠀⠀⠈⢿⣿⣿⡿⢏⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠐⣏⠒⢦⣀⣀⡀⠀⠳⡙⢷⣟⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⠙⢿⣿⣿⢿⡄⠀⠀⠀⠈⠿⣠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⢘⣿⠛⣾⣷⣬⢣⠀⠉⠢⣙⠻⣾⣽⣿⣿⢿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡳⣝⣤⣀⡘⣿⣾⣿⣿⣿⣶⣶⣦⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⢻⣁⢻⣿⣿⣿⢸⡆⠀⠀⠀⠉⠒⠀⠒⠤⠴⢍⢻⣿⣯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣶⣿⡼⣖⣻⣿⣿⣿⣿⣿⡳⢆⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⢀⡿⢠⣿⣿⣿⣎⡛⣆⢤⣤⠠⡆⠀⠀⠀⠀⠀⠑⢬⡛⢿⡾⣽⣻⣽⣷⣻⢿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣹⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⢸⡧⢹⣿⣿⣿⢱⣝⢿⣎⢻⡆⢷⠀⠀⠀⠀⠀⠀⠀⠈⣳⣿⣿⣽⣿⣾⣿⣟⡾⣽⢿⣟⣯⣿⢿⣟⣯⠿⣛⣁⡧⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⢠⠾⠯⣷⣘⣿⣿⣿⡇⠯⠓⣝⣯⣽⣏⠢⢀⣀⣀⣠⢤⣿⣭⣽⣿⣻⣿⣿⣿⣿⣿⣟⡿⠤⠬⢍⣋⣙⣉⠤⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⣠⠋⢀⢲⡼⣿⣾⣿⣿⡇⢸⠀⠀⠙⣿⣿⣿⣷⣶⣿⣿⣿⡟⣿⣿⣿⣷⣿⣿⣿⣿⣿⣍⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⢰⢧⢶⣬⣿⣿⣿⣿⣿⣿⠆⣿⠀⠀⣰⣿⣿⣿⣿⣿⢿⣛⡧⣟⣿⣿⣿⣿⣿⣿⣿⣻⣿⡝⠄⠀⠉⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⣿⢶⣯⣿⣿⣿⣿⣿⣿⣿⣧⡘⢄⠀⣻⣿⣿⣿⣿⣏⣶⣹⣾⣿⣞⡷⣯⡿⣟⢿⣯⣧⠙⠘⠀⠀⠀⠚⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠸⡯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣊⣦⣽⣿⡿⢏⡳⣮⣷⣿⣿⣿⣯⣿⣽⣟⣮⠷⣌⠛⣿⣆⡄⠀⠀⠰⡄⡱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠱⡝⣿⣿⣿⣿⣿⣿⣿⣿⣿⢳⡿⢋⣽⣚⣷⣿⢟⢻⣽⣿⣿⣿⣿⣿⣿⣾⡽⣦⣛⡤⢚⣿⣦⠀⠀⣹⣷⣌⡓⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠈⠢⢛⣿⡿⠿⣿⡿⣿⢷⡾⣡⢯⣿⣿⡿⠋⠁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣯⢞⡵⢊⢻⣧⡀⢿⢭⡻⣷⣦⡀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠈⠉⠉⠁⠉⢀⡼⣡⣿⣿⡿⠏⠀⠀⠀⣸⣻⣿⣿⣿⣿⣿⣿⣿⡿⣝⣧⢏⡰⠀⠂⢹⣧⠘⡇⠙⣎⢿⣽⣦⠈⠐⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⢀⠤⢐⣈⣩⢷⣳⡟⣽⠁⠀⠀⣰⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣮⡳⣌⠳⣈⠤⢹⣇⢷⠀⠈⢹⠟⣯⠑⢢⠀⠀⠐⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⢀⠤⢒⣵⣶⢿⣽⣾⣿⣿⡱⡇⠀⠀⠀⣇⢠⡙⣿⣿⣿⣿⣿⣿⣿⡿⣿⣻⢷⡻⣜⣣⢓⠎⢦⢻⡞⠀⠀⡞⢸⡇⣀⣠⣀⠀⢤⡀⠈⠐⡄⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⢸⣿⣶⣿⣿⣯⣿⣾⣿⣿⣿⣳⠀⢠⠖⠚⡩⠟⠰⢦⠙⡛⣿⡽⣻⣷⢿⡿⣽⣏⠿⣜⠢⣍⠚⡤⠂⡇⠀⠀⡇⣿⡹⣿⠫⠿⣿⣶⣳⠀⡀⢳⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⣸⢋⣹⣟⣿⣿⣿⣿⣿⠯⠋⠀⠀⢷⣾⡿⠁⠀⠀⠘⠳⠧⣄⠲⠉⠉⠯⣹⠷⣞⡿⣬⢳⡌⠓⢌⠡⡟⠀⠀⠹⣽⣷⣻⡄⠀⢹⡿⣿⣄⢻⣘⠆⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠛⢿⠟⣿⣿⡿⡯⠛⠁⠀⠀⠀⠀⠈⠙⡇⠀⠀⠀⠀⠀⠀⠈⠀⠰⢦⡐⠈⠇⠘⠅⢋⠣⠘⠀⠀⢀⣽⠀⠀⠀⠉⠛⠋⠀⠀⠀⡇⣿⣿⣿⠾⠁⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠐⣧⡾⣻⠕⠋⠀⠀⠀⠀⠀⡠⠐⠒⠒⠛⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡼⣀⢠⡅⠀⠈⢓⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣿⣿⣜⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⡜⠁⠀⠉⠉⠉⠁⠐⣂⠠⠤⣄⡀⠀⠀⠀⠀⠈⠳⣌⡈⠑⠠⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⣀⠀⣠⢦⣄⣆⢳⠲⣈⠷⣆⠌⠙⠂⣄⠀⠀⠀⠀⠁⡔⢌⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⣘⠶⣙⠾⣽⣯⡋⣷⣩⢶⣍⡛⢦⡐⠘⠳⡀⠀⠂⠀⢹⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⢀⡳⢄⠺⡍⣞⠲⡼⠀⠻⣏⠓⠯⣛⡄⠒⠨⠀⠀⠀⠀⠀⢨⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⢠⠑⣌⡱⢊⠌⡓⠀⠀⠀⠈⢦⠀⠈⠙⢶⣀⣀⣀⣀⣀⣤⣿⡄⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣱⢦⣟⡾⡙⢦⢊⠥⣉⠀⠀⠀⠙⡆⠀⠀⠀⠀⠀⣀⣤⠟⠟⢁⡉⠁⢈⣉⣀⡤⠤⠄⣈⠐⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣼⣿⣿⣽⣷⣮⣮⣵⢧⠶⠀⠀⣸⠃⠀⠀⠀⢶⣊⠁⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠙⠢⢀⠑⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⢿⣿⣷⣿⣾⡽⢦⠶⠃⠀⠀⠀⠀⢸⡉⢀⠀⡀⢀⡁⢀⠀⠀⢂⠀⣤⡄⢂⠀⣀⡀⠠⡄⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡁⢢⠐⠰⢡⣈⠦⡜⢶⡉⣶⣖⣺⣽⣻⣿⣾⣵⣶⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⣰⢎⡗⣫⡜⣷⢻⣷⣽⣶⣿⣿⣿⠿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            # ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠾⢷⡾⠽⠿⠽⠛⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀