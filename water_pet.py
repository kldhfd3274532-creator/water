import random
import tkinter as tk
from datetime import datetime, timedelta

try:
    from plyer import notification
except Exception:  # noqa: BLE001
    notification = None


class WaterPetApp:
    def __init__(self, root: tk.Tk, interval_minutes: int = 60) -> None:
        self.root = root
        self.interval = timedelta(minutes=interval_minutes)
        self.next_reminder = datetime.now() + self.interval

        self.root.title("喝水小人")
        self.root.geometry("220x260")
        self.root.attributes("-topmost", True)
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=220, height=180, bg="#f3fbff", highlightthickness=0)
        self.canvas.pack(pady=8)

        self.tip_label = tk.Label(root, text="准备开始补水吧 💧", font=("Microsoft YaHei", 11))
        self.tip_label.pack(pady=4)

        self.countdown_label = tk.Label(root, text="", font=("Consolas", 11), fg="#336699")
        self.countdown_label.pack(pady=2)

        controls = tk.Frame(root)
        controls.pack(pady=6)

        tk.Button(controls, text="现在喝一杯", command=self.drink_now).grid(row=0, column=0, padx=4)
        tk.Button(controls, text="拖动窗口", command=lambda: None).grid(row=0, column=1, padx=4)

        self.root.bind("<B1-Motion>", self._drag_window)

        self.body = None
        self.face = []
        self.draw_pet(happy=True)
        self.animate()
        self.update_countdown()

    def _drag_window(self, event: tk.Event) -> None:
        x = event.x_root - 110
        y = event.y_root - 20
        self.root.geometry(f"+{x}+{y}")

    def draw_pet(self, happy: bool = True) -> None:
        self.canvas.delete("all")
        self.body = self.canvas.create_oval(50, 35, 170, 155, fill="#8fd3ff", outline="#58a6d6", width=2)
        self.canvas.create_oval(78, 72, 92, 86, fill="#1f4d6b", outline="")
        self.canvas.create_oval(128, 72, 142, 86, fill="#1f4d6b", outline="")

        if happy:
            mouth = self.canvas.create_arc(90, 90, 130, 122, start=200, extent=140, style=tk.ARC, width=3)
        else:
            mouth = self.canvas.create_arc(90, 104, 130, 134, start=20, extent=140, style=tk.ARC, width=3)
        self.face = [mouth]

        self.canvas.create_text(110, 20, text="Hydro Buddy", fill="#2f78a8", font=("Arial", 11, "bold"))

    def animate(self) -> None:
        # 轻微上下浮动，模拟“桌面小人”效果
        dy = random.choice([-2, -1, 1, 2])
        self.canvas.move("all", 0, dy)

        coords = self.canvas.coords(self.body)
        if coords and (coords[1] < 25 or coords[3] > 165):
            self.canvas.move("all", 0, -dy)

        self.root.after(700, self.animate)

    def notify(self) -> None:
        msg = "该喝水啦！站起来活动一下，喝 200~300ml 水 💧"
        self.tip_label.config(text=msg)
        self.draw_pet(happy=False)

        if notification:
            notification.notify(
                title="喝水提醒",
                message=msg,
                timeout=8,
                app_name="Hydro Buddy",
            )
        else:
            # 退化方案：没有 plyer 时仅显示窗口文本提醒
            self.root.bell()

    def drink_now(self) -> None:
        self.tip_label.config(text="干得漂亮！下一杯已安排 ✅")
        self.draw_pet(happy=True)
        self.next_reminder = datetime.now() + self.interval

    def update_countdown(self) -> None:
        now = datetime.now()
        if now >= self.next_reminder:
            self.notify()
            self.next_reminder = now + self.interval

        remain = self.next_reminder - now
        mm, ss = divmod(max(0, int(remain.total_seconds())), 60)
        self.countdown_label.config(text=f"下次提醒：{mm:02d}:{ss:02d}")
        self.root.after(1000, self.update_countdown)


def main() -> None:
    root = tk.Tk()
    app = WaterPetApp(root, interval_minutes=60)
    root.mainloop()


if __name__ == "__main__":
    main()
