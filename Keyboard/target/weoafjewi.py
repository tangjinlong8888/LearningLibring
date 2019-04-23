import datetime

# print(datetime.datetime.now())
# import os
# import multiprocessing
#
# read_fd, write_fd = os.pipe()
#
#
# def func():
#     os.close(write_fd)
#     while True:
#         data = os.read(read_fd, 4)
#         print("READ: {}".format(int.from_bytes(data, 'big')))
#
#
# print("Parent process:{} {}".format(os.getpid(), os.getppid()))
# m = multiprocessing.Process(target=func)
# m.start()
# os.close(read_fd)
# while True:
#     data = input("Enter Integer: ")
#     try:
#         int_data = int(data.strip())
#         os.write(write_fd, int_data.to_bytes(4, "big"))
#     except:
#         pass

import signal


#def sig_func(*args, **kwargs):
#    print(args, kwargs)

#signal.signal(signal.SIGTERM, sig_func)
# signal.signal(signal.SIGSTOP, sig_func)

#while True:
#    try:
#        pid = input("Please enter the PID that you will kill:")
#        import os
#        os.kill(int(pid.strip()), signal.SIGKILL)
#    except Exception as e:
#        print(e)
#        pass

def inflection():
    while True:
        print("Inflecting ...")
        import time
        time.sleep(1)

def restart_sub_process():
    fork_sub_process()

def fork_sub_process():
    pid = fork()
    if pid == 0:
        inflection()
        sys.exit(0)
    elif pid > 0:
        return

fork_sub_process()
signal.signal(signal.SIGCHILD, restart_sub_process)
while True:
     import time
     time.sleep(1)


# if pid == 0:
# execution in sub process
#    func()
# while True:
#     print("Sub process: {} {}".format(os.getpid(), os.getppid()))
#     import time
#     time.sleep(1)
#    pass
# elif pid > 0:
# execution in parent process.
#    print("Parent process: {} {}".format(os.getpid(), os.getppid()))
#    pid, status, rusage = os.wait4(pid, 0)
#    print(pid, status, rusage)
#    pass
# else:
#    raise Exception()
