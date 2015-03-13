# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt4app.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

application_title = "Beacon Vets Stock Control" #what you want to application to be called
main_python_file = "Stock Control System.py" #the name of the python file you use to run the program

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit","re","matplotlib.backends.backend_tkagg","tkinter","tkinter.filedialog"]
includefiles = ['C:/Users/Matt/Desktop/Github/COMP4Coursework/Implementation/Gui/resources/app_logo.png','C:/Users/Matt/Desktop/Github/COMP4Coursework/Implementation/Gui/resources/close.png','C:/Users/Matt/Desktop/Github/COMP4Coursework/Implementation/Gui/resources/Counties.txt','C:/Users/Matt/Desktop/Github/COMP4Coursework/Implementation/Gui/resources/CumbriaPostcodes.csv','C:/Users/Matt/Desktop/Github/COMP4Coursework/Implementation/Gui/resources/minimize.png','C:/Users/Matt/Desktop/Github/COMP4Coursework/Implementation/Gui/resources/SystemLogo.jpg','C:/Users/Matt/Desktop/Github/COMP4Coursework/Implementation/Gui/resources/SystemLogo.png']

build_options = {"includes":includes,
                 'include_files' : includefiles,
                 'icon' : 'C:/Users/Matt/Desktop/Github/COMP4Coursework/Implementation/Gui/resources/windows_icon.ico'}
setup(
        name = application_title,
        version = "0.1",
        description = "Stock control system for the company: Beacon Veternary Center.",
        options = {"build_exe" : build_options},
        executables = [Executable(main_python_file, base = base)])
