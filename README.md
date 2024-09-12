# FontForge Glyph Exporter
A [FontForge](https://github.com/skef/fontforge) Python script for automatically exporting font characters/glyphs in SVG format.<br />
**Status:** *Little to no active maintenance by me.*<br />
See [epibirikka's](https://github.com/epibirikka) [sayketsu](https://github.com/CubeSolver25/fontforge-glyph-exporter/tree/sayketsu) branch for a more experimental/actively maintained version of this code.

# Instructions
1. Open any font in FontForge.
2. In FontForge, go to `File` then select `Execute Script`.
3. Open [Glyph SVG Exporter.py](https://github.com/CubeSolver25/fontforge-glyph-exporter/blob/main/Glyph%20SVG%20Exporter.py) in any text editor, like Notepad or TextEdit. 
4. Copy everything inside the Python fil, then paste it into the FontForge Script Window.
5. Select the bubble that says Python then run the script, following the prompts on-screen.
7. Assuming no errors were displayed, you should now have a folder containing all of your desired glyphs alongisde a *"kerning" file which contains the spacing data for every exported character. Use these to help create your own text engine if desired. <br />
\**Actual kerning data is not exported, so specific letter combinations like `AV` will leave larger gaps than the original font.*

# Tips
The `Characters` txt files in this repository can be used to export specific glyphs. You can create your own txt files containing every character you wish to export. <br />
No special formatting is needed, just include one instance of each character. <br />
*` 0123456789` will export all numbers and the space character (The spacing value of the font's whitespace will be included in the exported kerning file.)*

# Limitations
- Does not export the font's actual kerning data, so font spacing data isn't completely accurate.
- SVG Viewbox (ascent/descent) does not accommodate for accented characters, so they will often be cropped in the export. [(Advice by skef)](https://github.com/fontforge/fontforge/discussions/4997)

# Credits
- Initial Code by CubeSolver25.
- FontForge Python [API](https://fontforge.org/docs/scripting/python.html) and Support by [skef](https://github.com/skef), developer of FontForge.
- Python Support by NotestQ.
- Inspiration and "Kerning" Data Format from [Kuut's](https://kuut.xyz/) [Font Tool](https://kuut.xyz/fonttool). 

# Motivation
This script was originally created to aid in the development of a Scratch project which contained a text engine. Due to a lack of adequate glyph exporters at the time, I resorted to creating my own which runs on FontForge, a font editing program.

# Tips for Scratchers
If you're using the Sprite Folders addon from Scratch Addons, create a folder for each unique font for easier organization. If you cannot install the addon, you can set the prefix of the exported glyphs to '[FontName]//' instead.

If you want to create more copies of the same font to allow different saturation levels, you are free to do so, but in most cases you only need the **red** and **black/gray** versions of the glyphs. You can use brightness instead to simulate saturation to limited degrees.

