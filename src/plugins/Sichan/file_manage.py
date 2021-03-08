from tinydb import TinyDB,Query
from pathlib import Path

class Config(object):

    def __init__(self):
        pass
    def __enter__(self):
        data_file = str(Path().cwd().resolve()) + "\\data\\user_data.json"
        self.config = TinyDB(data_file, encoding='utf-8')
        self.user = self.config.table("user_data")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.config.close()



    async def add_rid(self,rid,nickname,islive,group_id):
        q = Query()
        if self.user.search((q.room_id == str(rid))&(q.group_id == str(group_id))):
            return "已经添加过了,请勿重复添加"
        else:

            self.user.insert({"room_id": str(rid), "user_name": nickname, "live_state": str(islive),"group_id":group_id})
            return "成功添加主播:{}\nRoom_id：{}".format(nickname,rid)

    async def Search_User(self,group_id):
        q = Query()
        user_list = self.user.search(q.group_id == str(group_id))
        return user_list

    async def Del_User(self,rid,group_id):
        q = Query()
        if  not self.user.search(q.room_id == str(rid)) and self.user.search(q.group_id == str(group_id)):

            return "您并没有添加过这位主播"

        else:
            name = self.user.search((q.room_id == str(rid))&(q.group_id == str(group_id)))[0]['user_name']
            self.user.remove((q.room_id == str(rid))&(q.group_id == str(group_id)))
            return "成功删除主播：{}".format(name)


    async def update_user(self,islive,rid,group_id):
        q = Query()
        try:
            result = self.user.search((q.group_id == str(group_id))&(q.room_id == str(rid)))[0]
            old_live_state = str(result['live_state'])
            result['live_state'] = str(islive)
            self.user.update(result,q.live_state==old_live_state)
            return ("主播状态更新成功")

        except Exception as e:
            return (str(e))


    async def get_all_user(self):

        user_list = self.user.all()

        return user_list










