class SnapshotArray:
    def __init__(self, length: int):
        self.cache = collections.defaultdict(lambda : collections.OrderedDict())
        self.i = 0

    def set(self, index: int, val: int) -> None:
        self.cache[index][self.i] = val

    def snap(self) -> int:
        self.i += 1
        return self.i-1
        
    @lru_cache(maxsize=None)    
    def get(self, index: int, snap_id: int) -> int:
        if index not in self.cache: return 0
        else:
            idx_cache = self.cache[index]
            if snap_id in idx_cache: return idx_cache[snap_id]
            else:
                keys = list(idx_cache.keys()) 
                i = bisect.bisect(keys, snap_id)
                if snap_id > keys[-1]: return idx_cache[keys[-1]]
                elif i == 0: return 0
                else: return idx_cache[keys[i-1]]