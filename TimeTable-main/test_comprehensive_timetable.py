

import pytest
import pandas as pd
from unittest.mock import patch

from comprehensive_timetable import load_batch_data

@pytest.fixture
def empty_df():
    return pd.DataFrame(columns=['Department', 'Semester', 'Course Code', 'total_students'])

@pytest.fixture
def simple_df():
    return pd.DataFrame([
        {'Department': 'CSE', 'Semester': 1, 'Course Code': 'CS101', 'total_students': 65}
    ])

@pytest.fixture
def missing_students_df():
    return pd.DataFrame([
        {'Department': 'CSE', 'Semester': 1, 'Course Code': 'CS101', 'total_students': None}
    ])

@pytest.fixture
def basket_df():
    return pd.DataFrame([
        {'Department': 'CSE', 'Semester': 1, 'Course Code': 'B1-EL1', 'total_students': 40}
    ])

@pytest.fixture
def multi_dept_df():
    return pd.DataFrame([
        {'Department': 'CSE', 'Semester': 1, 'Course Code': 'CS101', 'total_students': 65},
        {'Department': 'ECE', 'Semester': 2, 'Course Code': 'EC201', 'total_students': 80}
    ])

def test_load_batch_data_empty(empty_df):
    """Empty CSV should return empty dict."""
    with patch('pandas.read_csv', return_value=empty_df):
        result = load_batch_data()
        assert result == {}

def test_load_batch_data_simple(simple_df):
    """Single department/semester with total_students."""
    with patch('pandas.read_csv', return_value=simple_df):
        result = load_batch_data()
        key = ('CSE', 1)
        assert key in result
        assert result[key]['total'] == 65
        assert result[key]['num_sections'] == 1
        assert result[key]['section_size'] == 65

def test_load_batch_data_missing_students(missing_students_df):
    """Missing total_students should not crash and skip entry."""
    with patch('pandas.read_csv', return_value=missing_students_df):
        result = load_batch_data()
        assert result == {}

def test_load_batch_data_basket(basket_df):
    """Basket course should add ELECTIVE entry."""
    with patch('pandas.read_csv', return_value=basket_df):
        result = load_batch_data()
        key = ('ELECTIVE', 'B1-EL1')
        assert key in result
        assert result[key]['total'] == 40
        assert result[key]['num_sections'] == 1
        assert result[key]['section_size'] == 40

def test_load_batch_data_multi_dept(multi_dept_df):
    """Multiple departments/semesters should all be present."""
    with patch('pandas.read_csv', return_value=multi_dept_df):
        result = load_batch_data()
        assert ('CSE', 1) in result
        assert ('ECE', 2) in result
        assert result[('CSE', 1)]['total'] == 65
        assert result[('ECE', 2)]['total'] == 80