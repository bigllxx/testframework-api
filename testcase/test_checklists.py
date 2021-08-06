import sys

import allure
from api.app_api.ttp import Ttp
import pytest
from api.app_api.checklist import CheckList
from api.base_api import BaseApi
from common.logs import Logger


@allure.feature('清单相关接口')
class TestChecklists:
    data = BaseApi.yaml_load('/data/case_data/checklist.data.yaml')

    @classmethod
    def setup_class(cls):
        cls.c = CheckList()
        cls.t = Ttp()
        cls.c.log = Logger('checklist')
        try:
            cls.content_id = cls.t.contents_snack('新建单品标题', '新建单品内容', '[]', '[]', '[]').json()['contentId']  # 新建单品
            cls.checklist_id = cls.c.checklists('新建清单标题', 'true').json()['checklistId']  # 新建清单
        except:
            cls.c.log.logger.error('新建清单/单品失败')
            sys.exit()

    @classmethod
    def teardown_class(cls):
        cls.c.delete_checklists(cls.checklist_id)  # 删除清单
        cls.t.del_contents(cls.content_id)  # 删除单品

    @allure.story('获取当前用户清单 16')
    def test_author_me_checklists(self):
        res = self.c.author_me_checklists()
        self.c.my_assert(res, 'assert res.status_code == 200')

    @allure.story('新建清单 1')
    @pytest.mark.parametrize('title, is_private', data['test_checklists'])
    def test_checklists(self, title, is_private):
        res = self.c.checklists(title, is_private)
        self.c.my_assert(res, 'assert res.status_code != 200')

    @allure.story('更新清单 4')
    @pytest.mark.parametrize('title, is_private', data['test_patch_checklists'])
    def test_patch_checklists(self, title, is_private):
        res = self.c.patch_checklists(self.checklist_id, title, is_private)
        a = """
if args[0] != '':
    assert res.json()['code'] == 51101
else:
    assert res.json()['errCode'] == 10000
            """
        self.c.my_assert(res, a, title)

    @allure.story('获取清单信息 3')
    def test_get_checklists(self):
        res = self.c.get_checklists(self.checklist_id)
        self.c.my_assert(res, 'assert res.json()["id"]')

    @allure.story('点赞清单  6')
    def test_checklists_liked(self):
        res = self.c.checklists_liked(self.checklist_id)
        self.c.my_assert(res, 'assert res.json()["iLiked"] is True')

    @allure.story('取消点赞  7')
    def test_delete_checklists_liked(self):
        self.c.checklists_liked(self.checklist_id)
        res = self.c.delete_checklists_liked(self.checklist_id)
        self.c.my_assert(res, 'assert res.json()["iLiked"] is False')

    @allure.story('收藏清单  8')
    def test_checklists_favored(self):
        res = self.c.checklists_favored(self.checklist_id)
        self.c.my_assert(res, 'assert res.json()["iFavored"] is True')

    @allure.story('取消收藏  9')
    def test_delete_checklists_favored(self):
        self.c.checklists_favored(self.checklist_id)
        res = self.c.delete_checklists_favored(self.checklist_id)
        self.c.my_assert(res, 'assert res.json()["iFavored"] is False')

    @allure.story('获取单品能够被加入的清单列表 17')
    def test_author_me_checklists_add(self):
        res = self.c.author_me_checklists_add(self.content_id)
        self.c.my_assert(res, 'assert res.status_code == 200')

    @allure.story('单品添加到清单  15')
    def test_add_contents_checklists(self):
        res = self.c.add_contents_checklists(self.content_id, self.checklist_id)
        self.c.my_assert(res, 'assert res.status_code == 200')

    @allure.story('获取清单下内容  12')
    def test_checklists_contents(self):
        res = self.c.checklists_contents(self.checklist_id)
        self.c.my_assert(res, 'assert res.json()["code"] == 0')

    @allure.story('获取单品对应清单列表  14')
    def test_get_contents_checklists(self):
        self.c.add_contents_checklists(self.content_id, self.checklist_id)
        res = self.c.get_contents_checklists(self.content_id)
        self.c.my_assert(res, 'assert "list" in res.json()')

    @allure.story('移除清单下单品  13')
    def test_remove_checklists_contents(self):
        self.c.add_contents_checklists(self.content_id, self.checklist_id)
        res = self.c.remove_checklists_contents(self.checklist_id, self.content_id)
        self.c.my_assert(res, 'assert res.status_code == 200')

    @allure.story('删除清单  5')
    def test_delete_checklists(self):
        res = self.c.delete_checklists(self.checklist_id)
        self.c.my_assert(res, 'assert res.status_code == 204')

    @allure.story('清单首页列表 2')
    def test_checklists_feeds(self):
        res = self.c.checklists_feeds()
        self.c.my_assert(res, 'assert "list" in res.json()')

    @allure.story('标记观看  10')
    def test_checklists_mark(self):
        res = self.c.checklists_mark(self.checklist_id)
        self.c.my_assert(res, 'assert res.status_code == 200')

    @allure.story('标记分享  11')
    def test_checklists_share(self):
        res = self.c.checklists_share(self.checklist_id)
        self.c.my_assert(res, 'assert res.status_code == 200 or 500')

    @allure.story('获取指定用户的清单列表  18')
    def test_author_checklists(self):
        author_id = self.t.author_me().json()['id']
        res = self.c.author_checklists(author_id)
        self.c.my_assert(res, 'assert len(res.json()["list"]) >= 0')

    @allure.story('空清单添加内容  18')
    def test_batch_content_checklists(self):
        checklist_ids = [self.checklist_id]
        content_ids = [self.content_id]
        res = self.c.batch_content_checklists(str(content_ids), str(checklist_ids))
        self.c.my_assert(res, 'assert res.status_code == 200')

    # @allure.story('搜索清单列表 19')
    # @pytest.mark.skip(reason='废弃接口？')
    # @pytest.mark.parametrize('keyword', data['test_search_checklists'])
    # def test_search_checklists(self, keyword):
    #     res = self.c.search_checklists(keyword)
    #
    # @allure.story('搜索关键字补全 20')
    # @pytest.mark.skip(reason='废弃接口？')
    # @pytest.mark.parametrize('keyword', data['test_search_checklists'])
    # def test_search_checklists_hints(self, keyword):
    #     res = self.c.search_checklists_hints(keyword)

