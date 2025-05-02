import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    birthdate_str = entry.get()
    today = datetime.today()
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("输入错误", "❌ 请输入正确的日期格式，例如 2000-01-01")
        return

    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    result_label.config(
        text=f"✅ 截至 {today.strftime('%Y年%m月%d日')}，您是 {age} 岁。"
    )

# 获取系统当前日期
current_date = datetime.today()
current_date_str = current_date.strftime("日期：%Y年%m月%d日")

# 创建主窗口
root = tk.Tk()
root.title("🎂 年龄计算器")
root.geometry("400x280")
root.configure(bg="#f0f4f7")

# 字体样式
FONT_LARGE = ("微软雅黑", 14)
FONT_MEDIUM = ("微软雅黑", 12)

# 当前时间显示在最顶部
date_label = tk.Label(root, text=current_date_str, font=FONT_MEDIUM, fg="#2c3e50", bg="#f0f4f7")
date_label.pack(pady=(15, 5))

# 标题
title_label = tk.Label(root, text="年龄计算器", font=("微软雅黑", 18, "bold"), fg="#2c3e50", bg="#f0f4f7")
title_label.pack(pady=5)

# 输入提示
tk.Label(root, text="请输入出生日期（格式：YYYY-MM-DD）", font=FONT_MEDIUM, bg="#f0f4f7").pack(pady=5)

# 输入框
entry = tk.Entry(root, font=FONT_LARGE, justify="center", width=20)
entry.pack(pady=5)

# 按钮
calc_button = tk.Button(root, text="计算年龄", font=FONT_MEDIUM, bg="#3498db", fg="white", width=15, command=calculate_age)
calc_button.pack(pady=10)

# 结果显示
result_label = tk.Label(root, text="", font=FONT_LARGE, fg="#16a085", bg="#f0f4f7")
result_label.pack(pady=10)

# 启动主循环
root.mainloop()
