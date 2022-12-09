
import csv,json

open("data.json", "w").write(json.dumps(list(csv.reader(open('sample_data/california_housing_test.csv')))))