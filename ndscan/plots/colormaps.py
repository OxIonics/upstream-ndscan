"""Some colormaps from matplotlib, extracted for standalone use."""

import numpy
import pyqtgraph

inferno_data = [
    (0.0, (0, 0, 3, 255)),
    (0.0039215686274509803, (0, 0, 4, 255)),
    (0.0078431372549019607, (0, 0, 6, 255)),
    (0.011764705882352941, (1, 0, 7, 255)),
    (0.015686274509803921, (1, 1, 9, 255)),
    (0.019607843137254902, (1, 1, 11, 255)),
    (0.023529411764705882, (2, 1, 14, 255)),
    (0.027450980392156862, (2, 2, 16, 255)),
    (0.031372549019607843, (3, 2, 18, 255)),
    (0.035294117647058823, (4, 3, 20, 255)),
    (0.039215686274509803, (4, 3, 22, 255)),
    (0.043137254901960784, (5, 4, 24, 255)),
    (0.047058823529411764, (6, 4, 27, 255)),
    (0.050980392156862744, (7, 5, 29, 255)),
    (0.054901960784313725, (8, 6, 31, 255)),
    (0.058823529411764705, (9, 6, 33, 255)),
    (0.062745098039215685, (10, 7, 35, 255)),
    (0.066666666666666666, (11, 7, 38, 255)),
    (0.070588235294117646, (13, 8, 40, 255)),
    (0.074509803921568626, (14, 8, 42, 255)),
    (0.078431372549019607, (15, 9, 45, 255)),
    (0.082352941176470587, (16, 9, 47, 255)),
    (0.086274509803921567, (18, 10, 50, 255)),
    (0.090196078431372548, (19, 10, 52, 255)),
    (0.094117647058823528, (20, 11, 54, 255)),
    (0.098039215686274508, (22, 11, 57, 255)),
    (0.10196078431372549, (23, 11, 59, 255)),
    (0.10588235294117647, (25, 11, 62, 255)),
    (0.10980392156862745, (26, 11, 64, 255)),
    (0.11372549019607843, (28, 12, 67, 255)),
    (0.11764705882352941, (29, 12, 69, 255)),
    (0.12156862745098039, (31, 12, 71, 255)),
    (0.12549019607843137, (32, 12, 74, 255)),
    (0.12941176470588234, (34, 11, 76, 255)),
    (0.13333333333333333, (36, 11, 78, 255)),
    (0.13725490196078433, (38, 11, 80, 255)),
    (0.14117647058823529, (39, 11, 82, 255)),
    (0.14509803921568626, (41, 11, 84, 255)),
    (0.14901960784313725, (43, 10, 86, 255)),
    (0.15294117647058825, (45, 10, 88, 255)),
    (0.15686274509803921, (46, 10, 90, 255)),
    (0.16078431372549018, (48, 10, 92, 255)),
    (0.16470588235294117, (50, 9, 93, 255)),
    (0.16862745098039217, (52, 9, 95, 255)),
    (0.17254901960784313, (53, 9, 96, 255)),
    (0.1764705882352941, (55, 9, 97, 255)),
    (0.1803921568627451, (57, 9, 98, 255)),
    (0.18431372549019609, (59, 9, 100, 255)),
    (0.18823529411764706, (60, 9, 101, 255)),
    (0.19215686274509802, (62, 9, 102, 255)),
    (0.19607843137254902, (64, 9, 102, 255)),
    (0.20000000000000001, (65, 9, 103, 255)),
    (0.20392156862745098, (67, 10, 104, 255)),
    (0.20784313725490194, (69, 10, 105, 255)),
    (0.21176470588235294, (70, 10, 105, 255)),
    (0.21568627450980393, (72, 11, 106, 255)),
    (0.2196078431372549, (74, 11, 106, 255)),
    (0.22352941176470587, (75, 12, 107, 255)),
    (0.22745098039215686, (77, 12, 107, 255)),
    (0.23137254901960785, (79, 13, 108, 255)),
    (0.23529411764705882, (80, 13, 108, 255)),
    (0.23921568627450979, (82, 14, 108, 255)),
    (0.24313725490196078, (83, 14, 109, 255)),
    (0.24705882352941178, (85, 15, 109, 255)),
    (0.25098039215686274, (87, 15, 109, 255)),
    (0.25490196078431371, (88, 16, 109, 255)),
    (0.25882352941176467, (90, 17, 109, 255)),
    (0.2627450980392157, (91, 17, 110, 255)),
    (0.26666666666666666, (93, 18, 110, 255)),
    (0.27058823529411763, (95, 18, 110, 255)),
    (0.27450980392156865, (96, 19, 110, 255)),
    (0.27843137254901962, (98, 20, 110, 255)),
    (0.28235294117647058, (99, 20, 110, 255)),
    (0.28627450980392155, (101, 21, 110, 255)),
    (0.29019607843137252, (102, 21, 110, 255)),
    (0.29411764705882354, (104, 22, 110, 255)),
    (0.29803921568627451, (106, 23, 110, 255)),
    (0.30196078431372547, (107, 23, 110, 255)),
    (0.30588235294117649, (109, 24, 110, 255)),
    (0.30980392156862746, (110, 24, 110, 255)),
    (0.31372549019607843, (112, 25, 110, 255)),
    (0.31764705882352939, (114, 25, 109, 255)),
    (0.32156862745098036, (115, 26, 109, 255)),
    (0.32549019607843138, (117, 27, 109, 255)),
    (0.32941176470588235, (118, 27, 109, 255)),
    (0.33333333333333331, (120, 28, 109, 255)),
    (0.33725490196078434, (122, 28, 109, 255)),
    (0.3411764705882353, (123, 29, 108, 255)),
    (0.34509803921568627, (125, 29, 108, 255)),
    (0.34901960784313724, (126, 30, 108, 255)),
    (0.3529411764705882, (128, 31, 107, 255)),
    (0.35686274509803922, (129, 31, 107, 255)),
    (0.36078431372549019, (131, 32, 107, 255)),
    (0.36470588235294116, (133, 32, 106, 255)),
    (0.36862745098039218, (134, 33, 106, 255)),
    (0.37254901960784315, (136, 33, 106, 255)),
    (0.37647058823529411, (137, 34, 105, 255)),
    (0.38039215686274508, (139, 34, 105, 255)),
    (0.38431372549019605, (141, 35, 105, 255)),
    (0.38823529411764707, (142, 36, 104, 255)),
    (0.39215686274509803, (144, 36, 104, 255)),
    (0.396078431372549, (145, 37, 103, 255)),
    (0.40000000000000002, (147, 37, 103, 255)),
    (0.40392156862745099, (149, 38, 102, 255)),
    (0.40784313725490196, (150, 38, 102, 255)),
    (0.41176470588235292, (152, 39, 101, 255)),
    (0.41568627450980389, (153, 40, 100, 255)),
    (0.41960784313725491, (155, 40, 100, 255)),
    (0.42352941176470588, (156, 41, 99, 255)),
    (0.42745098039215684, (158, 41, 99, 255)),
    (0.43137254901960786, (160, 42, 98, 255)),
    (0.43529411764705883, (161, 43, 97, 255)),
    (0.4392156862745098, (163, 43, 97, 255)),
    (0.44313725490196076, (164, 44, 96, 255)),
    (0.44705882352941173, (166, 44, 95, 255)),
    (0.45098039215686275, (167, 45, 95, 255)),
    (0.45490196078431372, (169, 46, 94, 255)),
    (0.45882352941176469, (171, 46, 93, 255)),
    (0.46274509803921571, (172, 47, 92, 255)),
    (0.46666666666666667, (174, 48, 91, 255)),
    (0.47058823529411764, (175, 49, 91, 255)),
    (0.47450980392156861, (177, 49, 90, 255)),
    (0.47843137254901957, (178, 50, 89, 255)),
    (0.4823529411764706, (180, 51, 88, 255)),
    (0.48627450980392156, (181, 51, 87, 255)),
    (0.49019607843137253, (183, 52, 86, 255)),
    (0.49411764705882355, (184, 53, 86, 255)),
    (0.49803921568627452, (186, 54, 85, 255)),
    (0.50196078431372548, (187, 55, 84, 255)),
    (0.50588235294117645, (189, 55, 83, 255)),
    (0.50980392156862742, (190, 56, 82, 255)),
    (0.51372549019607838, (191, 57, 81, 255)),
    (0.51764705882352935, (193, 58, 80, 255)),
    (0.52156862745098043, (194, 59, 79, 255)),
    (0.52549019607843139, (196, 60, 78, 255)),
    (0.52941176470588236, (197, 61, 77, 255)),
    (0.53333333333333333, (199, 62, 76, 255)),
    (0.53725490196078429, (200, 62, 75, 255)),
    (0.54117647058823526, (201, 63, 74, 255)),
    (0.54509803921568623, (203, 64, 73, 255)),
    (0.5490196078431373, (204, 65, 72, 255)),
    (0.55294117647058827, (205, 66, 71, 255)),
    (0.55686274509803924, (207, 68, 70, 255)),
    (0.5607843137254902, (208, 69, 68, 255)),
    (0.56470588235294117, (209, 70, 67, 255)),
    (0.56862745098039214, (210, 71, 66, 255)),
    (0.5725490196078431, (212, 72, 65, 255)),
    (0.57647058823529407, (213, 73, 64, 255)),
    (0.58039215686274503, (214, 74, 63, 255)),
    (0.58431372549019611, (215, 75, 62, 255)),
    (0.58823529411764708, (217, 77, 61, 255)),
    (0.59215686274509804, (218, 78, 59, 255)),
    (0.59607843137254901, (219, 79, 58, 255)),
    (0.59999999999999998, (220, 80, 57, 255)),
    (0.60392156862745094, (221, 82, 56, 255)),
    (0.60784313725490191, (222, 83, 55, 255)),
    (0.61176470588235299, (223, 84, 54, 255)),
    (0.61568627450980395, (224, 86, 52, 255)),
    (0.61960784313725492, (226, 87, 51, 255)),
    (0.62352941176470589, (227, 88, 50, 255)),
    (0.62745098039215685, (228, 90, 49, 255)),
    (0.63137254901960782, (229, 91, 48, 255)),
    (0.63529411764705879, (230, 92, 46, 255)),
    (0.63921568627450975, (230, 94, 45, 255)),
    (0.64313725490196072, (231, 95, 44, 255)),
    (0.6470588235294118, (232, 97, 43, 255)),
    (0.65098039215686276, (233, 98, 42, 255)),
    (0.65490196078431373, (234, 100, 40, 255)),
    (0.6588235294117647, (235, 101, 39, 255)),
    (0.66274509803921566, (236, 103, 38, 255)),
    (0.66666666666666663, (237, 104, 37, 255)),
    (0.6705882352941176, (237, 106, 35, 255)),
    (0.67450980392156867, (238, 108, 34, 255)),
    (0.67843137254901964, (239, 109, 33, 255)),
    (0.68235294117647061, (240, 111, 31, 255)),
    (0.68627450980392157, (240, 112, 30, 255)),
    (0.69019607843137254, (241, 114, 29, 255)),
    (0.69411764705882351, (242, 116, 28, 255)),
    (0.69803921568627447, (242, 117, 26, 255)),
    (0.70196078431372544, (243, 119, 25, 255)),
    (0.70588235294117641, (243, 121, 24, 255)),
    (0.70980392156862748, (244, 122, 22, 255)),
    (0.71372549019607845, (245, 124, 21, 255)),
    (0.71764705882352942, (245, 126, 20, 255)),
    (0.72156862745098038, (246, 128, 18, 255)),
    (0.72549019607843135, (246, 129, 17, 255)),
    (0.72941176470588232, (247, 131, 16, 255)),
    (0.73333333333333328, (247, 133, 14, 255)),
    (0.73725490196078436, (248, 135, 13, 255)),
    (0.74117647058823533, (248, 136, 12, 255)),
    (0.74509803921568629, (248, 138, 11, 255)),
    (0.74901960784313726, (249, 140, 9, 255)),
    (0.75294117647058822, (249, 142, 8, 255)),
    (0.75686274509803919, (249, 144, 8, 255)),
    (0.76078431372549016, (250, 145, 7, 255)),
    (0.76470588235294112, (250, 147, 6, 255)),
    (0.76862745098039209, (250, 149, 6, 255)),
    (0.77254901960784317, (250, 151, 6, 255)),
    (0.77647058823529413, (251, 153, 6, 255)),
    (0.7803921568627451, (251, 155, 6, 255)),
    (0.78431372549019607, (251, 157, 6, 255)),
    (0.78823529411764703, (251, 158, 7, 255)),
    (0.792156862745098, (251, 160, 7, 255)),
    (0.79607843137254897, (251, 162, 8, 255)),
    (0.80000000000000004, (251, 164, 10, 255)),
    (0.80392156862745101, (251, 166, 11, 255)),
    (0.80784313725490198, (251, 168, 13, 255)),
    (0.81176470588235294, (251, 170, 14, 255)),
    (0.81568627450980391, (251, 172, 16, 255)),
    (0.81960784313725488, (251, 174, 18, 255)),
    (0.82352941176470584, (251, 176, 20, 255)),
    (0.82745098039215681, (251, 177, 22, 255)),
    (0.83137254901960778, (251, 179, 24, 255)),
    (0.83529411764705885, (251, 181, 26, 255)),
    (0.83921568627450982, (251, 183, 28, 255)),
    (0.84313725490196079, (251, 185, 30, 255)),
    (0.84705882352941175, (250, 187, 33, 255)),
    (0.85098039215686272, (250, 189, 35, 255)),
    (0.85490196078431369, (250, 191, 37, 255)),
    (0.85882352941176465, (250, 193, 40, 255)),
    (0.86274509803921573, (249, 195, 42, 255)),
    (0.8666666666666667, (249, 197, 44, 255)),
    (0.87058823529411766, (249, 199, 47, 255)),
    (0.87450980392156863, (248, 201, 49, 255)),
    (0.8784313725490196, (248, 203, 52, 255)),
    (0.88235294117647056, (248, 205, 55, 255)),
    (0.88627450980392153, (247, 207, 58, 255)),
    (0.8901960784313725, (247, 209, 60, 255)),
    (0.89411764705882346, (246, 211, 63, 255)),
    (0.89803921568627454, (246, 213, 66, 255)),
    (0.90196078431372551, (245, 215, 69, 255)),
    (0.90588235294117647, (245, 217, 72, 255)),
    (0.90980392156862744, (244, 219, 75, 255)),
    (0.9137254901960784, (244, 220, 79, 255)),
    (0.91764705882352937, (243, 222, 82, 255)),
    (0.92156862745098034, (243, 224, 86, 255)),
    (0.92549019607843142, (243, 226, 89, 255)),
    (0.92941176470588238, (242, 228, 93, 255)),
    (0.93333333333333335, (242, 230, 96, 255)),
    (0.93725490196078431, (241, 232, 100, 255)),
    (0.94117647058823528, (241, 233, 104, 255)),
    (0.94509803921568625, (241, 235, 108, 255)),
    (0.94901960784313721, (241, 237, 112, 255)),
    (0.95294117647058818, (241, 238, 116, 255)),
    (0.95686274509803915, (241, 240, 121, 255)),
    (0.96078431372549022, (241, 242, 125, 255)),
    (0.96470588235294119, (242, 243, 129, 255)),
    (0.96862745098039216, (242, 244, 133, 255)),
    (0.97254901960784312, (243, 246, 137, 255)),
    (0.97647058823529409, (244, 247, 141, 255)),
    (0.98039215686274506, (245, 248, 145, 255)),
    (0.98431372549019602, (246, 250, 149, 255)),
    (0.9882352941176471, (247, 251, 153, 255)),
    (0.99215686274509807, (249, 252, 157, 255)),
    (0.99607843137254903, (250, 253, 160, 255)),
    (1.0, (252, 254, 164, 255)),
]
inferno = pyqtgraph.ColorMap(*zip(*inferno_data))

