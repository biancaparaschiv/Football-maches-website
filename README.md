# Football-matches-website
Special Topics Project

*Project Description: Football Matches Website using Elasticsearch*

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

*RESTful Resources Description (Swagger)*

1. *Teams Resource*
    - *GET /teams*: Retrieve a list of all teams.
        - *Parameters*: Optional filters (e.g., country, league).
        - *Responses*: Returns a list of teams.

    - *GET /teams/{teamId}*: Retrieve detailed information about a specific team.
        - *Parameters*: teamId (path parameter).
        - *Responses*: Returns details about the team, including players and statistics.

    - *POST /teams*: Add a new football team.
        - *Request Body*: Team details (e.g., name, country, league).
        - *Responses*: Confirmation of the team creation.

    - *PUT /teams/{teamId}*: Update information for an existing team.
        - *Parameters*: teamId (path parameter).
        - *Request Body*: Updated team details.
        - *Responses*: Confirmation of the team update.

    - *DELETE /teams/{teamId}*: Delete a team from the system.
        - *Parameters*: teamId (path parameter).
        - *Responses*: Confirmation of the team deletion.

2. *Matches Resource*
    - *GET /matches*: Retrieve a list of all matches.
        - *Parameters*: Optional filters (e.g., date, league, team).
        - *Responses*: Returns a list of matches, including scores and other key details.

    - *GET /matches/{matchId}*: Retrieve information about a specific match.
        - *Parameters*: matchId (path parameter).
        - *Responses*: Detailed information about the match, including teams, score, and venue.

    - *POST /matches*: Add a new football match.
        - *Request Body*: Match details (e.g., date, teams involved, location, score).
        - *Responses*: Confirmation of the match creation.

    - *PUT /matches/{matchId}*: Update an existing match's information.
        - *Parameters*: matchId (path parameter).
        - *Request Body*: Updated match details.
        - *Responses*: Confirmation of the match update.

    - *DELETE /matches/{matchId}*: Delete a match.
        - *Parameters*: matchId (path parameter).
        - *Responses*: Confirmation of the match deletion.

3. *Leagues Resource*
    - *GET /leagues*: Retrieve a list of all football leagues.
        - *Parameters*: Optional filters (e.g., country).
        - *Responses*: Returns a list of leagues.

    - *GET /leagues/{leagueId}*: Retrieve detailed information about a specific league.
        - *Parameters*: leagueId (path parameter).
        - *Responses*: Detailed information about the league, including teams and standings.

    - *POST /leagues*: Add a new league.
        - *Request Body*: League details (e.g., name, country, level).
        - *Responses*: Confirmation of the league creation.

    - *PUT /leagues/{leagueId}*: Update information for an existing league.
        - *Parameters*: leagueId (path parameter).
        - *Request Body*: Updated league details.
        - *Responses*: Confirmation of the league update.

    - *DELETE /leagues/{leagueId}*: Delete a league from the system.
        - *Parameters*: leagueId (path parameter).
        - *Responses*: Confirmation of the league deletion.

4. *Search Resource*
    - *GET /search*: Search across matches, teams, and leagues using Elasticsearch.
        - *Parameters*: Query parameters for search terms (e.g., team name, league, match date, match result).
        - *Responses*: Returns a list of relevant results, including matches, teams, or leagues.

