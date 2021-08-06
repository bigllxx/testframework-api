from api.base_api import BaseApi


class Search(BaseApi):
    """
    search 接口集
    """
    data = BaseApi.yaml_load('/data/api_data/search.api.yaml')

    def search_resource(self, keyword, **kwargs):
        """
        搜索内容
        """
        self.params = {'keyword': keyword, 'resource_type': kwargs['resource_type'],
                       'content_type': kwargs['content_type']}
        res = self.api_send(self.data['search_resource'])
        return res

    def search_suggest(self, keyword, **kwargs):
        """
        关键字匹配
        """
        self.params = {'keyword': keyword, 'resource_type': kwargs['resource_type'],
                       'content_type': kwargs['content_type']}
        res = self.api_send(self.data['search_suggest'])
        return res


if __name__ == '__main__':
    Search().search_resource('亲子', resource_type='content', content_type='')
    Search().search_suggest('亲子', resource_type='content', content_type='')
