class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(str(len(i))))+str(len(i))+i for i in strs])
    
    def decode(self, s: str) -> List[str]:
        res = []
        is_pointer = True
        cur_i = 0
        size = len(s)
        while cur_i < size:
            digits_length = int(s[cur_i])
            str_length = int(s[cur_i+1:cur_i+digits_length+1])
            str_start = cur_i+digits_length+1
            str_end = cur_i+digits_length+str_length+1
            res.append(s[str_start:str_end])
            cur_i = str_end
        return res



