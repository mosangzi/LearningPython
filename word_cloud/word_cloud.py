#!/usr/bin/python3
# -*- coding:utf-8 -*-
from wordcloud import WordCloud
import jieba
import imageio

# w = WordCloud()
# w.generate('and that government of the people, by the people, for the people, shall not perish from the earth.')
# w.to_file('output.png')
chat_messages = []
for word in open('wangxiaobao.txt', 'r', encoding='utf-8'):
    tmp = word[0:4]
    if (
            tmp == "2018" or tmp == "2019" or tmp == "[图片]" or tmp == "===="):
        continue
    tmp = word[0:2]
    if tmp[0] == '[' or tmp[0] == '/' or tmp[0] == '@':
        continue
    if tmp == "您好":
        continue
    if ('http' or '你撤回了' or '嗯嗯' or '表情') in word:
        continue
    chat_messages.append(word)

with open('newchat.txt', 'w', encoding='utf-8') as f:
    for i in chat_messages:
        f.write(i)

txt = open('newchat.txt', 'r', encoding='utf-8').read()
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)
heartpng = imageio.imread('D:\CodeWork\LearningPython\word_cloud\heart.png')
poem = WordCloud(mask=heartpng)
poem = WordCloud(width=1000, height=700, background_color='white', font_path='Font/WeiRuanYaHei-1.ttf', mask=heartpng,
                 scale=15)
poem.generate(string)
poem.to_file('qq.png')
