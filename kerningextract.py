from lupa import LuaRuntime
from glob import glob
from os import getcwd
from os.path import basename, splitext

specialchars = ' !"#$%&\'*+./:<=>?@\`{|}'
specialcharnames = ['space', 'exclamation', 'double_quote', 'hash', 'dollar', 'percent', 'ampersand', 'single_quote', 'asterisk', 'plus', 'period', 'slash', 'colon', 'less', 'equal', 'greater', 'question', 'at', 'backslash', 'backtick', 'left_brace', 'pipe', 'right_brace']

def main(wlist, wlistpoints, dirname):
    svg_filenames = glob(f"{dirname}/*.svg")
    lua_filenames = glob(f"{dirname}/*.lua")

    if not svg_filenames:
        print("{dirname}: No svg files detected")
        return

    if not lua_filenames:
        print("{dirname}: No lua files returning kerning data detected")
        return

    print(f"Opening {lua_filenames[0]}...")

    lstate = LuaRuntime()

    with open(lua_filenames[0], "r") as file:
        evalstr = file.read()
        ldict = lstate.eval(evalstr[7:])

    svg_filenames.sort()

    wlistpoints.append(len(wlist))

    for idx, name in enumerate(svg_filenames):
        split = basename(name).split(f"font{dirname}-")

        if not split:
            print("nop")
            continue

        keyword, _ = splitext(split[1])

        if keyword in specialcharnames and keyword != "space":
            stitidx = specialcharnames.index(keyword)
            keyword = specialchars[stitidx]
        elif keyword.startswith("u") and len(keyword) > 1:
            keyword = keyword[1]

        if keyword not in ldict:
            print(f"{keyword} not in ldict ({name})")
            continue

        print(idx+1, keyword, ldict[keyword])

        wlist.append(ldict[keyword])

if __name__ == '__main__':
    wlist = []
    wlistpoints = []

    with open("kerninglist.txt", "w") as wfile:
        # TODO: replace those calls below me, with folders of exported glyphs you want to extract
        main(wlist, wlistpoints, "suit")
        main(wlist, wlistpoints, "magreg")
        main(wlist, wlistpoints, "magbold")

        wfile.writelines([str(x) + "\n" for x in wlist])

    with open("kerninglistpoints.txt", "w") as wfilepoints:
        wfilepoints.writelines([str(x) + "\n" for x in wlistpoints])
