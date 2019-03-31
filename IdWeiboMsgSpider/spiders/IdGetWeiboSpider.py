# -*- coding: utf-8 -*-
# @Author: hc
# @Email: cheng_H@163.com
# @Project: IdWeiboMsgSpider
# @File:   IdGetWeiboSpider.py
# @IDE: PyCharm 
# @CreateTime:   2019/3/19 17:11
# @Desc:根据指定csv文件中的微博用户id，爬取其基本信息

import re

import scrapy
import time
import csv
import os
from scrapy import Request
from IdWeiboMsgSpider.items import IdweibomsgspiderItem

class IdGetWeiboMsgSpider(scrapy.Spider):
    name = 'IdGetWeiboSpider'
    # start_urls = ['https://weibo.cn/3479625264']

    def __init__(self):
        self.cookie = {
            '_T_WM': '2a4255f0dbddfde000f7816f9c53bfa1',
            'SCF': 'Aje1ou_Gs5if3JqQM64Ru1mgGZZdOM3ul0_U6KjdjaCTGQjpuFLGCYwJqSRem54d333Up6iCkKV9IhLWUOy3Dxc.',
            'SUB': '_2A25xll0cDeRhGeNP6VUW8C3EyDWIHXVTeWNUrDV6PUJbkdANLXnskW1NTouUEUw-wv21Y083HbRd4fGqpVQRN7BR',
            'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh6Gd-ozMyR9ATFeUr7RAkX5JpX5K-hUgL.Fo-peoMNeheRe0.2dJLoIEXLxK-L1K-LBKBLxK.L1h-L1KzLxKqL12BLBKzLxK-L1KzL1KqLxK-L1K-LBK2t',
            'SUHB': '0V5lWYF6fJp5We',
            'SSOLoginState': '1553083724',
            '_WEIBO_UID': '5127703839'
        }
        self.header = {
            'Referer': 'https://weibo.cn',
        }
        self.id_list = []
        self.id_get_list = []
        self.id_list_filter = []


        self.index = 2
        self.user_id = 0
        self.user_name = ''
        self.user_is_tanlent = 0
        self.user_sex = ''
        self.user_vip_des = ''
        self.user_addr = ''
        self.user_name_other = ''
        self.user_sign = ''
        self.user_weibo_num = 0
        self.user_concern_num = 0
        self.user_fans_num = 0
        self.user_work_at = ''
        self.user_edu = ''
        self.user_img_url = ''
        self.user_vip_level = 0
        self.user_birthday = ""
        self.user_tab = ""
        self.user_is_vip = 0
        self.user_add_v = 0

    def start_requests(self):
        print("《《《start_requests")
        # 第一遍 读取csv文件中的用户id (即读取csv文件第一列)
        file_addr = os.path.dirname(__file__)+'/data/usertableG2.csv'
        print(file_addr)
        try:
            file = open(file_addr, 'r')  # 打开文件
        except FileNotFoundError:
            print('文件不存在')
        else:
            stus = csv.reader(file)  # 读取文件内容
            index = 0
            for stu in stus:  # 一行是一个数组
                if index != 0:
                    # print(stu[0])  # 取每个数组的第一个元素
                    self.id_list.append(stu[0])
                index += 1

        # # 开始
        # id_index = 1
        # for id_list_in in self.id_list:
        #     # time.sleep(2)
        #     print("爬取第"+str(id_index)+"个用户……,还剩"+str(len(self.id_list)-id_index)+"个")
        #     try:
        #         yield Request('https://weibo.cn/'+str(id_list_in), callback=self.user_parse, cookies=self.cookie, headers=self.header, meta={'id':str(id_list_in)})
        #         yield Request('https://weibo.cn/' + str(id_list_in)+'/info', callback=self.user_info, cookies=self.cookie, headers=self.header, meta={'id':str(id_list_in)})
        #     except Exception:
        #         time.sleep(5)
        #     id_index += 1



        # 第二遍读取（补漏）
        # 读取csv文件中的用户id (即读取csv文件第一列)
        file_get_addr = 'E:\scrapy\IdWeiboMsgSpider\IdWeiboMsgSpider' + '/get/UsertabelGet2.csv'
        print(file_get_addr)
        try:
            file = open(file_get_addr, encoding='utf-8')  # 打开文件
        except FileNotFoundError:
            print('文件不存在')
        else:
            stus = csv.reader(file)  # 读取文件内容
            index_get = 0
            for stu in stus:  # 一行是一个数组
                if index_get != 0:
                    # print(stu[0])  # 取每个数组的第一个元素
                    self.id_get_list.append(stu[0])
                index_get += 1
        # 爬取漏掉的
        print('漏掉：'+str(len(self.id_list)-len(self.id_get_list))+"个")
        id_get_index = 0
        for id_get in self.id_list:
            if id_get not in self.id_get_list:
                id_get_index += 1
                print("爬取遗漏的第" + str(id_get_index) + "个用户……,还剩" + str(len(self.id_list)-len(self.id_get_list) - id_get_index) + "个")
                try:
                    yield Request('https://weibo.cn/' + str(id_get), callback=self.user_parse, cookies=self.cookie,
                                  headers=self.header, meta={'id': str(id_get)})
                    yield Request('https://weibo.cn/' + str(id_get) + '/info', callback=self.user_info,
                                  cookies=self.cookie, headers=self.header, meta={'id': str(id_get)})
                except Exception:
                    time.sleep(5)


    def user_parse(self, response):
        print("《《《user_parse")
        # 用户基本信息（昵称、性别、地址、微博数、关注数、粉丝数、是否达人、个性签名、头像url）
        user = response.xpath("//div[@class='ut']/span[@class='ctt'][1]/text()").extract()
        if user != []:
            if self.index != 1:
                self.user_id = str(re.findall("\d+",response.meta['id'])[0])
                print("user_id:" + self.user_id)
                user_msg = ''
                for user_in in user:
                    # print(user_in)
                    user_in = str(user_in)
                    user_msg = user_in.split(' ')
                user_name = user_msg[0].strip()
                self.user_name = user_name

                if user_name == '':
                    user_name = response.xpath("//div[@class ='ut']/span[@ class ='ctt'][1]/text()[1]").extract()
                    for user_name_in in user_name:
                        user_name_in = str(user_name_in)
                        user_name = user_name_in
                    self.user_name = user_name
                    self.user_is_tanlent = 1
                    print("user_name:" + user_name)
                    print("user_is_tanlent："+str(self.user_is_tanlent))
                else:
                    self.user_is_tanlent = 0
                    print("user_name:" + self.user_name)
                    print("user_is_tanlent：" + str(self.user_is_tanlent))

                user_sex = user_msg[1].split('/')[0].strip()
                self.user_sex = user_sex
                print("user_sex:" + user_sex)

                self.user_vip_des = ''

                user_addr = user_msg[1].split('/')[1].strip()
                self.user_addr = user_addr
                print("user_addr:" + user_addr)

                self.user_name_other = ''

                # 个性签名：
                user_sign_list = response.xpath("//div[@class='ut']/span[@class='ctt'][2]/text()").extract()
                if user_sign_list == []:
                    user_sign = ''
                    self.user_sign = user_sign
                    print("user_sign:" + user_sign)
                elif user_sign_list != []:
                    for user_sign in user_sign_list:
                        user_sign = str(user_sign)
                        self.user_sign = user_sign
                        print("user_sign:" + user_sign)

                # 微博数
                user_weibo_num = response.xpath("//div[@class='tip2']/span[@class='tc']/text()").extract()
                for user_weibo_num_in in user_weibo_num:
                    user_weibo_num_in = str(re.findall("\d+", user_weibo_num_in)[0])
                    self.user_weibo_num = user_weibo_num_in
                    print("user_weibo_num：" + user_weibo_num_in)

                # 关注数
                user_concern_num = response.xpath("//div[@class='tip2']/a[1]/text()").extract()
                for user_concern_num_in in user_concern_num:
                    user_concern_num_in = str(re.findall("\d+", user_concern_num_in)[0])
                    self.user_concern_num = user_concern_num_in
                    print("user_concern_num:" + user_concern_num_in)

                # 粉丝数
                user_fans_num = response.xpath("//div[@class='tip2']/a[2]/text()").extract()
                for user_fans_num_in in user_fans_num:
                    user_fans_num_in = str(re.findall("\d+", user_fans_num_in)[0])
                    self.user_fans_num = user_fans_num_in
                    print("user_fans_num:" + user_fans_num_in)

                self.user_work_at = ''
                self.user_edu = ''

                # 头像url
                img_url_list = response.xpath("//div[4]//a/img/@src").extract()
                img_url = ''
                for img_url_list_in in img_url_list:
                    img_url = str(img_url_list_in)
                self.user_img_url = img_url
                print("user_img_url:" + img_url)

                # 加V
                user_add_v = response.xpath("//span[@class = 'ctt']/img/@alt").extract()
                index = 0
                for user_add_v_in in user_add_v:
                    if index == 0:
                        if str(user_add_v_in) == "V":
                            self.user_add_v = 1
                        else:
                            self.user_add_v = 0
                    index += 1

        else:
            print("user_parse挂了")
            self.user_id = "###"



    def user_info(self, response):
        print("《《《user_info")
        # 微博用户资料（生日、会员等级、标签）

        # 会员等级
        user_vip_level = response.xpath("//div[5]/text()[1]").extract()
        for user_vip_level_in in user_vip_level:
            if str(user_vip_level_in) == "会员等级：未开通 ":
                print("vip_level: 0")
                self.user_vip_level = 0
                self.user_is_vip = 0
            else:
                user_level_num = str(re.findall("\d+", user_vip_level_in)[0])
                print("vip_level: "+user_level_num)
                self.user_vip_level = int(user_level_num)
                self.user_is_vip = 1

        # 生日
        user_birthday_list = response.xpath("//div[7]/text()").extract()
        for user_birthday_in in user_birthday_list:
            if str(user_birthday_in).find("生日:") != -1:
                user_birthday = str(user_birthday_in).split(":")[1]
                self.user_birthday = user_birthday
            else:
                self.user_birthday = ""

        # 标签
        user_tab_list = response.xpath("//div[7]/text()").extract()
        for user_tab_list_in in user_tab_list:
            if str(user_tab_list_in).find("达人:") != -1:
                self.user_tab = str(user_tab_list_in).split(":")[1]

        # self.id_list_filter.append(response.meta['id'])
        # # 去掉重复的id
        # if self.user_id not in self.id_list_filter:
        item = IdweibomsgspiderItem()
        item['user_id'] = self.user_id
        item['user_name'] = self.user_name
        item['user_sex'] = self.user_sex
        item['user_vip_des'] = self.user_vip_des
        item['user_sign'] = self.user_sign
        item['user_addr'] = self.user_addr
        item['user_name_other'] = self.user_name_other
        item['user_concern_num'] = self.user_concern_num
        item['user_fans_num'] = self.user_fans_num
        item['user_weibo_num'] = self.user_weibo_num
        item['user_work_at'] = self.user_work_at
        item['user_edu'] = self.user_edu
        item['user_img_url'] = self.user_img_url
        item['user_add_v'] = self.user_add_v
        item['user_tab'] = self.user_tab
        item['user_birthday'] = self.user_birthday
        item['user_qq'] = ''
        item['user_msn'] = ''
        item['user_email'] = ''
        item['user_creat_time'] = ''
        item['user_concern_list'] = ''
        item['user_is_vip'] = self.user_is_vip
        item['user_is_tanlent'] = self.user_is_tanlent
        item['user_vip_level'] = self.user_vip_level
        yield item
        print("存入……")