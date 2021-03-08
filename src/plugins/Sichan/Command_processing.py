import nonebot
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,GroupMessageEvent,Message
from nonebot import on_command
from .get_info import get_info
from .file_manage import Config

add_user = on_command('添加主播')

@add_user.handle()

async def _(bot:Bot,event:GroupMessageEvent,state:dict):

    user_id = str(event.get_message()).strip()

    if user_id:
        try:
            state['user_id'] = user_id
            info_list = await get_info().get_msg(user_id)

            if info_list:
                nickname = info_list[0]
                room_id = info_list[1]
                live_state = info_list[2]

                with Config()as config:

                    await add_user.finish(await config.add_rid(room_id, nickname, live_state, str(event.group_id)))

            else:
                await add_user.finish('主播不存在')
        except Exception as e:
            await del_user.finish(str(e))



@add_user.got('user_id',prompt="请输入要添加的主播房间号")

async def _(bot:Bot,event:GroupMessageEvent,state:dict):

    user_id = state['user_id']

    try:
        info_list = await get_info().get_msg(user_id)
        if info_list:
            nickname = info_list[0]
            room_id = info_list[1]
            live_state = info_list[2]

            with Config()as config:
                await add_user.finish(await config.add_rid(room_id, nickname, live_state, str(event.group_id)))

        else:
            await add_user.finish('主播不存在')
    except Exception as e:
        await del_user.finish(str(e))



search_user = on_command('主播列表')

@search_user.handle()
async def _(bot:Bot,event:GroupMessageEvent,state:dict):

    with Config()as config:
        item = await config.Search_User(str(event.group_id))

    if item:

        result = '已添加的主播有：\n\n'

        for user in item:
            result+="{}({})\n\n".format(user['user_name'],user['room_id'])
        await search_user.finish(result)

    else:
        await search_user.finish("您没有添加过任何主播")

del_user = on_command('删除主播')

@del_user.handle()
async def _(bot:Bot,event:GroupMessageEvent,state:dict):
    user_id = str(event.get_message()).strip()

    if user_id:
        try:
            state['user_id'] = user_id
            group_id = str(event.group_id)
            with Config()as config:
                result = await config.Del_User(user_id,group_id)
            await del_user.finish(result)
        except Exception as e:
            await del_user.finish(str(e))




@del_user.got('user_id',prompt="请输入要删除的主播房间号")
async def _(bot:Bot,event:GroupMessageEvent,state:dict):
    user_id = state['user_id']

    try:
        state['user_id'] = user_id
        group_id = str(event.group_id)
        with Config()as config:
            result = await config.Del_User(user_id, group_id)
        await del_user.finish(result)
    except Exception as e:
        await del_user.finish(str(e))



