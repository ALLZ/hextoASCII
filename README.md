# Sublime Text 2/3 ASCII<->Hex converter Plugin #

Sublime Text plugin to convert ASCII->Hex and Hex->ASCII.

## Usage ##

Just select the string, then use key bindings, menu "Selection" or context menu to convert it.  
If you want to change the view of hexadecimal numbers, just open "HextoASCII.sublime-settings" file and change "literals" option.

## Key bindings ##

### for Windows and Linux ###

ASCII->Hex  ctrl+',  ctrl+h  
Hex->ASCII  ctrl+h,  ctrl+'   

### for OSX ###

ASCII->Hex  super+',  super+h  
Hex->ASCII  super+h,  super+'   

## Update ##
Thanks to D.Y. Kim for 'c arrays' idea, it was implemented by option).  
It works for multiple selections, too) But still may be some glitchces with tabs(\t) and breaklines(&lt;br&gt;).   
Now it works correctly both with ST2 and ST3.