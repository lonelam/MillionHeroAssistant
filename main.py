# -*- coding:utf-8 -*-


"""

    Xi Gua video Million Heroes

"""
import time
from argparse import ArgumentParser

import operator
from functools import partial
import os

from config import app_id
from config import app_key
from config import app_secret
from config import data_directory
from core.android import analyze_current_screen_text
from core.nearby import calculate_relation
from core.ocr.baiduocr import get_text_from_image as bai_get_text


def parse_args():
    parser = ArgumentParser(description="Million Hero Assistant")
    parser.add_argument(
        "-t", "--timeout",
        type=int,
        default=5,
        help="default http request timeout"
    )
    return parser.parse_args()


def parse_question_and_answer(text_list):
    question = ""
    start = 0
    for i, keyword in enumerate(text_list):
        question += keyword
        if "?" in keyword:
            start = i + 1
            break

    question = question.split(".")[-1]
    return question, text_list[start:]


def main():
    args = parse_args()
    timeout = args.timeout
    get_text_from_image = partial(
        bai_get_text,
        app_id=app_id,
        app_key=app_key,
        app_secret=app_secret,
        timeout=timeout)

    start = time.time()
    text_binary = analyze_current_screen_text(
        directory=data_directory
    )
    keywords = get_text_from_image(
        image_data=text_binary,
    )
    keywords
    if not keywords:
        print("text not recognize")
        return

    question, answers = parse_question_and_answer(keywords)
    #os.system("chromium-browser https://google.com/search?q=" + question)
    end = time.time()
    print("use {0} 秒".format(end - start))

    print("-" * 50)
    print("Q: ", question)
    print("-" * 50)
    print("\n".join(answers))
    print("-" * 50, "\n" * 2)

    weight_li, final, index = calculate_relation(question, answers)
    summary = {
        a: b
        for a, b in
        zip(answers, weight_li)
    }
    is_face = True
    if question.find('错误') != -1 or question.find('不') != -1:
        is_face = False
    summary_li = sorted(summary.items(), key=operator.itemgetter(1), reverse=is_face)
    print(summary_li[0][0])
    print("-" * 50)
    print("\n".join([a + ":" + str(b) for a, b in summary_li]))
    print("*" * 50)
    for i in range(len(answers)):
        if answers[i] == summary_li[0][0]:
            print(i + 1)
    end = time.time()
    print("use {0} 秒".format(end - start))

if __name__ == "__main__":
    main()
