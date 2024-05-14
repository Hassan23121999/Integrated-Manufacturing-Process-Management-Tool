#  Integrated Manufacturing Process Management Tool
An integrated tool for managing and submitting detailed manufacturing process plans and job details. This tool uses a graphical user interface (GUI) to gather user inputs and produces comprehensive outputs in various formats


## Project Description
This project provides an integrated tool for managing and submitting detailed manufacturing process plans and job details. The tool uses a graphical user interface (GUI) to prompt the user for necessary inputs and generates comprehensive outputs in various formats such as Excel and JSON.

## Features
- **CSV File Selection:** Choose an input CSV file containing initial data.
- **User Input for Job Details:** Input details such as the number of product variants, minimum process length, and number of jobs.
- **Job Detail Generation:** Automatically generates job details including product variants, job IDs, quantities, release and completion dates, and processes.
- **Step Process Plan Submission:** Submit step process plans with detailed attributes.
- **Process Plan Submission:** Submit comprehensive process plans with detailed attributes.
- **Output to Excel and JSON:** Saves the generated job information in both Excel and JSON formats.
- **API Integration:** Submit process plans and step process plans to specified API endpoints.

## Installation

### Prerequisites
- Python 3.x
- pandas
- tkinter
- PIL (Pillow)
- requests
- tkcalendar

You can install the required packages with pip:
```bash
pip install pandas tk pillow requests tkcalendar
```

### Setup
Clone this repository to your local machine:
```bash
git clone https://github.com/Hassan23121999/Integrated-Manufacturing-Process-Management-Tool.git
cd Integrated-Manufacturing-Process-Management-Tool
```

## Usage

Run the script to open the GUI for step process plan submission:
```bash
python Post_Moqui_Step_process.py
```
Run the script to open the GUI for process plan submission:
```bash
python Post_Moqui.py
```

Follow the GUI prompts to input the necessary details and specify output file paths. The scripts will generate the required outputs and submit process plans to the specified API endpoints.


## Support
For technical support or troubleshooting, please contact the support team via email at:
2016n1770@gmail.com

