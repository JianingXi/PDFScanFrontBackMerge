import os
from pypdf import PdfReader, PdfWriter
from PDFSpliter import split_pdf, rename_files_in_reverse_order, move_files_to_new_folder

def merge_pdfs(folder_path, output_path):
    # 检查文件夹是否存在
    if not os.path.isdir(folder_path):
        raise FileNotFoundError('The specified folder does not exist.')

    # 获取文件夹中的所有PDF文件
    files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # 按照字母顺序排序
    files.sort()

    # 创建一个 PdfWriter 对象
    pdf_writer = PdfWriter()

    # 遍历每个文件并添加到 PdfWriter 对象
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        pdf_reader = PdfReader(file_path)

        # 添加每一页到 pdf_writer
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    # 将所有页写入输出PDF文件
    with open(output_path, 'wb') as output_pdf_file:
        pdf_writer.write(output_pdf_file)

    print(f"PDF文件已成功合并为：{output_path}")

# 拆分1
input_pdf_1 = r'C:\Users\DELL\Desktop\研究生项目A02_校内获批与打印\扫描申请书\Scan1111.pdf'
output1_folder = r'C:\Users\DELL\Desktop\研究生项目A02_校内获批与打印\扫描申请书\正面'
split_pdf(input_pdf_1, output1_folder)

# 拆分2
input_pdf_2 = r'C:\Users\DELL\Desktop\研究生项目A02_校内获批与打印\扫描申请书\Scan2222.pdf'
output2_folder = r'C:\Users\DELL\Desktop\研究生项目A02_校内获批与打印\扫描申请书\反面'
split_pdf(input_pdf_2, output2_folder)

# 反转
rename_files_in_reverse_order(output2_folder)

# 文件合并
destination_folder = r'C:\Users\DELL\Desktop\研究生项目A02_校内获批与打印\扫描申请书\MergeDir'
move_files_to_new_folder(output1_folder, output2_folder, destination_folder)

# 输出
output_path = r'C:\Users\DELL\Desktop\研究生项目A02_校内获批与打印\扫描申请书\合并PDF.pdf'
merge_pdfs(destination_folder, output_path)
