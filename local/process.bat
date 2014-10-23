echo Current directory is %CD%
set folder=%CD%
for %%i in (*.zip) do (
	"c:\Program Files\7-Zip\7z.exe" x %%i
	cd %%~ni
	set subfolder = %%i
	echo Subfolder %CD%\%%~ni
	mkdir PNG
	cd SVG
	FOR %%A IN (*.svg) DO "c:\Program Files\Inkscape\inkscape.com" -f "%CD%\%%~ni\SVG\%%A" -e "%CD%\%%~ni\PNG\%%~nA.png"
	cd ..
	cd ..
	)