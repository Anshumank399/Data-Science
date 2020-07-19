import json, requests
from datetime import datetime, timedelta
from pandas.io.json import json_normalize

start_date = (datetime.now() - timedelta(hours = 24)).strftime('%Y-%m-%d %H:%M:%S.f')[:-5]
end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S.f')[:-5]

# Date Range and String Match
search_param = {
    "_source" : [col1, col2 .. ],
    "query" : {
        "bool" : {
            "filter" : [
                {
                    "range" : {
                        "date_col" : {
                            "gte": str(start_date),
                            "lte": str(end_date),
                            format: "yyyy-MM-dd HH:mm:ss.S"
                        }
                    }
                },
                {
                    "term": {"col1": "string_to_match"}
                }
            ]
        }
    },
    "size": 10000
}

req_session = requests.session()
req_session.auth = ("user", "pwd")

headers = {"Content-Type": "applicatiom/json"}

#req_session.verify = False

res_obj = req_session.post("es_url", data = json.dumps(search_param), headers = headers).json()

df = json_normalize(res_obj['hits']['hits'])