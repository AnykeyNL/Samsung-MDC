# Samsung-MDC
Serial control for Samsung MDC Multiple Display Control

## Why?
I got my hands on some Samsung 460DR-S screens. They where "child-locked", so was not able to use the menus. I was not able to find a download of the official Samsung MDC software. I did find the protocol specification: http://downloadcenter.samsung.com/content/UM/201201/20120120103506903/BN59-01122G-04Eng.pdf

My program allows you to easily unlock the childlock using the serial port. Do make sure you have the right kind of serial cable, I tried a few out of my old serial box and after testing a few, I found one with the correct pin layout.

The code ignores the ID of the screen and send the command to any screen (0xFE). 

Enjoy!
