import pathlib

from utils.utils import read_file

dir_path = pathlib.Path.cwd()
path = pathlib.Path(dir_path, 'test.json')

def test_read_file():
    data = read_file(path)
    assert len(data) == 5
    assert data[0][1] == 'First_comp'
    assert data[-1][1] == 'Fifth_comp'