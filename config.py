# -*- coding:utf-8 -*-


data_directory = "screenshots"

default_answer_number = 2

### 1代表灰度处理， 2代表二值化处理，如果需要使用二值化，需要将2放到前面, 0不使用
image_compress_level = (0, 1, 2)

### ocr config
hanwan_appcode = "714501eede0b4ac9a75a11af64b3b4d7"

### baidu orc
### baidu orc
app_id = "10671075"
app_key = "tDyIAYQ60RcTr2CkeFE2WUAB"
app_secret = " TxxaGWqIKQpo58G5Y9zGNeVq6hAiCU5f"


### 0 表示普通识别，配合compress_level 1使用
### 1 标识精确识别，精确识别建议配合image_compress_level 2使用
api_version = (0, 1)

### 如果你想要使用汉王的话，将汉王移动到前面，默认使用百度，每天封顶500次
prefer = ("baidu", "hanwang")

text_summary = True
summary_sentence_count = 3

### dataSet save
txt_data_fname = "./TestSet.txt"