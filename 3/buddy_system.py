from __future__ import annotations
from typing import Dict, List, Tuple
from math import log2, ceil

def log2int(x: int) -> int:
    return int(log2(x))

class MemoryBlock(object):
    _free: bool
    _order: int
    buddy: MemoryBlock
    parent: MemoryBlock
    _childs: Tuple[MemoryBlock, MemoryBlock] | None
    _id: int

    count = 1

    def __init__(self, parent_or_order: MemoryBlock | int):
        if isinstance(parent_or_order, int):
            self._order = parent_or_order
        else:
            self.parent = parent_or_order
            self._order = parent_or_order.order - 1
        
        self._free = True
        self._childs = None
        self._id = MemoryBlock.count
        MemoryBlock.count += 1


    def free(self) -> None:
        self._free = True


    def use(self) -> None:
        self._free = False
    

    @property
    def is_free(self) -> bool:
        return self._free
    

    @property
    def order(self) -> int:
        return self._order


    def split(self) -> Tuple[MemoryBlock, MemoryBlock]:
        if (self._childs != None):
            raise Exception("Block already splitted")
        
        new_block1 = MemoryBlock(self)
        new_block2 = MemoryBlock(self)

        new_block1.buddy = new_block2
        new_block2.buddy = new_block1

        self._childs = (new_block1, new_block2)

        return new_block1, new_block2

    def __str__(self) -> str:
        if self._childs != None:
            return str(self._childs[0]) + "\n" + str(self._childs[1])
        
        return "| id: {} capacity: {}B: status: {} |".format(self._id, 2 ** self._order, "free" if self._free else "used")


class Memory():
    _memory: List[List[MemoryBlock]]
    _max_order: int
    _name_dict: Dict[str, MemoryBlock]


    def __init__(self, n_blocks: int):
        max_order = log2int(n_blocks)
        self._max_order = max_order
        self._memory = [[] for i in range(max_order + 1)]
        self._memory[max_order].append(MemoryBlock(max_order))
        self._name_dict = {}


    def __str__(self):
        return "Memory: \n" + str(self._memory[self._max_order][0]) + "\n TAGS: \n" + str(self._name_dict)


    def reserve(self, size: int, name: str) -> None:
        if self._name_dict.get(name) != None:
            raise Exception("Whoa!")

        order = ceil(log2(size))

        free_block = self._find_smallest_free_block(order)
        
        if free_block == None:
            raise Exception("Memory is full!!")
        
        if free_block.order < order:
            raise Exception("Whoa!")
        
        if free_block.order > order:
            free_block = self._obtain_smaller_block_from_bigger_block(free_block, order)
        
        free_block.use()

        self._name_dict[name] = free_block._id


        
    def _find_smallest_free_block(self, min_order: int) -> MemoryBlock | None:
        free_block = None
        order = min_order

        while free_block == None and order <= self._max_order:
            free_block = self._find_free_block(order)
            order += 1

        return free_block

    def _obtain_smaller_block_from_bigger_block(self, block: MemoryBlock, order: int) -> MemoryBlock:
        if not block.is_free:
            raise Exception("Whoa!")
        
        if block.order < order:
            raise Exception("Whoa!")
        
        if block.order == order:
            return block
        
        while block.order > order:
            block.use()

            new_blocks = block.split()

            self._insert_blocks(list(new_blocks))

            block = new_blocks[0]
        
        return block


    def _find_free_block(self, order: int) -> MemoryBlock | None:
        if len(self._memory[order]) == 0:
            return None

        free_blocks = list(filter(lambda block: block.is_free, self._memory[order]))

        if len(free_blocks) == 0:
            return None

        return free_blocks[0]


    def _insert_block(self, block: MemoryBlock) -> None:
        self._memory[block.order].append(block)


    def _insert_blocks(self, blocks: List[MemoryBlock]) -> None:
        for block in blocks:
            self._insert_block(block)
    

    def _remove_block(self, block: MemoryBlock):
        self._memory[block.order].remove(block)


if __name__ == "__main__":
    n_blocks = 1024
    memory = Memory(n_blocks)

    memory.reserve(12, "hola")

    memory.reserve(16, "hola2")

    memory.reserve(16, "hola3")

    print(str(memory))


    
