import tkinter as tk
import tkinter.ttk as ttk
import subprocess
import threading

def start_scan():
  host = host_entry.get()
  start_port = int(start_port_entry.get())
  end_port = int(end_port_entry.get())
  result_text.delete("1.0", tk.END)
  progress_bar["value"] = 0
  progress_bar["maximum"] = end_port - start_port + 1
  scan_thread = threading.Thread(target=do_scan, args=(host, start_port, end_port))
  scan_thread.start()

def do_scan(host, start_port, end_port):
  result = subprocess.run(["nmap", "-p", "{}-{}".format(start_port, end_port), host], capture_output=True)
  result_text.insert(tk.END, result.stdout.decode())
  progress_bar["value"] = progress_bar["maximum"]

# create the main window
root = tk.Tk()
root.title("Port Scanner")

# create a frame for the host entry
host_frame = tk.Frame(root)
host_label = tk.Label(host_frame, text="Host:")
host_entry = tk.Entry(host_frame)
host_label.pack(side="left")
host_entry.pack(side="left")

# create a frame for the port range entry
port_range_frame = tk.Frame(root)
start_port_label = tk.Label(port_range_frame, text="Start port:")
start_port_entry = tk.Entry(port_range_frame)
end_port_label = tk.Label(port_range_frame, text="End port:")
end_port_entry = tk.Entry(port_range_frame)
start_port_label.pack(side="left")
start_port_entry.pack(side="left")
end_port_label.pack(side="left")
end_port_entry.pack(side="left")

# create a frame for the scan button and result text
button_frame = tk.Frame(root)
scan_button = tk.Button(button_frame, text="Scan", command=start_scan)
result_text = tk.Text(button_frame)
progress_bar = ttk.Progressbar(button_frame)
scan_button.pack(side="left")
result_text.pack(side="left")
progress_bar.pack(side="left")

# add all the frames to the main window
host_frame.pack()
port_range_frame.pack()
button_frame.pack()

# start the GUI event loop
root.mainloop()
