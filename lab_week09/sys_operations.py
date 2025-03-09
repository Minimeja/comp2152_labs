import os
import sys
import platform
import socket
import multiprocessing as mp

# Lab 9: Question3.a.a ,3a.b.
#Machine Type and Processor Type
print(platform.machine())
print(platform.architecture())

#Lab 9: Question 3.a.c,3.a.d.
#Set and Get socket timeout
print(socket.getdefaulttimeout())
socket.setdefaulttimeout(50)
print(socket.getdefaulttimeout())

#Lab 9: Question 3.a.e
#OS name
print(os.name)
print(platform.system())

#Lab 9: Question 3.a.f
#process ID - Unique every run
print(os.getpid())

#Lab 9: Question 3.b.a
#File Descriptors
#open( or close) a file named fdpractice.txt
f_name = "fdpractice.txt"
with open("fdpractice.txt", "a+") as f:
   print(f.readline())
   f.write("hello, World")

f1= open(f_name, "r")
print(f1)
f1.close()

f=os.open(f_name, os.O_RDWR | os.O_CREAT)
print(f)

f_obj = os.fdopen(f,"a+")
print(f_obj)
f_obj.close()

print()

#Lab 9: Question 3.b.e
#Forking
"""
print("Before forking",os.getpid())
p = os.fork()
print("After forking",os.getpid())
print("Last line")

if p == 0:
    print("Child Process")
else:
    print("Parent Process")
"""

def child_process(file_name):
    """Simulate child process operations."""
    child_pid = os.getpid()
    print(f"child process pid: {child_pid}")

    # Open the file, move pointer and write to it
    with open(file_name, "a") as file:
        file.write("\nThis is written by the child process.")

    # Exit child process
    print(f"child process pid last line: {child_pid}")


def parent_process(file_name, child_pid):
    """Simulate parent process operations."""
    parent_pid = os.getpid()
    print(f"parent process: {parent_pid}")

    # Wait for the child process to finish
    print(f"Waiting for child process (PID {child_pid.pid}) to finish...")
    child_pid.join()

    # Close the file (we don't need to write anything more here, just showing for completion)
    with open(file_name, "a") as file:
        file.write("\nParent process has finished.")

    print(f"after fork: {parent_pid}")


def main():
    file_name = "fdpractice.txt"  # File name for writing

    # Create the file or clear it if exists
    with open(file_name, "w") as file:
        file.write("File created or cleared for the processes.\n")

    # Use Windows-specific method to spawn a process
    context = mp.get_start_method('spawn')

    # Create child process using multiprocessing
    process = mp.Process(target=child_process, args=(file_name,))

    main_pid = os.getpid()
    print(f"Before fork: {main_pid}")

    # Start child process
    process.start()

    print(f"After fork: {main_pid}")

    # Parent process waits for the child process to finish
    parent_process(file_name, process)


if __name__ == "__main__":
    main()