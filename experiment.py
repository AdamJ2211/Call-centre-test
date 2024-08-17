import tkinter as tk
import time

loggedin = False
start_time = time.time()


# Defining all of the windows that will be required in the code.
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("FirstCall")
    new_window.configure(bg="#7BC8F6")
    label = tk.Label(new_window, text="Hello Agent!")
    label.grid()


def open_payment_window():
    payment_window = tk.Toplevel(root)
    payment_window.title("PAYMENT")
    payment_window.geometry("1920x1080")
    payment_window.configure(bg="#7BC8F6")


def open_calendar_window():
    calendar_window = tk.Toplevel(root)
    calendar_window.title("CALENDAR")
    calendar_window.geometry("1920x1080")
    calendar_window.configure(bg="#7BC8F6")


def open_leaderboards_window():
    leaderboards_window = tk.Toplevel(root)
    leaderboards_window.title("LEADERBOARDS AND STATISTICS")
    leaderboards_window.geometry("1920x1080")
    leaderboards_window.configure(bg="#7BC8F6")


def open_user_window():
    user_window = tk.Toplevel(root)
    user_window.title("USER")
    user_window.geometry("1920x1080")
    user_window.configure(bg="#7BC8F6")


def open_hours_window():
    hours_window = tk.Toplevel(root)
    hours_window.title("HOURS")
    hours_window.geometry("1920x1080")
    hours_window.configure(bg="#7BC8F6")

    time_label = tk.Label(hours_window, text="Time Completed (All Time):")
    time_label.grid(row=0, column=0, padx=5, pady=5)

    time_box = tk.Text(hours_window, height=5, width=20, bd=2, relief=tk.SOLID)
    time_box.grid(row=0, column=1, padx=5, pady=5)
    time_box.configure(bg="white", fg="black")

    logged_out_time_label = tk.Label(hours_window, text="Time Completed (This Month):")
    logged_out_time_label.grid(row=1, column=0, padx=5, pady=5)

    global logged_out_time_box
    logged_out_time_box = tk.Text(hours_window, height=5, width=20, bd=2, relief=tk.SOLID)
    logged_out_time_box.grid(row=1, column=1, padx=5, pady=5)
    logged_out_time_box.configure(bg="white", fg="black")

    time_box.insert(tk.END, "00:00:00")
    logged_out_time_box.insert(tk.END, "00:00:00")

    def start_timer(time_box, is_logged_out_time):
        if is_logged_out_time:
            elapsed_time = int(time.time() - start_time)
        else:
            elapsed_time = int(time.time() - start_time)

        if elapsed_time < 0:
            elapsed_time = 0

        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = (elapsed_time % 3600) % 60
        time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

        time_box.delete(1.0, tk.END)
        time_box.insert(tk.END, time_str)

        if is_logged_out_time:
            hours_window.after(1000, lambda: start_timer(logged_out_time_box, True))  # Update the logged out time box timer
        else:
            hours_window.after(1000, lambda: start_timer(time_box, False))  # Update the time box timer

    start_timer(time_box, False)  # Timer for time_box
    start_timer(logged_out_time_box, True)  # Timer for logged_out_time_box

    def reset_time():
        global logged_out_start_time
        logged_out_start_time = time.time()
        logged_out_time_box.delete(1.0, tk.END)
        logged_out_time_box.insert(tk.END, "00:00:00")

    reset_button = tk.Button(hours_window, text="Reset", command=reset_time)
    reset_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    reset_button.configure(bg="white")


def submit():
    global loggedin, start_time
    username = username_entry.get()
    password = password_entry.get()
    if username == "adam.jennings" and password == "Password1":
        loggedin = True
        start_time = time.time()
        open_new_window()
        window = tk.Tk()

        window.geometry("1920x1080")
        window.configure(bg="#7BC8F6")

        pay_button = tk.Button(window, text="PAYMENT", width=25, height=20, command=open_payment_window)
        pay_button.grid(row=0, column=0, padx=35, pady=70, sticky=tk.W + tk.E + tk.N + tk.S)
        pay_button.configure(bg="white")

        clndr_button = tk.Button(window, text="CALENDAR", width=25, height=20, command=open_calendar_window)
        clndr_button.grid(row=0, column=1, padx=35, pady=70, sticky=tk.W + tk.E + tk.N + tk.S)
        clndr_button.configure(bg="white")

        ldrbrd_button = tk.Button(window, text="LEADERBOARDS", width=25, height=20, command=open_leaderboards_window)
        ldrbrd_button.grid(row=0, column=2, padx=35, pady=70, sticky=tk.W + tk.E + tk.N + tk.S)
        ldrbrd_button.configure(bg="white")

        hourlog_button = tk.Button(window, text="HOURS", width=25, height=20, command=open_hours_window)
        hourlog_button.grid(row=0, column=3, padx=35, pady=70, sticky=tk.W + tk.E + tk.N + tk.S)
        hourlog_button.configure(bg="white")

        user_button = tk.Button(window, text="USER", width=25, height=20, command=open_user_window)
        user_button.grid(row=0, column=4, padx=35, pady=70, sticky=tk.W + tk.E + tk.N + tk.S)
        user_button.configure(bg="white")

        time_box = tk.Text(window, height=5, width=15, bd=2, relief=tk.SOLID)
        time_box.grid(row=65, column=0, rowspan=1, columnspan=2, padx=1, pady=1)
        time_box.configure(bg="white", fg="black")

        def start_timer():
            elapsed_time = int(time.time() - start_time)
            hours = elapsed_time // 3600
            minutes = (elapsed_time % 3600) // 60
            seconds = (elapsed_time % 3600) % 60
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            time_box.delete(1.0, tk.END)
            time_box.insert(tk.END, time_str)
            window.after(1000, start_timer)  # Update the timer every second (1000 milliseconds)

        start_timer()

        def msg_of_day():
            msg_of_day = entry.get()
            print("Message of the day! - ", msg_of_day)
            text_box = tk.Text(window, height=12, width=80)
            text_box.grid(row=20, column=12, rowspan=5, columnspan=5)

        greeting = tk.Label(text="Hello Agent!")
        greeting.grid()

        # Add an outlined text box for user input
        input_text_box = tk.Text(window, height=10, width=50, bd=2, relief=tk.SOLID)
        input_text_box.grid(row=65, column=0, rowspan=2, columnspan=5, padx=1, pady=1)

        window.mainloop()
    else:
        error_label.config(text="Incorrect username or password")


root = tk.Tk()
root.title("Login")
root.configure(bg="#7BC8F6")

username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)
username_label.configure(bg="white")

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)
password_label.configure(bg="white")

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
submit_button.configure(bg="white")

error_label = tk.Label(root, fg="red", bg="#7BC8F6")
error_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
