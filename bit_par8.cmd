path=%PATH%;C:\Users\user\AppData\Local\Programs\Python\Python38\
set mmm="2000000"
start "1" cmd /c python bitkeyf.py %MMM% ^>^>bittest1.txt
start "2" cmd /c python bitkeyf.py %MMM% ^>^>bittest2.txt
start "3" cmd /c python bitkeyf.py %MMM% ^>^>bittest3.txt
start "4" cmd /c python bitkeyf.py %MMM% ^>^>bittest4.txt
start "5" cmd /c python bitkeyf.py %MMM% ^>^>bittest5.txt
start "6" cmd /c python bitkeyf.py %MMM% ^>^>bittest6.txt
start "7" cmd /c python bitkeyf.py %MMM% ^>^>bittest7.txt
start "8" cmd /c python bitkeyf.py %MMM% ^>^>bittest8.txt

:python bitkeyf.py 2000000 >>bittest.txt

@echo First install python 3.8+
@echo then in command line...   
@echo >
@echo >pip install bit  
@echo >pip install tqdm  


:pause
