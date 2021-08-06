import sys
import allure
from api.app_api.ttp import Ttp
from common.logs import Logger
import pytest
from api.app_api.comment import Comment


@allure.feature('评论相关接口')
class TestComment:

    @classmethod
    def setup_class(cls):
        cls.log = Logger('comment')
        cls.comment = Comment()
        cls.t = Ttp()
        cls.comment.log = Logger('TestComment')
        cls.data = cls.comment.yaml_load('/data/case_data/comment.data.yaml')
        try:
            cls.snack_id = cls.t.contents_snack('新建单品标题', '新建单品内容', '[]', '[]', '[]').json()['contentId']  # 新建单品
            cls.post_id = cls.t.creat_contents('normal', '新建文章标题', '内容1', '内容2', '[]').json()['contentId']  # 新建文章
            cls.content_ids = [cls.snack_id, cls.post_id]
        except:
            cls.comment.log.logger.error('新建内容/获取snack_id、post_id、content_ids失败')
            sys.exit()

    @classmethod
    def teardown_class(cls):
        cls.t.del_contents(cls.snack_id)  # 删除单品
        cls.t.del_contents(cls.post_id)  # 删除文章

    @allure.story('获取内容下所有评论')
    def test_get_comments(self):
        for i in self.content_ids:
            res = self.comment.get_comments(i)
            self.comment.my_assert(res, 'assert res.status_code == 200')

    @allure.story('创建评论')
    @pytest.mark.parametrize('content', ['', '这是一个正常评论', '额外这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论这是一个300字评论'])
    def test_creat_comments(self, content):
        res = self.comment.creat_comments(self.snack_id, content)
        a = """
if args[0] == '':
    assert res.status_code == 400
else:
    assert res.status_code == 200
"""
        self.comment.my_assert(res, a, content)

    @allure.story('创建追评')
    @pytest.mark.parametrize('content', ['正常追评'])
    def test_creat_comments_too(self, content):
        comment_id = self.comment.creat_comments(self.post_id, '正常评论').json()['data']['id']
        res = self.comment.creat_comments_too(self.post_id, comment_id, content)
        self.comment.my_assert(res, 'assert res.status_code == 200')

    @allure.story('查看禁言状态')
    def test_ban_state(self):
        res = self.comment.ban_state()
        self.comment.my_assert(res, 'assert "expireTime" in res.json()')

    @allure.story('举报评论')
    def test_report_comment(self):
        comment_id = self.comment.creat_comments(self.post_id, '正常评论').json()['data']['id']
        res = self.comment.report_comment(comment_id)
        self.comment.my_assert(res, 'assert res.status_code == 200')

    @allure.story('收藏评论')
    def test_liked_comment(self):
        comment_id = self.comment.creat_comments(self.post_id, '正常评论').json()['data']['id']
        res = self.comment.liked_comment(comment_id)
        self.comment.my_assert(res, 'assert res.json()["likedCount"] == 1')

    @allure.story('取消收藏')
    def test_delete_liked(self):
        comment_id = self.comment.creat_comments(self.post_id, '正常评论').json()['data']['id']
        self.comment.liked_comment(comment_id)
        res = self.comment.delete_liked(comment_id)
        self.comment.my_assert(res, 'assert res.json()["likedCount"] == 0')

    @allure.story('删除评论')
    def test_delete_comments(self):
        comment_id = self.comment.creat_comments(self.post_id, '正常评论').json()['data']['id']
        res = self.comment.delete_comments(comment_id)
        self.comment.my_assert(res, 'assert res.status_code == 200')
