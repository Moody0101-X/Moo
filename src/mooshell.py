from sys import (platform, path, exit)
from os import (rmdir, chdir, mkdir, getcwd, path, scandir, removedirs,
remove, rename, stat_result, system, walk, getenv, name)
from shutil import move, copy
from Moocolors import *
from datetime import date
from time import sleep
from subprocess import check_output
from typing import Union
from Variables import *
from requests import get
from utility import dumptofile, getContent, getHeaders
from database import *

DOC = f"""{YELLOW}
----------------------------------------------------------------------------------
########################################################################
----------------------------------------------------------------------------------
basic Commands: 
    
    mkdir => make folders and directories
    touch => make files
    cd => navigate
    ls => list file/dirs
    rmdir => remove a dir
    cat => check the content of a file
    quit/exit => exits.
    scan => scan for the existence of a file.
    
    you can run:
    {MAGENTA} commandName --help
    for more information
------------------------------------------------------------------------------------
{WHITE} language: {BLUE} Python 3.9  
"""

# USERPROFILE = getenv("USERPROFILE")
if name == "posix":
    HOME = "/mnt"
    ROOT = HOME + "/Moo"
else:
    HOME = getenv("HOMEPATH")
    ROOT = HOME + "\\Moo"

class __installer:
    def __init__(self):
        if not path.exists(HOME):
            mkdir(HOME)
            cwd = getcwd()
            move(cwd, HOME)
            print(f"""
{GREEN}=> successfully Installed in {HOME}
{LIGHTMAGENTA_EX}=> Now you can try to add to PATH so you can access the shell from wherever you want!
                """)
        else:
            cwd = getcwd()
            move(cwd, HOME)
            print(f"""
{GREEN}=> successfully Installed in {HOME}
{LIGHTMAGENTA_EX}=> Now you can try to add to PATH so you can access the shell from wherever you want!
                """)


