# ASCII Art Studio

一个功能强大的 ASCII 艺术生成器，支持图片转 ASCII 和文字转 ASCII 艺术字。

## 功能特性

- 🖼️ **图片转 ASCII** - 将任意图片转换为 ASCII 字符画
- ✨ **文字转 ASCII** - 将文字转换为精美的 ASCII 艺术字
- 🎨 **多种字符集** - 支持 standard、simple、complex、blocks、numeric
- 🔄 **颜色反转** - 支持反转颜色以适应不同背景
- 💾 **保存输出** - 可将生成的 ASCII 艺术保存为文本文件
- 🎯 **示例生成** - 内置示例图片生成功能

## 安装

1. 克隆仓库：

```bash
git clone https://github.com/yourusername/ascii-art-studio.git
cd ascii-art-studio
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

## 使用方法

### 运行主程序

```bash
python ascii_art.py
```

程序提供交互式菜单：
- **[1]** 图片转 ASCII - 输入图片路径，设置宽度、字符集等参数
- **[2]** 文字转 ASCII - 输入文字，选择 banner 或 small 样式
- **[3]** 生成示例 - 自动生成示例图片并转换
- **[4]** 帮助信息

### 运行演示

```bash
python demo.py
```

## 支持的字符集

| 字符集 | 描述 | 示例字符 |
|--------|------|----------|
| standard | 标准字符集，细节平衡 | `@%#*+=-:. ` |
| simple | 简约字符集 | `@#=- ` |
| complex | 复杂字符集，最大细节 | `$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. ` |
| blocks | Unicode 块字符 | `▓▒░ ` |
| numeric | 数字字符集 | `0123456789 ` |

## 示例输出

### 文字转 ASCII (Banner 样式)

```
 ███  █   █ █████ █   █ █   █
█   █ █   █ █   █ █   █  █ █
█████ █   █ █████ █   █   █
█   █ █   █ █   █ █   █  █ █
█   █  ███  █   █  ███  █   █
```

### 图片转 ASCII

将图片转换为由 ASCII 字符组成的文本艺术画。

## 支持的图片格式

- JPG/JPEG
- PNG
- BMP
- GIF
- TIFF
- WebP
- 等 Pillow 支持的所有格式

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 贡献

欢迎提交 Issue 和 Pull Request！
