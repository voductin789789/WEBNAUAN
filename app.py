from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dữ liệu mẫu giả lập Database
recipes = [
    {"id": 1, "title": "Phở Bò Hà Nội", "category": "Món chính", "ingredients": ["Thịt bò", "Bánh phở"], "level": "Khó", "views": 1200},
    {"id": 2, "title": "Gỏi Cuốn", "category": "Món Á", "ingredients": ["Tôm", "Thịt heo"], "level": "Dễ", "views": 850}
]

@app.route('/') # UC 4, 5: Xem & Tìm kiếm
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>') # UC 6, 9, 10: Chi tiết, Bình luận, Yêu thích
def detail(recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    return render_template('detail.html', recipe=recipe)

@app.route('/login') # UC 2: Đăng nhập
def login():
    return render_template('login.html')

@app.route('/register') # UC 1: Đăng ký
def register():
    return render_template('register.html')

@app.route('/profile') # UC 3, 7: Xem & Cập nhật thông tin
def profile():
    return render_template('profile.html')

@app.route('/post-recipe') # UC 8: Đăng công thức
def post_recipe():
    return render_template('post_recipe.html')

@app.route('/admin') # UC 11, 12: Quản trị Admin
def admin():
    return render_template('admin.html', recipes=recipes)

@app.route('/reset-password') # UC 13: Quên mật khẩu
def reset_password():
    return render_template('reset_password.html')

if __name__ == '__main__':
    app.run(debug=True)