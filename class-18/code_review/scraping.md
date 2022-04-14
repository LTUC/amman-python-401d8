# Wikipedia Scraper

```python
import requests
from bs4 import BeautifulSoup

class WebScraper:

    def __init__(self, url= None):
        self.url = url
        self.anchors_list = []
    
    def get_citation_needed_count(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, "html.parser")
        paragraphs_div = soup.find('div', id ="mw-content-text")
        paragraphs_list = paragraphs_div.find_all("p")
        """
            - Loop thorugh paragraph_list
            - check for if citation needed is there:
                - get all <a> tags inside each <p>:
                    - check if <a> has title attribute with value of "Wikipedia:Citation needed":
                        - anchor.attrs["title"] == "Wikipedia:Citation needed" 
                        - anchors = p.find_all("a", title = "Wikipedia:Citation needed")
            
            - we will get a list of anchor tags (citation needed) 
            - assign self.ancahors_list = anchors
            - then use len(anchors) and return it as the count
        """
    
    def get_citations_needed_report(self):
        if len(self.anchors_list) == :
            self.get_citation_needed_count()
            
        anchors = self.anchors_list
        passages = ""
        passges_list = []
        for anchor in anchors:
            passage = anchor.find_parent("p")
            passages+= passage.get_text() + "\n"

```