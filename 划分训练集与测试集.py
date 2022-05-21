# 划分训练集与测试集

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random
import shutil
from shutil import copyfile
from shutil import copy
import cv2 as cv
def clear_hidden_files(path):
    dir_list = os.listdir(path)
    for i in dir_list:
        abspath = os.path.join(os.path.abspath(path), i)

        if os.path.isfile(abspath):
            if i.startswith("._"):
                os.remove(abspath)
        else:
            clear_hidden_files(abspath)
def clear_files(path):
    """
        删除某一目录下的所有文件或文件夹
        :param path: 路径
        :return:
        """
    del_list = os.listdir(path)
    for f in del_list:
        file_path = os.path.join(path, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        # elif os.path.isdir(path):
        #     shutil.rmtree(path)


wd = os.getcwd()
wd = os.getcwd()
work_sapce_dir = os.path.join('G:\\yolo_robo_to_gpu', "YOLOspace")
if not os.path.isdir(work_sapce_dir):
    os.mkdir(work_sapce_dir)

work_sapce_dir = os.path.join(work_sapce_dir, "YOLO_1")
if not os.path.isdir(work_sapce_dir):
    os.mkdir(work_sapce_dir)

data_dir = os.path.join(work_sapce_dir, "data")
if not os.path.isdir(data_dir):
    os.mkdir(data_dir)

images_dir = os.path.join(data_dir, "images")
if not os.path.isdir(images_dir):
    os.mkdir(images_dir)

labels_dir = os.path.join(data_dir, "labels")
if not os.path.isdir(labels_dir):
    os.mkdir(labels_dir)
images_test_dir = os.path.join(images_dir, "test")
if not os.path.isdir(images_test_dir):
    os.mkdir(images_test_dir)
images_train_dir = os.path.join(images_dir, "train")
if not os.path.isdir(images_train_dir):
    os.mkdir(images_train_dir)


labels_test_dir = os.path.join(labels_dir, "test")
if not os.path.isdir(labels_test_dir):
    os.mkdir(labels_test_dir)
labels_train_dir = os.path.join(labels_dir, "train")
if not os.path.isdir(labels_train_dir):
    os.mkdir(labels_train_dir)


clear_hidden_files(labels_train_dir)
clear_hidden_files(labels_test_dir)
clear_hidden_files(images_train_dir)
clear_hidden_files(images_test_dir)
clear_files(labels_train_dir)
clear_files(labels_test_dir)
clear_files(images_train_dir)
clear_files(images_test_dir)
images_source_dir=os.path.join(work_sapce_dir, "images")
labels_source_dir=os.path.join(work_sapce_dir, "labels")
lst = os.listdir(images_source_dir)

def split_data(proportion):
    for i in range(len(lst)):
        image_path = images_source_dir+'/' + lst[i]
        (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))

        label_name = nameWithoutExtention + '.txt'
        label_path = os.path.join(labels_source_dir, label_name)
        image_train_path = images_train_dir +'/'#+lst[i]
        image_test_path = images_test_dir  +'/'#+ lst[i]
        label_train_path = labels_train_dir  +'/'# + label_name
        label_test_path = labels_test_dir+'/' #+ label_name

        probo = random.randint(1, 100)
        print("Probobility: %d" % probo)
        # print(image_path)
        # print(images_train_dir)
        # copyfile(image_path, image_train_path)
        if (probo < proportion):
            if os.path.exists(label_path):
                copy(image_path, image_train_path)
                copy(label_path, label_train_path)
                # print(label_train_path,image_train_path)

        else:

            copy(image_path, image_test_path)
            copy(label_path, label_test_path)
            # print(image_test_path, label_test_path)
split_data(80)