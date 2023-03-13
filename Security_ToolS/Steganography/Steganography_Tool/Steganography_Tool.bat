@ECHO OFF 

TITLE Steganography Tool
COLOR 6
ECHO ######################################
ECHO #                                    #
ECHO #        Steganography               #
ECHO #        Engr. Fahad                 #
ECHO #                                    #
ECHO ######################################
ECHO                                       
ECHO                                       
ECHO  keep the tool in same directory of your img and secret file
ECHO                                       
ECHO Enter 0 to Conceal
ECHO Enter 1 to Reveal
SET /P option="Enter Option: "
rem ECHO %option%

IF %option%==0 ( GOTO :conceal )
IF %option%==1 ( GOTO :reveal )
IF %option% NEQ 0 IF %option% NEQ 1  ( GOTO :wrong_option )

:conceal
    COLOR E
    SET /P file_name="Secret File Name: "
    SET /P img_name="Image File Name: "
    ECHO %file_name% %img_name%
    rem zip command
    rem copy /b img.jpg + file.zip
    rem remove file.zip
    BREAK
:reveal
    COLOR A
    SET /P file_name="Image File Name: "
    ECHO %file_name%
    rem unzip command
    BREAK
:wrong_option
    COLOR E
    ECHO Enter valid option
    BREAK

PAUSE