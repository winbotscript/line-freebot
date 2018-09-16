from linepyopt.ttypes import Message


class Utils:
	def send_text(self, to, text):
		msg = Message()
		msg.to = to
		msg.text = text
		self.client.sendMessage(0, msg)