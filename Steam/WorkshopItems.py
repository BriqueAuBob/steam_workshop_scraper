from math import ceil
from scrapy import Selector
from Core.Request import Request
import w3lib.html

class WorkshopItems:
    def __init__(self, username):
        self.username = username
        self.response = Request.make(username + '/myworkshopfiles/?p=1&numperpage=30')
        self.selector = Selector(text=self.response)
        self.pages = [self.response]

    def getWorkshopItemsCount(self):
        text = self.selector.css('div.workshopBrowsePagingInfo::text').extract_first()
        for s in text.split():
            if s.isdigit():
                return int(s)

    def getPageCount(self):
        return ceil(self.getWorkshopItemsCount() / 30)

    def getPages(self):
        pageCount = self.getPageCount()
        if pageCount > 1:
            for i in range(2, pageCount + 1):
                self.pages.append(Request.make(self.username + "/myworkshopfiles/?p=" + str(i) + "&numperpage=30"))
        return self.pages

    def getWorkshopItems(self):
        pages = self.getPages()
        items = []
        for page in pages:
            selector = Selector(text=page)
            for workshopItems in selector.css('div.workshopItem'):
                thumbnail = workshopItems.css('img.workshopItemPreviewImage::attr(src)').extract_first()
                name = workshopItems.css("div.workshopItemTitle::text").extract_first()
                app = workshopItems.css("div.workshopItemApp::text").extract_first()
                items.append({ thumbnail, name, app })
        return items
