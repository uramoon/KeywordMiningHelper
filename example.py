import url_handler as uh
import text_handler as th
import word_cloud_generator as wcg

# url 목록이 있는 텍스트 파일로 부터 url가져옴
url_list = th.get_string_from_text(file_name="url_list.txt")
th.remove_blank_from_str_list(url_list)

# url 목록의 url로 부터 텍스트를 가져옴
text_list = uh.text_extract_from_res_obj_list(uh.get_urls_in_request(url_list))

# keywordminer객체 생성
miner = th.KeywordMiner()

# url로부터 가져온 텍스트 목록에서 키워드 추출(최대 단어 길이 = 20, 최소 빈도수 = 0)
miner.word_extraction_from_str_list(text_list, min_cnt=0, max_word_len=20)

# 추출한 키워드로 워드클라우드 생성(mask_image_path: 사용할 이미지 파일, coloring_opt: 사진의 색깔에 맞게 단어 색을 입히는 옵션)
wcgen = wcg.WordcloudGenerator(word_dict=miner.keyword_dict, mask_image_path='images4.png', coloring_opt=True)
wcgen.create_wordcloud()
