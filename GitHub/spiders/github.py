# -*- coding: utf-8 -*-
import scrapy


# requests
# 1.headers = {'Cookie:""'}
# 2.cookies = {}
# 3.代码登陆requests.session()

# scrapy
# 1.cookies = {}，直接在requests中的meta设置，不支持headers中放cookies
# 2.代码登陆，scrapy会自动保存cookies
# 3.from_response()自动解析form表单的参数和url


'''在spider的requests请求中添加cookies'''


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']

    # 目标url
    start_urls = ['https://github.com/']
    cookies_str = '_octo=GH1.1.2031420524.1559312140; _ga=GA1.2.2097468133.1563610078; tz=Asia%2FShanghai; has_recent_activity=1; _device_id=0be3dcaa1d6480dcb6888b910dcb5a2f; user_session=tXWoFx5p7avTInWen5CHrIVIEXuJkI-GyglwY5QA49mYvTos; __Host-user_session_same_site=tXWoFx5p7avTInWen5CHrIVIEXuJkI-GyglwY5QA49mYvTos; logged_in=yes; dotcom_user=Joldemox; _gat=1; _gh_sess=SU5GdCtxckNlYjM5QkVET2IyRDJvYUhoQUJqYUNTSlE3VzZ0cHZGWXFwSG5GOGhITDdPQzJYRGgrWVZSOWZaeGx0Zks4TmphaDJYd0w3VzhGeUF1NnJ2VWd6VFZQNFUrMjY5THRzT1Jsc3h5c2F6eENYS2p6MzBhRnBUcUZnRHgxSktGdnFFOVFGSDZOZkZOVEtoQWp3dkZqT2c1VDBmQWc1MWxBb1VXbEVBRzB6eFJiaVh3ZjJjZ2wvNUxWajJDSjBUaE5hcUtyRkI5b0V4bFl4WDdZaGpSNWR4VkRmMVpXeUFoWkNzMzVmbFVNbjg2Q1B1bi8rdnRLTm0vYzBFVU4zUk9CeE9sL1dTa3BKazFNcVdpaFE9PS0tdk0zcFFBd0IrN00vblhseG9pT2VJQT09--f61249c579a0487cdf18ccda61a91cf395a8576e'
    cookies_dict = {i.split('=')[0]: i.split('=')[1] for i in cookies_str.split('; ')}

    # 因为父类中没有传入cookies的方法，所以需要重写父类方法start_requests，添加cookies
    def start_requests(self):
        # 遍历url列表
        for url in self.start_urls:
            # 构建请求传递给引擎
            yield scrapy.Request(url, cookies=self.cookies_dict, callback=self.parse)

    # 解析方法
    def parse(self, response):
        with open('git1.html', 'wb')as f:
            f.write(response.body)
