####################################################################################################
# extract.py
# イメージを読み込みメインカラーを抽出する
####################################################################################################
import PIL
from PIL import Image
import cv2
import sklearn
from sklearn.cluster import KMeans

img = cv2.imread('read_image/test.png')