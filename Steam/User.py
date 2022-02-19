from scrapy import Selector
from Core.Request import Request
import w3lib.html

class User:
    def __init__(self, username):
        self.username = username
        self.response = Request.make(username)
        self.selector = Selector(text=self.response)

    def getUsername(self):
        return self.selector.css("span.actual_persona_name::text").extract_first()

    def getSummary(self):
        return w3lib.html.remove_tags(self.selector.css("div.profile_summary")[0].get()).lstrip()