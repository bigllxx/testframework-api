from api.base_api import BaseApi


class Topic(BaseApi):
    """
    话题接口集
    """
    data = BaseApi.yaml_load('/data/api_data/topic.api.yaml')

    def topic_homepage(self):
        """
        话题首页
        """
        res = self.api_send(self.data['topic_homepage'])
        return res

    def topic_all(self):
        """
        所有话题
        """
        res = self.api_send(self.data['topic_all'])
        return res

    def topic_details(self, topic_id):
        """
        话题下看法
        """
        self.params = {'topic_id': topic_id}
        res = self.api_send(self.data['topic_details'])
        return res

    def topic_follow(self, topic_id):
        """
        关注话题
        """
        self.params = {'topic_id': topic_id}
        res = self.api_send(self.data['topic_follow'])
        return res

    def topic_unfollow(self, topic_id):
        """
        取关话题
        """
        self.params = {'topic_id': topic_id}
        res = self.api_send(self.data['topic_unfollow'])
        return res

    def topic_content(self, topic_id, checklists_id):
        """
        创建讨论
        """
        self.params = {'topic_id': topic_id, 'checklists_id': checklists_id}
        res = self.api_send(self.data['topic_content'])
        return res

    def author_me_topic(self):
        """
        关注话题列表
        """
        res = self.api_send(self.data['author_me_topic'])
        return res

    # todo: 作者话题关注列表、他人关注话题列表、他人发布话题列表


if __name__ == '__main__':
    t = Topic()
    # a = t.topic_all().json()['data']['allTopics'][0]['id']
    # t.topic_details('3TysBvFFTOXLeetFfLdVAL0oDqutOP6MnlRUrrHCfPHgF4Hnz')
    # t.topic_homepage()
    # t.topic_content(a, '1EeDHueKcdMUWH1o1YRC6bu3AM8Mdxd3d58sFgqQgwgPps4Xq')
    t.author_me_topic()