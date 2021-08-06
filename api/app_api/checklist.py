from api.base_api import BaseApi


class CheckList(BaseApi):
    """
    清单接口集
    """
    data = BaseApi.yaml_load('/data/api_data/checklist.api.yaml')

    def checklists(self, title, is_private):
        """
        创建清单  1
        :param title: 清单名称
        :param is_private: 是否私密
        :return:
        """
        self.params = {'title': title, 'is_private': is_private}
        res = self.api_send(self.data['checklists'])
        return res

    def checklists_feeds(self):
        """
        清单首页列表  2
        :return:
        """
        res = self.api_send(self.data['checklists_feeds'])
        return res

    def get_checklists(self, checklists_id):
        """
        获取清单信息  3
        :param checklists_id: 清单id
        :return:
        """
        self.params = {'checklists_id': checklists_id}
        res = self.api_send(self.data['get_checklists'])
        return res

    def patch_checklists(self, checklists_id, title, is_private):
        """
        更新清单  4
        :param checklists_id:
        :param title:
        :param is_private:
        :return:
        """
        self.params = {'checklists_id': checklists_id, 'title': title, 'is_private': is_private}
        res = self.api_send(self.data['patch_checklists'])
        return res

    def delete_checklists(self, checklists_id):
        """
        删除清单  5
        :param checklists_id:
        :return:
        """
        self.params = {'checklists_id': checklists_id}
        res = self.api_send(self.data['delete_checklists'])
        return res

    def checklists_liked(self, checklists_id):
        """
        点赞清单  6
        :param checklists_id:
        :return:
        """
        self.params = {'checklists_id': checklists_id}
        res = self.api_send(self.data['checklists_liked'])
        return res

    def delete_checklists_liked(self, checklists_id):
        """
        取消点赞  7
        :param checklists_id:
        :return:
        """
        self.params = {'checklists_id': checklists_id}
        res = self.api_send(self.data['delete_checklists_liked'])
        return res

    def checklists_favored(self, checklists_id):
        """
        收藏清单  8
        :param checklists_id:
        :return:
        """
        self.params = {'checklists_id': checklists_id}
        res = self.api_send(self.data['checklists_favored'])
        return res

    def delete_checklists_favored(self, checklists_id):
        """
        取消收藏  9
        :param checklists_id:
        :return:
        """
        self.params = {'checklists_id': checklists_id}
        res = self.api_send(self.data['delete_checklists_favored'])
        return res

    def checklists_mark(self, checklists_id):
        """
        标记观看  10
        :param checklists_id:
        :return:
        """
        self.params = {'checklists_id': checklists_id}
        res = self.api_send(self.data['checklists_mark'])
        return res

    def checklists_share(self, checklists_id):
        """
        分享  11
        :param checklists_id:
        :return:
        """
        self.params = {'checklists_id': checklists_id}
        res = self.api_send(self.data['checklists_share'])
        return res

    def checklists_contents(self, checklists_id):
        """
        获取清单下单品  12
        :param checklists_id:
        :return:
        """
        self.params = {'checklists_id': checklists_id}
        res = self.api_send(self.data['checklists_contents'])
        return res

    def remove_checklists_contents(self, checklists_id, contents_id):
        """
        移除清单下单品  13
        :param checklists_id:
        :param contents_id: 单品id
        :return:
        """
        self.params = {'checklists_id': checklists_id, 'contents_id': '[{}]'.format(contents_id)}
        res = self.api_send(self.data['remove_checklists_contents'])
        return res

    def get_contents_checklists(self, content_id):
        """
        获取单品对应清单列表  14
        :param content_id:
        :return:
        """
        self.params = {'content_id': content_id}
        res = self.api_send(self.data['get_contents_checklists'])
        return res

    def add_contents_checklists(self, content_id, checklists):
        """
        将一个单品添加到多个清单  15
        :param content_id:
        :param checklists:
        :return:
        """
        self.params = {'content_id': content_id, 'checklists': '[{}]'.format(checklists)}
        res = self.api_send(self.data['add_contents_checklists'])
        return res

    def author_me_checklists(self):
        """
        获取当前用户清单  16
        :return:
        """
        res = self.api_send(self.data['author_me_checklists'])
        return res

    def author_me_checklists_add(self, content_id):
        """
        获取单品能够被加入的清单列表 17
        :param content_id:
        :return:
        """
        self.params = {'content_id': content_id}
        res = self.api_send(self.data['author_me_checklists_add'])
        return res

    def author_checklists(self, author_id):
        """
        获取指定用户的清单列表  18
        :param author_id: 用户id
        :return:
        """
        self.params = {'author_id': author_id}
        res = self.api_send(self.data['author_checklists'])
        return res

    def search_checklists(self, keyword):
        """
        搜索清单列表 19
        :param keyword: 关键字
        :return:
        """
        self.params = {'keyword': keyword}
        res = self.api_send(self.data['search_checklists'])
        return res

    def search_checklists_hints(self, keyword):
        """
        搜索关键字补全 20
        :param keyword: 关键字
        :return:
        """
        self.params = {'keyword': keyword}
        res = self.api_send(self.data['search_checklists_hints'])
        return res

    def batch_content_checklists(self, content_ids, checklist_ids):
        """
        空清单添加内容
        """
        self.params = {'contentIds': content_ids, 'checklistIds': checklist_ids}
        res = self.api_send(self.data['batch_content_checklists'])
        return res

