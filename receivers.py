from logging import getLogger
from .utils import Utils
from .message_receiver import MessageReceiver
from linepyopt.ttypes import OpType


class Receivers:
	def __init__(self, client):
		self.client = client
		self.utils = Utils(client)
		self.logger = getLogger("FreeBOT")
		self.mrecv = MessageReceiver(client)

    def invited(self, op):
        if self.client.mid in op.param3:
            self.client.acceptGroupInvitation(0, op.param1)
            self.logger.info("Joined->" + op.param1 + " Inviter->" + op.param2)
            self.utils.send_text(op.param1, "松坂さとうです。\n早く仕事がこなせるようがんばりますので、よろしくお願いします。")

    def recvmes(self, op):
    	mrecv.received(op.message)

    def set_poll(self, poll):
    	poll.set_receiver(OpType.NOTIFIED_INVITE_INTO_GROUP, invited)