import subprocess

def pipeline(command1, command2):
    p1 = subprocess.Popen(command1.split(), stdout=subprocess.PIPE)
    p2 = subprocess.Popen(command2.split(), stdin=p1.stdout)
    p1.stdout.close()
    p2.communicate()

if __name__ == "__main__":
    pipeline("cat pipeline.cpp", "grep hello")