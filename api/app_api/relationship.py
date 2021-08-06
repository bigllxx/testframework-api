from api.base_api import BaseApi


class Relationship(BaseApi):
    """
    关系类接口
    """
    data = BaseApi.yaml_load('/data/api_data/relationship.api.yaml')

    def get_follows(self, author_id):
        """
        获取关注列表
        """
        self.params = {'author_id': author_id}
        res = self.api_send(self.data['get_follows'])
        return res

    def get_fans(self, author_id):
        """
        获取粉丝列表
        """
        self.params = {'author_id': author_id}
        res = self.api_send(self.data['get_fans'])
        return res

    def follow(self, author_id):
        """
        关注用户
        """
        self.params = {'author_id': author_id}
        res = self.api_send(self.data['follow'])
        return res

    def unfollow(self, author_id):
        """
        取关用户
        """
        self.params = {'author_id': author_id}
        res = self.api_send(self.data['unfollow'])
        return res
