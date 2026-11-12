import keyboard
import pyperclip
import webbrowser
import urllib.parse
import time

def search_text():
    # 稍微等待0.1秒，确保系统的 Ctrl+C 复制动作已经完成
    time.sleep(0.1)
    
    # 获取当前剪贴板内容
    try:
        selected_text = pyperclip.paste().strip()
    except Exception:
        return
    
    if not selected_text:
        return

    # 对文本进行 URL 编码（处理中文和特殊字符）
    encoded_text = urllib.parse.quote(selected_text)
    
    # 拼接 Bing 搜索词，注意这里去掉了多余的等号，改为标准的 ?q=
    query = f"{encoded_text} 中文释义"
    url = f"https://cn.bing.com/search?q={query}"
    
    # 打开浏览器搜索
    webbrowser.open(url)
    print(f"已搜索：{selected_text}")

# 监听 Ctrl+C 触发搜索
keyboard.add_hotkey('ctrl+c', search_text)

print("极简翻译助手已启动！")
print("选中文本后按 Ctrl + C 即可搜索中文释义。")
print("按 Ctrl + Q 退出程序。")

# 监听 Ctrl+Q 退出程序
keyboard.wait('ctrl+q')