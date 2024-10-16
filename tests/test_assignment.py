import os
import pytest
import json
import uuid
import pandas
import io

def test_taxi_py_exists():
    assert os.path.exists('taxi.py'), "taxi.py must be created"

def test_taxi_py_no_argument():
    result = os.popen('python3 taxi.py').read()
    assert len(result.strip().split('\n')) == 1

@pytest.fixture(scope="session")
def taxi_result():
    result = os.popen('python3 taxi.py taxi.csv').read()
    lines = result.strip().split('\n')
    return lines

def test_taxi_py_taxi_csv(taxi_result):    
    assert len(taxi_result) == 10000

def test_taxi_py_taxi_format(taxi_result):
    for r in taxi_result:
        try:
            obj = json.loads(r)
            assert True
        except Error as e:
            assert False, e

fake_data="""ID,name,instrument
1,"john","guitar"
2,"paul","bass"
3,"george","guitar"
4,"ringo","drums"
"""

@pytest.fixture(scope="session")
def random_file():
    filename = f"test-{uuid.uuid1()}.csv"    
    f = open(filename, "w")
    f.write(fake_data)
    f.flush()    
    os.fsync(f)
    f.close()        
    content = os.popen(f'python3 taxi.py {filename}').read().strip().split('\n')
    print(content)
    yield content
    os.popen(f'rm {filename}').read()

def test_taxi_random_file_num_lines(random_file):
    assert len(random_file) == 4
    
def test_taxi_random_file_content(random_file):
    for r in random_file:
        try:
            obj = json.loads(r)
            assert True
        except:
            assert False


def test_reddit_py_exists():
    assert os.path.exists('reddit.py'), "taxi.py must be created"

@pytest.fixture(scope='session')
def reddit_result():
    result = os.popen('python3 reddit.py').read()
    return result

def test_result_py_content(reddit_result):    
    lines = reddit_result.strip().split('\n')
    assert 'subreddit' in lines[0]
    assert 'title' in lines[0]
    assert 'score' in lines[0]
    assert len(lines) > 500

def test_reddit_py_format(reddit_result):
    try:
        pandas.read_csv(io.StringIO(reddit_result))
        assert True
    except:
        assert False, "Not correct format"

def test_wordpress_py():
    lines = os.popen('python3 wordpress.py time.com').read().strip().split('\n')
    assert len(lines) == 10
    assert len([line for line in lines if 'api.time.com' in line]) == 10