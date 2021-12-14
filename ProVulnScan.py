import urllib.parse as urlparse
from bs4 import BeautifulSoup

import scannerclass
#Banner 

print('''                                                                                                               
*@@@***@@m                    *@@@@*   *@@@*             *@@@               m@***@m@                             
  @@   *@@m                     *@@     m@                 @@              m@@    *@                             
  @@   m@@ *@@@m@@@   m@@*@@m    @@m   m@   *@@@  *@@@     @@  *@@@@@@@@m  *@@@m     m@@*@@  m@*@@m  *@@@@@@@@m  
  @@@@@@@    @@* **  @@*   *@@    @@m  @*     @@    @@     !@    @@    @@    *@@@@@m@@*  @@ @@   @@    @@    @@  
  @@         @!      @@     @@    *!@ !*      !@    @@     !@    @!    @@        *@@@!       m@@@!@    @!    @@  
  @!         @!      @@     !@     !@@m       !@    @!     !@    @!    !@  @@     @@@!m    m@!   !@    @!    !@  
  @!         !!      !@     !!     !! !*      !@    !!     !!    !!    !!  !     *@!!!       !!!!:!    !!    !!  
  !!         !:      !!!   !!!     !!::       !!    !!     :!    !!    !!  !!     !!!:!    !!!   :!    !!    !!  
:!:!:      : :::      : : : :       :         :: !: :!:  : : : : :::  :!: ::!: : :!  : : :  :!: : !: : :::  :!: :
                                                                                                                 
 By:
 Sarthak kul.                                                                                                             
 ''')

target_url = input("[+] Enter the Target URL ~~> ")
links_to_ignore = [""] #enter links to ignore
 
data_dict = {"username": "admin", "password": "password", "Login": "submit"}
 
 
vuln = scannerclass.Scanner(target_url, links_to_ignore)
vuln.session.post("", data = data_dict)

vuln.crawl()
vuln.run_scanner()
