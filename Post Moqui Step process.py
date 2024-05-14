import tkinter as tk
from tkinter import ttk
import requests
from tkcalendar import Calendar
from datetime import datetime
from PIL import Image, ImageTk

def submit_step_plan():

    step_data = {
        "_entity": "stepPlan",
        "processStepPlanId": step_process_step_plan_id_entry.get(),
        "processPlanId": selected_process_plan_id.get(),
        "processStepPlanName": step_process_step_plan_name_entry.get(),
        "processStepPlanDescription": step_process_step_plan_description.get("1.0", tk.END).strip(),
        "isOptional": step_is_optional_var.get(),
        "dueStartTime": step_due_start_time_entry.get(),
        "dueEndTime": step_due_end_time_entry.get(),
        "planStartTime": step_plan_start_time_entry.get(),
        "planEndTime": step_plan_end_time_entry.get(),
        "orderNumber": step_order_number_var.get(),
        "createdDate": step_created_date_entry.get(),
        "version": step_version_var.get(),
        "lastUpdatedStamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    }

    step_response = requests.post(url_step_plan, headers=headers, json=step_data)

    if step_response.status_code == 200:
        step_result_label.config(text="Step Process Plan submitted successfully!")
        print(step_response.json())
    else:
        step_result_label.config(text=f"Step Process Plan submission failed with status code: {step_response.status_code}")
        print(step_response.text)

root = tk.Tk()
root.title("Step Process Plan Submission")

# Load and display the Fraunhofer logo
logo_path = r"C:\Users\JLM-MS\Desktop\Hiwi\Task 1\1920px-Fraunhofer-Gesellschaft_2009_logo.png"
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((300, 100))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = ttk.Label(root, image=logo_photo)
logo_label.pack()

# Create UI elements for Step Process Plan
ttk.Label(root, text="Step Process Plan ID:").pack()
step_process_step_plan_id_entry = ttk.Entry(root)
step_process_step_plan_id_entry.pack()

ttk.Label(root, text="Process Plan ID:").pack()
selected_process_plan_id = ttk.Entry(root)
selected_process_plan_id.pack()

ttk.Label(root, text="Step Process Plan Name:").pack()
step_process_step_plan_name_entry = ttk.Entry(root)
step_process_step_plan_name_entry.pack()

ttk.Label(root, text="Step Process Plan Description:").pack()
step_process_step_plan_description = tk.Text(root, wrap=tk.WORD, width=30, height=5)
step_process_step_plan_description.pack()

ttk.Label(root, text="Is Optional:").pack()
step_is_optional_var = tk.StringVar()
step_is_optional_dropdown = ttk.Combobox(root, textvariable=step_is_optional_var)
step_is_optional_dropdown['values'] = ["Y", "N"]
step_is_optional_dropdown.pack()

ttk.Label(root, text="Due Start Time (YYYY-MM-DDTHH:MM:SS.sssZ):").pack()
step_due_start_time_entry = ttk.Entry(root)
step_due_start_time_entry.pack()

ttk.Label(root, text="Due End Time (YYYY-MM-DDTHH:MM:SS.sssZ):").pack()
step_due_end_time_entry = ttk.Entry(root)
step_due_end_time_entry.pack()

ttk.Label(root, text="Plan Start Time (YYYY-MM-DDTHH:MM:SS.sssZ):").pack()
step_plan_start_time_entry = ttk.Entry(root)
step_plan_start_time_entry.pack()

ttk.Label(root, text="Plan End Time (YYYY-MM-DDTHH:MM:SS.sssZ):").pack()
step_plan_end_time_entry = ttk.Entry(root)
step_plan_end_time_entry.pack()

ttk.Label(root, text="Order Number:").pack()
step_order_number_var = tk.IntVar()
step_order_number_entry = ttk.Entry(root, textvariable=step_order_number_var)
step_order_number_entry.pack()

ttk.Label(root, text="Step Created Date (YYYY-MM-DD):").pack()
step_created_date_entry = ttk.Entry(root)
step_created_date_entry.pack()

ttk.Label(root, text="Step Version:").pack()
step_version_var = tk.IntVar()
step_version_entry = ttk.Entry(root, textvariable=step_version_var)
step_version_entry.pack()

step_result_label = ttk.Label(root, text="")
step_result_label.pack()

# Create a button for submitting Step Process Plan
submit_step_plan_button = ttk.Button(root, text="POST Step Process Plan", command=submit_step_plan)
submit_step_plan_button.pack()

# Set up the API endpoint and headers for Step Process Plan
url_step_plan = 'http://10.17.13.94:8080/rest/s1/processManagement/ProcessStepPlan'
headers = {
    'accept': 'application/json',
    'authorization': 'Basic am9obi5kb2U6bW9xdWk=',
    'Content-Type': 'application/json'
}

root.mainloop()
