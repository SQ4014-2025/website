import PyPDF2

input_pdf = "Morgan2025 - Coding with AI.pdf"
output_folder = ""

def split_pdf(input_pdf, output_folder):
    # Chapter ranges based on the table of contents [3-6]
    chapters = {
        "Chapter_1": (3+22, 26+22),
        "Chapter_2": (27+22, 54+22),
        "Chapter_3": (57+22, 77+22),
        "Chapter_4": (78+22, 100+22),
        "Chapter_5": (101+22, 148+22),
        "Chapter_6": (149+22, 176+22),
        "Chapter_7": (179+22, 209+22),
        "Chapter_8": (210+22, 243+22),
        "Chapter_9": (244+22, 284+22),
        "Chapter_10": (285+22, 308+22)
    }

    with open(input_pdf, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for name, (start, end) in chapters.items():
            writer = PyPDF2.PdfWriter()
            # PyPDF2 uses 0-based indexing; book uses physical page numbers
            for page_num in range(start - 1, end):
                writer.add_page(reader.pages[page_num])
            
            output_path = f"{output_folder}/{name}.pdf" if output_folder else f"{name}.pdf"
            with open(output_path, "wb") as output_file:
                writer.write(output_file)
            print(f"Created {name}.pdf")

# Call the function to actually split the PDF
split_pdf(input_pdf, output_folder)