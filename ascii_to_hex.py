import sublime, sublime_plugin, string

class AsciiToHexCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		astr = v.substr(v.sel()[0])
		bstr = ''
		i = 32
		sh = []
		while i<127:
			sh = sh.append(chr(i))

		
			#else:
			#	sublime.status_message("Wrong character \""+astr[i]+"\"!")
			#	sublime.error_message("Wrong character \""+astr[i]+"\"!")
			#	break