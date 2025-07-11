import os
from PyPDF2 import PdfMerger

# 📂 Change path if your PDFs are somewhere else
pdf_folder = os.path.expanduser("~/Downloads")  # or any folder with your PDFs
output_file = "merged_output.pdf"

def merge_pdfs(folder_path, output_filename):
    merger = PdfMerger()
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

    if not pdf_files:
        print("❌ No PDF files found in the folder.")
        return

    for pdf in sorted(pdf_files):  # sorted to maintain order
        full_path = os.path.join(folder_path, pdf)
        merger.append(full_path)
        print(f"📎 Added: {pdf}")

    merger.write(os.path.join(folder_path, output_filename))
    merger.close()
    print(f"\n✅ Merged PDF saved as: {output_filename}")

if __name__ == "__main__":
    print("🛠️ Merging PDFs...")
    merge_pdfs(pdf_folder, output_file)
    print("✅ Done!")