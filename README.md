# 🎈 世界上最小的翻译软件 (World's Smallest Translator)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-%3C40-success)
![License](https://img.shields.io/badge/License-MIT-green)

> **“没有臃肿的界面，没有昂贵的 API，只有 40 多行极致的效率。”**

你是否厌倦了打开笨重的翻译软件、复制、粘贴、再切回来的繁琐流程？
**世界上最小的翻译软件** 诞生了。它没有任何 UI 界面，在后台默默运行。你只需要选中文字，按下 `Ctrl + C`，它就会立刻在浏览器中为你展示 Bing 的“中文释义”搜索结果。

## ✨ 为什么叫“世界最小”？

* **代码极简**：核心逻辑不到 40 行 Python 代码。
* **内存极简**：没有 Electron，没有数百兆的安装包，几乎不占用系统资源。
* **操作极简**：没有复杂的设置，选中文字，按下复制键，翻译即刻呈现。

*(💡 如果你有比这更短的实现，欢迎提 Issue 挑战，我随时准备让出“世界最小”的宝座！)*

## 🚀 如何使用？

### 方式一：直接下载（推荐普通用户）
⚠️ 安全提示：由于本软件使用 PyInstaller 打包且无数字签名，Windows 可能会提示“不安全”。这是个人开源小工具的常见情况。请点击“更多信息” -> “仍要运行”，或在 Windows 安全中心添加信任。
1. 去右侧的 [Releases](https://github.com/Unlimitedlearning/Worlds-Smallest-Translator/releases) 页面下载 `translator.exe`。
2. **右键**点击 `translator.exe`，选择“**以管理员身份运行**”（因为监听全局快捷键需要权限）。
3. 保持黑框在后台运行。选中任意文字，按下 `Ctrl + C` 试试！

### 方式二：从源码运行（推荐开发者）

如果你有 Python 环境，可以自己运行：

```bash
# 1. 克隆仓库
git clone https://github.com/Unlimitedlearning/Worlds-Smallest-Translator.git

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行
python translator.py
```

## ⚠️ 重要说明（必看）

* **按需开启**：程序运行期间，你所有的 `Ctrl + C` 都会触发网页搜索。**建议在需要查文献、看外文时打开，打游戏或写作业时按 `Ctrl + Q` 关闭**。
* **只支持 Windows**：目前打包的是 exe 文件，由于 `keyboard` 库的特性，在 Windows 上体验最佳。

## 🛠️ 技术栈

* 使用 `keyboard` 监听全局快捷键
* 使用 `pyperclip` 读取剪贴板内容
* 使用 `webbrowser` 唤起默认浏览器
* 使用 `urllib.parse` 处理 URL 编码

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 开源。你可以随意使用、修改，甚至拿去卖钱，但请保留原作者的署名。

---
⭐ **如果这个“小工具”帮你节省了时间，或者博你一笑，不妨点个 Star 支持一下！**