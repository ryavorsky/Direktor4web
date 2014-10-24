echo Current directory is %CD%
set folder=%CD%
for %%i in (*.zip) do (
	"c:\Program Files\7-Zip\7z.exe" x %%i
	cd %%~ni
	set subfolder = %%i
	echo Subfolder %CD%\%%~ni
	cd SVG
	FOR %%A IN (*.svg) DO "c:\Program Files\Inkscape\inkscape.com" -f "%CD%\%%~ni\SVG\%%A" -e "%CD%\%%~ni\Tex\%%~nA.png"
	cd ..\Tex
	"C:\Program Files\MiKTeX 2.9\miktex\bin\pdflatex.exe" Result.tex
	cd ..
	)