
# PDFScanFrontBackMerge

## Overview

This project provides a set of Python scripts to handle PDFs scanned with a single-sided scanner. It includes scripts to split PDFs, rename files in reverse order, move files to a new folder, and merge PDFs into a complete document.

本项目提供了一组Python脚本，用于处理使用单面扫描仪扫描的PDF文件。它包括拆分PDF、反向重命名文件、将文件移动到新文件夹以及将PDF合并为完整文档的脚本。

## Features

- **Split PDF**: Split a PDF into individual pages.
- **Rename Files in Reverse Order**: Rename files in reverse alphabetical order.
- **Move Files to New Folder**: Move files from two folders into a new folder.
- **Merge PDFs**: Merge multiple PDF files into a single PDF document.

功能特点：

- **拆分PDF**：将PDF拆分为单页文件。
- **反向重命名文件**：按逆字母顺序重命名文件。
- **移动文件到新文件夹**：将两个文件夹中的文件移动到一个新文件夹。
- **合并PDF**：将多个PDF文件合并为一个PDF文档。

## Requirements

- Python 3.x
- PyPDF2

安装要求：

- Python 3.x
- PyPDF2

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/PDFScanFrontBackMerge.git
   cd PDFScanFrontBackMerge
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

安装步骤：

1. 克隆仓库：

   ```bash
   git clone https://github.com/yourusername/PDFScanFrontBackMerge.git
   cd PDFScanFrontBackMerge
   ```

2. 安装所需的软件包：

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Split PDF

To split a PDF into individual pages, use the `PDFSpliter.py` script. Specify the input PDF file and the output folder.

```bash
python PDFSpliter.py split /path/to/input.pdf /path/to/output_folder
```

### Rename Files in Reverse Order

To rename files in reverse alphabetical order, use the `PDFSpliter.py` script. Specify the folder containing the files.

```bash
python PDFSpliter.py rename /path/to/folder
```

### Move Files to New Folder

To move files from two folders into a new folder, use the `PDFSpliter.py` script. Specify the source folders and the destination folder.

```bash
python PDFSpliter.py move /path/to/source_folder1 /path/to/source_folder2 /path/to/destination_folder
```

### Merge PDFs

To merge multiple PDF files into a single PDF document, use the `demo_PDFScanFrontBackMerge.py` script. Specify the folder containing the PDF files and the output file.

```bash
python demo_PDFScanFrontBackMerge.py /path/to/pdf_folder /path/to/output.pdf
```

使用方法：

### 拆分PDF

要将PDF拆分为单页文件，请使用 `PDFSpliter.py` 脚本。指定输入PDF文件和输出文件夹。

```bash
python PDFSpliter.py split /path/to/input.pdf /path/to/output_folder
```

### 反向重命名文件

要按逆字母顺序重命名文件，请使用 `PDFSpliter.py` 脚本。指定包含文件的文件夹。

```bash
python PDFSpliter.py rename /path/to/folder
```

### 移动文件到新文件夹

要将两个文件夹中的文件移动到一个新文件夹，请使用 `PDFSpliter.py` 脚本。指定源文件夹和目标文件夹。

```bash
python PDFSpliter.py move /path/to/source_folder1 /path/to/source_folder2 /path/to/destination_folder
```

### 合并PDF

要将多个PDF文件合并为一个PDF文档，请使用 `demo_PDFScanFrontBackMerge.py` 脚本。指定包含PDF文件的文件夹和输出文件。

```bash
python demo_PDFScanFrontBackMerge.py /path/to/pdf_folder /path/to/output.pdf
```

## Script Details

### PDFSpliter.py

This script provides three functions: splitting a PDF into individual pages, renaming files in reverse alphabetical order, and moving files to a new folder.

#### split_pdf(input_pdf_path, output_folder)

- **Input**: Path to the input PDF file.
- **Output**: Folder where the split pages will be saved.

#### rename_files_in_reverse_order(folder_path)

- **Input**: Path to the folder containing the files to be renamed.
- **Output**: Files renamed in reverse alphabetical order.

#### move_files_to_new_folder(source_folder1, source_folder2, destination_folder)

- **Input**: Paths to the two source folders and the destination folder.
- **Output**: Files moved to the new destination folder.

### demo_PDFScanFrontBackMerge.py

This script combines the functionalities provided by `PDFSpliter.py` to merge front and back scanned PDFs into a complete document.

#### merge_pdfs(folder_path, output_path)

- **Input**: Path to the folder containing the PDF files.
- **Output**: Path to the output merged PDF file.

脚本详情：

### PDFSpliter.py

此脚本提供三个功能：将PDF拆分为单页文件、按逆字母顺序重命名文件以及将文件移动到新文件夹。

#### split_pdf(input_pdf_path, output_folder)

- **输入**：输入PDF文件的路径。
- **输出**：保存拆分页的文件夹。

#### rename_files_in_reverse_order(folder_path)

- **输入**：包含要重命名文件的文件夹路径。
- **输出**：按逆字母顺序重命名的文件。

#### move_files_to_new_folder(source_folder1, source_folder2, destination_folder)

- **输入**：两个源文件夹和目标文件夹的路径。
- **输出**：移动到新目标文件夹的文件。

### demo_PDFScanFrontBackMerge.py

此脚本结合 `PDFSpliter.py` 提供的功能，将正反面扫描的PDF合并为一个完整的文档。

#### merge_pdfs(folder_path, output_path)

- **输入**：包含PDF文件的文件夹路径。
- **输出**：输出合并PDF文件的路径。


