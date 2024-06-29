import tkinter as tk
from tkinter import ttk
import psutil
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

class NetworkMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Monitor")

        self.create_widgets()

        self.previous_net_io = psutil.net_io_counters()
        self.bytes_sent = [0]
        self.bytes_recv = [0]
        self.time_points = [0]

        self.update_stats()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.process_label = ttk.Label(self.frame, text="Active Processes:")
        self.process_label.pack()

        self.process_listbox = tk.Listbox(self.frame)
        self.process_listbox.pack(fill=tk.BOTH, expand=True)

        self.port_label = ttk.Label(self.frame, text="Open Ports:")
        self.port_label.pack()

        self.port_listbox = tk.Listbox(self.frame)
        self.port_listbox.pack(fill=tk.BOTH, expand=True)

        self.figure = Figure(figsize=(5, 2), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Network Usage")
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Bytes Sent/Received")

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def update_stats(self):
        self.update_process_list()
        self.update_port_list()
        self.update_network_usage()

        self.root.after(1000, self.update_stats)  # Update every second

    def update_process_list(self):
        self.process_listbox.delete(0, tk.END)
        for proc in psutil.process_iter(['pid', 'name']):
            self.process_listbox.insert(tk.END, f"{proc.info['pid']}: {proc.info['name']}")

    def update_port_list(self):
        self.port_listbox.delete(0, tk.END)
        for conn in psutil.net_connections(kind='inet'):
            self.port_listbox.insert(tk.END, f"{conn.laddr.port}: {conn.status}")

    def update_network_usage(self):
        new_net_io = psutil.net_io_counters()
        bytes_sent_diff = new_net_io.bytes_sent - self.previous_net_io.bytes_sent
        bytes_recv_diff = new_net_io.bytes_recv - self.previous_net_io.bytes_recv

        self.bytes_sent.append(bytes_sent_diff)
        self.bytes_recv.append(bytes_recv_diff)
        self.time_points.append(self.time_points[-1] + 1)

        self.previous_net_io = new_net_io

        self.ax.clear()
        self.ax.plot(self.time_points, self.bytes_sent, label='Bytes Sent')
        self.ax.plot(self.time_points, self.bytes_recv, label='Bytes Received')
        self.ax.legend()
        self.canvas.draw()

def main():
    root = tk.Tk()
    app = NetworkMonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
