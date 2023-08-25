import tkinter as tk
from tkinter import messagebox, ttk


def calculate():
    ranks = {
        "1": 0,
        "2": 30,
        "3": 60,
        "4": 90,
        "5": 99,
        "6": 99.9,
        "7": 99.99,
        "8": 99.999,
        "9": 99.9999,
        "10": 99.99999,

    }
    try:
        hurt = int(entry_hurt.get().replace(",", ""))
        rank = combo_rank.get()

        if rank in ranks:
            ori = hurt / (1 - ranks[rank] / 100)
            result_text.set(f"原始伤害为：{ori}\n{ori / 10 ** 19} 京")
        else:
            messagebox.showerror("错误", "无效的减伤等级")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字")


# Create the main window
root = tk.Tk()
root.title("伤害计算器")

# 调整大小
root.geometry("300x250")
root.configure(bg='#f2f2f2')
root.iconbitmap('bg.ico')

# Create labels, entries, and button
label_hurt = tk.Label(root, text="请输入初始伤害", bg='#f2f2f2', fg='#000000')
label_hurt.pack(pady=10)

entry_hurt = tk.Entry(root)
entry_hurt.pack(pady=10)

label_rank = tk.Label(root, text="请选择减伤等级")
label_rank.pack(pady=10)

# 创建一个下拉选择器，并为其提供从0到10的选项
combo_rank = ttk.Combobox(root, values=[str(i) for i in range(11)])
combo_rank.pack(pady=10)
combo_rank.set("0")  # 设置默认值为0

btn_calculate = tk.Button(root, text="计算", command=calculate)
btn_calculate.pack(pady=20)

result_text = tk.StringVar()
label_result = tk.Label(root, textvariable=result_text)
label_result.pack(pady=10)

root.mainloop()






