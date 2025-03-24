import tkinter as tk
from tkinter import messagebox

class InterviewAdminApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Interview Administrator")
        
        self.interviews = []  # Store interview details
        
        # Labels and Entry Fields
        tk.Label(root, text="Candidate Name:").grid(row=0, column=0)
        self.candidate_entry = tk.Entry(root)
        self.candidate_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=1, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=1, column=1)
        
        tk.Label(root, text="Time (HH:MM):").grid(row=2, column=0)
        self.time_entry = tk.Entry(root)
        self.time_entry.grid(row=2, column=1)
        
        tk.Label(root, text="Status:").grid(row=3, column=0)
        self.status_entry = tk.Entry(root)
        self.status_entry.grid(row=3, column=1)
        
        # Buttons
        tk.Button(root, text="Add Interview", command=self.add_interview).grid(row=4, column=0, columnspan=2)
        tk.Button(root, text="View Interviews", command=self.view_interviews).grid(row=5, column=0, columnspan=2)
        
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.grid(row=6, column=0, columnspan=2)
        
    def add_interview(self):
        candidate = self.candidate_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        status = self.status_entry.get()
        
        if candidate and date and time and status:
            interview = f"{candidate} - {date} {time} - {status}"
            self.interviews.append(interview)
            self.listbox.insert(tk.END, interview)
            
            # Clear fields
            self.candidate_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.status_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please fill in all fields!")
        
    def view_interviews(self):
        self.listbox.delete(0, tk.END)
        for interview in self.interviews:
            self.listbox.insert(tk.END, interview)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterviewAdminApp(root)
    root.mainloop()
