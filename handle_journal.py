from bs4 import BeautifulSoup
import urllib.request
import re
class journal:
    def __init__(self,paper_name,author_name,published_date,journal_id):
        self.paper_name = paper_name
        self.author_name = author_name
        self.published_date = published_date
        self.journal_id = journal_id     
    def write_out(self): 
        print(self.author_name)
        print(self.paper_name)
        print(self.journal_id)
        print(self.published_date)
    
def get_info(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    #get author name
    author_name = []
    meta_tag = soup.find_all("meta",attrs={"name":"citation_author"}) #first find all meta tag with attribute "name" = "citation_author"
    for meta in meta_tag:
        author_name.append(meta.get("content")) #traverse all meta tag and get the author name which cover in "content" attribute

    #get paper name
    head_title = soup.find("title")
    combine_name = head_title.text
    end_index = combine_name.find("|") #Remove "| Journal of International Economics and Management" cause it's the same for every journal
    paper_name = combine_name[:end_index].strip() #remove the leading space and ending space of a string with str.strip()
    # refer to: https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string

    #get published date
    published_date_class = soup.find(class_="list-group-item date-published").text
    start_index = published_date_class.find(":") + 1
    published_date = published_date_class[start_index:].strip()

    #get journal_id
    journal_id = soup.find(class_="panel-body").text.strip()
    

    #adding
    new_journal = journal(paper_name,author_name,published_date,journal_id)
    new_journal.write_out()
    return journal(paper_name,author_name,published_date,journal_id)


def get_journal(url):
    journal_list = []
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    lead_to_another_page = soup.find_all(class_ = "media-body")
    for ltap in lead_to_another_page:
        sub_url = ltap.find(href=re.compile("https://jiem.ftu.edu.vn/index.php/jiem/article/view/")).get("href")
        journal_list.append(get_info(sub_url))
    return journal_list
    