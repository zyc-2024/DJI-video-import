@echo off
setlocal enabledelayedexpansion

:: Set the directory containing the video files
set "input_dir=."
set "output_prefix=G:/mp4/o/1_"
set "file_list=file_list.txt"
set "counter=0"
set "group=1"

:: Clean up any previous file list
if exist %file_list% del %file_list%

:: Loop through all video files in the directory
for %%f in (1\*.mp4) do (
    echo file '%%f' >> %file_list%
    set /a counter+=1

    :: If 10 files are added, concatenate them
    if !counter! equ 10 (
        ffmpeg -f concat -safe 0 -i %file_list% -c copy %output_prefix%!group!.mp4
        del %file_list%
        set /a counter=0
        set /a group+=1
    )
)

:: Handle remaining files if any
if exist %file_list% (
    ffmpeg -f concat -safe 0 -i %file_list% -c copy %output_prefix%!group!.mp4
    del %file_list%
)

echo Done!
pause