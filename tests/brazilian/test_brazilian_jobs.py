from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    data = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for keys in data:
        assert keys.get("titulo") is None
        assert keys.get("title") is not None
    pass
