from config import *
from telethon import events
from help import *


@xdexer.on(events.NewMessage(outgoing=True))
async def _(event):
    id = str(event.sender_id)
    idas = await xdexer.get_messages("sadstory7", limit=1)
    msg = str(idas[0].message)
    if id in msg and ispay[0] == 'no':
        ispay.clear()
        ispay.append("yes")
    elif id not in msg and ispay[0] == 'yes':
        ispay.clear()
        ispay.append("no")
    else:
        pass
    id = str(event.sender_id)
    idas = await xdexer.get_messages("sadstory6", limit=1)
    msg = str(idas[0].message)
    if id in msg and ispay2[0] == 'no':
        ispay2.clear()
        ispay2.append("yes")
    elif id not in msg and ispay2[0] == 'yes':
        ispay2.clear()
        ispay2.append("no")
    else:
        pass
