import re
import requests
import zipfile
from bs4 import BeautifulSoup


'''
  Defined 3 modules
  --> 1. to downlaod the zip file content to the local container/machine
  --> 2. Extract zip file to the normal repository
  --> 3. Extract the data using bs4 library and preprocess according to 
          our required meta fields and filtered with removing spaces
          a) Date
          b) title
          c) patent id
          d) full text(text-content): headings as key and content as value
'''
## dowload the zipfile content
def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

## extract zip file
def extract_zip(save_path,extract_path):
  with zipfile.ZipFile(save_path, 'r') as zip_ref:
           zip_ref.extractall(extract_path)

##preprocessing the data of the xml file
def get_predata(file_name):
    result = {}
    infile = open(file_name, "r")
    contents = infile.read()
    soup = BeautifulSoup(contents, 'xml')
    result["title"] = soup.find('invention-title').text
    result["patent_id"] = soup.find('publication-reference').find('doc-number').text
    result["date"] = soup.find('publication-reference').find('date').text
    abs_str = soup.find('abstract').find("p").text
    result["abstract"] = ".".join([p.replace("\n","").lstrip() for p in abs_str.split(".")])
    textsdes = soup.find('description').text
    headings = soup.find_all('heading')
    list_headings = [i.text for i in headings]
    total_texts = {}
    for x1 in range(len(list_headings)):
        try:
            xc = re.search(list_headings[x1], textsdes)
            xe = re.search(list_headings[x1 + 1], textsdes)
            str_text = textsdes[xc.span()[1]:xe.span()[0]]
            if '--' not in str_text:
                total_texts[list_headings[x1]] = ".".join(p.replace("\n", "").strip() for p in str_text.split("."))
        except IndexError:
            str_text = textsdes[xc.span()[1]:]
            total_texts[list_headings[x1]] = ".".join(p.replace("\n", "").strip() for p in str_text.split("."))
    result["text-content"] = total_texts
    return result

