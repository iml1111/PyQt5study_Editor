from cx_Freeze import setup, Executable
import sys

buildOptions = dict(
	packages = ["PyQt5","sys","cryptography","base64","hashlib","_cffi_backend","eediter","idna.idnadata"], 
	excludes = ["tkinter", "sqlite3"])

base = None
if sys.platform == "win32": #windows GUI 일경우 
    base = "Win32GUI"
    #base = "Console"

exe = [Executable("main.py", base=base,  targetName="IEE.exe")]

setup(
    name='IML Encryption Editor',
    version = '0.1',
    author = "IML",
    description = "I'M IML!",
    options = dict(build_exe = buildOptions),
    executables = exe
)