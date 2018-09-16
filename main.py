import os
from receivers import Receivers
import linepyopt


client = linepyopt.token_login(os.environ["FREEBOT_TOKEN"])
client.mid = client.getProfile().mid
receivers = Receivers(client)
poll = linepyopt.Poll(client)
receivers.set_poll(poll)
poll.start()