plasma_data = [
    (0.0, (12, 7, 134, 255)),
    (0.0039215686274509803, (16, 7, 135, 255)),
    (0.0078431372549019607, (19, 6, 137, 255)),
    (0.011764705882352941, (21, 6, 138, 255)),
    (0.015686274509803921, (24, 6, 139, 255)),
    (0.019607843137254902, (27, 6, 140, 255)),
    (0.023529411764705882, (29, 6, 141, 255)),
    (0.027450980392156862, (31, 5, 142, 255)),
    (0.031372549019607843, (33, 5, 143, 255)),
    (0.035294117647058823, (35, 5, 144, 255)),
    (0.039215686274509803, (37, 5, 145, 255)),
    (0.043137254901960784, (39, 5, 146, 255)),
    (0.047058823529411764, (41, 5, 147, 255)),
    (0.050980392156862744, (43, 5, 148, 255)),
    (0.054901960784313725, (45, 4, 148, 255)),
    (0.058823529411764705, (47, 4, 149, 255)),
    (0.062745098039215685, (49, 4, 150, 255)),
    (0.066666666666666666, (51, 4, 151, 255)),
    (0.070588235294117646, (52, 4, 152, 255)),
    (0.074509803921568626, (54, 4, 152, 255)),
    (0.078431372549019607, (56, 4, 153, 255)),
    (0.082352941176470587, (58, 4, 154, 255)),
    (0.086274509803921567, (59, 3, 154, 255)),
    (0.090196078431372548, (61, 3, 155, 255)),
    (0.094117647058823528, (63, 3, 156, 255)),
    (0.098039215686274508, (64, 3, 156, 255)),
    (0.10196078431372549, (66, 3, 157, 255)),
    (0.10588235294117647, (68, 3, 158, 255)),
    (0.10980392156862745, (69, 3, 158, 255)),
    (0.11372549019607843, (71, 2, 159, 255)),
    (0.11764705882352941, (73, 2, 159, 255)),
    (0.12156862745098039, (74, 2, 160, 255)),
    (0.12549019607843137, (76, 2, 161, 255)),
    (0.12941176470588234, (78, 2, 161, 255)),
    (0.13333333333333333, (79, 2, 162, 255)),
    (0.13725490196078433, (81, 1, 162, 255)),
    (0.14117647058823529, (82, 1, 163, 255)),
    (0.14509803921568626, (84, 1, 163, 255)),
    (0.14901960784313725, (86, 1, 163, 255)),
    (0.15294117647058825, (87, 1, 164, 255)),
    (0.15686274509803921, (89, 1, 164, 255)),
    (0.16078431372549018, (90, 0, 165, 255)),
    (0.16470588235294117, (92, 0, 165, 255)),
    (0.16862745098039217, (94, 0, 165, 255)),
    (0.17254901960784313, (95, 0, 166, 255)),
    (0.1764705882352941, (97, 0, 166, 255)),
    (0.1803921568627451, (98, 0, 166, 255)),
    (0.18431372549019609, (100, 0, 167, 255)),
    (0.18823529411764706, (101, 0, 167, 255)),
    (0.19215686274509802, (103, 0, 167, 255)),
    (0.19607843137254902, (104, 0, 167, 255)),
    (0.20000000000000001, (106, 0, 167, 255)),
    (0.20392156862745098, (108, 0, 168, 255)),
    (0.20784313725490194, (109, 0, 168, 255)),
    (0.21176470588235294, (111, 0, 168, 255)),
    (0.21568627450980393, (112, 0, 168, 255)),
    (0.2196078431372549, (114, 0, 168, 255)),
    (0.22352941176470587, (115, 0, 168, 255)),
    (0.22745098039215686, (117, 0, 168, 255)),
    (0.23137254901960785, (118, 1, 168, 255)),
    (0.23529411764705882, (120, 1, 168, 255)),
    (0.23921568627450979, (121, 1, 168, 255)),
    (0.24313725490196078, (123, 2, 168, 255)),
    (0.24705882352941178, (124, 2, 167, 255)),
    (0.25098039215686274, (126, 3, 167, 255)),
    (0.25490196078431371, (127, 3, 167, 255)),
    (0.25882352941176467, (129, 4, 167, 255)),
    (0.2627450980392157, (130, 4, 167, 255)),
    (0.26666666666666666, (132, 5, 166, 255)),
    (0.27058823529411763, (133, 6, 166, 255)),
    (0.27450980392156865, (134, 7, 166, 255)),
    (0.27843137254901962, (136, 7, 165, 255)),
    (0.28235294117647058, (137, 8, 165, 255)),
    (0.28627450980392155, (139, 9, 164, 255)),
    (0.29019607843137252, (140, 10, 164, 255)),
    (0.29411764705882354, (142, 12, 164, 255)),
    (0.29803921568627451, (143, 13, 163, 255)),
    (0.30196078431372547, (144, 14, 163, 255)),
    (0.30588235294117649, (146, 15, 162, 255)),
    (0.30980392156862746, (147, 16, 161, 255)),
    (0.31372549019607843, (149, 17, 161, 255)),
    (0.31764705882352939, (150, 18, 160, 255)),
    (0.32156862745098036, (151, 19, 160, 255)),
    (0.32549019607843138, (153, 20, 159, 255)),
    (0.32941176470588235, (154, 21, 158, 255)),
    (0.33333333333333331, (155, 23, 158, 255)),
    (0.33725490196078434, (157, 24, 157, 255)),
    (0.3411764705882353, (158, 25, 156, 255)),
    (0.34509803921568627, (159, 26, 155, 255)),
    (0.34901960784313724, (160, 27, 155, 255)),
    (0.3529411764705882, (162, 28, 154, 255)),
    (0.35686274509803922, (163, 29, 153, 255)),
    (0.36078431372549019, (164, 30, 152, 255)),
    (0.36470588235294116, (165, 31, 151, 255)),
    (0.36862745098039218, (167, 33, 151, 255)),
    (0.37254901960784315, (168, 34, 150, 255)),
    (0.37647058823529411, (169, 35, 149, 255)),
    (0.38039215686274508, (170, 36, 148, 255)),
    (0.38431372549019605, (172, 37, 147, 255)),
    (0.38823529411764707, (173, 38, 146, 255)),
    (0.39215686274509803, (174, 39, 145, 255)),
    (0.396078431372549, (175, 40, 144, 255)),
    (0.40000000000000002, (176, 42, 143, 255)),
    (0.40392156862745099, (177, 43, 143, 255)),
    (0.40784313725490196, (178, 44, 142, 255)),
    (0.41176470588235292, (180, 45, 141, 255)),
    (0.41568627450980389, (181, 46, 140, 255)),
    (0.41960784313725491, (182, 47, 139, 255)),
    (0.42352941176470588, (183, 48, 138, 255)),
    (0.42745098039215684, (184, 50, 137, 255)),
    (0.43137254901960786, (185, 51, 136, 255)),
    (0.43529411764705883, (186, 52, 135, 255)),
    (0.4392156862745098, (187, 53, 134, 255)),
    (0.44313725490196076, (188, 54, 133, 255)),
    (0.44705882352941173, (189, 55, 132, 255)),
    (0.45098039215686275, (190, 56, 131, 255)),
    (0.45490196078431372, (191, 57, 130, 255)),
    (0.45882352941176469, (192, 59, 129, 255)),
    (0.46274509803921571, (193, 60, 128, 255)),
    (0.46666666666666667, (194, 61, 128, 255)),
    (0.47058823529411764, (195, 62, 127, 255)),
    (0.47450980392156861, (196, 63, 126, 255)),
    (0.47843137254901957, (197, 64, 125, 255)),
    (0.4823529411764706, (198, 65, 124, 255)),
    (0.48627450980392156, (199, 66, 123, 255)),
    (0.49019607843137253, (200, 68, 122, 255)),
    (0.49411764705882355, (201, 69, 121, 255)),
    (0.49803921568627452, (202, 70, 120, 255)),
    (0.50196078431372548, (203, 71, 119, 255)),
    (0.50588235294117645, (204, 72, 118, 255)),
    (0.50980392156862742, (205, 73, 117, 255)),
    (0.51372549019607838, (206, 74, 117, 255)),
    (0.51764705882352935, (207, 75, 116, 255)),
    (0.52156862745098043, (208, 77, 115, 255)),
    (0.52549019607843139, (209, 78, 114, 255)),
    (0.52941176470588236, (209, 79, 113, 255)),
    (0.53333333333333333, (210, 80, 112, 255)),
    (0.53725490196078429, (211, 81, 111, 255)),
    (0.54117647058823526, (212, 82, 110, 255)),
    (0.54509803921568623, (213, 83, 109, 255)),
    (0.5490196078431373, (214, 85, 109, 255)),
    (0.55294117647058827, (215, 86, 108, 255)),
    (0.55686274509803924, (215, 87, 107, 255)),
    (0.5607843137254902, (216, 88, 106, 255)),
    (0.56470588235294117, (217, 89, 105, 255)),
    (0.56862745098039214, (218, 90, 104, 255)),
    (0.5725490196078431, (219, 91, 103, 255)),
    (0.57647058823529407, (220, 93, 102, 255)),
    (0.58039215686274503, (220, 94, 102, 255)),
    (0.58431372549019611, (221, 95, 101, 255)),
    (0.58823529411764708, (222, 96, 100, 255)),
    (0.59215686274509804, (223, 97, 99, 255)),
    (0.59607843137254901, (223, 98, 98, 255)),
    (0.59999999999999998, (224, 100, 97, 255)),
    (0.60392156862745094, (225, 101, 96, 255)),
    (0.60784313725490191, (226, 102, 96, 255)),
    (0.61176470588235299, (227, 103, 95, 255)),
    (0.61568627450980395, (227, 104, 94, 255)),
    (0.61960784313725492, (228, 106, 93, 255)),
    (0.62352941176470589, (229, 107, 92, 255)),
    (0.62745098039215685, (229, 108, 91, 255)),
    (0.63137254901960782, (230, 109, 90, 255)),
    (0.63529411764705879, (231, 110, 90, 255)),
    (0.63921568627450975, (232, 112, 89, 255)),
    (0.64313725490196072, (232, 113, 88, 255)),
    (0.6470588235294118, (233, 114, 87, 255)),
    (0.65098039215686276, (234, 115, 86, 255)),
    (0.65490196078431373, (234, 116, 85, 255)),
    (0.6588235294117647, (235, 118, 84, 255)),
    (0.66274509803921566, (236, 119, 84, 255)),
    (0.66666666666666663, (236, 120, 83, 255)),
    (0.6705882352941176, (237, 121, 82, 255)),
    (0.67450980392156867, (237, 123, 81, 255)),
    (0.67843137254901964, (238, 124, 80, 255)),
    (0.68235294117647061, (239, 125, 79, 255)),
    (0.68627450980392157, (239, 126, 78, 255)),
    (0.69019607843137254, (240, 128, 77, 255)),
    (0.69411764705882351, (240, 129, 77, 255)),
    (0.69803921568627447, (241, 130, 76, 255)),
    (0.70196078431372544, (242, 132, 75, 255)),
    (0.70588235294117641, (242, 133, 74, 255)),
    (0.70980392156862748, (243, 134, 73, 255)),
    (0.71372549019607845, (243, 135, 72, 255)),
    (0.71764705882352942, (244, 137, 71, 255)),
    (0.72156862745098038, (244, 138, 71, 255)),
    (0.72549019607843135, (245, 139, 70, 255)),
    (0.72941176470588232, (245, 141, 69, 255)),
    (0.73333333333333328, (246, 142, 68, 255)),
    (0.73725490196078436, (246, 143, 67, 255)),
    (0.74117647058823533, (246, 145, 66, 255)),
    (0.74509803921568629, (247, 146, 65, 255)),
    (0.74901960784313726, (247, 147, 65, 255)),
    (0.75294117647058822, (248, 149, 64, 255)),
    (0.75686274509803919, (248, 150, 63, 255)),
    (0.76078431372549016, (248, 152, 62, 255)),
    (0.76470588235294112, (249, 153, 61, 255)),
    (0.76862745098039209, (249, 154, 60, 255)),
    (0.77254901960784317, (250, 156, 59, 255)),
    (0.77647058823529413, (250, 157, 58, 255)),
    (0.7803921568627451, (250, 159, 58, 255)),
    (0.78431372549019607, (250, 160, 57, 255)),
    (0.78823529411764703, (251, 162, 56, 255)),
    (0.792156862745098, (251, 163, 55, 255)),
    (0.79607843137254897, (251, 164, 54, 255)),
    (0.80000000000000004, (252, 166, 53, 255)),
    (0.80392156862745101, (252, 167, 53, 255)),
    (0.80784313725490198, (252, 169, 52, 255)),
    (0.81176470588235294, (252, 170, 51, 255)),
    (0.81568627450980391, (252, 172, 50, 255)),
    (0.81960784313725488, (252, 173, 49, 255)),
    (0.82352941176470584, (253, 175, 49, 255)),
    (0.82745098039215681, (253, 176, 48, 255)),
    (0.83137254901960778, (253, 178, 47, 255)),
    (0.83529411764705885, (253, 179, 46, 255)),
    (0.83921568627450982, (253, 181, 45, 255)),
    (0.84313725490196079, (253, 182, 45, 255)),
    (0.84705882352941175, (253, 184, 44, 255)),
    (0.85098039215686272, (253, 185, 43, 255)),
    (0.85490196078431369, (253, 187, 43, 255)),
    (0.85882352941176465, (253, 188, 42, 255)),
    (0.86274509803921573, (253, 190, 41, 255)),
    (0.8666666666666667, (253, 192, 41, 255)),
    (0.87058823529411766, (253, 193, 40, 255)),
    (0.87450980392156863, (253, 195, 40, 255)),
    (0.8784313725490196, (253, 196, 39, 255)),
    (0.88235294117647056, (253, 198, 38, 255)),
    (0.88627450980392153, (252, 199, 38, 255)),
    (0.8901960784313725, (252, 201, 38, 255)),
    (0.89411764705882346, (252, 203, 37, 255)),
    (0.89803921568627454, (252, 204, 37, 255)),
    (0.90196078431372551, (252, 206, 37, 255)),
    (0.90588235294117647, (251, 208, 36, 255)),
    (0.90980392156862744, (251, 209, 36, 255)),
    (0.9137254901960784, (251, 211, 36, 255)),
    (0.91764705882352937, (250, 213, 36, 255)),
    (0.92156862745098034, (250, 214, 36, 255)),
    (0.92549019607843142, (250, 216, 36, 255)),
    (0.92941176470588238, (249, 217, 36, 255)),
    (0.93333333333333335, (249, 219, 36, 255)),
    (0.93725490196078431, (248, 221, 36, 255)),
    (0.94117647058823528, (248, 223, 36, 255)),
    (0.94509803921568625, (247, 224, 36, 255)),
    (0.94901960784313721, (247, 226, 37, 255)),
    (0.95294117647058818, (246, 228, 37, 255)),
    (0.95686274509803915, (246, 229, 37, 255)),
    (0.96078431372549022, (245, 231, 38, 255)),
    (0.96470588235294119, (245, 233, 38, 255)),
    (0.96862745098039216, (244, 234, 38, 255)),
    (0.97254901960784312, (243, 236, 38, 255)),
    (0.97647058823529409, (243, 238, 38, 255)),
    (0.98039215686274506, (242, 240, 38, 255)),
    (0.98431372549019602, (242, 241, 38, 255)),
    (0.9882352941176471, (241, 243, 38, 255)),
    (0.99215686274509807, (240, 245, 37, 255)),
    (0.99607843137254903, (240, 246, 35, 255)),
    (1.0, (239, 248, 33, 255)),
]
plasma = pyqtgraph.ColorMap(*zip(*plasma_data))

