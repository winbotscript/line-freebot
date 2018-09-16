import time
import multiprocessing as mp
from .utils import Utils
from linepyopt.ttypes import MIDType


class MessageReceiver(object):
	def __init__(self, client):
		self.client = client
		self.send_gid = []
		self.send_mid = []
		self.resp = {}
		self.utils = Utils(client)
		self.start_reseter()

	def received(self, msg):
		if msg.text:
			for prefix in ["さとちゃん:", "さとう:"]
				if prefix == text[:len(prefix)-1]:
					cmd = text[len(prefix):]
					if msg.text in self.resp.keys():
						if msg.toType == MIDType.GROUP:
							if (not msg.to in self.send_gid) and (not msg._from in send_mid):
								self.send_gid.append(msg.to)
								self.send_mid.append(msg._from)
								self.resp[cmd](msg)

	def reseter(self):
		while True:
			time.sleep(3)
			self.send_gid = []
			self.send_mid = []

	def start_reseter(self):
		p = mp.Process(target=reseter, args=(self,))
		p.daemon = True
		p.start()

	def add_resp(self, *args, **kwargs):
		def decorator(f):
			self.resp[args[0]] = f
		return decorator

	@add_resp("help")
	def _resp_help(self, msg):
		"""ヘルプを送信します。"""
		helpstr = ""
		for k, v in self.resp:
			helpstr += f"{k} -> {v.__doc__}"
		self.utils.send_text(msg.to, helpstr)

	@add_resp("mid")
	def _resp_mid(self, msg):
		"""送信者のmidを送信します。"""
		self.utils.send_text(msg.to, msg._from)