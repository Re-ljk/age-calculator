import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# 星座计算函数
def get_zodiac(month, day):
    zodiac_signs = {
        (1, 20): "水瓶座", (2, 19): "双鱼座", (3, 21): "白羊座", (4, 20): "金牛座", 
        (5, 21): "双子座", (6, 21): "巨蟹座", (7, 23): "狮子座", (8, 23): "处女座", 
        (9, 23): "天秤座", (10, 23): "天蝎座", (11, 22): "射手座", (12, 22): "摩羯座"
    }

    for (m, d), sign in reversed(sorted(zodiac_signs.items())):
        if (month, day) >= (m, d):
            return sign
    return "摩羯座"  # 默认摩羯座

# 计算年龄并显示倒计时
def calculate_age():
    birthdate_str = entry.get()
    today = datetime.today()
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("输入错误", "❌ 请输入正确的日期格式，例如 2000-01-01")
        return

    # 计算年龄
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    # 获取星座
    zodiac = get_zodiac(birthdate.month, birthdate.day)

    # 计算下一个生日的倒计时
    next_birthday = datetime(today.year, birthdate.month, birthdate.day)
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)

    countdown_time = next_birthday - today
    countdown_text = f"{countdown_time.days} 天 {countdown_time.seconds // 3600} 小时 " \
                     f"{(countdown_time.seconds // 60) % 60} 分钟 " \
                     f"{countdown_time.seconds % 60} 秒"

    # 显示计算结果
    result_label.config(
        text=f"✅ 截至 {today.strftime('%Y年%m月%d日')}，您是 {age} 岁。\n星座：{zodiac}"
    )
    countdown_label.config(text=f"🎉 距离下一个生日还有：\n{countdown_text}")

    # 保存历史记录
    history.append({
        "birthdate": birthdate_str,
        "age": age,
        "zodiac": zodiac,
        "countdown": countdown_text
    })
    update_history()

# 更新历史记录显示
def update_history():
    history_listbox.delete(0, tk.END)  # 清空历史记录
    for record in history:
        history_listbox.insert(tk.END, f"{record['birthdate']} - {record['age']} 岁 - 星座: {record['zodiac']}")

# 删除历史记录
def delete_history():
    try:
        selected_index = history_listbox.curselection()[0]
        history.pop(selected_index)
        update_history()
    except IndexError:
        messagebox.showwarning("选择错误", "❌ 请先选择一个历史记录。")

# 获取系统当前日期
current_date = datetime.today()
current_date_str = current_date.strftime("日期：%Y年%m月%d日")

# 创建主窗口
root = tk.Tk()
root.title("🎂 年龄计算器")
root.geometry("500x450")
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

# 倒计时显示
countdown_label = tk.Label(root, text="", font=("微软雅黑", 16), fg="#e74c3c", bg="#f0f4f7")
countdown_label.pack(pady=15)

# 历史记录显示
history_label = tk.Label(root, text="历史记录", font=FONT_MEDIUM, bg="#f0f4f7")
history_label.pack(pady=10)

# 显示历史记录的列表框
history_listbox = tk.Listbox(root, font=FONT_MEDIUM, width=50, height=5)
history_listbox.pack(pady=5)

# 删除历史记录按钮
delete_button = tk.Button(root, text="删除选中记录", font=FONT_MEDIUM, bg="#e74c3c", fg="white", width=15, command=delete_history)
delete_button.pack(pady=10)

# 历史记录初始化
history = []

# 启动主循环
root.mainloop()
