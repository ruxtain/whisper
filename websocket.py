#!/home/michael/anaconda3/bin/python
# reference: https://websockets.readthedocs.io/en/stable/

import asyncio
import websockets

pool = {}

# 每当有人对我们ws服务发出请求，就会异步调用一次这个函数
async def whisper(websocket, path):
    
    # 我理解的 websocket 是所有 session 的集合
    # 不过官方用的 message 来表示，我也就用 message，而不用 session 这个词了
    async for message in websocket:
        print(dir(websocket))
        # 我自定义的“协议”，用|||分割字段
        room_id, user_id, content = message.split('|||')

        print('received:', content)
        print('room_id:', room_id)
        print('user_id:', user_id)

        # 对于新的房间id，则绑定到该消息所属的 websocket session 下
        if room_id not in pool:
            pool[room_id] = [websocket]
        else:
            pool[room_id].append(websocket)

            updated = []

            # 遍历当前房间的所有 session
            # 这个 updated 没啥别的意思，就是去重，我忘了为啥会有重复了
            for ws in pool[room_id]:
                if not ws.closed and ws not in updated:
                    updated.append(ws)
            pool[room_id] = updated
        
        print(pool)
        # 给房间里所有广播服务器刚刚接收到的消息
        for ws in pool[room_id]:
            await ws.send('{}|||{}|||{}'.format(room_id, user_id, content))

# 启动咱们的websocket服务
start_server = websockets.serve(whisper, '172.17.150.194', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
