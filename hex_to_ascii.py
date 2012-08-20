import sublime, sublime_plugin, hexasciiList

class HexToAsciiCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        hx = v.substr(v.sel()[0])
        hx = hx.strip()
        astr = ''
        l = True
        if hx == '': l = False
        if ' ' in hx: t=1 
        else: t=2
        for i in xrange(0,len(hx)-1,t):
            if (hx[i] == ' ') or (hx[i+1] == ' '): continue #use in "A3 2B 41" view
            st = hx[i]+hx[i+1]
            new = hexasciiList.ls.get(st,'error')
            if new != 'error':
                astr = astr + new
                v.replace(edit, v.sel()[0], astr)
            else:
                sublime.status_message("Wrong character \""+hx[i]+hx[i+1]+"\"!")
                sublime.error_message("Wrong character \""+hx[i]+hx[i+1]+"\"!")
                break
