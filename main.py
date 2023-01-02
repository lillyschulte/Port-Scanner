import socket
import tkinter as tk
import threading

def scan(host, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(0.5)
  try:
    s.connect((host, port))
    return True
  except:
    return False
  finally:
    s.close()

def start_scan():
  host = host_entry.get()
  start_port = int(start_port_entry.get())
  end_port = int(end_port_entry.get())
  result_text.delete("1.0", tk.END)
  scan_thread = threading.Thread(target=do_scan, args=(host, start_port, end_port))
  scan_thread.start()

def do_scan(host, start_port, end_port):
  for port in range(start_port, end_port+1):
    if scan(host, port):
      result_text.insert(tk.END, "Port {} is open\n".format(port))

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
scan_button.pack(side="left")
result_text.pack(side="left")

# add all the frames to the main window
host_frame.pack()
port_range_frame.pack()
button_frame.pack()

# start the GUI event loop
root.mainloop()
