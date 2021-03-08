import aiohttp
from urllib import parse


class get_info:

    def __init__(self):
        pass

    async def get_msg(self,rid):

        async with aiohttp.ClientSession() as session:

            url = f'https://apiv2.douyucdn.cn/japi/search/api/getSearchRec?kw={rid}&tagTest=a&client_sys=android'

            response = await session.get(url,verify_ssl = False)

            data = await response.json()

            recList = data['data']['recList']

            if recList:

                nick_name = recList[0]['roomInfo']['nickName']

                room_id =  recList[0]['roomInfo']['rid']

                live_state = recList[0]['roomInfo']['isLive']

                r_cover_src = parse.unquote(recList[0]['roomInfo']['url'].split('&')[3].split('=')[1])

                info_list = [nick_name,room_id,live_state,r_cover_src]

                return info_list

            else:

                return








