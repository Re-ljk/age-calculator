from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta
import json

app = Flask(__name__)

# 存储用户历史记录
history = []

# 计算星座的函数
def get_zodiac(month, day):
    zodiac_dates = {
        (1, 20): "水瓶座",
        (2, 19): "双鱼座",
        (3, 21): "白羊座",
        (4, 20): "金牛座",
        (5, 21): "双子座",
        (6, 21): "巨蟹座",
        (7, 23): "狮子座",
        (8, 23): "处女座",
        (9, 23): "天秤座",
        (10, 23): "天蝎座",
        (11, 22): "射手座",
        (12, 22): "摩羯座"
    }
    for date, zodiac in zodiac_dates.items():
        if (month, day) >= date:
            zodiac_sign = zodiac
    return zodiac_sign

@app.route("/", methods=["GET", "POST"])
def home():
    age_detail = {}
    error_message = None
    zodiac_sign = None
    countdown = None

    if request.method == "POST":
        birth_year = request.form.get("birth_year")
        birth_month = request.form.get("birth_month")
        birth_day = request.form.get("birth_day")

        # 验证输入是否完整
        if birth_year and birth_month and birth_day:
            try:
                # 构建出生日期
                birth_date = datetime(int(birth_year), int(birth_month), int(birth_day))
                today = datetime.today()

                # 计算年、月、天
                years = today.year - birth_date.year
                if (today.month, today.day) < (birth_date.month, birth_date.day):
                    years -= 1

                months = today.month - birth_date.month
                if months < 0:
                    months += 12

                days = (today - birth_date).days
                hours = (today - birth_date).seconds // 3600
                minutes = (today - birth_date).seconds // 60

                # 获取星座
                zodiac_sign = get_zodiac(birth_date.month, birth_date.day)

                # 计算生日倒计时
                next_birthday = datetime(today.year, birth_date.month, birth_date.day)
                if today > next_birthday:
                    next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)
                countdown = next_birthday - today

                # 保存历史记录
                history.append({
                    'birth_date': f'{birth_year}-{birth_month}-{birth_day}',
                    'age': years,
                    'zodiac': zodiac_sign,
                    'countdown': str(countdown).split()[2]  # 只取时分秒部分
                })

                # 更新年龄详情
                age_detail = {
                    "years": years,
                    "months": months,
                    "days": days,
                    "hours": hours,
                    "minutes": minutes
                }

                flash("年龄计算成功！", "success")

            except ValueError:
                error_message = "请输入有效的日期！请检查年月日格式。"
        else:
            error_message = "请输入完整的出生日期！"

    return render_template("index.html", age_detail=age_detail, error_message=error_message,
                           zodiac_sign=zodiac_sign, countdown=countdown, history=history)


@app.route("/delete/<int:history_id>", methods=["POST"])
def delete_history(history_id):
    try:
        # 删除指定的历史记录
        history.pop(history_id)
        flash("历史记录已成功删除！", "success")
    except IndexError:
        flash("删除失败：记录不存在！", "danger")

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