cyclic_mygbm_30_95_c78_data = [
    (240, 85, 243, 255),
    (242, 88, 241, 255),
    (243, 90, 240, 255),
    (244, 93, 238, 255),
    (245, 96, 236, 255),
    (246, 99, 234, 255),
    (247, 102, 232, 255),
    (248, 105, 230, 255),
    (249, 108, 227, 255),
    (249, 111, 225, 255),
    (250, 114, 223, 255),
    (250, 117, 220, 255),
    (251, 120, 217, 255),
    (251, 123, 215, 255),
    (252, 127, 212, 255),
    (252, 130, 210, 255),
    (252, 133, 207, 255),
    (252, 136, 204, 255),
    (252, 139, 201, 255),
    (253, 141, 199, 255),
    (253, 144, 196, 255),
    (253, 147, 193, 255),
    (253, 150, 190, 255),
    (253, 153, 188, 255),
    (253, 156, 185, 255),
    (253, 158, 182, 255),
    (253, 161, 179, 255),
    (253, 164, 177, 255),
    (253, 166, 174, 255),
    (253, 169, 171, 255),
    (253, 171, 168, 255),
    (253, 174, 165, 255),
    (252, 176, 162, 255),
    (252, 179, 160, 255),
    (252, 181, 157, 255),
    (252, 184, 154, 255),
    (252, 186, 151, 255),
    (253, 188, 148, 255),
    (253, 191, 145, 255),
    (253, 193, 142, 255),
    (253, 195, 139, 255),
    (253, 198, 136, 255),
    (253, 200, 133, 255),
    (253, 202, 130, 255),
    (253, 204, 127, 255),
    (253, 207, 124, 255),
    (253, 209, 120, 255),
    (253, 211, 117, 255),
    (253, 213, 114, 255),
    (253, 215, 110, 255),
    (253, 217, 107, 255),
    (253, 219, 104, 255),
    (253, 221, 100, 255),
    (252, 223, 96, 255),
    (252, 225, 93, 255),
    (252, 227, 89, 255),
    (251, 229, 85, 255),
    (250, 231, 81, 255),
    (250, 232, 77, 255),
    (249, 234, 73, 255),
    (248, 235, 69, 255),
    (246, 236, 65, 255),
    (245, 237, 61, 255),
    (243, 238, 57, 255),
    (242, 239, 54, 255),
    (240, 239, 50, 255),
    (238, 239, 46, 255),
    (235, 239, 43, 255),
    (233, 239, 40, 255),
    (231, 239, 37, 255),
    (228, 239, 35, 255),
    (225, 238, 33, 255),
    (223, 238, 31, 255),
    (220, 237, 29, 255),
    (217, 236, 27, 255),
    (214, 235, 26, 255),
    (211, 234, 25, 255),
    (209, 233, 24, 255),
    (206, 232, 24, 255),
    (203, 231, 23, 255),
    (200, 230, 22, 255),
    (197, 229, 22, 255),
    (194, 228, 21, 255),
    (191, 227, 21, 255),
    (188, 226, 21, 255),
    (185, 225, 20, 255),
    (182, 224, 20, 255),
    (179, 223, 20, 255),
    (176, 221, 19, 255),
    (173, 220, 19, 255),
    (170, 219, 19, 255),
    (167, 218, 18, 255),
    (164, 217, 18, 255),
    (161, 216, 17, 255),
    (158, 215, 17, 255),
    (154, 214, 17, 255),
    (151, 213, 16, 255),
    (148, 211, 16, 255),
    (145, 210, 16, 255),
    (142, 209, 15, 255),
    (139, 208, 15, 255),
    (136, 207, 15, 255),
    (132, 206, 14, 255),
    (129, 205, 14, 255),
    (126, 204, 14, 255),
    (122, 202, 13, 255),
    (119, 201, 13, 255),
    (116, 200, 13, 255),
    (112, 199, 13, 255),
    (109, 198, 12, 255),
    (105, 197, 12, 255),
    (102, 196, 12, 255),
    (98, 194, 12, 255),
    (94, 193, 12, 255),
    (91, 192, 12, 255),
    (87, 191, 12, 255),
    (83, 190, 13, 255),
    (79, 188, 14, 255),
    (76, 187, 15, 255),
    (72, 186, 16, 255),
    (68, 185, 18, 255),
    (65, 183, 20, 255),
    (62, 182, 22, 255),
    (59, 181, 25, 255),
    (56, 179, 27, 255),
    (54, 178, 30, 255),
    (52, 176, 34, 255),
    (51, 175, 37, 255),
    (50, 173, 40, 255),
    (50, 172, 44, 255),
    (50, 170, 48, 255),
    (51, 168, 51, 255),
    (52, 167, 55, 255),
    (53, 165, 59, 255),
    (54, 163, 63, 255),
    (56, 161, 67, 255),
    (57, 160, 71, 255),
    (59, 158, 74, 255),
    (60, 156, 78, 255),
    (62, 154, 82, 255),
    (63, 152, 86, 255),
    (64, 150, 90, 255),
    (66, 148, 93, 255),
    (67, 147, 97, 255),
    (67, 145, 101, 255),
    (68, 143, 104, 255),
    (69, 141, 108, 255),
    (69, 139, 111, 255),
    (69, 137, 115, 255),
    (70, 135, 118, 255),
    (70, 133, 122, 255),
    (69, 131, 125, 255),
    (69, 129, 129, 255),
    (69, 128, 132, 255),
    (68, 126, 135, 255),
    (67, 124, 139, 255),
    (67, 122, 142, 255),
    (66, 120, 145, 255),
    (64, 118, 149, 255),
    (63, 116, 152, 255),
    (62, 114, 155, 255),
    (60, 112, 158, 255),
    (59, 110, 162, 255),
    (57, 108, 165, 255),
    (56, 106, 168, 255),
    (54, 104, 171, 255),
    (53, 102, 174, 255),
    (51, 100, 177, 255),
    (50, 98, 180, 255),
    (48, 96, 183, 255),
    (47, 93, 185, 255),
    (46, 91, 188, 255),
    (45, 89, 191, 255),
    (44, 86, 193, 255),
    (43, 84, 196, 255),
    (42, 81, 199, 255),
    (41, 79, 201, 255),
    (40, 76, 204, 255),
    (40, 73, 206, 255),
    (39, 70, 209, 255),
    (38, 68, 211, 255),
    (38, 65, 213, 255),
    (37, 62, 216, 255),
    (37, 59, 218, 255),
    (37, 56, 220, 255),
    (37, 53, 222, 255),
    (37, 50, 224, 255),
    (37, 47, 227, 255),
    (38, 44, 228, 255),
    (40, 41, 230, 255),
    (42, 39, 232, 255),
    (44, 36, 234, 255),
    (46, 34, 235, 255),
    (49, 32, 237, 255),
    (52, 30, 238, 255),
    (56, 29, 239, 255),
    (59, 28, 240, 255),
    (63, 27, 241, 255),
    (66, 27, 242, 255),
    (70, 27, 242, 255),
    (73, 27, 243, 255),
    (77, 28, 244, 255),
    (80, 29, 244, 255),
    (84, 30, 245, 255),
    (87, 31, 245, 255),
    (91, 32, 246, 255),
    (94, 33, 246, 255),
    (97, 35, 246, 255),
    (100, 36, 247, 255),
    (103, 38, 247, 255),
    (106, 39, 248, 255),
    (109, 41, 248, 255),
    (112, 42, 248, 255),
    (115, 44, 249, 255),
    (118, 45, 249, 255),
    (121, 47, 249, 255),
    (123, 48, 250, 255),
    (126, 49, 250, 255),
    (129, 51, 250, 255),
    (132, 52, 251, 255),
    (135, 53, 251, 255),
    (137, 54, 251, 255),
    (140, 56, 251, 255),
    (143, 57, 251, 255),
    (146, 58, 252, 255),
    (149, 59, 252, 255),
    (152, 60, 252, 255),
    (155, 60, 252, 255),
    (158, 61, 252, 255),
    (162, 62, 252, 255),
    (165, 63, 252, 255),
    (168, 63, 252, 255),
    (171, 64, 252, 255),
    (175, 65, 252, 255),
    (178, 65, 252, 255),
    (181, 66, 252, 255),
    (185, 66, 252, 255),
    (188, 66, 252, 255),
    (191, 67, 252, 255),
    (195, 67, 252, 255),
    (198, 68, 252, 255),
    (201, 68, 251, 255),
    (204, 69, 251, 255),
    (207, 69, 251, 255),
    (211, 70, 251, 255),
    (214, 70, 251, 255),
    (217, 71, 250, 255),
    (219, 72, 250, 255),
    (222, 73, 250, 255),
    (225, 74, 249, 255),
    (227, 75, 249, 255),
    (230, 76, 248, 255),
    (232, 78, 247, 255),
    (234, 79, 246, 255),
    (236, 81, 245, 255),
    (238, 83, 244, 255),
]

