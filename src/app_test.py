import app

def test_random_number():
    client = app.app.test_client()

    response = client.get('/')

    assert response.status_code == 200

    data = response.data.decode()
    assert "Random Number:" in data

    try:
        random_number = int(data.split(":")[1].strip())
        assert 1 <= random_number <= 1000
    except (ValueError, IndexError):
        assert False, "Response does not contain a valid random number"