# if __name__ == '__main__':
#     c = CheckList()
#     # c.checklists('bigllxx的清单', 'true')
#     # c.checklists_feeds()
#     # c.get_checklists('4Q2v2MQ5DMhC1OeKEMrQMdcGsSi7koa4RTA8wE1brkGjHkQvj')
#     # c.patch_checklists('4Q2v2MQ5DMhC1OeKEMrQMdcGsSi7koa4RTA8wE1brkGjHkQvj', 'bigllxx好物推荐', 'false')
#     # c.delete_checklists('4Q2v2MQ5DMhC1OeKEMrQMdcGsSi7koa4RTA8wE1brkGjHkQvj')
#     # c.checklists_liked('sWOhGKuzNhRqtcDmLQhQxssiIO2bnW8Q06iczryYvF74c0HQ')
#     # c.delete_checklists_liked('sWOhGKuzNhRqtcDmLQhQxssiIO2bnW8Q06iczryYvF74c0HQ')
#     # c.checklists_favored('sWOhGKuzNhRqtcDmLQhQxssiIO2bnW8Q06iczryYvF74c0HQ')
#     # c.delete_checklists_favored('sWOhGKuzNhRqtcDmLQhQxssiIO2bnW8Q06iczryYvF74c0HQ')
#     # c.checklists_mark('sWOhGKuzNhRqtcDmLQhQxssiIO2bnW8Q06iczryYvF74c0HQ')
#     # c.checklists_share('47ZYIWhOAgR8MVsgdG1OfNiytoIPLQN3928AVhk6xwxHqFVoR')
#     # c.checklists_contents('sWOhGKuzNhRqtcDmLQhQxssiIO2bnW8Q06iczryYvF74c0HQ')
#     # c.get_contents_checklists('1V5eTggCMr6YOcU7QZvd5cqWZRBpiPz3Lxd6wVTk2YWIKxJN7')
#     # c.add_contents_checklists('1V5eTggCMr6YOcU7QZvd5cqWZRBpiPz3Lxd6wVTk2YWIKxJN7',
#                               # '[47ZYIWhOAgR8MVsgdG1OfNiytoIPLQN3928AVhk6xwxHqFVoR]')
#     # c.author_me_checklists()
#     # c.author_me_checklists_add('1V5eTggCMr6YOcU7QZvd5cqWZRBpiPz3Lxd6wVTk2YWIKxJN7')
#     # c.author_checklists('lr0wcBTApf3xAuSJe3pVK3uHM5vfJ0nwFdupu7L0VqEmSvt3')
#     c.search_checklists_hints('育儿')

