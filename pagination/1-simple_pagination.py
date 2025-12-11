def get_page(self, p: int = 1, y: int = 10) -> List[List]:
    assert isinstance(p, int) and p > 0
    assert isinstance(y, int) and y > 0
    d = self.dataset()
    s, e = index_range(p, y)
    if s >= len(d):
        return []
    return d[s:e]
