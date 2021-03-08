from nonebot import require
import nonebot
from .get_info import get_info
from .file_manage import Config


scheduler = require('nonebot_plugin_apscheduler').scheduler

@scheduler.scheduled_job('cron', second ='*/10', id='live_status_inquiry')
async def _():
    with Config() as config:
        user_dic = await config.get_all_user()
    if user_dic:
        for item in user_dic:
            user_id = item["room_id"]
            group_id = item["group_id"]
            info_list = await get_info().get_msg(user_id)
            if str(info_list[2]) == str(item['live_state']):
                pass
            else:
                if str(info_list[2]) == str(1) or str(info_list[2]) == str(0):
                    with Config() as config:
                        updata_result = await config.update_user(info_list[2],user_id,group_id)
                        bot = nonebot.get_bots()['Your bot id']
                        msg = "你关注的主播：{} 开播啦！！\n\n传送门：https://www.douyu.com/{}[CQ:image,file={}]".format(info_list[0],info_list[1],info_list[3])
                        await bot.call_api("send_group_msg",**{"group_id":group_id,"message":msg})

                else:
                    with Config() as config:
                        updata_result = await config.update_user(info_list[2],user_id,group_id)
                        bot = nonebot.get_bots()['Your bot id']
                        msg = "你关注的主播：{} 下播啦！！".format(info_list[0])
                        await bot.call_api("send_group_msg",**{"group_id": group_id,"message": msg})
    else:
        pass







