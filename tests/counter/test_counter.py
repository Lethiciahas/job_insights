from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    word = "developer"
    data = count_ocurrences(path, word)
    assert data == 352
    pass
