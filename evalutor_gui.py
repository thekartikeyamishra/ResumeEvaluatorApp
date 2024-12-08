import tkinter as tk
from tkinter import filedialog
from utils.evaluator_logic import extract_text_from_pdf, extract_text_from_txt, calculate_ats_score
from utils.ats_score import plot_ats_score

class ResumeEvaluatorApp:
    def __init__(self):
        self.root = tk.Tk()  # Initialize Tkinter root window
        self.root.title("Automated Resume Evaluator")

        # Create GUI components
        tk.Label(self.root, text="Resume Evaluator", font=("Helvetica", 16)).pack(pady=10)

        self.upload_resume_button = tk.Button(self.root, text="Upload Resume", command=self.upload_resume)
        self.upload_resume_button.pack(pady=5)

        self.upload_job_desc_button = tk.Button(self.root, text="Upload Job Description", command=self.upload_job_description)
        self.upload_job_desc_button.pack(pady=5)

        self.evaluate_button = tk.Button(self.root, text="Evaluate", command=self.evaluate_resume, state=tk.DISABLED)
        self.evaluate_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="ATS Score: ", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        self.resume_text = None
        self.job_desc_text = None

    def upload_resume(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf"), ("Text Files", "*.txt")])
        if file_path:
            self.resume_text = extract_text_from_pdf(file_path) if file_path.endswith('.pdf') else extract_text_from_txt(file_path)
            if self.resume_text:
                self.evaluate_button.config(state=tk.NORMAL)

    def upload_job_description(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.job_desc_text = extract_text_from_txt(file_path)
            if self.job_desc_text:
                self.evaluate_button.config(state=tk.NORMAL)

    def evaluate_resume(self):
        if self.resume_text and self.job_desc_text:
            ats_score, matched_skills = calculate_ats_score(self.resume_text, self.job_desc_text)
            self.result_label.config(text=f"ATS Score: {ats_score:.2f}%")
            plot_ats_score(ats_score)

    def run(self):
        self.root.mainloop()


class ResumeEvaluatorAp:
    pass