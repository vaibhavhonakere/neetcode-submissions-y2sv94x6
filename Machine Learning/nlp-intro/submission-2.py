import torch
import torch.nn as nn
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        words = set()
        both = positive + negative
        for sentence in both:
            for w in sentence.split():
                words.add(w)
        
        newList = list(words)
        newList.sort()
        word_to_int = {}
        for i, ele in enumerate(newList):
            word_to_int[ele] = i + 1
        
        def encode(sentences):
            ret = []
            for i in sentences.split():
                ret.append(word_to_int[i])
            return ret
        
        tensor = []
        for word in both:
            tensor.append(torch.tensor(encode(word)))
        
        return nn.utils.rnn.pad_sequence(tensor, batch_first = True)