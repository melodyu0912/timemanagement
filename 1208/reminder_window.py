# reminder_window.py

import tkinter as tk
from tkinter import messagebox

def show_reminder_window_tkinter(course_name):
    """使用 Tkinter 建立置頂提醒視窗[cite: 41, 80]."""
    # 建立主視窗
    window = tk.Tk()
    window.title("時間管理大師提醒")
    
    # 設定視窗置頂
    window.attributes("-topmost", True)
    
    # 視窗內容
    tk.Label(window, text=f"現在該複習 {course_name} 了!").pack(pady=10, padx=20)
    tk.Label(window, text="請選擇動作:").pack(padx=20)
    
    # 按鈕
    def on_start():
        # 實作開始計時/記錄邏輯
        messagebox.showinfo("開始", f"開始複習 {course_name}!")
        window.destroy()

    def on_defer():
        # 實作延後排程邏輯
        messagebox.showwarning("延後", f"延後複習 {course_name} (需實作延後邏輯)")
        window.destroy()
        
    def on_done():
        # 實作標記完成/更新權重邏輯
        messagebox.showinfo("完成", f"已完成本次 {course_name} 複習任務!")
        window.destroy()

    tk.Button(window, text="開始", command=on_start).pack(side=tk.LEFT, padx=5, pady=10) # 開始按鈕
    tk.Button(window, text="延後", command=on_defer).pack(side=tk.LEFT, padx=5, pady=10) # 延後按鈕
    tk.Button(window, text="完成", command=on_done).pack(side=tk.LEFT, padx=5, pady=10) # 完成按鈕

    # 執行視窗主迴圈
    window.mainloop()