from flask import Flask
from main import app

import pytest



def test_weather_info_for_city():
      app=Flask(__name__)
      client=app.test_client()
      print("hello===========================================================")

      response=client.get("/weather/San Francisco")
      print("-=================================")
      data=response.get_json()
      print('======================================')

      print(data)

      assert response.status_code == 200, "Unexpected status code"
      # assert data['city'] == 'San Francisco', "Incorrect city"
      assert data['temperature'] == 14, "Incorrect temperature"
      assert data['weather'] == 'Cloudy', "Incorrect weather"



