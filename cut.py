from pypdf import PdfReader, PdfWriter

file_name = "artifact.pdf"
def extract_pages(input_path, output_path, pages_to_extract):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page_num in pages_to_extract:
        if 1 <= page_num <= len(reader.pages):
            writer.add_page(reader.pages[page_num - 1])
        else:
            print(f"スキップ: {page_num} は範囲外です（全{len(reader.pages)}ページ）")

    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"{output_path} に {len(pages_to_extract)} ページを書き出しました")

# 使用例
extract_pages(file_name,file_name, [1, 2])
