import os

os.system('clear')



N="""

███╗░░██╗░█████╗░██╗░░██╗██╗██████╗░
████╗░██║██╔══██╗██║░░██║██║██╔══██╗
██╔██╗██║███████║███████║██║██║░░██║
██║╚████║██╔══██║██╔══██║██║██║░░██║
██║░╚███║██║░░██║██║░░██║██║██████╔╝
╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░
"""
A="""

[1] Gmail
[2] Gmail2
[3] web
[4] web2
[5] Facbook
[6] Facbook2
[7] Github
[8]
[9]
"""
kk="""
[1] Mano
[2] Exit
"""
Github="""
gmail: nahidpeda00@gmaio.com
pass: Nahid@20087
"""
Gmail="""
pedanahid0@gmail.com

password: nahidpeda@2008
"""
Gmail2="""
nahidpeda00@gmail.com

password: Nahid@20087
"""
web="""
web: http://nahidff001.rf.gd

Admin panel : http://nahidff001.rf.gd/wp-admin/

"""
web2="""

web: http://nahidgameshopbd.rf.gd

Admin panel: http://nahidgameshopbd.rf.gd/wp-admin/
"""
print(N+A)

mad=input("Enter your id nambee: ")
if mad=="1":
      os.system('clear')
      print(N+Gmail)
if mad=="2":
     os.system('clear')
     print(N+Gmail2)
if mad=="3":
      os.system('clear')
      print(N+web)
if mad=="4":
      os.system('clear')
      print(N+web2)
if mad=="5":
      os.system('clear')
      print(N)
if mad=="6":
      os.system('clear')
      print(N)
if mad=="7":
      os.system('clear')
      print(N+Github)
else:
      print("  ")

print(kk)
kk=input("Enter your cods namber: ")
if kk=="1":
      os.system('python ALL-ID.py')
if kk=="1":
      os.system('exit')
