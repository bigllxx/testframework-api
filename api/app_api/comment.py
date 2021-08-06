from api.base_api import BaseApi


class Comment(BaseApi):
    """
    评论接口集
    """
    data = BaseApi.yaml_load('/data/api_data/comment.api.yaml')

    def get_comments(self, contentsId):
        """
        获取文章评论  3
        :param contentsId:
        :return:
        """
        self.params = {'contentsId': contentsId}
        res = self.api_send(self.data['get_comments'])
        return res

    def creat_comments(self, contentsId, content):
        """
        创建普通评论  1
        :param content: 评论内容
        :return:
        """
        self.params = {'contentsId': contentsId, 'content': content}
        res = self.api_send(self.data['creat_comments'])
        return res

    def creat_comments_too(self, contentsId, parentId, content):
        """
        创建追评  2
        :param parentId: 追评id
        :param content: 评论内容
        :return:
        """
        self.params = {'contentsId': contentsId, 'parentId': parentId, 'content': content}
        res = self.api_send(self.data['creat_comments_too'])
        return res

    def ban_state(self):
        """
        查看禁言状态  4
        :return:
        """
        res = self.api_send(self.data['ban_state'])
        return res

    def report_comment(self, commentId):
        """
        举报评论  5
        :param contentsId:
        :return:
        """
        self.params = {'commentId': commentId}
        res = self.api_send(self.data['report_comment'])
        return res

    def liked_comment(self, commentId):
        """
        点赞评论  6
        :param contentsId:
        :return:
        """
        self.params = {'commentId': commentId}
        res = self.api_send(self.data['liked_comment'])
        return res

    def delete_liked(self, commentId):
        """
        取消点赞  7
        :param contentsId:
        :return:
        """
        self.params = {'commentId': commentId}
        res = self.api_send(self.data['delete_liked'])
        return res

    def delete_comments(self, commentId):
        """
        删除评论  8
        :param contentsId:
        :return:
        """
        self.params = {'commentId': commentId}
        res = self.api_send(self.data['delete_comments'])
        return res


if __name__ == '__main__':
    c = Comment()
    # c.get_comments('2799wOitnl2JIsQTay5ceH0CTzJSIBELA6maQt11pMbrVl5kw')
    # c.liked_comment('ATyrXBmfOBtzKZZDWg4LJ3RklbPORmu9x74j15n4u9qOJ6RQ')
    c.delete_liked('ATyrXBmfOBtzKZZDWg4LJ3RklbPORmu9x74j15n4u9qOJ6RQ')

