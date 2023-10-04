import tkinter as tk
from tkinter import messagebox
import pygame

# variáveis de tempo
WORK_MINUTES = 25
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 30
WORK_CYCLES = 4

# atualiza o tempo de trabalho
def update_work_time():
    global work_time
    work_time += WORK_MINUTES
    work_time_label.config(text=f'Tempo de trabalho: {work_time} minutos')

# atualiza o timer
def update_timer():
    global current_state, current_timer, cycles_completed, running

    if running:
        if current_state == 'work':
            if current_timer <= 0:
                update_work_time()
                cycles_completed += 1

                if cycles_completed < WORK_CYCLES:
                    current_state = 'short_break'
                    current_timer = SHORT_BREAK_MINUTES * 60
                else:
                    current_state = 'long_break'
                    current_timer = LONG_BREAK_MINUTES * 60

                alarm1()
            else:
                current_timer -= 1
        elif current_state == 'short_break':
            if current_timer <= 0:
                current_state = 'work'
                current_timer = WORK_MINUTES * 60
                alarm2()
            else:
                current_timer -= 1
        elif current_state == 'long_break':
            if current_timer <= 0:
                current_state = 'work'
                current_timer = WORK_MINUTES * 60
                cycles_completed = 0
                alarm3()
            else:
                current_timer -= 1

        update_display()
        root.after(1000, update_timer)

# toca alarme de relax
def alarm1():
    pygame.mixer.init()
    som_path = "sounds/save.mp3"
    pygame.mixer.music.load(som_path)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    messagebox.showinfo("Pomodoro", "Se alongue e de um CNTRL + S!")

def alarm2():
    pygame.mixer.init()
    som_path = "sounds/resume.mp3"
    pygame.mixer.music.load(som_path)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    messagebox.showinfo("Pomodoro", "Tempo encerrado!")

def alarm3():
    pygame.mixer.init()
    som_path = "sounds/COMPUTEREXIT.mp3"
    pygame.mixer.music.load(som_path)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    messagebox.showinfo("Pomodoro", "Tempo encerrado!")

def alarm4():
    pygame.mixer.init()
    som_path = "sounds/ENDPROGRAM.mp3"
    pygame.mixer.music.load(som_path)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    messagebox.showinfo("Pomodoro", "VOLTE AMANHA!")

def alarm5():
    pygame.mixer.init()
    som_path = "sounds/start.mp3"
    pygame.mixer.music.load(som_path)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    messagebox.showinfo("Pomodoro", "Bons Estudos!")

def alarm6():
    pygame.mixer.init()
    som_path = "sounds/freeze.mp3"
    pygame.mixer.music.load(som_path)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    messagebox.showinfo("Pomodoro", "AI AI AI!")

# iniciar o timer
def start_timer():
    alarm5()
    global running
    if not running:
        running = True
        update_timer()

# pausar o timer
def pause_timer():
    alarm6()
    global running
    running = False

# reiniciar o timer
def resume_timer():
    global running
    if not running:
        running = True
        update_timer()

# fechar o app
def close_app():
    alarm4()
    root.destroy()

# GUI
root = tk.Tk()
root.title("Pomodoro Timer")

work_time = 0
current_state = 'work'
current_timer = WORK_MINUTES * 60
cycles_completed = 0
running = False

work_time_label = tk.Label(root, text=f'Tempo de trabalho: {work_time} minutos')
work_time_label.pack()

start_button = tk.Button(root, text="Iniciar", command=start_timer)
pause_button = tk.Button(root, text="Pausar", command=pause_timer)
#resume_button = tk.Button(root, text="Continuar", command=resume_timer)#
close_button = tk.Button(root, text="Fechar", command=close_app)

start_button.pack()
pause_button.pack()
#resume_button.pack()#
close_button.pack()

def update_display():
    minutes = current_timer // 60
    seconds = current_timer % 60
    timer_label.config(text=f'{minutes:02}:{seconds:02}', fg='red' if current_state == 'work' else 'blue')

timer_label = tk.Label(root, text="", font=("Helvetica", 48))
timer_label.pack()

update_display()

root.mainloop()
