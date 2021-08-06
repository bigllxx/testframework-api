import os
import sys
import allure
import pytest
from api.app_api.topic import Topic
from common.logs import Logger
from api.app_api.checklist import CheckList


@allure.feature('话题相关接口')
class TestLabel:
    # data = BaseApi.yaml_load('/data/case_data/label.data.yaml')

    @classmethod
    def setup_class(cls):
        cls.t = Topic()
        cls.t.log = Logger('topic')
        try:
            cls.topic_id = cls.t.topic_all().json()['data']['allTopics'][0]['id']
        except:
            cls.t.log.logger.warn('获取topic_id失败')
            sys.exit()

    @allure.story('话题首页')
    def test_topic_homepage(self):
        res = self.t.topic_homepage()
        self.t.my_assert(res, "assert res.json()['code'] == 0")

    @allure.story('获取所有话题/话题组')
    def test_topic_all(self):
        res = self.t.topic_all()
        self.t.my_assert(res, "assert res.json()['code'] == 0")

    @allure.story('获取话题下看法')
    def test_topic_details(self):
        res = self.t.topic_details(self.topic_id)
        self.t.my_assert(res, "assert res.json()['code'] == 0")

    @allure.story('关注话题')
    def test_topic_follow(self):
        res = self.t.topic_follow(self.topic_id)
        self.t.my_assert(res, "assert res.json()['code'] == 0")

    @allure.story('取关话题')
    def test_topic_unfollow(self):
        res = self.t.topic_unfollow(self.topic_id)
        self.t.my_assert(res, "assert res.json()['code'] == 0")

    @allure.story('新建讨论')
    def test_topic_content(self):
        checklist_id = CheckList().author_me_checklists().json()['list'][0]['id']
        res = self.t.topic_content(self.topic_id, checklist_id)
        self.t.my_assert(res, "assert res.json()['code'] == 0")

    @allure.story('关注话题列表')
    def test_author_me_topic(self):
        res = self.t.author_me_topic()
        self.t.my_assert(res, "assert res.json()['code'] == 0")