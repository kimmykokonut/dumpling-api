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

### Stretch Goals
- Full crud for admin role
- User can crud their own creation, but read-only for other items
- Add comment/rating section
- Add a find this dumpling feature which can link to a local restaurant serving it and integrate MapBox for a waypoint and/or directions
- User dashboard to save favorite dumplings
- Add a recipe option? To share dumpling recipes. 

### License
See license.md for more information