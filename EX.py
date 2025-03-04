import tkinter as tk
from tkinter import filedialog, Text, Button, scrolledtext
from PyPDF2 import PdfReader  # Assuming you have PyPDF2 installed

def extract_text_from_pdf(pdf_path):
  """
  Extracts text from a PDF document.

  Args:a
    pdf_path: Path to the PDF file.

  Returns:
    Extracted text from the PDF, or an error message if extraction fails.
  """
  try:
    with open(pdf_path, 'rb') as pdf_file:
      reader = PdfReader(pdf_file)
      num_pages = len(reader.pages)
      text = ""
      for page_num in range(num_pages):
        page = reader.pages[page_num]
        text += page.extract_text()
      return text
  except Exception as e:
    print(f"Error extracting text from PDF: {e}")
    return f"Error: An error occurred while processing the PDF. ({e})"

class PDFTextExtractor:
    def __init__(self, master):
        self.master = master
        master.title("PDF Text Extractor")

        self.pdf_path = ""
        self.extracted_text = ""

        # Create widgets
        self.label = tk.Label(master, text="Select a PDF file:")
        self.label.pack()

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_pdf)
        self.browse_button.pack()

        self.text_box = scrolledtext.ScrolledText(master, width=80, height=20)
        self.text_box.pack()

        self.extract_button = tk.Button(master, text="Extract Text", command=self.extract_text)
        self.extract_button.pack()

    def browse_pdf(self):
        self.pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    def extract_text(self):
        if self.pdf_path:
            self.extracted_text = extract_text_from_pdf(self.pdf_path)
            self.text_box.delete('1.0', 'end')  # Clear previous text
            self.text_box.insert('end', self.extracted_text)
        else:
            self.text_box.delete('1.0', 'end')
            self.text_box.insert('end', "Please select a PDF file first.")

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = PDFTextExtractor(root)
    root.mainloop()