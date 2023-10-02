import tkinter as tk
import winsound


class PomodoroTimer:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x300")  # Aumentei a altura para acomodar o novo rótulo

        self.time_left = 1500  # 25 minutos em segundos
        self.is_pomodoro = True
        self.pomodoro_count = 0
        self.total_work_time = 0  # Variável para rastrear o tempo total de trabalho

        self.work_time_label = tk.Label(root, text="Pomodoro Timer", font=("Helvetica", 18))
        self.work_time_label.pack(pady=10)

        self.label = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.total_time_label = tk.Label(root, text="Tempo Total de Trabalho: 00:00", font=("Helvetica", 12))
        self.total_time_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Iniciar", command=self.start_timer)
        self.pause_button = tk.Button(root, text="Pausar", command=self.pause_timer)
        self.reset_button = tk.Button(root, text="Redefinir", command=self.reset_timer)

        self.start_button.pack()
        self.pause_button.pack()
        self.reset_button.pack()

        self.update_display()

    def start_timer(self):
        self.start_button.config(state="disabled")
        self.pause_button.config(state="active")
        self.is_pomodoro = True

        self.timer()

    def pause_timer(self):
        self.start_button.config(state="active")
        self.pause_button.config(state="disabled")

        self.root.after_cancel(self.timer_id)

    def reset_timer(self):
        self.start_button.config(state="active")
        self.pause_button.config(state="disabled")

        self.time_left = 1500
        self.pomodoro_count = 0
        self.is_pomodoro = True
        self.total_work_time = 0  # Redefina o tempo total

        self.update_display()
        self.root.after_cancel(self.timer_id)

    def timer(self):
        if self.time_left > 0:
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            time_str = f"{minutes:02}:{seconds:02}"
            self.label.config(text=time_str)
            self.timer_id = self.root.after(1000, self.timer)
            self.time_left -= 1
        else:
            self.play_alarm()
            if self.is_pomodoro:
                self.pomodoro_count += 1
                if self.pomodoro_count >= 4:
                    self.time_left = 1800  # 30 minutos em segundos
                    self.is_pomodoro = False
                else:
                    self.time_left = 300  # 5 minutos em segundos
                    self.is_pomodoro = False
            else:
                self.time_left = 1500  # 25 minutos em segundos
                self.is_pomodoro = True
                self.total_work_time += 1500  # Adicione o tempo de trabalho ao tempo total
                self.update_total_time()  # Atualize o tempo total
            self.update_display()

    def update_display(self):
        if self.is_pomodoro:
            self.label.config(text="25:00", fg="green")
        else:
            if self.time_left == 1800:  # Verifique se o tempo restante é de 30 minutos
                self.label.config(text="30:00", fg="blue")
            else:
                self.label.config(text="05:00", fg="red")

    def update_total_time(self):
        total_minutes = self.total_work_time // 60
        total_seconds = self.total_work_time % 60
        total_time_str = f"Tempo Total de Trabalho: {total_minutes:02}:{total_seconds:02}"
        self.total_time_label.config(text=total_time_str)

    def play_alarm(self):
        winsound.Beep(1000, 1000)  # Toca um som por 1 segundo


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