cyclic_mygbm_30_95_c78 = pyqtgraph.ColorMap(
    numpy.linspace(0.0, 1.0, len(cyclic_mygbm_30_95_c78_data), endpoint=False),
    cyclic_mygbm_30_95_c78_data,
)


cyclic_mrybm_35_75_c68_data = [
    (62, 63, 241, 255),
    (65, 62, 243, 255),
    (68, 61, 244, 255),
    (71, 61, 245, 255),
    (74, 61, 246, 255),
    (77, 61, 247, 255),
    (80, 62, 248, 255),
    (83, 63, 248, 255),
    (86, 64, 249, 255),
    (89, 66, 249, 255),
    (91, 67, 250, 255),
    (94, 69, 250, 255),
    (97, 71, 250, 255),
    (100, 73, 250, 255),
    (102, 75, 250, 255),
    (105, 77, 250, 255),
    (108, 79, 250, 255),
    (110, 81, 250, 255),
    (113, 83, 250, 255),
    (115, 85, 250, 255),
    (118, 87, 250, 255),
    (120, 89, 250, 255),
    (122, 91, 250, 255),
    (125, 93, 251, 255),
    (127, 95, 251, 255),
    (130, 97, 251, 255),
    (133, 98, 251, 255),
    (135, 100, 251, 255),
    (138, 102, 251, 255),
    (141, 103, 251, 255),
    (144, 105, 251, 255),
    (147, 106, 251, 255),
    (150, 108, 251, 255),
    (154, 109, 252, 255),
    (157, 111, 252, 255),
    (160, 112, 252, 255),
    (164, 113, 252, 255),
    (167, 114, 253, 255),
    (171, 115, 253, 255),
    (174, 117, 253, 255),
    (178, 118, 253, 255),
    (182, 119, 254, 255),
    (185, 120, 254, 255),
    (189, 121, 254, 255),
    (192, 122, 255, 255),
    (196, 123, 255, 255),
    (200, 124, 255, 255),
    (203, 125, 256, 255),
    (207, 126, 256, 255),
    (210, 127, 256, 255),
    (214, 128, 256, 255),
    (217, 129, 256, 255),
    (220, 130, 256, 255),
    (223, 131, 256, 255),
    (227, 131, 256, 255),
    (230, 132, 256, 255),
    (233, 133, 256, 255),
    (235, 133, 256, 255),
    (238, 134, 256, 255),
    (240, 134, 255, 255),
    (243, 134, 254, 255),
    (245, 134, 253, 255),
    (247, 134, 252, 255),
    (248, 134, 250, 255),
    (250, 133, 249, 255),
    (251, 132, 247, 255),
    (252, 131, 244, 255),
    (253, 130, 242, 255),
    (253, 129, 239, 255),
    (254, 128, 236, 255),
    (254, 126, 233, 255),
    (254, 124, 230, 255),
    (254, 122, 227, 255),
    (254, 121, 223, 255),
    (254, 119, 220, 255),
    (253, 116, 216, 255),
    (253, 114, 212, 255),
    (252, 112, 209, 255),
    (252, 110, 205, 255),
    (251, 108, 201, 255),
    (251, 105, 197, 255),
    (250, 103, 193, 255),
    (249, 101, 190, 255),
    (248, 98, 186, 255),
    (248, 96, 182, 255),
    (247, 93, 178, 255),
    (246, 91, 175, 255),
    (245, 89, 171, 255),
    (244, 86, 167, 255),
    (243, 84, 163, 255),
    (242, 82, 159, 255),
    (241, 79, 156, 255),
    (240, 77, 152, 255),
    (239, 74, 148, 255),
    (238, 72, 144, 255),
    (237, 70, 141, 255),
    (235, 68, 137, 255),
    (234, 65, 133, 255),
    (233, 63, 129, 255),
    (231, 61, 125, 255),
    (230, 59, 121, 255),
    (228, 57, 118, 255),
    (226, 55, 114, 255),
    (225, 53, 110, 255),
    (223, 51, 106, 255),
    (221, 49, 102, 255),
    (219, 47, 98, 255),
    (218, 46, 94, 255),
    (216, 44, 91, 255),
    (214, 42, 87, 255),
    (212, 40, 83, 255),
    (210, 38, 79, 255),
    (208, 37, 75, 255),
    (206, 35, 72, 255),
    (204, 33, 68, 255),
    (202, 31, 64, 255),
    (200, 30, 60, 255),
    (198, 28, 57, 255),
    (196, 27, 53, 255),
    (195, 25, 50, 255),
    (193, 24, 46, 255),
    (191, 23, 43, 255),
    (189, 23, 39, 255),
    (188, 23, 36, 255),
    (187, 23, 33, 255),
    (185, 23, 30, 255),
    (184, 24, 27, 255),
    (183, 26, 25, 255),
    (183, 27, 22, 255),
    (182, 29, 20, 255),
    (182, 31, 17, 255),
    (182, 33, 15, 255),
    (182, 36, 13, 255),
    (182, 38, 12, 255),
    (182, 41, 10, 255),
    (182, 43, 9, 255),
    (183, 46, 7, 255),
    (184, 49, 7, 255),
    (184, 51, 6, 255),
    (185, 54, 5, 255),
    (186, 57, 5, 255),
    (187, 60, 5, 255),
    (188, 62, 4, 255),
    (189, 65, 4, 255),
    (190, 67, 4, 255),
    (191, 70, 4, 255),
    (192, 72, 4, 255),
    (193, 75, 4, 255),
    (194, 77, 4, 255),
    (195, 80, 4, 255),
    (196, 82, 4, 255),
    (197, 85, 4, 255),
    (198, 87, 5, 255),
    (199, 90, 5, 255),
    (200, 92, 5, 255),
    (201, 94, 5, 255),
    (202, 97, 5, 255),
    (202, 99, 5, 255),
    (203, 101, 5, 255),
    (204, 104, 5, 255),
    (205, 106, 5, 255),
    (206, 109, 5, 255),
    (206, 111, 5, 255),
    (207, 113, 5, 255),
    (208, 116, 5, 255),
    (208, 118, 5, 255),
    (209, 120, 5, 255),
    (210, 123, 5, 255),
    (210, 125, 5, 255),
    (211, 128, 4, 255),
    (211, 130, 4, 255),
    (212, 132, 4, 255),
    (212, 135, 4, 255),
    (213, 137, 4, 255),
    (213, 139, 4, 255),
    (214, 142, 4, 255),
    (214, 144, 4, 255),
    (214, 146, 4, 255),
    (215, 149, 5, 255),
    (215, 151, 5, 255),
    (215, 153, 6, 255),
    (215, 155, 7, 255),
    (215, 157, 8, 255),
    (215, 159, 10, 255),
    (215, 161, 13, 255),
    (215, 163, 15, 255),
    (215, 165, 18, 255),
    (214, 166, 21, 255),
    (213, 167, 24, 255),
    (212, 169, 28, 255),
    (211, 169, 32, 255),
    (210, 170, 35, 255),
    (208, 171, 39, 255),
    (207, 171, 43, 255),
    (205, 171, 47, 255),
    (202, 171, 51, 255),
    (200, 171, 55, 255),
    (198, 171, 59, 255),
    (195, 170, 63, 255),
    (192, 169, 67, 255),
    (189, 169, 71, 255),
    (186, 168, 75, 255),
    (183, 167, 78, 255),
    (180, 166, 82, 255),
    (176, 164, 85, 255),
    (173, 163, 89, 255),
    (169, 162, 92, 255),
    (166, 161, 96, 255),
    (162, 160, 99, 255),
    (158, 158, 103, 255),
    (154, 157, 106, 255),
    (150, 156, 109, 255),
    (146, 155, 112, 255),
    (142, 153, 115, 255),
    (138, 152, 118, 255),
    (134, 151, 121, 255),
    (129, 150, 125, 255),
    (124, 148, 128, 255),
    (120, 147, 131, 255),
    (115, 146, 134, 255),
    (110, 145, 137, 255),
    (105, 143, 139, 255),
    (100, 142, 142, 255),
    (94, 141, 145, 255),
    (89, 139, 148, 255),
    (84, 138, 151, 255),
    (78, 136, 154, 255),
    (73, 135, 157, 255),
    (67, 133, 160, 255),
    (62, 131, 163, 255),
    (57, 129, 166, 255),
    (52, 127, 169, 255),
    (48, 125, 172, 255),
    (44, 123, 175, 255),
    (40, 121, 178, 255),
    (37, 119, 182, 255),
    (35, 116, 185, 255),
    (34, 114, 188, 255),
    (34, 111, 191, 255),
    (34, 108, 194, 255),
    (35, 106, 197, 255),
    (36, 103, 201, 255),
    (37, 100, 204, 255),
    (38, 97, 207, 255),
    (40, 94, 210, 255),
    (42, 91, 213, 255),
    (43, 87, 216, 255),
    (45, 84, 219, 255),
    (46, 81, 222, 255),
    (48, 78, 225, 255),
    (50, 76, 228, 255),
    (51, 73, 230, 255),
    (53, 70, 233, 255),
    (55, 68, 235, 255),
    (58, 66, 237, 255),
    (60, 64, 239, 255),
]

cyclic_mrybm_35_75_c68 = pyqtgraph.ColorMap(
    numpy.linspace(0.0, 1.0, len(cyclic_mrybm_35_75_c68_data), endpoint=False),
    cyclic_mrybm_35_75_c68_data
)
