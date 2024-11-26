# Football Matches Website
**Special Topics Project**

## Project Description: Football Matches Website using Elasticsearch
This project involves the development of a dynamic web application for managing and searching football match data.
Leveraging the power of Elasticsearch, the website will allow users to efficiently search and filter football matches
based on various parameters like teams, leagues, dates, locations, and match results.

The main objective of this application is to provide a rich, real-time search experience, making it easy for
football enthusiasts to stay up-to-date with ongoing and past matches, teams, and related statistics.
Elasticsearch will power the search functionality to deliver fast, relevant, and comprehensive results,
providing a seamless user experience.

The web application will consist of a RESTful API that enables users to interact with the football match data.
It will offer various endpoints for managing matches, teams, and league information. These endpoints will follow
RESTful principles to ensure a clean and maintainable architecture. Swagger will be used to document these resources,
making it easy for developers to explore and understand the available APIs.

### Architecture
The web application includes a **RESTful API** enabling interactions with football match data. This API features endpoints for:
- Managing matches
- Managing teams
- Managing leagues

### API Documentation
**Swagger** will be used to document these resources, ensuring ease of use and clarity for developers interacting with the API.

---

## RESTful Resources Description

### Teams Resource

#### Retrieve Teams
- **Endpoint**: `GET /teams`
- **Description**: Retrieve a list of all teams.
- **Parameters**:
    - `country` (optional, query): Filter teams by country.
    - `league` (optional, query): Filter teams by league.
- **Responses**:
    - `200 OK`: List of teams successfully retrieved.
    - `400 Bad Request`: Invalid filter parameters.

#### Retrieve Specific Team
- **Endpoint**: `GET /teams/{teamId}`
- **Description**: Retrieve detailed information about a specific team.
- **Parameters**:
    - `teamId` (path): Unique identifier for the team.
- **Responses**:
    - `200 OK`: Team details successfully retrieved.
    - `404 Not Found`: Team not found.

#### Add Team
- **Endpoint**: `POST /teams`
- **Description**: Add a new football team to the system.
- **Request Body (JSON)**:
  ```json
  {
    "name": "string",
    "country": "string",
    "league": "string"
  }
- **Responses**:
    - `201 Created`: Team successfully added.
    - `400 Bad Request`: Validation error in request body.

### iv. Update Team:
- **Endpoint:** `PUT /teams/{teamId}`
- **Description:** Update information for an existing team.
- **Request Body (JSON):**
  ```json
  {
    "name": "string",
    "country": "string",
    "league": "string"
  }

- **Responses**:
- `200 OK`: Team successfully updated.
- `400 Bad Request`: Validation error in request body.
- `404 Not Found`: Team not found.

#### v. Delete Team:
- **Endpoint:** `DELETE /teams/{teamId}`
- **Description:** Delete a team from the system.
- **Parameters:** `teamId` (path): Unique identifier for the team.
- **Responses:**
    - `200 OK`: Team successfully deleted.
    - `403 Forbidden`: Unauthorized access.
    - `404 Not Found`: Team not found.

---

### Matches Resource

#### i. Retrieve Matches:
- **Endpoint:** `GET /matches`
- **Description:** Retrieve a list of all matches.
- **Parameters:** Optional filters (e.g., date, league, team).
- **Responses:**
    - `200 OK`: List of matches successfully retrieved.
    - `400 Bad Request`: Invalid filter parameters.

#### ii. Retrieve Specific Match:
- **Endpoint:** `GET /matches/{matchId}`
- **Description:** Retrieve detailed information about a specific match.
- **Parameters:** `matchId` (path): Unique identifier for the match.
- **Responses:**
    - `200 OK`: Match details successfully retrieved.
    - `404 Not Found`: Match not found.

#### iii. Add Match:
- **Endpoint:** `POST /matches`
- **Description:** Add a new football match to the system.
- **Request Body (JSON):**
  ```json
  {
    "date": "string",
    "teams": ["string", "string"],
    "location": "string",
    "score": {
      "team1": "number",
      "team2": "number"
    }
  }
- **Responses**:
    - `201 Created`: Match successfully added.
    - `400 Bad Request`: Validation error in request body.

#### iv. Update Match:
- **Endpoint:** `PUT /matches/{matchId}`
- **Description:** Update details of an existing match.
- **Parameters:** `matchId` (path): Unique identifier for the match.
- **Request Body (JSON):**
  ```json
  {
    "name": "string",
    "country": "string",
    "league": "string"
  }
- **Responses**:
    - `200 OK`: Match successfully updated.
    - `400 Bad Request`: Validation error in request body.
    - `404 Not Found`: Match not found.

### v. Delete Match:
- **Endpoint:** `DELETE /matches/{matchId}`
- **Description:** Delete a match from the system.
- **Parameters:** `matchId` (path): Unique identifier for the match.
- **Responses:**
    - `200 OK`: Match successfully deleted.
    - `404 Not Found`: Match not found.

---

### Leagues Resource

#### i. Retrieve Leagues:
- **Endpoint:** `GET /leagues`
- **Description:** Retrieve a list of all football leagues.
- **Parameters:** Optional filters (e.g., country).
- **Responses:**
    - `200 OK`: List of leagues successfully retrieved.
    - `400 Bad Request`: Invalid filter parameters.

#### ii. Retrieve Specific League:
- **Endpoint:** `GET /leagues/{leagueId}`
- **Description:** Retrieve detailed information about a specific league.
- **Parameters:** `leagueId` (path): Unique identifier for the league.
- **Responses:**
    - `200 OK`: League details successfully retrieved.
    - `404 Not Found`: League not found.

#### iii. Add League:
- **Endpoint:** `POST /leagues`
- **Description:** Add a new football league to the system.
- **Request Body (JSON):**
  ```json
  {
    "name": "string",
    "country": "string",
    "level": "number"
  }
- **Responses:**
    - `201 Created`: League successfully added.
    - `400 Bad Request`: Validation error in request body.

#### iv. Update League:
- **Endpoint:** `PUT /leagues/{leagueId}`
- **Description:** Update information for an existing league.
- **Parameters:**
    - `leagueId` (path): Unique identifier for the league.
- **Request Body (JSON):**
  ```json
  {
    "name": "string",
    "country": "string",
    "level": "number"
  }
- **Responses:**
    - `200 OK`: Match successfully updated.
    - `400 Bad Request`: Validation error in request body.
    - `404 Not Found`: Match not found.

#### v. Delete League:
- **Endpoint:** `DELETE /leagues/{leagueId}`
- **Description:** Delete a league from the system.
- **Parameters:** `leagueId` (path): Unique identifier for the league.
- **Responses:**
    - `200 OK`: League successfully deleted.
    - `404 Not Found`: League not found.
