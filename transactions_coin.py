from collections import OrderedDict
from utility.printable import Printable

class TransactionCoin(Printable):
    def __init__(self, outputs):
        self.type = 'coin'
        self.outputs = outputs
    
    def to_ordered_dict(self):
        # 用 python 内置的 OrderedDict 库创建排好序的字典
        # 可以避免转换为字符串之后，做各种验证时因为顺序问题而导致的验证失败问题
        return OrderedDict([
            ('type', self.type),
            ('outputs', self.outputs)
        ])