from api.base_api import BaseApi


class Ttp(BaseApi):
    """
    ttp接口集
    """
    data = BaseApi.yaml_load('/data/api_data/ttp.api.yaml')

    def tab(self):
        """
        获取首页tab  1
        :return:
        """
        res = self.api_send(self.data['tab'])
        return res

    def bulletin(self):
        """
        获取公告列表  2
        :return:
        """
        res = self.api_send(self.data['bulletin'])
        return res

    def me_contents(self, state):
        """
        获取个人文章列表  3
        :param state:
        :param offset:
        :param limit:
        :return:
        """
        self.params = {'state': state}
        res = self.api_send(self.data['me_contents'])
        return res

    def me_search_my_contents(self, titleKeyWord, state):
        """
        搜索个人文章列表  4
        :param titleKeyWord:
        :param state:
        :param offset:
        :param limit:
        :return:
        """
        self.params = {'titleKeyWord': titleKeyWord, 'state': state}
        res = self.api_send(self.data['me_search_my_contents'])
        return res

    def me(self):
        """
        获取个人信息  5
        :return:
        """
        res = self.api_send(self.data['me'])
        return res

    def feeds(self, content_type, tab):
        """
        获取首页文章列表  6
        :param content_type:
        :return:
        """
        self.params = {'content_type': content_type, 'tab': tab}
        res = self.api_send(self.data['feeds'])
        return res

    def feeds_touched(self, fetchType, ids):
        """
        已经看到文章的上报接口  7
        :param fetchType:
        :param ids:
        :return:
        """
        self.params = {'fetchType': fetchType, 'ids': ids}
        res = self.api_send(self.data['feeds_touched'])
        return res

    def favorite(self, begin):
        """
        获得关注列表  8
        :return:
        """
        self.params = {'begin': begin}
        res = self.api_send(self.data['favorite'])
        return res

    def send_feed_back(self, contact, content):
        """
        上传用户反馈  9
        :param contact:
        :param content:
        :return:
        """
        self.params = {'contact': contact, 'content': content}
        res = self.api_send(self.data['send_feed_back'])
        return res

    def author_me(self):
        """
        获取当前作者信息  10
        :return:
        """
        res = self.api_send(self.data['author_me'])
        return res

    def author_me_update(self, nickname, avatar):
        """
        更新作者信息  11
        :param nickname: 名称
        :param avatar: 头像
        :return:
        """
        self.params = {'nickname': nickname, 'avatar': avatar}
        res = self.api_send(self.data['author_me_update'])
        return res

    def author_me_content(self, content_type):
        """
        我的发布  12
        :param content_type: 类型 呼啦圈（post）文章（snack）
        :return:
        """
        self.params = {'contentType': content_type}
        res = self.api_send(self.data['author_me_content'])
        return res

    def author_me_footprint(self):
        """
        我的足迹  13
        :return:
        """
        res = self.api_send(self.data['author_me_footprint'])
        return res

    def author_me_liked(self, content_type):
        """
        我的点赞  14
        :param content_type: 类型 呼啦圈（post）文章（snack）
        :return:
        """
        self.params = {'contentType': content_type}
        res = self.api_send(self.data['author_me_liked'])
        return res

    def author_me_favored(self, content_type, offset, limit):
        """
        我的收藏  15
        :param content_type: 类型 呼啦圈（post）文章（snack）
        :param offset: 偏移量
        :param limit: 条数
        :return:
        """
        self.params = {'contentType': content_type, 'offset': offset, 'limit': limit}
        res = self.api_send(self.data['author_me_favored'])
        return res

    def author_id(self, id):
        """
        根据id获取作者信息  16
        :param id: 作者id
        :return:
        """
        self.params = {'id': id}
        res = self.api_send(self.data['author_id'])
        return res

    def author_id_content(self, id, content_type):
        """
        根据id获取作者文章列表  17
        :param id:
        :param content_type:
        :return:
        """
        self.params = {'id': id, 'content_type': content_type}
        res = self.api_send(self.data['author_id_content'])
        return res

    def contents(self, ids):
        """
        文章详情  20
        :param ids:
        :return:
        """
        self.params = {'ids': '[{}]'.format(ids)}
        res = self.api_send(self.data['contents'])
        return res

    def creat_contents(self, state, title, quote_text, paragraph_text, labels):
        """
        创建文章  21
        :param state: 文章状态 normal, deleted, disable, draft
        :param title: 文章标题
        :param quote_text: quote格式正文内容
        :param paragraph_text: paragraph格式正文内容
        :param labels: 标签list
        :return:
        """
        self.params = {'state': state, 'title': title, 'quote_text': quote_text, 'paragraph_text': paragraph_text,
                       'labels': labels}
        res = self.api_send(self.data['creat_contents'])
        return res

    def contents_snack(self, title, content, labels, goods, checklists):
        """
        新增单品  22
        :param title: 单品
        :param content: 内容
        :param labels: 标签list
        :param goods: 商品id
        :param checklists: 清单id
        :return:
        """
        self.params = {'title': title, 'content': content, 'labels': labels, 'goods': goods, 'checklists': checklists}
        res = self.api_send(self.data['contents_snack'])
        return res

    def contents_snack_contentid(self, contentId):
        # 更新单品  23
        # todo: 参数补全 不知道那些字段是能修改的
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['contents_snack_contentid'])
        return res

    def get_contents(self, contentId):
        """
        文章详情，创作者中心使用  24
        :param contentId:
        :return:
        """
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['get_contents'])
        return res

    def patch_contents(self, contentId):
        # 更新文章 25
        # todo: 参数补全 不知道那些字段是能修改的
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['patch_contents'])
        return res

    def del_contents(self, contentId):
        """
        删除文章  26
        :param contentId:
        :return:
        """
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['del_contents'])
        return res

    def contents_mark_view(self, contentId):
        """
        标记已阅读  27
        :param contentId:
        :return:
        """
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['contents_mark_view'])
        return res

    def contents_is_liked(self, contentId):
        """
        文章是否已点赞  28
        :param contentId:
        :return:
        """
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['contents_is_liked'])
        return res

    def contents_is_like(self, contentId):
        """
        点赞  29
        :param contentId:
        :return:
        """
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['contents_is_like'])
        return res

    def contents_is_cancel_like(self, contentId):
        """
        取消点赞  30
        :param contentId:
        :return:
        """
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['contents_is_cancel_like'])
        return res

    def contents_share(self, contentId):
        """
        分享  31
        :param contentId:
        :return:
        """
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['contents_share'])
        return res

    def contents_report(self, contentId):
        """
        举报  32
        :param contentId:
        :return:
        """
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['contents_report'])
        return res

    def contents_is_favored(self, contentId):
        """
        文章是否已关注  33
        :param contentId:
        :return:
        """
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['contents_is_favored'])
        return res

    def contents_is_creat_favored(self, contentId):
        """
        添加关注  34
        :param contentId:
        :return:
        """
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['contents_is_creat_favored'])
        return res

    def contents_is_del_favored(self, contentId):
        """
        取消关注  35
        :param contentId:
        :return:
        """
        self.params = {'contentId': contentId}
        res = self.api_send(self.data['contents_is_del_favored'])
        return res

    def guess_like_list(self):
        """
        猜你喜欢  36
        :return:
        """
        res = self.api_send(self.data['guess_like_list'])
        return res

    def recommend_banner(self):
        """
        首页banner推荐  37
        :return:
        """
        res = self.api_send(self.data['recommend_banner'])
        return res

    def transfer(self, file, custom):
        """
        转存图片  38
        :param file:
        :param custom:
        :return:
        """
        self.params = {'file': file, 'custom': custom}
        res = self.api_send(self.data['transfer'])
        return res

    def upload(self, type, target, custom):
        """
        获取图片上传相关信息  39
        :param type:
        :param target:
        :param custom:
        :return:
        """
        self.params = {'type': type, 'target': target, 'custom': custom}
        res = self.api_send(self.data['upload'])
        return res

    def upload_sts(self, target):
        """
        获取oss临时token，给客户端sdk调用  40
        :param target:
        :return:
        """
        self.params = {'target': target}
        res = self.api_send(self.data['upload_sts'])
        return res

    def upload_callback(self, filename, size, height, width):
        """
        文件上传回调，oss调用  41
        :param filename:
        :param size:
        :param height:
        :param width:
        :return:
        """
        self.params = {'filename': filename, 'size': size, 'height': height, 'width': width}
        res = self.api_send(self.data['upload_callback'])
        return res

    def upgrate(self):
        """
        获取升级信息  42
        :return:
        """
        res = self.api_send(self.data['upgrate'])
        return res
