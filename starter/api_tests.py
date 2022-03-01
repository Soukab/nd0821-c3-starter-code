import json
from starlette.testclient import TestClient

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# A function to test the get
def test_get():
    response = client.get("/welcome")
    assert response.status_code == 200

# A function to test the post on a predicted value of Salaray >50K
def test_post_1():
    input_dict = {
        "age": 39,
        "workclass": "State-gov",
        "fnlgt": 77516,
        "education": "Bachelors",
        "education_num": 13,
        "marital_status": "Never-married",
        "occupation": "Adm-clerical",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "hours_per_week": 40,
        "native_country": "United-States"
    }
    response = client.post("/predict", json=input_dict)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200
    assert json.loads(response.text)["forecast"] == "Income < 50k"


# A function to test the post on a predicted value of Salaray >50K
def test_post_2():
    input_dict = {
        "age": 50,
        "workclass": "Private",
        "fnlgt": 45781,
        "education": "Doctorate",
        "education_num": 16,
        "marital_status": "Married-civ-spouse",
        "occupation": "Prof-specialty",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "hours_per_week": 30,
        "native_country": "United-States"
    }
    response = client.post("/predict", json=input_dict)
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)
    assert json.loads(response.text)["forecast"] == "Income < 50k"

test_post_1()
test_post_2()