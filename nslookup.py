import tkinter as tk
import subprocess

def perform_nslookup():
    server = server_entry.get()
    pc_tag = pc_tag_entry.get()
    result = subprocess.run(['nslookup', server], capture_output=True, text=True)
    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.insert(tk.END, result.stdout)
    
    # Extract IP address and display it
    ip_address = extract_ip_address(result.stdout)
    system_ip_entry.delete(0, tk.END)
    system_ip_entry.insert(tk.END, ip_address)
    
    # Insert watermark
    output_text.insert(tk.END, "\nMade By RwKY00978")

def extract_ip_address(output):
    lines = output.split('\n')
    for i in range(len(lines)):
        if 'Name:' in lines[i] and 'Address:' in lines[i+1]:
            name_line = lines[i]
            address_line = lines[i+1]
            name_parts = name_line.split()
            address_parts = address_line.split()
            name = name_parts[-1]
            address = address_parts[-1]
            return f"{address}"

# Create GUI window
window = tk.Tk()
window.title("Find_ip_NSlookup")

# Default values for server and PC tag
default_server = ""
default_pc_tag = ""

# Server input box
server_label = tk.Label(window, text="System Name:")
server_label.grid(row=0, column=0, padx=5, pady=5)
server_entry = tk.Entry(window)
server_entry.grid(row=0, column=1, padx=5, pady=5)
server_entry.insert(tk.END, default_server)

# PC tag input box
pc_tag_label = tk.Label(window, text="Domain IP:")
pc_tag_label.grid(row=1, column=0, padx=5, pady=5)
pc_tag_entry = tk.Entry(window)
pc_tag_entry.grid(row=1, column=1, padx=5, pady=5)
pc_tag_entry.insert(tk.END, default_pc_tag)

# System IP input box
system_ip_label = tk.Label(window, text="System IP:")
system_ip_label.grid(row=2, column=0, padx=5, pady=5)
system_ip_entry = tk.Entry(window)
system_ip_entry.grid(row=2, column=1, padx=5, pady=5)

# Button to perform NSLookup
lookup_button = tk.Button(window, text="Find IP", command=perform_nslookup)
lookup_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Output text area
output_text = tk.Text(window, height=10, width=40)
output_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start GUI
window.mainloop()
