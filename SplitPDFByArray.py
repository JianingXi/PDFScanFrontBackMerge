import os
from PyPDF2 import PdfReader, PdfWriter


def split_pdf_by_pages(pdf_path, start_pages, output_dir):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 读取原PDF
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)

    # 获取原文件名（不带扩展名）
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # 补上一个最后的结束页，方便计算每段范围
    start_pages = sorted(start_pages)
    start_pages.append(total_pages + 1)  # 用总页数+1作为最后一个结束标志

    # 遍历每个段
    for idx in range(len(start_pages) - 1):
        start = start_pages[idx] - 1  # 页码转为索引
        end = start_pages[idx + 1] - 1  # 不包含end
        writer = PdfWriter()

        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        # 按要求生成新文件名，起始页码用3位数格式
        new_filename = f"{base_name}_{start_pages[idx]:03d}.pdf"
        output_path = os.path.join(output_dir, new_filename)

        with open(output_path, 'wb') as f:
            writer.write(f)
        print(f"Saved: {output_path}")


# 使用示例
pdf_path = r"C:\Users\xijia\Desktop\信号与系统\信号与系统-第01章-生物医学中的信号-课件.pdf"  # 修改为你的PDF路径
start_pages = [1, 7, 16, 56, 69]  # 首页页码
output_dir = r"C:\Users\xijia\Desktop\信号与系统\File"  # 输出文件夹

split_pdf_by_pages(pdf_path, start_pages, output_dir)
