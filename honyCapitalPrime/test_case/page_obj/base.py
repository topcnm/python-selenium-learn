# coding:utf-8


class Page(object):
    """
    基本类：以后的所有页面都继承自改页面；
            1 该页面不涉及任何单元测试
            2 该页面对webDriver 方法做简易封装，更加语义化
    """

    hony_url = "xxxxx"

    def __init__(self, selenium_driver, base_url=hony_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 15
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not load on {}'.format(url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url.find(self.base_url + self.url) > -1

    def script(self, src):
        return self.driver.execute_script(src)

    def on_title(self):
        return self.driver.title

    def on_url(self):
        return self.driver.current_url

