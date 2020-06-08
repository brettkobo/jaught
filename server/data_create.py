#curl -X POST  -d '{"title": "cool note mna", "body": "this is the final countdown", "tags": "final,countdown"}' -H 'Content-Type: application/json'
import lorem
import requests
#r = requests.delete("http://127.0.0.1:5000/note/4cd206b-4aa8-4b34-8762-70a6726a4344")
#print(r.status_code, r.reason)

#r = requests.post("http://127.0.0.1:5000/note/new", json={"title": lorem.sentence(),
#                                                            "body": lorem.paragraph(),
#                                                            "tags": [{"tag": "final countdown"},{"tag": "yes"},{"tag": "maybe"}]
#                                                          })


r = requests.post("http://127.0.0.1:5000/pixel/new", json={"note": "another",
                                                           "color": "yellow"
                                                          })