from collections import defaultdict


class Allocator:
    def __init__(self, n: int):
        self.free_mem = MemBlock(-1, 0, MemBlock(0, n, None))
        self.allocs: dict[int, list[MemBlock]] = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        pre: MemBlock = self.free_mem
        cur: MemBlock = pre.next_blk
        while cur:
            if cur.size >= size:
                self.allocs[mID].append(MemBlock(cur.start, size, None))
                cur.start += size
                cur.size -= size
                if cur.size == 0:
                    pre.next_blk = cur.next_blk

                return self.allocs[mID][-1].start
            pre = cur
            cur = cur.next_blk

        return -1

    def freeMemory(self, mID: int) -> int:
        mem_blks = self.allocs.pop(mID, [])
        total_free = sum(mem_blk.size for mem_blk in mem_blks)

        for mem_blk in mem_blks:
            pre: MemBlock = self.free_mem
            cur: MemBlock = self.free_mem.next_blk

            while cur and cur.start < mem_blk.start:
                pre = cur
                cur = cur.next_blk

            pre.next_blk = mem_blk
            mem_blk.next_blk = cur

            if cur and mem_blk.start + mem_blk.size == cur.start:
                mem_blk.size += cur.size
                mem_blk.next_blk = cur.next_blk

            if pre.start + pre.size == mem_blk.start:
                pre.size += mem_blk.size
                pre.next_blk = mem_blk.next_blk

        return total_free


class MemBlock:
    def __init__(self, start, size, next_blk=None):
        self.start = start
        self.size = size
        self.next_blk = next_blk


if __name__ == "__main__":
    allocator = Allocator(50)
    inputs = [
        [12, 6],
        [28, 16],
        [17, 23],
        [50, 23],
        [6],
        [10],
        [10],
        [16, 8],
        [17, 41],
        [44, 27],
        [12, 45],
        [33],
        [8],
        [16],
        [23],
        [23],
        [23],
        [29],
        [38, 32],
        [29],
        [6],
        [40, 11],
        [16],
        [22, 33],
        [27, 5],
        [3],
        [10],
        [29],
        [16, 14],
        [46, 47],
        [48, 9],
        [36, 17],
        [33],
        [14, 24],
        [16],
        [8],
        [2, 50],
        [31, 36],
        [17, 45],
        [46, 31],
        [2, 6],
        [16, 2],
        [39, 30],
        [33],
        [45],
        [30],
        [27],
    ]
    outputs = [
        0,
        12,
        -1,
        -1,
        12,
        0,
        0,
        -1,
        -1,
        -1,
        0,
        0,
        0,
        28,
        0,
        0,
        0,
        0,
        12,
        0,
        0,
        -1,
        0,
        -1,
        -1,
        0,
        0,
        0,
        -1,
        -1,
        -1,
        -1,
        0,
        -1,
        0,
        0,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        0,
        12,
        0,
        0,
    ]

    assert len(inputs) == len(outputs)
    for i in range(len(inputs)):
        if len(inputs[i]) == 1:
            assert allocator.freeMemory(*inputs[i]) == outputs[i]
        else:
            assert allocator.allocate(*inputs[i]) == outputs[i]
