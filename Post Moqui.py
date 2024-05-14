import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime
from PIL import Image, ImageTk

def submit_all():
    selected_product_id = product_var.get()
    selected_tags = [tag_listbox.get(idx) for idx in tag_listbox.curselection()]
    selected_is_simulated = is_simulated_var.get()
    selected_is_experimental = is_experimental_var.get()
    
    created_date = created_date_entry.get()
    last_updated_stamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    data = {
        "_entity": "org.moqui.mom.processManagement.ProcessPlan",
        "processPlanId": process_plan_id_entry.get(),
        "productId": selected_product_id,
        "processPlanName": process_plan_name_entry.get(),
        "processPlanDescription": process_plan_description.get("1.0", tk.END).strip(),
        "tags": selected_tags,
        "isSimulated": selected_is_simulated,
        "isExperimental": selected_is_experimental,
        "duration": duration_var.get(),
        "level": level_var.get(),
        "processLoopNr": process_loop_nr_var.get(),
        "createdDate": created_date,
        "version": version_var.get(),
        "lastUpdatedStamp": last_updated_stamp
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result_label.config(text="Request successful!")
        print(response.json())
    else:
        result_label.config(text=f"Request failed with status code: {response.status_code}")
        print(response.text)

# Create the main Tkinter window
root = tk.Tk()
root.title("Process Plan Submission")
# Load and display the Fraunhofer logo

logo_path = r"C:\Users\JLM-MS\Desktop\Hiwi\Task 1\1920px-Fraunhofer-Gesellschaft_2009_logo.png"
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((300, 100))  # Resize the image to fit
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = ttk.Label(root, image=logo_photo)
logo_label.pack()

# Create and place form elements
ttk.Label(root, text="Process Plan ID:").pack()
process_plan_id_entry = ttk.Entry(root)
process_plan_id_entry.pack()

ttk.Label(root, text="Product ID:").pack()
product_var = tk.StringVar()
product_dropdown = ttk.Combobox(root, textvariable=product_var)
product_dropdown['values'] = [
    "EQUIP_AB4", "DEMO_PA", "DEMO_UNIT", "DEMO_1_1", "DEMO_1_2", "DEMO_3_1",
    "DEMO_2_1", "DEMO_RM_1", "DEMO_DIG_SER", "DEMO_SA_1", "DEMO_SA_2",
    "DEMO_VAR", "DEMO_VAR_BL_XL", "DEMO_VAR_BL_LG", "DEMO_VAR_BL_MD",
    "DEMO_VAR_BL_SM", "DEMO_VAR_BU_XL", "DEMO_VAR_BU_LG", "DEMO_VAR_BU_MD",
    "DEMO_VAR_BU_SM", "DEMO_VAR_RD_XL", "DEMO_VAR_RD_LG", "DEMO_VAR_RD_MD",
    "DEMO_VAR_RD_SM", "EQUIP_1"
]
product_dropdown.pack()

ttk.Label(root, text="Process Plan Name:").pack()
process_plan_name_entry = ttk.Entry(root)
process_plan_name_entry.pack()

ttk.Label(root, text="Process Plan Description:").pack()
process_plan_description = tk.Text(root, wrap=tk.WORD, width=30, height=5)
process_plan_description.pack()

ttk.Label(root, text="Tags:").pack()
tags = [
    "Assembly", "Continuous Improvement", "Experiment", "Maintenance and Repair",
    "Manufacturing", "Packaging and Labeling", "Quality Control and Inspection",
    "Shipping and Logistics", "Supply Chain", "Warehouse", "Waste Management"
]
tag_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
for tag in tags:
    tag_listbox.insert(tk.END, tag)
tag_listbox.pack()

ttk.Label(root, text="Is Simulated:").pack()
is_simulated_var = tk.StringVar()
is_simulated_dropdown = ttk.Combobox(root, textvariable=is_simulated_var)
is_simulated_dropdown['values'] = ["Y", "N"]
is_simulated_dropdown.pack()

ttk.Label(root, text="Is Experimental:").pack()
is_experimental_var = tk.StringVar()
is_experimental_dropdown = ttk.Combobox(root, textvariable=is_experimental_var)
is_experimental_dropdown['values'] = ["Y", "N"]
is_experimental_dropdown.pack()

ttk.Label(root, text="Created Date (YYYY-MM-DD):").pack()
created_date_entry = ttk.Entry(root)
created_date_entry.pack()

ttk.Label(root, text="Duration:").pack()
duration_var = tk.IntVar()
duration_entry = ttk.Entry(root, textvariable=duration_var)
duration_entry.pack()

ttk.Label(root, text="Level:").pack()
level_var = tk.IntVar()
level_entry = ttk.Entry(root, textvariable=level_var)
level_entry.pack()

ttk.Label(root, text="Process Loop Nr:").pack()
process_loop_nr_var = tk.IntVar()
process_loop_nr_entry = ttk.Entry(root, textvariable=process_loop_nr_var)
process_loop_nr_entry.pack()

ttk.Label(root, text="Version:").pack()
version_var = tk.IntVar()
version_entry = ttk.Entry(root, textvariable=version_var)
version_entry.pack()

submit_all_button = ttk.Button(root, text="POST", command=submit_all)
submit_all_button.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

# Set up the API endpoint and headers
url = 'http://10.17.13.94:8080/rest/s1/processManagement/ProcessPlan'
headers = {
    'accept': 'application/json',
    'authorization': 'Basic am9obi5kb2U6bW9xdWk=',
    'Content-Type': 'application/json'
}

# Start the Tkinter event loop
root.mainloop()
