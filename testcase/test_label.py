import allure
import pytest
from api.app_api.label import Label
from api.base_api import BaseApi
from common.logs import Logger


@allure.feature('标签相关接口')
class TestLabel:
    data = BaseApi.yaml_load('/data/case_data/label.data.yaml')

    @classmethod
    def setup_class(cls):
        cls.la = Label()
        cls.la.log = Logger('label')

    @allure.story('获取所有标签分组')
    def test_label_groups(self):
        res = self.la.label_groups()
        self.la.my_assert(res, "assert res.status_code == 200")

    @allure.story('根据内容（name）搜索标签')
    @pytest.mark.parametrize('text', data['test_labels_search'])
    def test_labels_search(self, text):
        res = self.la.labels_search(text)
        self.la.my_assert(res, "assert res.status_code == 200")

    @allure.story('根据id搜索标签')
    def test_labels_id(self):
        label_id = self.la.label_groups().json()[0]['labels'][0]['id']
        res = self.la.labels_id(label_id)
        self.la.my_assert(res, "assert res.json()['id'] == args[0]", label_id)

    @allure.story('根据id获取该标签下所有内容')
    def test_labels_id_contents(self):
        label_id = self.la.label_groups().json()[0]['labels'][0]['id']
        res = self.la.labels_id_contents(label_id)
        self.la.my_assert(res, "assert res.json()['total']")

    @allure.story('获取所有标签')
    def test_label(self):
        res = self.la.label()
        self.la.my_assert(res, 'assert res.json()["code"] == 0')

    @allure.story('获取标签页详情')
    @pytest.mark.parametrize('group_id', ['True', 'False'])
    def test_label_content(self, group_id):
        if group_id == 'True':
            group_id = self.la.label_groups().json()[0]['groupId']
            res = self.la.label_contents(group_id, '')
        else:
            label_id = self.la.label().json()['data']['common'][0]['id']
            res = self.la.label_contents('', label_id)
        self.la.my_assert(res, 'assert res.json()["code"] == 0')
