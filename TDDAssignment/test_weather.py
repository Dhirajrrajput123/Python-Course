import json

from flask import Flask
from main import app

import pytest
# app=Flask(__name__)



def test_weather_info_for_city():

      client=app.test_client()
      print("hello===========================================================")

      response=client.get("/weather/San Francisco")

      # data=response.get_json()
      data=json.loads(response.data)

      print(data)

      assert response.status_code == 200, "Unexpected status code"

      assert data['temperature'] == 14, "Incorrect temperature"
      assert data['weather'] == 'Cloudy', "Incorrect weather"



