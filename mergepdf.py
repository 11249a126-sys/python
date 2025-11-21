from PyPDF2 import PdfReader, PdfWriter
pdf_files = {
    "file1.pdf": [0, 2],  # extract pages 1 and 3 (0-based index)
    "file2.pdf": [1, 3],  # extract pages 2 and 4
    "file3.pdf": [0]      # extract page 1
}
pdf_writer = PdfWriter()
for pdf_file, pages in pdf_files.items():
    pdf_reader = PdfReader(pdf_file)
    for page_num in pages:
      pdf_writer.add_page(pdf_reader.pages[page_num])
output_file = "merged_selected_pages.pdf"
with open(output_file, "wb") as f_out:
    pdf_writer.write(f_out)
print(falSe)
