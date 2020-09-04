#!/home/michael/anaconda3/bin/python

import asyncio
import websockets


pool = {}

async def whisper(websocket, path):
    
    async for message in websocket:
        
        room_id, user_id, content = message.split('|||')

        print('received:', content)
        print('room_id:', room_id)
        print('user_id:', user_id)

        if room_id not in pool:
            pool[room_id] = [websocket]
        else:
            pool[room_id].append(websocket)

            updated = []
            for ws in pool[room_id]:
                if not ws.closed and ws not in updated:
                    updated.append(ws)
            pool[room_id] = updated
        
        print(pool)
        for ws in pool[room_id]:
            await ws.send('{}|||{}|||{}'.format(room_id, user_id, content))

start_server = websockets.serve(whisper, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
