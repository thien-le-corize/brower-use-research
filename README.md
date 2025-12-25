# 🚀 Browser-use UI Automation (Python)

Dự án này sử dụng **Browser-use + LLM Agent** để tự động kiểm thử giao diện website (UI Test).  
Mục tiêu là mô phỏng thao tác **đăng nhập** như người dùng thật, sau đó trả về kết quả PASS/FAIL.

---

## 1. Yêu cầu môi trường

- Python 3.10+
- pip / virtualenv (khuyến nghị dùng venv)
- Có OpenAI API Key để LLM chạy AI suy luận

---

## 2. Cài đặt môi trường

```bash
# tạo virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# cài thư viện cần thiết
pip install browser-use python-dotenv

# Sau đó chạy lệnh
python ./main.py
