# Sichan_Bot

## How to start

这是一个nonebot2插件
使用前请确认你的电脑装有nonebot2以及其所依赖的包

### 1.下载文件后在env.prod中添加你的配置
SUPERUSERS=[""]  # 配置 NoneBot 超级用户的QQ号
NICKNAME=[""]  # 配置机器人的昵称

### 2.打开src\plugins\Sichan\live_status_inquiry.py


在 bot = nonebot.get_bots()['Your bot id'] 的中括号内添加你的机器人的QQ
注意，在live_status_inquiry.py文件内需要添加QQ的有两处

下载所有文件后运行bot.py .

## 功能

斗鱼直播推送 

### 1.添加主播
  艾特机器人 + 添加主播 + 主播房间号 或者直接 机器人昵称 + 添加主播 + 主播房间号

### 2. 删除主播
  艾特机器人 + 删除主播 + 主播房间号 或者直接 机器人昵称 + 删除主播 + 主播房间号
  
### 3. 主播列表
  艾特机器人 + 主播列表 或者直接 机器人昵称 + 主播列表
  
