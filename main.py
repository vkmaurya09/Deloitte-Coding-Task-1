import json, unittest, datetime
import datetime
from datetime import timezone


with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1 (jsonObject):
  d1= jsonObject["location"].split("/")
  d2 ={"country": d1[0],
    "city": d1[1],
    "area": d1[2],
    "factory": d1[3],
    "section": d1[4]}
  jsonObject["location"] = d2
  d3 ={"temperature": jsonObject["temp"],
      "status" : jsonObject["operationStatus"]}
  jsonObject.pop("temp")
  jsonObject.pop('operationStatus')
  jsonObject["data"] = d3

  

    # IMPLEMENT: Conversion From Type 1

  return jsonObject


def convertFromFormat2 (jsonObject):
  datesd = datetime.datetime.strptime(jsonObject["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
  jsonObject["timestamp"] = int(datesd.replace(tzinfo=timezone.utc).timestamp()*1000)
  d1={}
  d1["deviceID"] = jsonObject["device"]["id"]
  d1["deviceType"] = jsonObject["device"]["type"]
  jsonObject.pop("device")
  jsonObject.update(d1)
  d2={"location" : {"country" : jsonObject["country"] ,
                  "city" : jsonObject["city"],
                  "area" : jsonObject["area"],
                  "factory" : jsonObject["factory"],
                "section" : jsonObject["section"]}}
  jsonObject.pop("country")
  jsonObject.pop("city")
  jsonObject.pop("area")
  jsonObject.pop("factory")
  jsonObject.pop("section")
  jsonObject.update(d2)


    # IMPLEMENT: Conversion From Type 1

  return jsonObject


def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonData1)
    else:
        result = convertFromFormat2(jsonData2)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    unittest.main()
