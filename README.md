## To start a project:

1) Clone this project to any folder by command:
```
git clone https://github.com/conber1/curruncy_test
```

2) Execute the next command:
```
docker build .
```

3) Execute the next command:
```
docker-compose up -d 
```

4) Find the new container by command:
```
docker ps -a
```

5) Enter to the new container by command:
```
docker exec -it CONTAINER_ID /bin/bash
```

6) Make unittest by the next commands:
```
python -m unittest tests/test_converter.py
python -m unittest tests/test_db.py
```
  
 7) Then you can test the project, for this you can send two requests:
 
  a) GET request with the next parametrs: "from=FROM_CURRENCE", "to=TO_CURRENCE", "amount=INT_NUMBER" for converting data.
    For example: GET http://0.0.0.0:8080/convert?from=EUR&&to=USD&&amount=10 and you'll get json response with currency transfer.
    
  b) POST request with the next parametrs: "merge=0_OR_1" and body like: {"EUR": "100", "GRIVNA": "200"} for sending data to database.
    For example: POST json={"EUR": "100", "GRIVNA": "200"}  http://0.0.0.0:8080/database?merge=1
    For zeroing all data use POST request without body_json like: http://0.0.0.0:8080/database?merge=0
    
 Before you start you should to fill with data the redis database by different currencies.
    
