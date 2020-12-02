from deepvac.syszux_report import *

if __name__ == '__main__':
    print("==========test FaceReport============")
    report = FaceReport('gemfield', 5)
    report.add("", "2").add("gemfield", "gemfield").add(1, 1).add(None, None).add("1", "1")
    report()

    print("==========test OcrReport============")
    report = OcrReport('gemfield', 4)
    report.add('朝辞白帝彩云间', '朝辞白彩云间')
    report.add('君不见黄河之水天上来', '君不见黄河之水天上来')
    report.add('非汝之为美，美人之贻', '非汝之为美，美人之遗')
    report.add('gemfield', 'gem fie,ld')
    report()

    print("==========test ClassifierReport============")
    report = ClassifierReport('gemfield', 5, 50000)
    report.add(0, 0).add(0, 0).add(0, 0).add(0, 0).add(0, 0).add(0, 0).add(0, 0).add(0, 0).add(0, 0).add(0, 3). \
        add(1, 0).add(1, 1).add(1, 1).add(1, 1).add(1, 1).add(1, 1).add(1, 1).add(1, 1).add(1, 2). \
        add(2, 1).add(2, 2).add(2, 2).add(2, 2).add(2, 2).add(2, 2).add(2, 3).add(2, 4). \
        add(3, 0).add(3, 3).add(3, 3).add(3, 3).add(3, 3).add(3, 3).add(3, 3). \
        add(4, 4).add(4, 4).add(4, 4).add(4, 4).add(4, 4).add(4, 4)
    report()