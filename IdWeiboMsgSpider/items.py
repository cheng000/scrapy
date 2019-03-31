# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IdweibomsgspiderItem(scrapy.Item):
    # define the fields for your item here like:
    user_id = scrapy.Field()  # 用户ID
    user_name = scrapy.Field()  # 屏幕名
    user_sex = scrapy.Field()  # 性别
    user_vip_des = scrapy.Field()  # VIP描述(null)
    user_sign = scrapy.Field()  # 自我介绍
    user_addr = scrapy.Field()  # 地区
    user_name_other = scrapy.Field()  # 用户名(null)
    user_concern_num = scrapy.Field()  # 关注
    user_fans_num = scrapy.Field()  # 粉丝
    user_weibo_num = scrapy.Field()  # 微博
    user_work_at = scrapy.Field()  # 工作(null)
    user_edu = scrapy.Field()  # 教育(null)
    user_img_url = scrapy.Field()  # 头像
    user_add_v = scrapy.Field()  # 加V
    user_tab = scrapy.Field()  # 标签
    user_birthday = scrapy.Field()  # 生日
    user_qq = scrapy.Field()  # QQ(null)
    user_msn = scrapy.Field()  # Msn(null)
    user_email = scrapy.Field()  # Email(null)
    user_creat_time = scrapy.Field()  # 创建时间(null)
    user_concern_list = scrapy.Field()  # 关注列表(null)
    user_is_vip = scrapy.Field()  # 会员
    user_is_tanlent = scrapy.Field()  # 达人
    user_vip_level = scrapy.Field()  # 等级

