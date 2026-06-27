import tkinter as tk


def set_result(text):
    result.config(text=text)


def solve(event=None):
    text = entry.get().strip()

    # =========================
    # 输入校验（无弹窗版本）
    # =========================

    if not text:
        set_result("❌ 请输入顾客购买总瓶数")
        restore_input()
        return

    try:
        z = int(text)
    except ValueError:
        set_result("❌ 请输入合法整数")
        entry.delete(0, tk.END)
        restore_input()
        return

    if z < 6:
        set_result("❌ 顾客购买总瓶数必须 ≥ 6")
        entry.delete(0, tk.END)
        restore_input()
        return

    # =========================
    # 核心计算
    # =========================

    m = z // 4
    d = (m - z) % 3

    y = m - d
    x = (z - 4 * y) // 3

    # =========================
    # 输出结果
    # =========================

    set_result(f"""📦 计算结果

顾客购买总瓶数：{z} 瓶

7×9 盒子：{x} 个
9×9 盒子：{y} 个

────────────────────
最少盒子总数：{x + y} 个
""")

    # 清空 + 保持连续输入体验
    entry.delete(0, tk.END)
    restore_input()


def restore_input():
    # ⭐ Windows稳定关键：强制焦点 + 光标
    entry.focus_force()
    entry.icursor(tk.END)
    entry.select_clear()


# ==========================
# 主窗口
# ==========================

root = tk.Tk()
root.title("盒子数量自动计算器")
root.geometry("820x600")
root.resizable(False, False)

# ==========================
# 标题
# ==========================

title = tk.Label(
    root,
    text="盒子数量自动计算器",
    font=("Arial", 26, "bold")
)
title.pack(pady=(20, 10))

subtitle = tk.Label(
    root,
    text="输入顾客购买总瓶数，自动计算 7×9 与 9×9 盒子最优分配",
    font=("Arial", 20),
    justify="center"
)
subtitle.pack()

# ==========================
# 输入区
# ==========================

input_frame = tk.Frame(root)
input_frame.pack(pady=30)

label = tk.Label(
    input_frame,
    text="顾客购买总瓶数：",
    font=("Arial", 20)
)
label.pack(side="left", padx=10)

entry = tk.Entry(
    input_frame,
    font=("Arial", 22),
    width=14,
    justify="center"
)
entry.pack(side="left")

entry.focus_force()
entry.bind("<Return>", solve)

# ==========================
# 按钮
# ==========================

button = tk.Button(
    root,
    text="开始计算",
    command=solve,
    font=("Arial", 25, "bold"),
    width=14,
    height=2
)
button.pack()

# ==========================
# 分隔线
# ==========================

separator = tk.Frame(root, height=2, bd=1, relief="sunken")
separator.pack(fill="x", padx=30, pady=25)

# ==========================
# 结果面板（无弹窗核心）
# ==========================

result = tk.Label(
    root,
    text="请输入顾客购买总瓶数，然后点击“开始计算”",
    font=("Arial", 19),
    justify="left",
    wraplength=720,
    bg="#f5f5f5",
    padx=15,
    pady=15
)
result.pack()

# ==========================
# 稳定性（Windows DPI兼容）
# ==========================

root.after(100, lambda: root.minsize(
    root.winfo_width(),
    root.winfo_height()
))

# ==========================
# 启动
# ==========================

root.mainloop()