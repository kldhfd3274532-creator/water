# 喝水桌面小人（Hydro Buddy）

这是一个简单的 Python 桌面小人，会**每隔 60 分钟提醒你喝水**。

## 功能
- 漂浮的“水滴小人”窗口（始终置顶）。
- 每 60 分钟提醒一次喝水。
- 倒计时显示下一次提醒时间。
- 点击“现在喝一杯”可手动重置倒计时。

---

## 安装教程（Windows / macOS / Linux）

> 下面命令都在终端里运行。

### 1）安装 Python 3.10+
- 到官网下载安装：<https://www.python.org/downloads/>
- 安装后验证：

```bash
python --version
```

> 如果你的系统用 `python3`，就把下面命令中的 `python` 改成 `python3`。

### 2）下载项目并进入目录
如果你已经有项目文件，直接进入目录即可：

```bash
cd water
```

### 3）安装依赖
```bash
python -m pip install -r requirements.txt
```

### 4）启动桌面小人
```bash
python water_pet.py
```

看到小水滴后就表示运行成功了。

---

## 开机自动启动（可选）

### Windows
1. 按 `Win + R`，输入 `shell:startup` 并回车。
2. 在打开的启动文件夹里，新建一个 `.bat` 文件（例如 `start_water_pet.bat`），填入：

```bat
cd /d 你的项目路径\water
python water_pet.py
```

3. 下次开机会自动启动。

### macOS（使用 Login Items）
1. 系统设置 → 通用 → 登录项。
2. 添加一个终端脚本或打包后的应用（见下文“打包”）。

### Linux（GNOME）
1. 打开“启动应用程序”。
2. 添加命令：

```bash
python /你的路径/water/water_pet.py
```

---

## 打包成单文件应用（可选）
你可以用 PyInstaller 打包，方便双击启动：

```bash
python -m pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed water_pet.py
```

打包后文件在 `dist/` 目录。
