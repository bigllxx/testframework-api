from api.base_api import BaseApi


class HomePage(BaseApi):
    """
    广告位接口集
    """
    data = BaseApi.yaml_load('/data/api_data/homepage.api.yaml')

    def homepage(self):
        """
        首页接口合辑
        :return:
        """
        res = self.api_send(self.data['homepage'])
        return res

    def homepage_weekly_hottest(self):
        """
        当前最热
        :return:
        """
        res = self.api_send(self.data['homepage_weekly_hottest'])
        return res

    def recommend_grid_cell(self):
        """
        推荐页瓦片区
        """
        res = self.api_send(self.data['recommend_grid_cell'])
        return res

    def recommend_nav_bar(self):
        """
        推荐页瓦片区
        """
        res = self.api_send(self.data['recommend_nav_bar'])
        return res


if __name__ == '__main__':
    h = HomePage()
    h.homepage_weekly_hottest()
