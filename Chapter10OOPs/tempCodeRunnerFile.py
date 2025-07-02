import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

class Train:
    def __init__(self, train_name, total_seats=100, fare=500):
        self.train_name = train_name
        self.seats = total_seats
        self.booked_seats = 0
        self.fare = fare
        self.ticket_folder = "tickets"
        self.counter_file = "ticket_counter.txt"

        if not os.path.exists(self.ticket_folder):
            os.makedirs(self.ticket_folder)

    def get_next_ticket_number(self):
        count = 1
        if os.path.exists(self.counter_file):
            with open(self.counter_file, "r") as f:
                try:
                    count = int(f.read().strip()) + 1
                except ValueError:
                    count = 1
        with open(self.counter_file, "w") as f:
            f.write(str(count))
        return f"R-{count:02d}"


class TrainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🚆 Train Ticket Booking System")
        self.train = Train("Rajdhani Express")
        self.frames = {}
        self.current_passengers = []

        self.create_frames()
        self.show_frame("menu")

    def create_frames(self):
        self.frames["menu"] = self.create_menu_frame()
        self.frames["book"] = self.create_booking_frame()
        self.frames["fare"] = self.create_fare_frame()
        self.frames["pnr"] = self.create_pnr_frame()

    def show_frame(self, name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[name].pack(fill="both", expand=True)

    def create_menu_frame(self):
        frame = tk.Frame(self.root)

        tk.Label(frame, text="🚆 Rajdhani Express Ticketing System", font=("Arial", 16)).pack(pady=20)
        tk.Button(frame, text="🎟️ Book Ticket", width=30, command=lambda: self.show_frame("book")).pack(pady=10)
        tk.Button(frame, text="📈 Seat Status", width=30, command=self.show_status).pack(pady=10)
        tk.Button(frame, text="💰 Check Fare", width=30, command=lambda: self.show_frame("fare")).pack(pady=10)
        tk.Button(frame, text="🔍 Check PNR", width=30, command=lambda: self.show_frame("pnr")).pack(pady=10)
        tk.Button(frame, text="❌ Exit", width=30, command=self.root.quit).pack(pady=20)

        return frame

    def create_booking_frame(self):
        frame = tk.Frame(self.root)

        tk.Label(frame, text="🎟️ Book Your Ticket", font=("Arial", 14)).pack(pady=10)

        self.tickets_entry = tk.Entry(frame)
        self.date_entry = tk.Entry(frame)

        tk.Label(frame, text="Number of Tickets:").pack()
        self.tickets_entry.pack()

        tk.Label(frame, text="Date of Journey (YYYY-MM-DD):").pack()
        self.date_entry.pack()

        self.passenger_form_frame = tk.Frame(frame)
        self.passenger_form_frame.pack(pady=10)

        tk.Button(frame, text="Proceed ➡️", command=self.get_passenger_details).pack(pady=5)
        tk.Button(frame, text="⬅️ Back to Menu", command=lambda: self.show_frame("menu")).pack(pady=10)

        return frame

    def get_passenger_details(self):
        self.current_passengers.clear()
        for widget in self.passenger_form_frame.winfo_children():
            widget.destroy()

        try:
            count = int(self.tickets_entry.get())
            date_str = self.date_entry.get()
            journey_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if journey_date < datetime.now().date():
                messagebox.showerror("Invalid", "Journey date cannot be in the past.")
                return
        except Exception:
            messagebox.showerror("Error", "Please enter valid ticket number and date.")
            return

        self.passenger_entries = []
        for i in range(count):
            tk.Label(self.passenger_form_frame, text=f"Passenger {i+1}").pack()
            name = tk.Entry(self.passenger_form_frame)
            age = tk.Entry(self.passenger_form_frame)
            tk.Label(self.passenger_form_frame, text="Name:").pack()
            name.pack()
            tk.Label(self.passenger_form_frame, text="Age:").pack()
            age.pack()
            self.passenger_entries.append((name, age))

        tk.Button(self.passenger_form_frame, text="Pay & Book ✅", command=self.final_booking).pack(pady=10)

    def final_booking(self):
        total_fare = 0
        full = half = senior = free = 0
        passengers = []

        for name_entry, age_entry in self.passenger_entries:
            name = name_entry.get().strip()
            try:
                age = int(age_entry.get())
            except:
                messagebox.showerror("Error", "Invalid age.")
                return

            if age < 5:
                fare = 0
                free += 1
            elif age <= 12:
                fare = self.train.fare * 0.5
                half += 1
            elif age <= 60:
                fare = self.train.fare
                full += 1
            else:
                fare = self.train.fare * 0.25
                senior += 1

            passengers.append((name, age, fare))
            total_fare += fare

        paid = tk.simpledialog.askfloat("Payment", f"💳 Total to pay: ₹{total_fare:.2f}\nEnter payment amount:")
        if paid is None or paid < total_fare:
            messagebox.showerror("Payment Failed", "Payment insufficient.")
            return

        self.train.booked_seats += len(passengers)
        ticket_no = self.train.get_next_ticket_number()
        now = datetime.now()
        ticket_file = os.path.join(self.train.ticket_folder, f"{ticket_no}.txt")

        ticket_text = f"{'🎉 Happy Journey 🎉':^60}\n" + "-" * 60 + "\n"
        ticket_text += f"Train: {self.train.train_name}   Ticket No: {ticket_no}\n"
        ticket_text += f"Date: {now.date()}   Time: {now.strftime('%H:%M:%S')}\n"
        ticket_text += "-" * 60 + "\n"
        for i, (n, a, f) in enumerate(passengers, 1):
            ticket_text += f"👤 Passenger {i}: {n} | Age: {a}\n"
        ticket_text += "-" * 60 + f"\n💰 Paid: ₹{total_fare:.2f}\n"
        if half or senior or free:
            ticket_text += "✅ Age-based discount applied.\n"

        with open(ticket_file, "w", encoding="utf-8") as f:
            f.write(ticket_text)

        messagebox.showinfo("Booked", f"🎫 Ticket Booked Successfully!\nTicket No: {ticket_no}")
        self.show_frame("menu")

    def create_fare_frame(self):
        frame = tk.Frame(self.root)
        tk.Label(frame, text="💰 Fare Calculator", font=("Arial", 14)).pack(pady=10)
        self.fare_entry = tk.Entry(frame)
        tk.Label(frame, text="Enter number of tickets:").pack()
        self.fare_entry.pack()
        tk.Button(frame, text="Calculate", command=self.calculate_fare).pack(pady=5)
        tk.Button(frame, text="⬅️ Back to Menu", command=lambda: self.show_frame("menu")).pack(pady=10)
        return frame

    def calculate_fare(self):
        try:
            n = int(self.fare_entry.get())
            if n <= 0:
                raise ValueError
            messagebox.showinfo("Fare Info", f"💸 Total Fare: ₹{n * self.train.fare}")
        except:
            messagebox.showerror("Invalid", "Enter a valid number.")

    def create_pnr_frame(self):
        frame = tk.Frame(self.root)
        tk.Label(frame, text="🔍 Check PNR Status", font=("Arial", 14)).pack(pady=10)
        self.pnr_entry = tk.Entry(frame)
        tk.Label(frame, text="Enter Ticket No (e.g., R-01):").pack()
        self.pnr_entry.pack()
        tk.Button(frame, text="Check", command=self.check_pnr).pack(pady=5)
        tk.Button(frame, text="⬅️ Back to Menu", command=lambda: self.show_frame("menu")).pack(pady=10)
        return frame

    def check_pnr(self):
        ticket_no = self.pnr_entry.get().strip().upper()
        ticket_file = os.path.join(self.train.ticket_folder, f"{ticket_no}.txt")
        if os.path.exists(ticket_file):
            with open(ticket_file, "r", encoding="utf-8") as f:
                content = f.read()
            win = tk.Toplevel(self.root)
            win.title(f"Ticket {ticket_no}")
            tk.Text(win, width=70, height=20).pack()
            win.children["!text"].insert("1.0", content)
            win.children["!text"].config(state=tk.DISABLED)
        else:
            messagebox.showerror("Not Found", "❌ Ticket not found.")

    def show_status(self):
        available = self.train.seats - self.train.booked_seats
        messagebox.showinfo("Status", f"📊 Available Seats: {available}/{self.train.seats}")


# ---------- RUN APP ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = TrainGUI(root)
    root.mainloop()
