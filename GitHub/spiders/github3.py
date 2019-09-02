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
    name = 'github3'
    allowed_domains = ['github.com']

    # 1、登陆页，获取登陆的url与参数
    start_urls = ['https://github.com/login']

    # 2、发送登陆请求:POST
    def parse(self, response):
        # 登陆参数
        form_data = {
            'login': 'joldemox@163.com',
            'password': 'xiongfeng351015',
        }

        # 发送POST请求
        yield scrapy.FormRequest.from_response(
            response,
            formxpath='//*[@id="login"]/form',
            formdata=form_data,
            callback=self.parse_item
        )

    # 3、目标url
    # 因为会重定向url，所以不用再标明需要请求的地址了

    # 解析方法
    def parse_item(self, response):
        with open('git3.html', 'wb')as f:
            f.write(response.body)
