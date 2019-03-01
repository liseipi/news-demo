class _ConfigParser(object):
	"""docstring for Users"""
	def __init__(self, file_path):
		self.file = file_path
		import configparser
		self.parser = configparser.ConfigParser()
		self.parser.read(self.file)
	
	def get_option(self, section, option, b_none=True):

		try:
			# section = section.lower()
			# if 
			# option = option.lower()
			value = self.parser.get(section, option)
			if not b_none and not value:
				raise Exception("cannot find option(or value is none): {} in section: {} of the file: {}".format(option, section, self.file))
			return value
		except Exception as e:
			print(e)
			return None
	
	def get_boolean(self, section, option, b_none=True):
		try:
			value = self.parser.getboolean(section, option)

			if not b_none and not value:
				raise Exception("cannot find option(or value is none): {} in section: {} of the file: {}".format(option, section, self.file))
		except Exception as e:
			print(e)
			return None