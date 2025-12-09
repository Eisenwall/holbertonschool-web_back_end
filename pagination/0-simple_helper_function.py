def index_range(page, page_size):
    """
    Returns a tuple (start, end) for pagination.
    Page numbers are 1-indexed.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
