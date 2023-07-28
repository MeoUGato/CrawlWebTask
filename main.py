from handle_journal import *
   
journal_lt = []
seed_url = "https://jiem.ftu.edu.vn/index.php/jiem/issue/archive/"
while True:
    page = urllib.request.urlopen(seed_url)
    soup = BeautifulSoup(page, 'html.parser')
    list_of_link = soup.find_all(class_="cover")
    for link in list_of_link:
        journal_new = get_journal(link.get("href"))
        if journal_new != None:
            journal_lt += journal_new
    new_page = soup.find("a",class_="next")
    if new_page == None:
        break
    else:
        seed_url = new_page.get("href")

current_id = 1
with open("info.txt","w") as file:
    file.write("id;journal_id;paper_name;author_name;published_date\n")
    for jo in journal_lt:
        file.write(f"{current_id};{jo.journal_id};{jo.paper_name};")
        for id in range(0,len(jo.author_name)):
            if id == len(jo.author_name) - 1:
                file.write(f"{jo.author_name[id]};")
            else:
                file.write(f"{jo.author_name[id]},")
        file.write(f"{jo.published_date}\n")
        current_id += 1

