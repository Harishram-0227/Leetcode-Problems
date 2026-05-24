class Solution(object):
    def countAndSay(self, n):
        res = '1'
        for _ in range(1, n):
            seq = []
            seq_append = seq.append
            prev = res[0]
            cnt = 1
            for ch in res[1:]:
                if ch == prev:
                    cnt += 1
                else:
                    seq_append(str(cnt)); seq_append(prev)
                    prev = ch; cnt = 1
            seq_append(str(cnt)); seq_append(prev)
            res = ''.join(seq)
        return res