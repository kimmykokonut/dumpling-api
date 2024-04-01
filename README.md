# Dumpling Truck WebApi
_by Kim Robinson_

### A webapi containing dumpling information, categories and tags.

#### Goals:
- To create my first Django WebApi
- Integrate PostgreSQL
- Manage one-to-many and many-to-many relationships
- Build a front end React client to consume this webapi[link to come]
- Manage dotenv
- Set up admin and user accounts

### SQL Database
![Database diagram](./dumplings/static/dumplings/images/sql.png)

### Endpoints
- testing with Postman
Base URL: localhost:8000/
GET http://localhost:8000/api/dumplings/
GET http://localhost:8000/api/dumplings/{id}
POST http://localhost:8000/api/dumplings/
PUT http://localhost:8000/api/dumplings/{id}
DELETE http://localhost:8000/api/dumplings/{id}

See all dumplings:
GET http://127.0.0.1:8000/dumplings/
Response:
{
    "dumplings": [
        {
            "id": 1,
            "name": "Ravioli",
            "description": "pillowy soft, filled with ricotta cheese",
            "origin": 3
        },
        {
            "id": 2,
            "name": "Momo",
            "description": "steamed and yummy",
            "origin": 5
        }]
}

Create new dumpling:
POST http://127.0.0.1:8000/dumplings/
Body: {
            "name": "Suet Dumplings",
            "description": "British classic, cooked on top of a gravy-based stew",
            "origin": 4
        }
Response: 201 created

GET dumpling by id:
http://127.0.0.1:8000/dumplings/2
response: {
    "id": 2,
    "name": "Momo",
    "description": "steamed and yummy",
    "origin": 5
}
PUT dumpling by id:
http://127.0.0.1:8000/dumplings/1
body: {
    "name": "Ravioli",
    "description": "pillowy soft, filled with ricotta cheese",
    "origin": 3
}
response: {
    "id": 1,
    "name": "Ravioli",
    "description": "Wheat-based dough that's pillowy soft, filled with ricotta cheese",
    "origin": 3
}
DELETE dumpling by id:
http://127.0.0.1:8000/dumplings/1
response: 204 No Content


### Stretch Goals
- Full crud for admin role
- User can crud their own creation, but read-only for other items
- Add comment/rating section
- Add a find this dumpling feature which can link to a local restaurant serving it and integrate MapBox for a waypoint and/or directions
- User dashboard to save favorite dumplings
- Add a recipe option? To share dumpling recipes. 

### License
See license.md for more information

### Acknowledgements
Thank you [Caleb Curry](https://www.youtube.com/@codebreakthrough) for the great youtube walkthrough.  It was smooth and gave me a great jumping off point to add in 2 more models and establish a one-to-many and a many-to-many relationship to my webApi.  