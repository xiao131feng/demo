from selenium import webdriver

class Pyselenium():
    def __init__(self,browser="chrome"):
        if browser == "chrome":
            driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
        elif browser == "IE":
            driver = webdriver.Ie(executable_path="./drivers/IEDriverServer.exe")
        elif browser == "Firefox":
            driver = webdriver.Firefox(executable_path="./drivers/geckodriver.exe")
        elif browser == "Opera":
            driver = webdriver.Opera(executable_path="./drivers/operadriver.exe")
        elif browser == "PhantomJS":
            driver = webdriver.PhantomJS(executable_path="./drivers/phantomjs.exe")
        elif browser == "Edge":
            driver = webdriver.Edge(executable_path="./drivers/MicrosoftWebDriver.exe")
        else:
            print("警告：傻逼！您选择的浏览器不存在！请检查后再选择！")
            raise
        self.dr = driver
        # return self.driver
    
    def quit(self):
        "退出浏览器！"
        self.dr.quit()
    
    def open(self,url):
        "打开网址"
        self.dr.get(url)

    def get_element(self,element):
        '''
        说明：获取元素的方法
        用法：find_element('id-->kw')
        '''
        elementl = element.split("-->")
        by = elementl[0].strip()
        value = elementl[1].strip()
        if by == "id":
            element = self.dr.find_element_by_id(value)
        elif by == "name":
            element = self.dr.find_element_by_name(value)
        elif by == "class_name":
            element = self.dr.find_element_by_class_name(value)
        elif by == "css_selector":
            element = self.dr.find_element_by_css_selector(value)
        elif by == "link_text":
            element = self.dr.find_element_by_link_text(value)
        elif by == "partial_link_text":
            element = self.dr.find_element_by_partial_link_text(value)
        elif by == "tag_name":
            element = self.dr.find_element_by_tag_name(value)
        elif by == "xpath":
            element = self.dr.find_elements_by_xpath(value)
        else:
            print("傻逼！请输入正确的获取元素的方式！")
            raise
        return element
    
    def send_keys(self,element,value):
        '''
        说明：在文本框输入内容
        用法:send_keys("id-->kw","浪晋的测试小讲堂")
        '''
        el = self.get_element(element)
        el.send_keys(value)

    def click(self,element):
        '''
        说明：实现点击功能
        用法:click("id-->kw")
        '''
        el = self.get_element(element)
        el.click()

    def send_and_click(self,element,value,element1):
        '''
        说明：在文本框输入内容并点击
        用法:send_keys("id-->kw","浪晋的测试小讲堂")
        '''
        el = self.get_element(element)
        el.send_keys(value)
        self.click(element1)

    def get_title(self):
        '''
        说明：获取网页title
        用法:get_title()
        '''
        return self.dr.title