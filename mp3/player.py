import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.title("MP3 Player")
root.geometry("500x400")

def add_song():
    song = filedialog.askopenfilename()


def add_many_songs():
    pass


# Create Playlist box
playlist_box = tk.Listbox(root, bg="black", fg = "green", width = 60)
playlist_box.pack(pady = 20)

# Button images 
back_btn_img = tk.PhotoImage(file = 'images/back.png')
forward_btn_img = tk.PhotoImage(file = 'images/forward.png')
play_btn_img = tk.PhotoImage(file = 'images/play.png')
pause_btn_img = tk.PhotoImage(file = 'images/pause.png')
stop_btn_img = tk.PhotoImage(file = 'images/stop.png')

# Create Button frame
control_frame = tk.Frame(root)
control_frame.pack(pady = 20)

# Create Play/Stop etc Buttons
back_button = tk.Button(control_frame, image = back_btn_img, bd = 0)
forward_button = tk.Button(control_frame, image = forward_btn_img, bd = 0)
play_button = tk.Button(control_frame, image = play_btn_img, bd = 0)
pause_button = tk.Button(control_frame, image = pause_btn_img, bd = 0)
stop_button = tk.Button(control_frame, image = stop_btn_img, bd = 0)

back_button.grid(row = 0, column = 0, padx = 10)
forward_button.grid(row = 0, column = 1, padx = 10)
play_button.grid(row = 0, column = 2, padx = 10)
pause_button.grid(row = 0, column = 3, padx = 10)
stop_button.grid(row = 0, column = 4, padx = 10)

# Create menu
my_menu = tk.Menu(root)
root.config(menu = my_menu)

# Create add song menu dropdows
add_song_menu = tk.Menu(my_menu, tearoff = 0)
my_menu.add_cascade(label = "Add Songs", menu = add_song_menu)
add_song_menu.add_command(label = "Add one song to playlist", command = add_song)
# Add many song 
add_song_menu.add_command(label = "Add many song to playlist", command = add_many_songs)


root.mainloop()
