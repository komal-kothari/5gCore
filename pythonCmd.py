import os
import subprocess
#os.system('ls')
#os.system('sudo brctl addbr br0')

p = subprocess.Popen('sudo brctl addbr br0',shell=True,close_fds=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
#p.stdin.write(b'"123\n"')
#p.wait()
p = subprocess.Popen('sudo ip tuntap add dev port mode tap',shell=True)
#p.wait()
p = subprocess.Popen('sudo ifconfig port up',shell=True)
#p.wait()
p = subprocess.Popen('sudo brctl addif br0 port',shell=True)
#p.wait()
p = subprocess.Popen('sudo brctl addif br0 enp3s0',shell=True)
#p.wait()
p = subprocess.Popen('sudo ifconfig br0 up',shell=True)
p = subprocess.Popen('sudo dhclient br0',shell=True)
#p.wait()
#p.wait()
#p.terminate()
#p.kill()
#p.stdin.write(b'"123\n"')
p.communicate(b'123\n')
#p.wait()