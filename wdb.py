from telex import plugin

import wdb


class WdbPlugin(plugin.TelexPlugin):
    """
    Triggers python wdb debugger
    """

    patterns = {
        "^{prefix}wdb(.+)$": "trigger_wdb",
    }

    usage = [
        "{prefix}wdb: invokes wdb debugger",
    ]


    def trigger_wdb(self, msg, matches):
        peer = self.bot.get_peer_to_send(msg)
        wdb.set_trace()
