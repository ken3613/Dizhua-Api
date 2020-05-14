# Dizhua-Api
有关递爪APP的相关API，非官方

![Python3.8](https://img.shields.io/badge/Python-3.8-brightgreen) 

### API方法

- 聚会记录

  - 调用方法
  
    ```
    API地址：https://apis-ff.zaih.com/flash-whisper/v2/applications?filter=all&page=1&per_page=100
    方法：GET
    Headers：
    Authorization:你的JWT
    Host:apis-ff.zaih.com
    User-Agent:ios dizhuaApp 1.9.2 (暂时未知版本号对api调用的影响)
    ```
  
  - 返回值
  
    ```
    返回值：包含所有聚会信息的字典列表
    Content-Type：application/json
    ```
  
  - 聚会信息字典字段详情
  
    ```
    character_id		未知
    chat_id				未知
    date_created		聚会被创建时间，格式为含时区的标准datetime格式，时区为utc
    date_now			聚会报名时间，格式为含时区的标准datetime格式，时区为utc
    date_started		聚会开始时间，格式为含时区的标准datetime格式，时区为utc
    icon_url			聚会图标url
    id					聚会ID，可用于查询聚会详情API
    name				聚会名称
    result_status		聚会结果，值为fail或success，真正意义未知
    room_chat_id		聚会房间ID
    status				聚会状态，值为talking_over/canceled/quit
    template_type		聚会模版/类型，值normal为普通聚会，值parlor为客厅
    topic_creator_id	聚会创建者ID，普通聚会为null，客厅为客厅主人user_id
    topic_id			聚会主题ID
    topic_type			未知
    user_avatar			匿名人物的头像
    user_id				你的user_id
    user_nickname		匿名人物的昵称
    user_random_status	未知，当前值恒为true
    ```
  
    
  
  - 聚会信息字典样例
  
    ```json
    {
            "character_id": "1043730759261957",
            "chat_id": "114537193865217",
            "date_created": "2020-05-04T21:40:32.519421+00:00",
            "date_now": "2020-05-14T08:00:26+00:00",
            "date_started": "2020-05-04T22:00:00+00:00",
            "icon_url": "https://medias.zaih.com/FqUJEFjnj81GZ6UH4TLDTq2eM6cu",
            "id": "111869209271509725184",
            "name": "人生小酒馆",
            "result_status": "success",
            "room_chat_id": "114537193865217",
            "status": "talking_over",
            "template_type": "topic",
            "topic_creator_id": null,
            "topic_id": "201869033253581201408",
            "topic_type": "normal",
            "user_avatar": "https://img4.izaihang.cn/Fvi1o6Fr1y0Z1vUz6DV2_A-UQqRd",
            "user_id": "a1jfayl4zp",
            "user_nickname": "堂岛旺太郎",
            "user_random_status": true
    }
    ```
  
    
