import allure
from api.app_api.relationship import Relationship
from common.logs import Logger
from api.app_api.ttp import Ttp


@allure.feature('关系类接口')
class TestRelationship:
    rs = Relationship()
    ttp = Ttp()
    rs.log = Logger('Relationship')

    @classmethod
    def setup_class(cls):
        cls.author_id = cls.ttp.feeds('post', '9').json()['list'][0]['author']['id']

    @allure.story('获取关注列表')
    def test_get_follows(self):
        res = self.rs.get_follows(self.author_id)
        self.rs.my_assert(res, 'assert res.json()["errCode"] == 0')

    @allure.story('获取粉丝列表')
    def test_get_fans(self):
        res = self.rs.get_fans(self.author_id)
        self.rs.my_assert(res, 'assert res.json()["errCode"] == 0')

    @allure.story('关注用户')
    def test_follow(self):
        self.rs.unfollow(self.author_id)  # 取关
        follow_count = self.ttp.author_me().json()['follow_count']  # 获取自己的关注数
        follower_count = self.ttp.author_id(self.author_id).json()['follower_count']  # 获取他人的粉丝数
        res = self.rs.follow(self.author_id)  # 关注
        follow_count_too = self.ttp.author_me().json()['follow_count']  # 获取自己的关注数
        follower_count_too = self.ttp.author_id(self.author_id).json()['follower_count']  # 获取他人的粉丝数
        self.rs.my_assert(res,
                          'assert args[2] == args[0] + 1 and args[3] == args[1] + 1',
                          follow_count, follower_count, follow_count_too, follower_count_too)

    @allure.story('取关用户')
    def test_unfollow(self):
        res = self.rs.unfollow(self.author_id)
        self.rs.my_assert(res, 'assert res.json()["errCode"] == 0')
