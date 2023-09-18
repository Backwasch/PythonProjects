###You need to convert this file into an exe (i.e. by using pyinstall) then just drag and drop it into an command prompt

import os
import sys
import subprocess


def checkFolders(ffmpegExe_path,path): #Check if all req. folders exist
    ffmpeg_path = ffmpegExe_path
    checkFolder = True
    if not os.path.isdir(str(path)+"//input"):#Check if input folder exist if not create it
        os.mkdir(str(path)+"//input")
        print("Input folder created. Please put your files into the folder!")
    if not os.path.isdir(str(path)+"//output"):#Check if output folder exist if not create it
        os.mkdir(str(path)+"//output")
    while(checkFolder == True): #Check if the folder exists and if the exe is in it
        try:
            while not "ffmpeg.exe" in str(os.listdir(ffmpeg_path)):
                ffmpeg_path = input("ffmeg.exe not found or correct, please enter the PATH to the exe: ")
                checkFolder = False
            return ffmpeg_path
        except FileNotFoundError: #Happens if the user enters a non existant path
            ffmpeg_path = input("ffmeg.exe not found or correct, please enter the PATH to the exe: ")
            checkFolder = True
        except NotADirectoryError:#Happens if the user enters a path to a spec. file (i.e. ...\file.exe)
            ffmpeg_path = input("Please enter only the path to the exe, please try again: ")
            checkFolder = True
    return ffmpeg_path


path = os.path.dirname(sys.executable)
ffmpegExe_path = str(os.path.join(path, 'ffmpeg', 'bin'))
check_path = ""


while (str(check_path) != "y") and (str(check_path) != "n"): #Ask if the choosen path is correct
    check_path = input("ATTENTION: The folder of the .exe: " + str(path) + " will be used! \nType y to accept or n to decline ")
if str(check_path) == "n":
    sys.exit("Move the .exe to the desired folder")

ffmpegExe_path = checkFolders(ffmpegExe_path,path)

while (len(os.listdir(str(path)+"//input")) == 0): #Check if input folder is empty
    input("Input folder empty, please put your files into the folder and press enter to continue.")

for i in os.listdir(str(path)+"//input"): #Check if non .mkv files are in the input folder
    y,y = os.path.splitext(i)
    if str(y) != ".mkv":
        sys.exit("Error: non .mkv in " + str(str(path)+"\input") + " detected.\nPlease remove the wrong files and try again.")


for i in os.listdir(str(path)+"//input"): #convert .mkv into .mp4 using ffmpeg
    output_Name = i.replace(".mkv", ".mp4")
    print(i)
    print(output_Name)
    subprocess.run([str(os.path.join(ffmpegExe_path,"ffmpeg.exe")), "-i", str(os.path.join(str(path)+"//input", i)),"-codec", "copy", str(os.path.join(str(path)+"//output", output_Name))], check=True)