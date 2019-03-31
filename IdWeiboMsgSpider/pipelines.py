# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os

class IdweibomsgspiderPipeline(object):
    def __init__(self):
        store_file1 = os.path.dirname(__file__) + '/get/UsertabelGet2add.csv'
        print("****************************创建csv文件***********************************")
        # 打开(创建)文件
        self.file1 = open(store_file1, 'a+', encoding='utf_8_sig', newline = '')
        # csv写法
        self.writer1 = csv.writer(self.file1, dialect="excel")

    def process_item(self, item, spider):
        print("正在写入......")
        # 虚假用户基本信息表1
        self.writer1.writerow([
                                item['user_id'],
                                item['user_name'],
                                item['user_sex'],
                                item['user_vip_des'],
                                item['user_sign'],
                                item['user_addr'],
                                item['user_name_other'],
                                item['user_concern_num'],
                                item['user_fans_num'],
                                item['user_weibo_num'],
                                item['user_work_at'],
                                item['user_edu'],
                                item['user_img_url'],
                                item['user_add_v'],
                                item['user_tab'],
                                item['user_birthday'],
                                item['user_qq'],
                                item['user_msn'],
                                item['user_email'],
                                item['user_creat_time'],
                                item['user_concern_list'],
                                item['user_is_vip'],
                                item['user_is_tanlent'],
                                item['user_vip_level']
        ])
        return item
        # 虚假用户基本信息表2
        # self.writer1.writerow([
        #     item['user_id'],
        #     item['user_name'],
        #     item['user_sex'],
        #     item['user_vip_des'],
        #     item['user_sign'],
        #     item['user_addr'],
        #     item['user_name_other'],
        #     item['user_concern_num'],
        #     item['user_fans_num'],
        #     item['user_weibo_num'],
        #     item['user_work_at'],
        #     item['user_edu'],
        #     item['user_img_url'],
        #     item['user_add_v'],
        #     item['user_tab'],
        #     item['user_birthday'],
        #     item['user_qq'],
        #     item['user_msn'],
        #     item['user_email'],
        #     item['user_creat_time'],
        #     item['user_concern_list'],
        #     item['user_is_vip'],
        #     item['user_is_tanlent'],
        #     item['user_vip_level']
        # ])
        # return item
