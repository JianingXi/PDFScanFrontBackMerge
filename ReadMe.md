# PDFScanFrontBackMerge

## Overview

This project provides a Python script for merging the front and back pages of PDFs scanned with a printer that does not support duplex scanning. The script combines the pages in the correct order to produce a complete PDF document.

本项目提供了一个Python脚本，用于将无法双面扫描的打印机扫描的PDF正反面按顺序拼接为一个完整的PDF文件。脚本将页面按正确的顺序组合，生成完整的PDF文档。

## Features

- **Merge Front and Back Pages**: Automatically merge front and back pages of scanned PDFs.
- **Correct Order**: Ensure the pages are in the correct order.
- **Easy to Use**: Simple command-line interface for easy usage.

功能特点：

- **拼接正反面页面**：自动拼接扫描的PDF正反面页面。
- **顺序正确**：确保页面顺序正确。
- **易于使用**：简单的命令行界面，便于使用。

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

To merge the front and back pages of scanned PDFs, run the script with the directory containing your front and back PDF files:

```bash
python merge_scanned_pdfs.py /path/to/front_pdfs /path/to/back_pdfs /path/to/output_pdf
```

For example:

```bash
python merge_scanned_pdfs.py /path/to/front_pdfs /path/to/back_pdfs /path/to/output/merged.pdf
```

使用方法：

要拼接扫描的PDF正反面页面，请运行脚本并提供包含正面和反面PDF文件的目录：

```bash
python merge_scanned_pdfs.py /path/to/front_pdfs /path/to/back_pdfs /path/to/output_pdf
```

例如：

```bash
python merge_scanned_pdfs.py /path/to/front_pdfs /path/to/back_pdfs /path/to/output/merged.pdf
```

## Script Details

### merge_scanned_pdfs.py

This script merges the front and back pages of scanned PDFs. It reads the pages from the front and back PDF directories and combines them in the correct order to produce a complete PDF document.

- **Input**: 
  - Directory containing front PDF files.
  - Directory containing back PDF files.
  - Output PDF file path.
- **Output**: Merged PDF file with pages in the correct order.

脚本详情：

### merge_scanned_pdfs.py

此脚本拼接扫描的PDF正反面页面。它从正面和反面PDF目录读取页面，并按正确的顺序将它们组合在一起，生成一个完整的PDF文档。

- **输入**：
  - 包含正面PDF文件的目录。
  - 包含反面PDF文件的目录。
  - 输出PDF文件路径。
- **输出**：按正确顺序拼接的PDF文件。

## Examples

Here are some examples of how to use the script.

### Example 1: Merge Scanned PDFs

Suppose you have the following directory structure:

```
/path/to/front_pdfs
├── page1.pdf
├── page2.pdf
...
/path/to/back_pdfs
├── page1.pdf
├── page2.pdf
...
```

To merge these files, run:

```bash
python merge_scanned_pdfs.py /path/to/front_pdfs /path/to/back_pdfs /path/to/output/merged.pdf
```

### 示例1：拼接扫描的PDF

假设你有以下目录结构：

```
/path/to/front_pdfs
├── page1.pdf
├── page2.pdf
...
/path/to/back_pdfs
├── page1.pdf
├── page2.pdf
...
```

要拼接这些文件，运行：

```bash
python merge_scanned_pdfs.py /path/to/front_pdfs /path/to/back_pdfs /path/to/output/merged.pdf
```

## Customization

You can customize the script to handle different naming conventions or add additional features by modifying the `merge_scanned_pdfs.py` script.

自定义：

你可以通过修改 `merge_scanned_pdfs.py` 脚本来自定义处理不同的命名约定或添加其他功能。

## Troubleshooting

### Issue: Incorrect Page Order

If the pages are not in the correct order, ensure that the front and back PDF files are named sequentially and match each other. For example, if the front PDF files are named `page1.pdf`, `page2.pdf`, etc., the back PDF files should also follow the same naming convention and order.

