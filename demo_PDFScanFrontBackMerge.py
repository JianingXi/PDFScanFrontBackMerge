
import os
import shutil

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



# 删除多余文件
def delete_files_and_folders(files, folders):
    for file in files:
        if os.path.isfile(file):
            try:
                os.remove(file)
                print(f"文件已删除: {file}")
            except Exception as e:
                print(f"删除文件时出错: {file}, 错误信息: {e}")
        else:
            print(f"文件未找到: {file}")

    for folder in folders:
        if os.path.isdir(folder):
            try:
                shutil.rmtree(folder)
                print(f"文件夹已删除: {folder}")
            except Exception as e:
                print(f"删除文件夹时出错: {folder}, 错误信息: {e}")
        else:
            print(f"文件夹未找到: {folder}")

# 拆分1
input_pdf_1 = r'C:\Users\xijia\Documents\Scan.pdf'
output1_folder = r'C:\Users\xijia\Documents\Temp01Front'
split_pdf(input_pdf_1, output1_folder)

# 拆分2
input_pdf_2 = r'C:\Users\xijia\Documents\Scan2.pdf'
output2_folder = r'C:\Users\xijia\Documents\Temp02Back'
split_pdf(input_pdf_2, output2_folder)

# 反转
rename_files_in_reverse_order(output2_folder)

# 文件合并
destination_folder = r'C:\Users\xijia\Documents\Temp03MergeDir'
move_files_to_new_folder(output1_folder, output2_folder, destination_folder)

# 输出
output_path = r'C:\Users\xijia\Documents\合并PDF02.pdf'
merge_pdfs(destination_folder, output_path)


# 删除文件和文件夹
delete_files_and_folders([input_pdf_1, input_pdf_2], [output1_folder, output2_folder, destination_folder])
