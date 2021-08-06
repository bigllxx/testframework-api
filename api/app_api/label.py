from api.base_api import BaseApi


class Label(BaseApi):
    """
    标签接口集
    """
    data = BaseApi.yaml_load('/data/api_data/label.api.yaml')

    def labels_search(self, text):
        """
        根据标签名称查询
        :param text:
        :return:
        """
        self.params = {'text': text}
        res = self.api_send(self.data['labels_search'])
        return res

    def label_groups(self):
        """
        获取所有标签组
        :return:
        """
        res = self.api_send(self.data['label_groups'])
        return res

    def labels_id(self, labels_id):
        """
        根据ID查询标签
        :param labels_id:
        :return:
        """
        self.params = {'labels_id': labels_id}
        res = self.api_send(self.data['labels_id'])
        return res

    def labels_id_contents(self, labels_id):
        """
        获取标签下所有内容
        :param labels_id:
        :return:
        """
        self.params = {'labels_id': labels_id}
        res = self.api_send(self.data['labels_id_contents'])
        return res

    def label(self):
        """
        获取标签列表
        """
        res = self.api_send(self.data['label'])
        return res

    def label_contents(self, group_id, label_id):
        """
        标签页详情
        """
        self.params = {'labelGroupId': group_id, 'labelId': label_id}
        res = self.api_send(self.data['label_contents'])
        return res


if __name__ == '__main__':
    l = Label()
    # l.label()
    # l.label_groups() 2oouQsNcdWb0j0iG5YevEtpFKxbULDY8gCsMlvpqFCHXsKZdV
    # l.contents('yqqwfuge4zF5hXbW2x3GViABpmSVsCPSv9h5cNZkF2aZpXbW', '')
    l.label_contents('', '2oouQsNcdWb0j0iG5YevEtpFKxbULDY8gCsMlvpqFCHXsKZdV')
