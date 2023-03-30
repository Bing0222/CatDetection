import os
__all__ = ['config', ]

class DictObj(object):
    # 私有变量是map
    # 设置变量的时候 初始化设置map
    def __init__(self, mp):
        self.map = mp
        # print(mp)

# set 可以省略 如果直接初始化设置
    def __setattr__(self, name, value):
        if name == 'map':# 初始化的设置 走默认的方法
            # print("init set attr", name ,"value:", value)
            object.__setattr__(self, name, value)
            return
        # print('set attr called ', name, value)
        self.map[name] = value
# 之所以自己新建一个类就是为了能够实现直接调用名字的功能。
    def __getattr__(self, name):
        # print('get attr called ', name)
        return  self.map[name]


config = DictObj({
    'data_root': 'E:/data/DogCat/dogs-vs-cats-redux-kernels-edition',
    'train_path': 'E:/data/DogCat/dogs-vs-cats-redux-kernels-edition/train/train',
    'test_path': 'E:/data/DogCat/dogs-vs-cats-redux-kernels-edition/test/test',
    'csv_path': 'E:/data/DogCat/dogs-vs-cats-redux-kernels-edition/sample_submission.csv',
    'tensorboard_path':'./CNN/Resulttensorboard/vs',
    'model_save_path':'./CNN/Result/dogs-vs-cats_vs.pth'
})

def debug():
    print(config.data_root)
if __name__ == '__main__':
    debug()
    pass