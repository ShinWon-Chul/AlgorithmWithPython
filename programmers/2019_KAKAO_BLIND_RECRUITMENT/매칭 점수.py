import re
from collections import defaultdict

def solution(word, pages):
    word = word.lower()
    page_dict = defaultdict(dict)
    max_escore = 0
    result = []
    
    body_patern = re.compile("<body>[\S\s]*</body>")
    href_patern = re.compile("<a href=[\S]*>")
    
    for idx, page in enumerate(pages):
        c = re.search(r'<meta property=\"og:url\" content=\"https://([\S]*)\"/>', page).group(1)
        b = body_patern.search(page)
        h = href_patern.findall(page)
        num_link = len(h)
        body_list = list(map(lambda x : x.lower(), re.split('[^a-zA-Z]', b[0])))
        link_list = list(map(lambda x : re.split('\"', x)[1][8:], h))
        default_score = body_list.count(word)
        if len(h) == 0:
            i_score = 0
        else: 
            i_score = default_score/num_link
        page_dict[c] = {"idx": idx, "href": link_list, "num_link": num_link, 
                        "default_score": default_score, "i_score" : i_score}
    
    for current_page, current_page_info in page_dict.items():
        target_page = current_page
        e_score = 0
        for k, v in page_dict.items():
            if target_page in v['href']:
                e_score += v['i_score']
        e_score += current_page_info["default_score"]
        page_dict[current_page]['e_score'] = e_score
        max_escore = max(max_escore, e_score)
    
    for current_page, current_page_info in page_dict.items():
        if current_page_info['e_score'] == max_escore:
            result.append(current_page_info['idx'])
    answer = min(result)    
    return answer