## Detailed Steps for Each Script

### PDFSpliter.py

#### split_pdf(input_pdf_path, output_folder)

1. **Load PDF File**: The script opens the input PDF file.
2. **Create Output Folder**: It creates the output folder if it doesn't exist.
3. **Split Pages**: The script iterates through each page of the PDF and saves them as individual PDF files named sequentially (e.g., PDF0001.pdf, PDF0002.pdf).
4. **Save Pages**: Each page is saved in the specified output folder.

#### rename_files_in_reverse_order(folder_path)

1. **Check Folder**: The script checks if the specified folder exists.
2. **Get Files**: It retrieves all files in the folder and sorts them in reverse alphabetical order.
3. **Rename Files**: The script renames each file in reverse order, appending `_rev` to the filenames.

#### move_files_to_new_folder(source_folder1, source_folder2, destination_folder)

1. **Create Destination Folder**: The script creates the destination folder if it doesn't exist.
2. **Move Files from Source Folder 1**: It moves all files from the first source folder to the destination folder.
3. **Move Files from Source Folder 2**: It moves all files from the second source folder to the destination folder.

### demo_PDFScanFrontBackMerge.py

This script combines the functionalities provided by `PDFSpliter.py` to merge front and back scanned PDFs into a complete document.

#### merge_pdfs(folder_path, output_path)

1. **Check Folder**: The script checks if the specified folder exists.
2. **Get PDF Files**: It retrieves all PDF files in the folder and sorts them alphabetically.
3. **Create PdfWriter Object**: A PdfWriter object is created to compile the pages.
4. **Add Pages**: The script iterates through each PDF file and adds all pages to the PdfWriter object.
5. **Save Merged PDF**: The combined pages are saved as a single PDF file at the specified output path.

## Examples

Here are some examples of how to use the scripts.

### Example 1: Split PDF into Individual Pages

```python
from PDFSpliter import split_pdf

input_pdf_path = '/path/to/input.pdf'
output_folder = '/path/to/output_folder'

split_pdf(input_pdf_path, output_folder)
```

### Example 2: Rename Files in Reverse Order

```python
from PDFSpliter import rename_files_in_reverse_order

folder_path = '/path/to/folder'

rename_files_in_reverse_order(folder_path)
```

### Example 3: Move Files to a New Folder

```python
from PDFSpliter import move_files_to_new_folder

source_folder1 = '/path/to/source_folder1'
source_folder2 = '/path/to/source_folder2'
destination_folder = '/path/to/destination_folder'

move_files_to_new_folder(source_folder1, source_folder2, destination_folder)
```

### Example 4: Merge PDFs into a Single Document

```python
from demo_PDFScanFrontBackMerge import merge_pdfs

folder_path = '/path/to/pdf_folder'
output_path = '/path/to/output.pdf'

merge_pdfs(folder_path, output_path)
```

示例：

### 示例1：将PDF拆分为单页文件

```python
from PDFSpliter import split_pdf

input_pdf_path = '/path/to/input.pdf'
output_folder = '/path/to/output_folder'

split_pdf(input_pdf_path, output_folder)
```

### 示例2：反向重命名文件

```python
from PDFSpliter import rename_files_in_reverse_order

folder_path = '/path/to/folder'

rename_files_in_reverse_order(folder_path)
```

### 示例3：移动文件到新文件夹

```python
from PDFSpliter import move_files_to_new_folder

source_folder1 = '/path/to/source_folder1'
source_folder2 = '/path/to/source_folder2'
destination_folder = '/path/to/destination_folder'

move_files_to_new_folder(source_folder1, source_folder2, destination_folder)
```

### 示例4：将多个PDF合并为一个文档

```python
from demo_PDFScanFrontBackMerge import merge_pdfs

folder_path = '/path/to/pdf_folder'
output_path = '/path/to/output.pdf'

merge_pdfs(folder_path, output_path)
```

## Troubleshooting

### Issue: Incorrect Page Order

Ensure that the PDF files are named sequentially and follow the correct order before processing.

### Issue: Missing Files

Verify that all files are present in the specified directories and are named correctly. Check the console output for any error messages.

### Issue: Unsupported File Format

Ensure that all files in the specified directories are in the correct format (PDF for splitting and merging).

故障排除：

### 问题：页面顺序错误

确保PDF文件按顺序命名，并在处理前遵循正确的顺序。

### 问题：缺少文件

验证所有文件是否存在于指定目录中，并正确命名。检查控制台输出以获取任何错误消息。

### 问题：不支持的文件格式

确保指定目录中的所有文件都为正确的格式（拆分和合并时为PDF）。

## Future Improvements

Here are some potential improvements for the project:

- **Enhanced Error Handling**: Improve error handling to provide more informative messages and handle edge cases.
- **Additional File Formats**: Add support for additional file formats like PNG, TIFF.
- **Automatic Sorting**: Implement automatic sorting of PDF files to ensure correct order.
- **GUI Interface**: Develop a graphical user interface for easier use.

未来改进：

以下是该项目的一些潜在改进：

- **增强错误处理**：改进错误处理以提供更有用的信息并处理边缘情况。
- **更多文件格式**：添加对其他文件格式（如PNG，TIFF）的支持。
- **自动排序**：实现PDF文件的自动排序，确保正确的顺序。
- **图形用户界面**：开发图形用户界面以便更容易使用。

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you encounter any problems.

欢迎贡献！如果你遇到任何问题，请随时提交拉取请求或打开问题。

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

许可证：

本项目采用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。