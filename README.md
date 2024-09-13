Welcome to my [personal branch!](https://github.com/epibirikka)

# FontForge Glyph Exporter
A [FontForge](https://github.com/skef/fontforge) Python script for automatically exporting font characters/glyphs in SVG format.

# Instructions
1. Open any font in FontForge.
2. In FontForge, go to "File -> Execute Script"
3. Open 'Glyph SVG Exporter.py' in any text editor, like Notepad or TextEdit. 
4. Copy everything inside the Python file, and paste it into the FontForge Script Window.
5. Select the bubble that says Python, and then run the script, following the prompts on-screen.
7. Assuming no errors were displayed, you should now have a folder containing all of your desired glyphs alongisde a "kerning" file which contains the spacing data for every exported character. Use these to help create your own text engine if desired.

# Kerning Data Extraction Instructions

Unless you are using exported kerning data for a project directly made for Lua, you might want to extract kerning data for Scratch.

*You must run the kerning extraction script through with a standalone Python interpreter, not the Python interpreter bundled by FontForge. It is recommended to run it with versions higher than 3.10.*

## Prequisites

- Install the [lupa](https://pypi.org/project/lupa/) module, which you can install it with PIP.

- Make sure your terminal's current directory has folders of exported glyphs, and it must have kerning data written in Lua.

- Adjust the calls of, `    main(wlist, wlistpoints, "FOLDERNAME")`, under this line

```python
    with open("kerninglist.txt", "w") as wfile:
```

Keep in mind - The glyph filename has to match this pattern, `font{FOLDERNAME}-{CHARACTER KEYWORD}.svg`

## Process

- The extraction outputs two files as two lists of numbers, those files named, "kerninglist.txt," and "kerninglistpoints.txt."

- kerninglist.txt is a file that carries all kerning widths for all exported glyphs from different fonts.

- kerninglistpoints.txt is a file that has starting indexes of the first alphabetical characters, for different fonts. Useful if you want to support multiple fonts.

## Importing

- *Be sure you have the costumes in order, matching the order of the kerning data.*

- Right-click on two lists, then open the respective files. One is meant for storing kerning data, and another is meant for storing kerning data starting indexes.

# Credits
<<<<<<< HEAD
- Initial Code by CubeSolver25.
- FontForge Python Support by [skef](https://github.com/skef), developer of Fontforge.
- Python Support by NotestQ.

=======
Initial Code by CubeSolver25.
Python Support by NotestQ.
FontForge Python Support by [skef](https://github.com/skef), developer of Fontforge.
Personal revisions by sayketsu.
>>>>>>> ba832ee (Pull request?)

# Motivation
This script was originally created to aid in the development of a Scratch project which contained a text engine. Due to a lack of adequate glyph exporters at the time, I resorted to creating my own which runs with the assistance of FontForge, a font editing program.

# Revision Motivation
Similiar motivation as above, but this is for developing a simple and quick text engine for a Scratch game. Instead of manually exporting each character through a vector graphics program, this seemed to be the way to go. I highly appreciate this tool, because it made development easier.

# Tips for Scratchers
If you're using the Sprite Folders addon from Scratch Addons, create a folder for each unique font for easier organization. If you cannot install the addon, you can set the prefix of the exported glyphs to '[FontName]//' instead.

If you want to create more copies of the same font to allow different saturation levels, you are free to do so, but in most cases you only need the RED and BLACK versions of the glyphs. You can use brightness instead to simulate saturation to limited degrees.

## sayketsu's notes:

This is a tool we developed as if we spent a few hours just for our needs, do not expect a fully-fledged tool. This is a patch branch meant for experienced developers.

I can also say the same of my documentation, I wanted to continue working on my game with the text engine.
