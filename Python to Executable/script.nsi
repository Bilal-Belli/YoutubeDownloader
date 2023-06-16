; 1
;  execute this two commands on terminal:
;  pyi-makespec --onefile .\mainScript.py
;  pyinstaller .\mainScript.spec

; 2
;  install NSIS
;  compile this file (use your appropriate paths)

Outfile "youtubeDownloader.exe"
Section
SetOutPath "$INSTDIR"
File "C:\Users\Hp\OneDrive\Bureau\Nouveau dossier\YoutubeDownloader\Python to Executable\dist\mainScript.exe"  ; Include the executable file created by PyInstaller
File "C:\Users\Hp\OneDrive\Bureau\Nouveau dossier\YoutubeDownloader\Project\logo.ico"  ; Include the logo file, if needed
File "C:\Users\Hp\OneDrive\Bureau\Nouveau dossier\YoutubeDownloader\Project\download.ico"  ;
CreateShortcut "$DESKTOP\youtubeDownloader.lnk" "$INSTDIR\mainScript.exe"
SectionEnd