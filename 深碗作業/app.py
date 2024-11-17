from flask import Flask, render_template, request, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用於會話管理和顯示消息

# 隨機生成的數字
random_number = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def index():
    global random_number  # 使用全域變數保存隨機數字
    
    if request.method == "POST":
        guess = request.form.get("guess")
        if guess:
            try:
                guess = int(guess)
            except ValueError:
                flash("請輸入一個有效的數字！", "error")
                return redirect(url_for("index"))
            
            if guess < random_number:
                flash("猜的數字太小了！再試一次。", "warning")
            elif guess > random_number:
                flash("猜的數字太大了！再試一次。", "warning")
            else:
                flash("恭喜你猜對了！遊戲重新開始。", "success")
                random_number = random.randint(1, 100)  # 重新生成數字
                return redirect(url_for("index"))
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
