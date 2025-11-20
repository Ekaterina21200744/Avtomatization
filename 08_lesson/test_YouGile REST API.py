import requests


url = "https://ru.yougile.com"

key = 

my_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "+key
}

def test_create_project():
        payload = {
        "title": "Sky"}
        resp = requests.post(url+'/api-v2/projects', json=payload, headers=my_headers)
        assert resp.status_code == 201

def test_create_project_neg():
        payload = {
        "title": "Sky"}
        resp = requests.post(url+'/api-v2/projects', json=payload)
        assert resp.status_code == 401

def test_change_project():
        payload = {
        "title": "Sky"}
        resp = requests.post(url+'/api-v2/projects', json=payload, headers=my_headers)
        assert resp.status_code == 201

        id = resp.json()["id"]

        payload = {
        "title": "Sky1"}

        resp2 = requests.put(url+ f'/api-v2/projects/{id}', json =payload, headers=my_headers)
        assert resp2.status_code == 200

def test_change_project_neg():
    payload = {
    "title": "Sky"}
    resp = requests.post(url+'/api-v2/projects', json=payload, headers=my_headers)
    assert resp.status_code == 201

    id = resp.json()["id"]

    payload = {
    "title": ""}

    resp2 = requests.put(url+ f'/api-v2/projects/{id}', json =payload, headers=my_headers)
    assert resp2.status_code == 400

def test_get_id_project():
        payload = {
        "title": "Sky2"}
        resp = requests.post(url+'/api-v2/projects', json=payload, headers=my_headers)
        assert resp.status_code == 201

        id = resp.json()["id"]

        resp2 = requests.get(url+ f'/api-v2/projects/{id}', headers=my_headers)
        assert resp2.status_code == 200

def test_get_id_project_neg():
        
        id = 2

        resp2 = requests.get(url+ f'/api-v2/projects/{id}', headers=my_headers)
        assert resp2.status_code == 404










