import sublime, sublime_plugin, asciihexList

class AsciiToHexCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		astr = v.substr(v.sel()[0])
		hx = ''
		for i in astr:
			new = asciihexList.ls.get(i,'error')          # Not good, but
			if new != 'error':                            # all this
				hx = hx + new + ' '                       # replaces
				v.replace(edit, v.sel()[0], hx.strip())# few if-else. Need a little advice.

			else: 		
				sublime.status_message("Wrong character \""+i+"\"!")
				sublime.error_message("Wrong character \""+i+"\"!")
				break
