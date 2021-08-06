import sys
import allure
import pytest
from api.base_api import BaseApi
from api.app_api.ttp import Ttp
from common.logs import Logger


@allure.feature('ttp相关接口')
class TestTtp:
    data = BaseApi.yaml_load('/data/case_data/ttp.data.yaml')

    @classmethod
    def setup_class(cls):
        cls.ttp = Ttp()
        cls.ttp.log = Logger('ttp')
        try:
            cls.content_id = cls.ttp.creat_contents('normal', '新建文章标题', '内容1', '内容2', '[]').json()['contentId']
        except:
            cls.ttp.log.logger.error('新建内容/获取content_id失败')
            sys.exit()

    @classmethod
    def teardown_class(cls):
        cls.ttp.del_contents(cls.content_id)

    @allure.story('获取精选文章tab 1')
    def test_tab(self):
        res = self.ttp.tab()
        self.ttp.my_assert(res, 'assert len(res.json()) > 0')

    @allure.story('获取公告 2')
    def test_bulletin(self):
        res = self.ttp.bulletin()
        self.ttp.my_assert(res, "assert res.status_code == 200")

    @allure.story('获取个人文章列表 3')
    @pytest.mark.parametrize('state', data['test_me_contents'])
    def test_me_contents(self, state):
        res = self.ttp.me_contents(state)
        self.ttp.my_assert(res, 'assert res.status_code == 200')

    @allure.story('搜索个人文章列表 4')
    @pytest.mark.parametrize('titleKeyWord, state', data['test_me_search_my_contents'])
    def test_me_search_my_contents(self, titleKeyWord, state):
        res = self.ttp.me_search_my_contents(titleKeyWord, state)
        a = """
if args[0] != '':
    assert 'list' in res.json()
else:
    assert res.json()['errCode'] == 10000
        """
        self.ttp.my_assert(res, a, titleKeyWord)

    @allure.story('获取个人信息 5')
    def test_me(self):
        res = self.ttp.me()
        self.ttp.my_assert(res, "assert res.json()['id']")

    @allure.story('获取首页文章列表 6')
    @pytest.mark.parametrize('content_type, tab', data['test_feeds'])
    def test_feeds(self, content_type, tab):
        res = self.ttp.feeds(content_type, tab)
        self.ttp.my_assert(res, "assert res.json()['list'][0]['type'] == args[0]", content_type)

    @allure.story('已经看到的文章上报接口 7')
    @pytest.mark.parametrize('fetchType', data['test_feeds_touched'])
    def test_feeds_touched(self, fetchType):
        feeds = self.ttp.feeds('post', '').json()['list']
        ids = repr([feeds[0]['id'], feeds[1]['id']])
        res = self.ttp.feeds_touched(fetchType, ids)
        self.ttp.my_assert(res, "assert res.status_code == 204")

    @allure.story('上传用户反馈 9')
    @pytest.mark.parametrize('contact, content', data['test_send_feed_back'])
    def test_send_feed_back(self, contact, content):
        res = self.ttp.send_feed_back(contact, content)
        self.ttp.my_assert(res, "assert res.status_code == 201")

    @allure.story('获取当前作者信息 10')
    def test_author_me(self):
        res = self.ttp.author_me()
        self.ttp.my_assert(res, "assert res.json()['id']")

    @allure.story('更新作者信息 11')
    @pytest.mark.parametrize('nickname, avatar', data['test_author_me_update'])
    def test_author_me_update(self, nickname, avatar):
        res = self.ttp.author_me_update(nickname, avatar)
        name = self.ttp.author_me().json()['nickname']
        self.ttp.my_assert(res, 'assert args[0] == args[1]', name, nickname)

    @allure.story('我的发布 12')
    @pytest.mark.parametrize('content_type', ['post', 'snack'])
    def test_author_me_content(self, content_type):
        res = self.ttp.author_me_content(content_type)
        a = """
if len(res.json()['list']) == 0:
    assert True
else:
    assert res.json()['list'][0]['type'] == args[0]
        """
        self.ttp.my_assert(res, a, content_type)

    @allure.story('我的足迹 13')
    def test_author_me_footprint(self):
        res = self.ttp.author_me_footprint()
        self.ttp.my_assert(res, 'assert res.json()["code"] == 0')

    @allure.story('我的点赞 14')
    @pytest.mark.parametrize('content_type', ['post', 'snack', ''])
    def test_author_me_liked(self, content_type):
        res = self.ttp.author_me_liked(content_type)
        a = """
if len(res.json()['list']) == 0:
    assert True 
elif args[0] == '':
    assert res.json()['list'][0]['type'] == 'post' or 'snack'
else:
    assert res.json()['list'][0]['type'] == args[0]
                """
        self.ttp.my_assert(res, a, content_type)

    @allure.story('我的收藏 15')
    @pytest.mark.parametrize('content_type', ['post', 'snack'])
    def test_author_me_favored(self, content_type):
        res = self.ttp.author_me_liked(content_type)
        a = """
if len(res.json()['list']) != 0:
    assert res.json()['list'][0]['type'] == args[0]
        """
        self.ttp.my_assert(res, a, content_type)

    @allure.story('作者信息 16')
    def test_author_id(self):
        author_id = self.ttp.author_me().json()['id']
        res = self.ttp.author_id(author_id)
        self.ttp.my_assert(res, "assert 'id' in res.json()")

    @allure.story('根据id获取作者文章列表 17')
    @pytest.mark.parametrize('content_type', ['post', 'snack', 'video'])
    def test_author_id_content(self, content_type):
        author_id = self.ttp.author_me().json()['id']
        res = self.ttp.author_id_content(author_id, content_type)
        self.ttp.my_assert(res, "assert res.status_code == 200")

    @allure.story('获取文章详情 20')
    def test_contents(self):
        res = self.ttp.contents(self.content_id)
        self.ttp.my_assert(res, "assert res.json()[0]['id'] == args[0]", self.content_id)

    @allure.story('获取文章详情 24')
    def test_get_contents(self):
        res = self.ttp.get_contents(self.content_id)
        self.ttp.my_assert(res, "assert 'type' in res.json()")

    @allure.story('创建文章 21')
    @pytest.mark.parametrize('state, title, quote_text, paragraph_text, labels', data['test_creat_contents'])
    def test_creat_contents(self, state, title, quote_text, paragraph_text, labels):
        res = self.ttp.creat_contents(state, title, quote_text, paragraph_text, labels)
        a = """
if args[1] != '':
    assert 'contentId' in res.json()
    args[0].del_contents(res.json()['contentId'])
else:
    assert 'errCode' in res.json()
        """
        self.ttp.my_assert(res, a, self.ttp, title)

    # @allure.story('更新文章 25')
    # @pytest.mark.skip(reason='不执行该用例')
    # def test_patch_contents(self):
    #     # todo: 参数补全  23
    #     res = self.ttp.patch_contents(self.contents_id[0])

    @allure.story('新增单品')
    @pytest.mark.parametrize('title, content, labels, goods, checklists', data['test_contents_snack'])
    def test_contents_snack(self, title, content, labels, goods, checklists):
        res = self.ttp.contents_snack(title, content, labels, goods, checklists)
        a = """
if args[1] != '':
    assert 'contentId' in res.json()
    args[0].del_contents(res.json()['contentId'])
else:
    assert 'errCode' in res.json()
                """
        self.ttp.my_assert(res, a, self.ttp, title)

    # @allure.story('更新单品 23')
    # @pytest.mark.skip(reason='不执行该用例')
    # def test_contents_snack_contentid(self, contentId):
    #     # todo: 参数补全  23
    #     res = self.ttp.contents_snack_contentid(self.contents_id[-1])

    @allure.story('删除文章 26')
    def test_del_contents(self):
        """
        删除文章 26
        :return:
        """
        content_id = self.ttp.creat_contents('normal', '新建文章标题', '内容1', '内容2', '[]').json()['contentId']
        res = self.ttp.del_contents(content_id)
        self.ttp.my_assert(res, "assert res.status_code == 200")

    @allure.story('标为已读 27')
    def test_contents_mark_view(self):
        res = self.ttp.contents_mark_view(self.content_id)
        self.ttp.my_assert(res, "assert res.status_code == 204")

    @allure.story('点赞&查询是否点赞 29')
    def test_contents_is_like(self):
        self.ttp.contents_is_like(self.content_id)  # 点赞
        res = self.ttp.contents_is_liked(self.content_id)  # 是否点赞
        self.ttp.my_assert(res, "assert res.json()['isLiked'] is True")

    @allure.story('取消点赞 30')
    def test_contents_is_cancel_like(self):
        self.ttp.contents_is_like(self.content_id)  # 点赞
        self.ttp.contents_is_cancel_like(self.content_id)  # 取消点赞
        res = self.ttp.contents_is_liked(self.content_id)  # 是否点赞
        self.ttp.my_assert(res, "assert res.json()['isLiked'] is False")

    @allure.story('分享 31')
    def test_contents_share(self):
        res = self.ttp.contents_share(self.content_id)
        self.ttp.my_assert(res, "assert res.status_code < 210")

    @allure.story('举报 32')
    def test_contents_report(self):
        res = self.ttp.contents_report(self.content_id)
        self.ttp.my_assert(res, "assert res.status_code < 210")

    @allure.story('文章是否已关注 33')
    def test_contents_is_favored(self):
        res = self.ttp.contents_is_favored(self.content_id)
        self.ttp.my_assert(res, "assert 'isFavored' in res.json()")

    @allure.story('关注 34')
    def test_contents_is_creat_favored(self):
        self.ttp.contents_is_creat_favored(self.content_id)
        res = self.ttp.contents_is_favored(self.content_id)
        self.ttp.my_assert(res, "assert res.json()['isFavored'] is True")

    @allure.story('取消关注 35')
    def test_contents_is_del_favored(self):
        self.ttp.contents_is_creat_favored(self.content_id)
        self.ttp.contents_is_del_favored(self.content_id)
        res = self.ttp.contents_is_favored(self.content_id)
        self.ttp.my_assert(res, "assert res.json()['isFavored'] is False")

    @allure.story('猜你喜欢 36')
    def test_guess_like_list(self):
        res = self.ttp.guess_like_list()
        self.ttp.my_assert(res, "assert len(res.json()) == 2")

    @allure.story('获取banner图 37')
    def test_recommend_banner(self):
        res = self.ttp.recommend_banner()
        self.ttp.my_assert(res, "assert type(res.json()) is list")

    # @allure.story('转存图片 38')
    # @pytest.mark.skip(reason='不执行该用例')
    # @pytest.mark.parametrize('file, custom', [('1', '1')])
    # def test_transfer(self, file, custom):
    #     res = self.ttp.transfer(file, custom)
    #
    # @allure.story('获取图片上传相关信息 39')
    # @pytest.mark.skip(reason='不执行该用例')
    # @pytest.mark.parametrize('type, target, custom', [('', '', '')])
    # def test_upload(self, type, target, custom):
    #     res = self.ttp.upload(type, target, custom)
    #
    # @allure.story('获取oss临时token 40')
    # @pytest.mark.skip(reason='不执行该用例')
    # @pytest.mark.parametrize('target', [''])
    # def test_upload_sts(self, target):
    #     res = self.ttp.upload_sts(target)

    # @allure.story('文件上传回调 41')
    # # @pytest.mark.skip(reason='不执行该用例')
    # @pytest.mark.parametrize('filename, size, height, width', [('../data/file/1.jpg', '100', '200', '400')])
    # def test_upload_callback(self, filename, size, height, width):
    #     res = self.ttp.upload_callback(filename, size, height, width)
    #
    # @allure.story('获取升级信息 42')
    # @pytest.mark.skip(reason='不执行该用例')
    # def test_upgrate(self):
    #     res = self.ttp.upgrate()
