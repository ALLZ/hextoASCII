import sublime
import sublime_plugin


class AsciiToHexCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        v = self.view
        reglist = list(v.sel())
        for j in range(0, len(reglist)):
            self.settings = sublime.load_settings("HextoASCII.sublime-settings")
            setting = self.settings.get("literals")
            astr = v.substr(v.sel()[j])
            hx = ''
            if setting == 4:
                hx = '{'
            for i in astr:
                if setting == 1:
                    new = hex(ord(i)) + ' '
                elif setting == 2:
                    new = '{0:x}'.format(ord(i))
                elif setting == 3:
                    new = '{0:x}'.format(ord(i)) + ' '
                else:
                    new = hex(ord(i)) + ', '
                hx = hx + new
            if setting == 4:
                hx = hx[:len(hx)-2] + '}'
            v.replace(edit, v.sel()[j], hx.strip())
