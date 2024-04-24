import random
import tkinter as tk
import pygame
from tkinter import messagebox

pygame.init()

def play_gwin_music():
    pygame.mixer.music.load("gamewin.mp3.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()

def play_glose_music():
    pygame.mixer.music.load("gamelose.mp3.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()

def play_win_music():
    pygame.mixer.music.load("win.mp3.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()

def play_lose_music():
    pygame.mixer.music.load("lose.mp3.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick()

word_list = ["apple", "beautiful", "potato"]
chosen_word = random.choice(word_list)
display = ['_' for _ in chosen_word]
lives = 6
game_over = False
ref_word = [0] * len(chosen_word)
window = tk.Tk()
window.title("Hangman Game")
window.configure(bg="#FF9C09")  
heading_label = tk.Label(window, text="Hangman Stages - Word Guess Game", font=("Arial", 16, "bold"), bg="#FF9C09")
heading_label.pack(pady=10)
hangman_images = [f"hangman{i}.png" for i in range(7)]
hangman_image = tk.PhotoImage(file=hangman_images[lives])
hangman_label = tk.Label(window, image=hangman_image, bg="#FF9C09")
hangman_label.pack(pady=10)

def guess_letter(event=None):
    global chosen_word, display, lives, ref_word
    guessed_letter = entry_guess.get().lower()
    entry_guess.delete(0, tk.END)  
    letter_found = False
    for position in range(len(chosen_word)):
        if chosen_word[position] == guessed_letter and ref_word[position] == 0:
            display[position] = guessed_letter
            letter_found = True
            ref_word[position] = 1
            label_display.config(text=' '.join(display))
            play_win_music()
            break
    if not letter_found:
        global lives
        lives -= 1
        play_lose_music()
        label_lives.config(text=f'Lives: {lives}')
        hangman_image.config(file=hangman_images[lives])   
        if lives == 0:
            play_glose_music()
            messagebox.showinfo("Game Over", "You Lost!")
            window.destroy()
    elif '_' not in display:
        label_display.config(text=' '.join(display))
        play_gwin_music()
        messagebox.showinfo("Game Over", "You Won!")
        window.destroy()

label_display = tk.Label(window, text=' '.join(display), font=("Arial", 14), bg="#FF9C09")
label_display.pack(pady=20)   
label_lives = tk.Label(window, text=f'Lives: {lives}', font=("Arial", 12), bg="#FF9C09")
label_lives.pack()
entry_guess = tk.Entry(window, width=5, font=("Arial", 12))
entry_guess.pack(pady=10)   
entry_guess.bind("<Return>", guess_letter)   
button_guess = tk.Button(window, text="Enter", command=guess_letter, font=("Arial", 12))
button_guess.pack(pady=10)    
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")  
window.update_idletasks()
x = (screen_width - window.winfo_width()) // 2
y = 0  
window.geometry(f"+{x}+{y}")
window.mainloop()
