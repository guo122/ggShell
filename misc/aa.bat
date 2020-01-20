echo off
set avnum=%1
set /a start=%3
set /a numsum=%2
set /a end=%start%+%numsum%-1

echo start:%start% to %end%
for /l %%i in (%start%,1,%end%) do (start "" "http://www.flvcd.com/parse.php?format=&kw=https%%3A%%2F%%2Fwww.bilibili.com%%2Fvideo%%2Fav%avnum%%%3Fp%%3D%%i")
