import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

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
        self.root.title("🚆Ticket Booking System")
        self.train = Train("Rajdhani Express")
        self.frames = {}
        self.passenger_entries = []

        self.setup_frames()
        self.show_frame("menu")

    def setup_frames(self):
        self.frames["menu"] = self.build_main_menu()
        self.frames["book"] = self.build_booking_screen()
        self.frames["fare"] = self.build_fare_screen()
        self.frames["pnr"] = self.build_pnr_screen()

    def show_frame(self, name):
        for f in self.frames.values():
            f.pack_forget()
        self.frames[name].pack(fill="both", expand=True)

    def build_main_menu(self):
        frame = tk.Frame(self.root)

        tk.Label(frame, text="🚆 Rajdhani Express Ticketing System", font=("Arial", 16)).pack(pady=20)
        tk.Button(frame, text="🎟️ Book Ticket", width=30, command=lambda: self.show_frame("book")).pack(pady=10)
        tk.Button(frame, text="📈 Seat Status", width=30, command=self.show_status).pack(pady=10)
        tk.Button(frame, text="💰 Check Fare", width=30, command=lambda: self.show_frame("fare")).pack(pady=10)
        tk.Button(frame, text="🔍 Check PNR", width=30, command=lambda: self.show_frame("pnr")).pack(pady=10)
        tk.Button(frame, text="❌ Exit", width=30, command=self.root.quit).pack(pady=20)

        return frame

    def build_booking_screen(self):
        frame = tk.Frame(self.root)

        tk.Label(frame, text="🎟️ Book Ticket", font=("Arial", 14)).pack(pady=10)

        tk.Label(frame, text="Number of Tickets:").pack()
        self.tickets_entry = tk.Entry(frame)
        self.tickets_entry.pack()

        tk.Label(frame, text="Date of Journey (YYYY-MM-DD):").pack()
        self.date_entry = tk.Entry(frame)
        self.date_entry.pack()

        tk.Button(frame, text="➡️ Proceed", command=self.collect_passenger_info).pack(pady=5)
        self.passenger_form_frame = tk.Frame(frame)
        self.passenger_form_frame.pack(pady=10)

        tk.Button(frame, text="⬅️ Back", command=lambda: self.show_frame("menu")).pack(pady=10)
        return frame

    def collect_passenger_info(self):
        for widget in self.passenger_form_frame.winfo_children():
            widget.destroy()
        self.passenger_entries.clear()

        try:
            count = int(self.tickets_entry.get())
            date_str = self.date_entry.get()
            journey_date = datetime.strptime(date_str, "%Y-%m-%d").date()

            if journey_date < datetime.now().date():
                raise ValueError("Past date not allowed.")
        except Exception as e:
            messagebox.showerror("Error", "❌ Invalid number or date.")
            return

        for i in range(count):
            tk.Label(self.passenger_form_frame, text=f"Passenger {i + 1}").pack()
            tk.Label(self.passenger_form_frame, text="Name:").pack()
            name = tk.Entry(self.passenger_form_frame)
            name.pack()
            tk.Label(self.passenger_form_frame, text="Age:").pack()
            age = tk.Entry(self.passenger_form_frame)
            age.pack()
            self.passenger_entries.append((name, age))

        tk.Button(self.passenger_form_frame, text="✅ Pay & Book", command=self.finalize_booking).pack(pady=10)

    def finalize_booking(self):
        passengers = []
        total_fare = 0
        full = half = senior = free = 0

        for name_entry, age_entry in self.passenger_entries:
            name = name_entry.get().strip()
            try:
                age = int(age_entry.get())
            except:
                messagebox.showerror("Error", "⚠️ Invalid age input.")
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

        paid = simpledialog.askfloat("💳 Payment", f"Total fare: ₹{total_fare:.2f}\nEnter amount:")
        if paid is None or paid < total_fare:
            messagebox.showerror("Payment Failed", "❌ Insufficient amount.")
            return

        self.train.booked_seats += len(passengers)
        ticket_no = self.train.get_next_ticket_number()
        now = datetime.now()
        ticket_path = os.path.join(self.train.ticket_folder, f"{ticket_no}.txt")

        # Save Ticket
        with open(ticket_path, "w", encoding="utf-8") as f:
            f.write("*" * 60 + "\n")
            f.write(f"{'🎉 Happy Journey 🎉':^60}\n")
            f.write("*" * 60 + "\n")
            f.write(f"Train: {self.train.train_name}  | Ticket No: {ticket_no}\n")
            f.write(f"Date: {now.date()}   Time: {now.strftime('%H:%M:%S')}\n")
            f.write("-" * 60 + "\n")
            for i, (name, age, fare) in enumerate(passengers, 1):
                f.write(f"👤 Passenger {i}: {name:<30} Age: {age}\n")
            f.write("-" * 60 + f"\nTotal Paid: ₹{total_fare:.2f}\n")
            if half or senior or free:
                f.write("✅ Age-based discount applied.\n")
            f.write("*" * 60 + "\n")

        messagebox.showinfo("Success", f"🎫 Ticket Booked!\nTicket No: {ticket_no}")
        self.show_frame("menu")

    def build_fare_screen(self):
        frame = tk.Frame(self.root)
        tk.Label(frame, text="💰 Fare Calculator", font=("Arial", 14)).pack(pady=10)
        tk.Label(frame, text="Enter number of tickets:").pack()
        self.fare_entry = tk.Entry(frame)
        self.fare_entry.pack()
        tk.Button(frame, text="Calculate", command=self.calculate_fare).pack(pady=5)
        tk.Button(frame, text="⬅️ Back", command=lambda: self.show_frame("menu")).pack(pady=10)
        return frame

    def calculate_fare(self):
        try:
            n = int(self.fare_entry.get())
            if n <= 0:
                raise ValueError
            messagebox.showinfo("Fare", f"💸 Total Fare: ₹{n * self.train.fare}")
        except:
            messagebox.showerror("Error", "⚠️ Enter valid number of tickets.")

    def build_pnr_screen(self):
        frame = tk.Frame(self.root)
        tk.Label(frame, text="🔍 PNR Status", font=("Arial", 14)).pack(pady=10)
        tk.Label(frame, text="Enter Ticket No (e.g., R-01):").pack()
        self.pnr_entry = tk.Entry(frame)
        self.pnr_entry.pack()
        tk.Button(frame, text="Check", command=self.check_pnr).pack(pady=5)
        tk.Button(frame, text="⬅️ Back", command=lambda: self.show_frame("menu")).pack(pady=10)
        return frame

    def check_pnr(self):
        ticket_no = self.pnr_entry.get().strip().upper()
        path = os.path.join(self.train.ticket_folder, f"{ticket_no}.txt")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            win = tk.Toplevel(self.root)
            win.title(f"Ticket {ticket_no}")
            text = tk.Text(win, width=70, height=20)
            text.pack()
            text.insert("1.0", content)
            text.config(state="disabled")
        else:
            messagebox.showerror("Not Found", "❌ Ticket not found.")

    def show_status(self):
        available = self.train.seats - self.train.booked_seats
        messagebox.showinfo("Seats", f"📊 Available Seats: {available}/{self.train.seats}")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = TrainGUI(root)
    root.mainloop()