class mooShell:

    def __init__(self):
        print(DOC)
        
        if not self.exist(ROOT):
            mkdir(ROOT)
            self.changedir(ROOT)
        else:
            self.changedir(ROOT)
        self.PRIMARY = BLUE
        self.SECANDARY = WHITE
        self.YELLOW = YELLOW
        self.ERR = RED
        self.RUN = True
        
    def run(self):
        """ THE ENTRY POINT FOR THE PROGRAM. """
        while self.RUN:
            try:
                self.dir = getcwd()
                self.prompt = input(f'{GREEN}[MOO] {self.YELLOW} {self.dir} => ' + self.SECANDARY)
                self.processArgs()
            
            except Exception as e:
                print(f"{self.ERR} some went bad!! :(", e) 

    def processArgs(self):
        
        if len(self.prompt.split(' ')) == 1:
            self.promp =  self.prompt.strip().upper()
           
            if self.promp == "LS" or self.promp == "DIR":
                self.ls()
            elif self.promp == "HELP":
                print(HELP)
            elif self.promp == "CD":
                print()
                print(self.dir)
                print()
            elif self.promp == "FONTD":
                print(FontdownloaderDoc)
            elif self.promp == "QUIT" or self.promp == "EXIT":
                self.quit()
            elif self.promp == "ENCODER":
                self.args = None
                self.Cmd()
            elif self.promp == "scan":
                print(scanDoc)
            elif self.promp == "COMMANDS":
                print(availableCommands)
            elif self.promp == "SCRAP":
                print(ScrapDoc)
            elif self.promp == "DATABASE":
                print(doc)
            elif self.promp == "CP":
                self.cp()
            elif self.promp == "MV":
                print(mvDoc)
            elif self.promp == "ORG":
                self.ORGANIZE('.')

            elif self.promp == "COMPILER":
                self.args = ["compiler.py"]

                self.Cmd()
            else:
                self.args = None
                self.Cmd()

        elif len(self.prompt.split(' ')) > 1:
            self.prompt = self.prompt.split(' ')

            if self.prompt[0].strip().upper() == "CD":
                self.changedir(self.prompt[1])

            elif self.prompt[0].strip().upper() == "ORG":
                self.ORG(self.prompt[1])

            elif self.prompt[0].strip().upper() == "FONTD":
                self.donwloadFont()
            elif self.prompt[0].strip().upper() == "DATABASE":
                self.callDataBase(self.prompt)
            elif self.prompt[0].strip().upper() == "TOUCH":
                if len(self.prompt) > 2:
                    self.touch(self.prompt[1:])
                else:
                    self.touch(self.prompt[1])
            elif self.prompt[0].strip().upper() == "RM":
                if len(self.prompt) == 2:
                    if self.prompt[1] == '--help' or self.prompt[1] == '-h':
                        print(Rmdoc)
                    else:
                        self.rm(self.prompt[1])
                elif len(self.prompt) > 2:
                    self.rm(self.prompt[1:])
                elif len(self.prompt) > 2:
                        print(Rmdoc)

            elif self.prompt[0].strip().upper() == "MV":
                if len(self.prompt) == 3:
                    self.mv(self.prompt[1], self.prompt[2])
                elif len(self.prompt) > 3:
                    self.mv(self.prompt[1:-1], self.prompt[-1])
                elif len(self.prompt) == 2:
                    if self.prompt[1] == '--help' or self.prompt[1] == '-h':
                        print(mvDoc)
                    else:
                        print("seems like the distination has not been specified yet!!")
                else:
                    print(mvDoc)
            elif self.prompt[0].strip().upper() == "SCAN":
                if self.prompt[1] == "--help" or self.prompt[1] == '-h':
                    print(scanDoc)
                else:
                    self.scan(self.prompt[1])
            elif self.prompt[0].strip().upper() == "MKDIR":
                if self.prompt[1].strip().upper() == '--help' or self.prompt[1].strip().upper() == '-h':
                    print(mkDoc)
                else:
                    try:
                        mkdir(self.prompt[1])
                    except:
                        print('something went wrong!!')
            elif self.prompt[0].strip().upper() == "RMDIR":
                try:
                    rmdir(self.prompt[1])
                except:
                    print('something went wrong!!')
            elif self.prompt[0].strip().upper() == "ENCODER":
                self.setArgs()
                self.Cmd()
            elif self.prompt[0].strip().upper() == "COMPILER":
    
                self.args = [f"{self.prompt[0]}.py", *self.prompt[1:]]
                self.Cmd()
            elif self.prompt[0].strip().upper() == "CAT":
                if self.prompt[1] == '--help' or self.prompt[1] == '-h':
                    print(catDoc)
                else:
                    self.cat()

            elif self.prompt[0].strip().upper() == "LS" or self.prompt[0].strip().upper() == "DIR":
                self.dir = self.prompt[1]
                self.ls()
            elif self.prompt[0].strip().upper() == "HELP":
                print()
                print(availableCommands)
                print()

            elif self.prompt[0].strip().upper() == "SCRAP":
                if len(self.prompt) == 2:
                    if self.prompt[1] == '--help' or self.prompt[1] == '-h':
                        print(ScrapDoc)
                    else:
                        self.scrap(self.prompt[1])
                elif len(self.prompt) >= 3:
                    self.scrap(self.prompt[1], self.prompt[2:])
            elif self.prompt[0].strip().upper() == "MIM":
                self.mim(self.prompt[1])
                print("quiting mim")
            
            elif self.prompt[0].strip().upper() == "CP":
                self.cp(self.prompt[1:])

            else:
                self.setArgs()
                self.Cmd()
    

    def setArgs(self):
        self.args = ' '.join(self.prompt[0:])
    
    def ORG(self, path_):
        if path_.strip().upper() == "--HELP":
            print(ORGdoc)
        else:
            if not self.exist(path_):
                print("the path does not exist.")
            else:
                for i in scandir(path_):
                    if str(i.name).split('.')[1] in ["py", "ps", "bash", "yaml", "html", "c", "cpp", "c++", "r", "rb", "js", "css", "scss", "json", "tsx", "c#", "java"]:
                        self.move_(path_, i, "code")

                    elif str(i.name).split('.')[1] in ["mp3", "m4a", "wav"]:
                        self.move_(path_, i, "Audio")
                    
                    elif str(i.name).split('.')[1] in ["docx", "pdf", "ai", "fig", "psd", "xd"]:
                        self.move_(path_, i, "Docs")

                    elif str(i.name).split('.')[1] in ["mp4", "webm", "mkv"]:
                        self.move_(path_, i, "videos")

                    elif str(i.name).split('.')[1] in ["gif", "jpeg", "png", "svg"]:
                        self.move_(path_, i, "pictures")

                    elif str(i.name).split('.')[1] in ["exe", "", "msi"]:
                        self.move_(path_, i, "Programs")

                    elif str(i.name).split('.')[1] == "iso":
                        self.move_(path_, i, "ISO")

                    else:
                        self.move_(path_, i, "other")
                print(f"{GREEN}Completed!!")


    def move_(self, path_, file, folderName):
        """this function checks if the folder does not exist this is why I did not use the other one
            shutil.move().
        """
        if not self.exist(path.join(path_, folderName)):
            mkdir(path.join(path_, folderName))
        self.mv(file.name, path.join(path_, folderName))

    def rm(self, file: Union[str, list]) -> None:
        if isinstance(file, str):
            if self.exist(file):
                try:
                    remove(file)
                except:
                    system(f"del {file}")
            else:
                print(f"{self.ERR} the file specified to be deleted does not exist!!")
        else:
            for _ in file:
                self.rm(_)

    def donwloadFont(self):
        fontName = self.prompt[1].strip()
        if fontName != '--help':
            urls = [
                f"https://fonts.google.com/download?family={fontName}",
                f"https://dl.dafont.com/dl/?f={fontName}"
            ]

            reqs = [get(urls[0]), get(urls[1])]
            APIS = ["Google Font", "Dafont"]
            
            for i, res in enumerate(reqs):
                
                if int(res.status_code) == 200:
                    if len(res.content) < 200:
                        print(f"{Fore.RED}[*] {Fore.MAGENTA}{fontName} was not fount in {APIS[i]}")
                    else:
                        print(f"""{Fore.YELLOW}
File name: {Fore.LIGHTYELLOW_EX}{fontName}.zip
{Fore.YELLOW}size:  {Fore.LIGHTYELLOW_EX}{len(res.content)} Bytes
{Fore.YELLOW}provider: {Fore.LIGHTYELLOW_EX}google fonts
{Fore.YELLOW}Download directory: {Fore.LIGHTYELLOW_EX}{getcwd()}
{Fore.YELLOW}Api: {Fore.LIGHTYELLOW_EX}{APIS[i]}
""")
                        with open(f"{fontName}.zip", "wb") as f:
                            print(f"{Fore.BLUE}downloading.. {fontName}")
                            f.write(res.content)
                        print(f"{Fore.GREEN}successfully donwloaded {fontName}")
                        break
                else:
                    print(f"{Fore.RED}[*] {Fore.MAGENTA}{fontName} was not fount in {APIS[i]}")
        else:
            print(FontdownloaderDoc)

    def callDataBase(self, argv: list, n=0):
        if len(argv) == n+2 or len(argv) == n+1:
            if argv[n+1] == '--help':
                print(doc)
            elif argv[n+1] == '--version':
                print('0.0.0!')
            else:
                if argv[n+1] == "--register":
                    dbname = input(f"{YELLOW}DbName: {WHITE}")
                    
                    for _ in ['\\', '|', '/', '-', '\\', '|', '/', '-', '\\', '|', '/', '-']:
                        print(f"{BLUE} initializing database! {_}{WHITE}", end="\r")
                        sleep(0.3)
                    print(f'{YELLOW}initialized!!{WHITE}')
                    db = database(dbName=dbname)
                    db.register()
                    db.cleanUp()
                
                elif argv[n+1] == "--login":
                    dbname = input(f"{YELLOW}DbName: {WHITE}")
                    dbpassword = input(f"{YELLOW}Password: {WHITE}")
                    print(f"{BLUE}Querying the database..{WHITE}")
                    db = database(dbName=dbname, password=dbpassword)
                    db.QueryDb()
                    db.cleanUp()
                elif argv[n+1] == "--getItems":
                    dbname = input(f"{YELLOW}DbName: {WHITE}")
                    dbpassword = input(f"{YELLOW}Password: {WHITE}")
                    print(f"{BLUE}Querying the database..{WHITE}")
                    db = database(dbName=dbname, password=dbpassword)
                    db.database(dbName=dbname, password=dbpassword)
                    db.getItems()
                    db.cleanUp()
                elif argv[n+1] == "--getHeaders":
                    dbname = input(f"{YELLOW}DbName: {WHITE}")
                    dbpassword = input(f"{YELLOW}Password: {WHITE}")
                    print(f"{BLUE}Querying the database..{WHITE}")
                    db = database(dbName=dbname, password=dbpassword)
                    db.database(dbName=dbname, password=dbpassword)
                    db.getHeaders()
                    db.cleanUp()
                elif argv[n+1] == "--update":
                    dbname = input(f"{YELLOW}DbName: {WHITE}")
                    dbpassword = input(f"{YELLOW}Password: {WHITE}")
                    db.database(dbName=dbname, password=dbpassword)
                    db.OPEN()
                    # logic to post!!
                    db.cleanUp()
                else:
                    print(doc)

        elif len(argv) > 2:
            if argv[1+n] == "--register":
                # cmd = arg0 --register dbName password  (make new db, with this name and passsword!)
                if len(argv) == 4+n:    
                    for _ in ['\\', '|', '/', '-', '\\', '|', '/', '-', '\\', '|', '/', '-']:
                        print(f"{BLUE} initializing database! {_}{WHITE}", end="\r")
                        sleep(0.3)
                    print(f'{YELLOW}initialized!!{WHITE}')
                    db = database(dbName=argv[2+n])
                    db.register(psswd=argv[3+n])
                    db.cleanUp()
                    exit(0)
                else:
                    print(f"{RED}either the database name of the password is messing!{WHITE}")

            elif argv[1+n] == "--login":
                if len(argv) == 4+n:
                    #cmd2 = arg0 --login dbName password (login using this name and password!)
                    print(f"{BLUE}Querying the database..{WHITE}")
                    sleep(2)
                    db = database(dbName=argv[2+n], password=argv[3+n])
                    db.QueryDb()
                    db.cleanUp()
                else:
                    print(f"{RED}either the database name of the password is messing!{WHITE}")
            elif argv[1+n] == "--update":
                if len(argv) >= 5+n:
                    db = database(dbName=argv[2+n], password=argv[3+n])
                    db.POST([argv[4+n], argv[5+n]])
                    db.cleanUp()
                else:
                    print(len(argv))
                    print(f"{RED}either the database name of the password is messing!{WHITE}")

        else:
            print(doc)

    def ls(self):
        print()
        for _ in scandir(self.dir):
                print(self.PRIMARY + '  [*]  ' + self.SECANDARY + _.name)
        print()

    def changedir(self, d):
        
        if d == '--help':
            print(cdDoc)
        else:
            if self.exist(d):
                chdir(f"{d}")
            else:
                print(f'{self.SECANDARY} it seems like it does not exist!')

    def touch(self, name):
        if name == '--help' or name == '-h':
            print(touchDoc)
        else:
            if isinstance(name, list):
                for _ in name:
                    self.touch(_)
            else:
                return open(name, 'w+').close()
    def scan(self, ext):
        out = [i.name for i in scandir(self.dir) if i.name.endswith(ext)]
        if len(out) > 0:
            for _ in out:
                print(f"{GREEN} ==> {_}")
        else:
            print("there is no files for the specified extention!")
        return out
    def mv(self, src, dist):
        if isinstance(src, str):
            if self.exist(src):
                if not self.exist(dist):
                    self.mkdir(dist)
                try:
                    move(src, dist)
                except:
                    system(f"move {src} {dist}")
            else:
                print(f"{self.ERR} the file specified to be moved does not exist!!")
        else:
            for _ in src:
                self.mv(_, dist)
    def cp(self, files=None):
        if files == None:
            print(f"{CYAN} description:\n {WHITE} A command to copy files \n {CYAN} Usage:\n {WHITE}cp <filepath> <destinationpath>")
        elif len(files) < 2:
            print(f"{RED} something was not specified\n {YELLOW}check if you specified both the file and destination")
        elif len(files) > 2:
            for _ in files[:-1]:
                self.cp([_, files[-1]])
            print(f'{GREEN} copied {len(files)} files!!')
        else:
            try:
                copy(files[0], files[1])
                print(f'{GREEN} copied one file!!')
            except:
                system(f"copy {files[0]} {files[1]}")
    def scrap(self, url, args=[]):
        if not "http" in url.split(":"):
            url = "http://" + url
            
        if len(args) == 0:

            if get(url).status_code == 200:
                
                res = {
                    0: get(url).content,
                    1: get(url).headers,
                    2: get(url).encoding,
                    3: get(url).json,
                    4: get(url).text
                }

                print(f"{GREEN} status_code = 200 OK")
                scr = True
                reqprompt = f"""
{LIGHTCYAN_EX}
    specify what you want:
    => (0) content
    => (1) headers
    => (2) Encoding
    => (3) json
    => (4) text
    => (99) exit
"""
                while scr:
                    req = int(input(reqprompt))
                    print()
                    try:
                        if req in res.keys():
                            req2 = res[req]                    
                            print(req2.decode("latin1") if isinstance(req2, bytes) else req2)
                            print()
                            redcondition = str(input("want to redirect to a file (yes/no, y/n): "))
                            if redcondition.strip().upper() in ['YES', 'Y']:
                                redirect = str(input("file to redirect to:"))
                                dumptofile(redirect, req2)
                            else:
                                pass
                        else:
                            if req == 99:
                                scr = False
                            else:
                                print(f"{self.ERR}the number you specified is wrong! try again{RESET}")
                    except Exception as e:
                        print(f'{self.ERR}something went wrong!', e)
            else:
                print(f"{GREEN} status_code =  {get(url).status_code} :(")
        else:
            if len(args) > 3:
                if args[-1]:
                    if len(args) == 3:
                        if args[0].upper().strip() == 'HEADERS':
                            self.redirectOutput(getHeaders(url), args[1], args[2])
                        elif args[0].upper().strip() == 'CONTENT':
                            self.redirectOutput(getContent(url), args[1], args[2])
                        else:
                           self.redirectOutput(getContent(url), args[1], args[2])
                    else:
                        print(f"{MAGENTA} expected 4 arguments, got {len(args)} instead!")
                else:
                    print(f"{MAGENTA} expected 4 arguments, got {len(args)} instead!")
            else:
                if args[0].upper().strip() == 'HEADERS':
                    re0 = getHeaders(url)
                elif args[0].upper().strip() == 'CONTENT':
                    re0 = getContent(url)
                else:
                    re0 = getContent(url)
                print("-"*20)
                
                try: print(re0.decode("latin1") if isinstance(re0, bytes) else re0) 
                except: print(re0) # print(req2.decode() if isinstance(req2, Bytes) else req2)

                print("-"*20)
                redirect = input(f'[*] {YELLOW}file to redirect to ({MAGENTA}PRESS ENTER TO IGNORE): ')
                if redirect:
                    dumptofile(redirect, re0)

    def Cmd(self):
        try:
            if platform == "win32":
                if self.args is not None:
                    print(check_output(self.args, shell=True).decode("utf-8"))
                else:
                    print(check_output(self.prompt.strip(), shell=True).decode("utf-8"))
            else:
                if self.args is not None:
                    string = " ".join(self.args)
                    print(check_output(f"python3 {string}", shell=True).decode("utf-8"))
                else:
                    print(check_output(self.prompt.strip(), shell=True).decode("utf-8"))
        except Exception as e:
            print(e)

    def unzip(self):
        pass

    def mim(self, filename):
        print(f"{self.PRIMARY} to quit and save type /|/")
        self.lineNum = 1
        input_ = ""
        temp = ""
        if self.exist(filename):
            for _ in open(filename).readlines():
                _ = _.replace("\n", "")
                print(f" {CYAN}{self.lineNum}  {self.YELLOW}{_}")
                self.lineNum += 1
        while input_ != "/|/":  
            input_ = input(f"{CYAN}{self.lineNum}{self.YELLOW} ")
            if input_ != "/|/":
                if self.exist(filename):
                    with open(filename, 'a') as f:
                        f.write(f"{input_}\n")
                else:
                    with open(filename, 'w') as f:
                        f.write(f"{input_}\n")
            self.lineNum += 1

    def cat(self):
        if self.exist(self.prompt.split(' ')[1]):
            if len(self.prompt.split(' ')) > 2:
                if not self.exist(self.prompt.split(' ')[3]):
                    self.touch(self.prompt.split(' ')[3])
                if self.prompt.split(' ')[2] == ">>":
                    with open(self.prompt.split(' ')[1]) as f:
                        with open(self.prompt.split(' ')[3], 'w+') as f2:
                            f2.write(f.read())
                            print(f"{self.prompt.split(' ')[1]} > {self.prompt.split(' ')[3]}")
                            return
                elif self.prompt.split(' ')[2] == ">":
                    with open(self.prompt.split(' ')[1]) as f:
                        with open(self.prompt.split(' ')[3], 'a') as f2:
                            f2.write(f.read())
                            print(f"{self.prompt.split(' ')[1]} > {self.prompt.split(' ')[3]}")
                            return
            else:
                with open(self.prompt.split(' ')[1]) as f:
                    print(f.read())
        else:
            print(f"{self.ERR} this file you specified does not exist")
    
    def scandrive(self, name):
        pass

    def exist(self, p):
        if p in ["..", '.']:
            return True
        else:
            try:
                return path.exists(p)
            except:
                return False
    
    def redirectOutput(self, content, method=None, fileName=None):
        if not method:
            method = ">"
        else:
            if method == ">":
                self.appendToFile(fileName, content)
            elif method == ">>":
                self.overwrite(fileName, content)
            else:
                print(f"{method} is not a valid switch, either use > to append or >> to overwrite") 

    

    def appendToFile(self, fileName, content):
        with open(fileName, "a+") as f:
            if isinstance(content, bytes):
                f.write(content.decode())
            else:
                f.write(str(content))

    def overwrite(self, fileName, content):
        with open(fileName, "w+") as f:
            if isinstance(content, bytes):
                f.write(content.decode())
            else:
                f.write(str(content))

    def quit(self):
        for i in ['-','\\' , '|', '/']*2:
            print(f'{LIGHTBLACK_EX} quiting {i}', end="\r")
            sleep(.3)
        self.RUN = False