### Issue: Missing Pages

If some pages are missing from the merged PDF, make sure that all front and back PDF files are present in their respective directories and are named correctly. Check the console output for any error messages.

### Issue: Unsupported File Format

If you encounter issues with unsupported file formats, ensure that all files in the specified directories are PDFs. The script currently only supports PDF files.

故障排除：

### 问题：页面顺序错误

如果页面顺序不正确，请确保正面和反面PDF文件按顺序命名并相互匹配。例如，如果正面PDF文件命名为 `page1.pdf`，`page2.pdf` 等，反面PDF文件也应遵循相同的命名规则和顺序。

### 问题：缺少页面

如果合并后的PDF中缺少某些页面，请确保所有正面和反面PDF文件都存在于各自的目录中并正确命名。检查控制台输出以获取任何错误信息。

### 问题：不支持的文件格式

如果遇到不支持的文件格式问题，请确保指定目录中的所有文件都是PDF。脚本目前仅支持PDF文件。

## Future Improvements

Here are some potential improvements for the project:

- **Enhanced Error Handling**: Improve error handling to provide more informative messages and handle edge cases.
- **Additional File Formats**: Add support for additional file formats like images (JPG, PNG).
- **Automatic Sorting**: Implement automatic sorting of PDF files to ensure they are in the correct order.
- **GUI Interface**: Develop a graphical user interface for easier use.

未来改进：

以下是该项目的一些潜在改进：

- **增强错误处理**：改进错误处理以提供更有用的信息并处理边缘情况。
- **更多文件格式**：添加对其他文件格式（如图像（JPG，PNG））的支持。
- **自动排序**：实现PDF文件的自动排序，确保它们按正确顺序排列。
- **图形用户界面**：开发图形用户界面以便更容易使用。

## Detailed Steps for Merging PDFs

### Step 1: Load PDF Files

The script first loads all front and back PDF files from the specified directories.

### Step 2: Check Page Count

The script checks if the number of front pages matches the number of back pages. If they do not match, an error message is displayed, and the process is halted.

### Step 3: Merge Pages

For each front page, the script finds the corresponding back page and merges them in the correct order. The pages are interleaved such that the final PDF has the correct sequence.

### Step 4: Save the Result

The merged PDF file is saved to the specified output path.

拼接PDF的详细步骤：

### 第一步：加载PDF文件

脚本首先从指定目录加载所有正面和反面PDF文件。

### 第二步：检查页面数量

脚本检查正面页面的数量是否与反面页面的数量匹配。如果不匹配，将显示错误消息，并且过程将停止。

### 第三步：合并页面

对于每个正面页面，脚本找到相应的反面页面，并按正确的顺序将它们合并。页面交错排列，以确保最终PDF具有正确的顺序。

### 第四步：保存结果

合并后的PDF文件将保存到指定的输出路径。

## Example Code Snippets

Here are some example code snippets that demonstrate how to use the script.

### Example 1: Merge Scanned PDFs

```python
import os
from merge_scanned_pdfs import merge_pdfs

# Specify the directories containing your front and back PDF files
front_dir = '/path/to/front_pdfs'
back_dir = '/path/to/back_pdfs'
output_pdf = '/path/to/output/merged.pdf'

# Merge the PDFs
merge_pdfs(front_dir, back_dir, output_pdf)
```

### 示例1：拼接扫描的PDF

```python
import os
from merge_scanned_pdfs import merge_pdfs

# 指定包含正面和反面PDF文件的目录
front_dir = '/path/to/front_pdfs'
back_dir = '/path/to/back_pdfs'
output_pdf = '/path/to/output/merged.pdf'

# 拼接PDF
merge_pdfs(front_dir, back_dir, output_pdf)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

许可证：

本项目采用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。

## Contact

For any questions or issues, please contact [yourname] at [youremail@example.com].

联系方式：

如果有任何问题或疑问，请联系 [yourname]，邮箱 [youremail@example.com]。