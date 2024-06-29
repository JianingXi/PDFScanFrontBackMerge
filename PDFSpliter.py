import os
from pypdf import PdfReader, PdfWriter
import shutil

def split_pdf(input_pdf_path, output_folder):
    # 创建输出文件夹，如果不存在的话
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开输入PDF文件
    reader = PdfReader(input_pdf_path)
    total_pages = len(reader.pages)

    for page_number in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[page_number])

        # 创建新的文件名，格式为 PDF0001.pdf, PDF0002.pdf 等等
        output_pdf_path = os.path.join(output_folder, f'PDF{page_number + 1:04}.pdf')
        with open(output_pdf_path, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)

    print(f"PDF拆分完成，拆分后的文件保存在: {output_folder}")





def move_files_to_new_folder(source_folder1, source_folder2, destination_folder):
    # 创建目标文件夹，如果不存在的话
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 获取第一个源文件夹中的所有文件
    files1 = [f for f in os.listdir(source_folder1) if os.path.isfile(os.path.join(source_folder1, f))]
    # 获取第二个源文件夹中的所有文件
    files2 = [f for f in os.listdir(source_folder2) if os.path.isfile(os.path.join(source_folder2, f))]

    # 移动第一个源文件夹中的文件到目标文件夹
    for file_name in files1:
        source_file = os.path.join(source_folder1, file_name)
        destination_file = os.path.join(destination_folder, file_name)
        shutil.move(source_file, destination_file)

    # 移动第二个源文件夹中的文件到目标文件夹
    for file_name in files2:
        source_file = os.path.join(source_folder2, file_name)
        destination_file = os.path.join(destination_folder, file_name)
        shutil.move(source_file, destination_file)

    print(f"所有文件已成功移动到：{destination_folder}")

def rename_files_in_reverse_order(folder_path):
    # 检查文件夹是否存在
    if not os.path.isdir(folder_path):
        raise FileNotFoundError('The specified folder does not exist.')

    # 获取文件夹中的所有文件
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # 按照字母顺序排序并反转
    sorted_files = sorted(files, reverse=True)

    # 遍历每个文件并重命名
    for file_name in files:
        # 获取文件的扩展名
        file_base, file_ext = os.path.splitext(file_name)

        # 找到反转后的文件名
        sorted_file = sorted_files.pop(0)
        sorted_file_base, sorted_file_ext = os.path.splitext(sorted_file)

        # 创建新的文件名
        new_name = f"{sorted_file_base}_rev{sorted_file_ext}"
        old_name_full = os.path.join(folder_path, file_name)
        new_name_full = os.path.join(folder_path, new_name)

        # 重命名文件
        shutil.move(old_name_full, new_name_full)

    print('Files have been renamed in reverse alphabetical order.')

