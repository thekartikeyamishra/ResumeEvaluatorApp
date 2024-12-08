# Automated Resume Evaluator

## Overview

For the next 15 days, I'll be creating and sharing 15 projects – one per day! Free versions will be open to all on my GitHub, and a low-cost paid version will be available too. Can't wait to hear your thoughts!

The **Automated Resume Evaluator** is a Python-based tool that evaluates resumes against job descriptions. It calculates an **Applicant Tracking System (ATS)** score, helping users determine how well their resume matches a specific job description. The project includes a simple GUI for uploading resumes and job descriptions, calculating the ATS score, and visualizing the results.

## Features

- Upload resumes (`.txt` or `.pdf`) and job descriptions (`.txt`).
- Calculate ATS scores based on keyword matches.
- Display ATS scores visually as pie charts.
- User-friendly GUI built with **Tkinter**.

## Folder Structure

AutomatedResumeEvaluator/
├── data/                         
│   ├── sample_resumes/           # Sample resumes for testing
│   ├── sample_job_descriptions/  # Sample job descriptions for testing
├── gui/                          
│   ├── __init__.py               # Initializes the GUI module
│   ├── evaluator_gui.py          # GUI for resume evaluator
├── utils/                         
│   ├── __init__.py               # Initializes the utils module
│   ├── evaluator_logic.py        # Logic for extracting text and calculating ATS score
│   ├── ats_score.py              # Visualization logic for ATS score
├── main.py                       # Main entry point for the application
├── requirements.txt              # Required dependencies
├── README.md                     # Project documentation



## Installation Instructions

### Prerequisites
- **Python 3.8+**
- **pip**: Python's package manager.

### Steps to Install and Run:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/thekartikeyamishra/AutomatedResumeEvaluator.git
    cd AutomatedResumeEvaluator
    ```

2. **Set up a virtual environment** (optional):
    ```bash
    python -m venv .venv
    ```

3. **Activate the virtual environment**:
    - On **Windows**:
        ```bash
        .venv\Scripts\activate
        ```
    - On **macOS/Linux**:
        ```bash
        source .venv/bin/activate
        ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```

5. **Run the application**:
    ```bash
    python main.py
    ```

## Usage

1. Launch the application (`main.py`).
2. Use the "Upload Resume" button to upload a `.txt` or `.pdf` resume file.
3. Use the "Upload Job Description" button to upload a `.txt` job description file.
4. Click "Evaluate" to calculate the ATS score and view the results in the GUI and as a pie chart.


