# Dizhua-Api
有关递爪APP的相关API，非官方

![Python3.8](https://img.shields.io/badge/Python-3.8-brightgreen) 
[![Build Status](https://travis-ci.org/ken3613/Dizhua-Api.svg?branch=master)](https://travis-ci.org/ken3613/Dizhua-Api) 
[![codecov](https://codecov.io/gh/ken3613/Dizhua-Api/branch/master/graph/badge.svg?token=qWbwx459b4)](https://codecov.io/gh/ken3613/Dizhua-Api)

### API列表

> [1、聚会记录](#聚会记录)
>
> [2、用户信息](#用户信息)

### API方法

##### 聚会记录

- 调用方法

  ```
  API地址：https://apis-ff.zaih.com/flash-whisper/v2/applications?filter=all
  方法：GET
  Headers：
          Authorization:你的JWT
          Host:apis-ff.zaih.com
          User-Agent:ios dizhuaApp 1.26.0(暂时未知版本号对api调用的影响)
  ```

- 返回值

  ```
  返回值：包含所有聚会信息的字典列表
  Content-Type：application/json
  ```

- 字典字段详情

  ```
  character_id        未知
  chat_id             未知
  date_created        聚会被创建时间，格式为含时区的标准datetime格式，时区为utc
  date_now            聚会报名时间，格式为含时区的标准datetime格式，时区为utc
  date_started        聚会开始时间，格式为含时区的标准datetime格式，时区为utc
  icon_url            聚会图标url
  id                  聚会ID，可用于查询聚会详情API
  name                聚会名称
  result_status       聚会结果，值为fail或success，真正意义未知
  room_chat_id        聚会房间ID
  status              聚会状态，值为talking_over/canceled/quit
  template_type       聚会模版/类型，值normal为普通聚会，值parlor为客厅
  topic_creator_id    聚会创建者ID，普通聚会为null，客厅为客厅主人user_id
  topic_id            聚会主题ID
  topic_type          未知,值为normal等
  user_avatar         匿名人物的头像
  user_id             查询者user_id
  user_nickname       匿名人物的昵称
  user_random_status  未知，当前值恒为true
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

  

##### 用户信息

- 调用方法

  ```
  API地址：https://dz.zaih.com/activity/whisper_api/v2/square/accounts/user_id
  方法：GET
  Headers:
          Host:dz.zaih.com
          User-Agent:ios dizhuaApp 1.26.0 (暂时未知版本号对api调用的影响)
          Authorization:你的JWT (本Headers可忽略，区别请看下方字段详情)
  ```

- 返回值

  ```
  返回值：用户账号信息字典
  Content-Type：application/json
  ```

- 字典字段详情

  ```
  age              		用户设定的出生年份
  avatar           		用户头像url
  city             		用户设定的所在城市/城市的行政区，值为汉字
  close_grade			爪级
  current_age      		用户年龄，值为"xx岁"
  emchat_id        		未知
  enable_parlor			true/false，客厅主人标识
  gender           		性别，0为女性，1为男性
  has_blacked      		是否设置为黑名单，bool
  has_greeted			是否递爪，bool
  has_parlor			是否拥有客厅，bool
  headwear         		未知
  is_blocked       		是否设置屏蔽，bool
  is_greeted			是否递爪，bool
  is_official			是否官方人员，bool
  is_view_friend   		是否为爪友，bool
  is_view_self			是否查看的是自己，bool
  journal				用户的兴趣话题，list(array)
  kindness_level			喵级，int
  matched_pct			三观相合百分比,int
  my_three_test_is_done		是否完成三观测试，bool
  online_status			在线状态，string，如："1小时前在线"
  self_cover			封面图url，string
  today_topic			未知
  total_gift			总共收到的礼物，int
  user_id				用户userId，string
  user_nickname			用户昵称，string
  ```


- 用户信息字典样例  

  ```
  {
      "age": "1950",
      "avatar": "https://img4.izaihang.cn/FrVoCW80au4lois24p1KIvXNQ8Qc!avatar",
      "city": "杭州",
      "close_grade": 1.5,
      "current_age": "70岁",
      "emchat_id": "hx2046236280907390",
      "enable_parlor": true,
      "friend_remark": "",
      "gender": 0,
      "has_blacked": false,
      "has_greeted": false,
      "has_parlor": true,
      "headwear": "",
      "is_blocked": false,
      "is_greeted": true,
      "is_official": false,
      "is_view_friend": true,
      "is_view_self": false,
      "journal": [],
      "kindness_level": 8,
      "matched_pct": 62,
      "my_three_test_is_done": true,
      "online_status": "1小时前在线",
      "self_cover": "https://img4.izaihang.cn/FkeAF92XQW-o7skvFb6s2l0Eh7ze",
      "today_topic": null,
      "total_gift": "9464",
      "user_id": "a4enufamiy",
      "user_nickname": "西西弗斯之歌"
  }
  ```

  

  