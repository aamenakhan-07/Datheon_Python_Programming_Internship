
from pypdf import PdfReader

pdf_path = "/storage/emulated/0/Download/Internship Tasks/Internship Task1 Word List.pdf"

reader = PdfReader(pdf_path)

all_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        all_text += text + "\n"

output_path = "/storage/emulated/0/Internship Python/words.txt"


with open(output_path, "w", encoding="utf-8") as file:
    for line in all_text.splitlines():
        word = line.strip().lower()
        if word and word.isalpha():
            file.write(word + "\n")

print("Words extracted successfully!")

print("Total words extracted:", sum(
    1 for line in all_text.splitlines()
    if line.strip().isalpha()
))
print("Output file saved as: words.txt")

print("Saved file:", output_path)