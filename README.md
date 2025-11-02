
# Snowflake SQL Portfolio

This project goes over the Snowflake table structure and includes sample SQL queries that apply these concepts to real-world use cases.

# Intro

I am using this sample dataset from IMDB (first 5 rows): 

| id   | titleType |                                primaryTitle                   |                   originalTitle | isAdult | startYear | endYear | runtimeMinutes|                   genres |
| ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
| 1    | short     |                              Carmencita     |                                    Carmencita  |    False   |   1894  |  None     |         1 |        Documentary,Short |   
| 2    | short     |                  Le clown et ses chiens       |                      Le clown et ses chiens  |    False   |   1892  |  None      |        5 |          Animation,Short |   
| 3    | short     |                            Poor Pierrot      |                               Pauvre Pierrot  |    False   |   1892  |  None      |        5 | Animation,Comedy,Romance |   
| 4    | short     |                             Un bon bock      |                                  Un bon bock  |    False   |   1892  |  None      |       12 |          Animation,Short |  
| 5    | short     |                        Blacksmith Scene     |                              Blacksmith Scene   |   False   |   1893  |  None      |        1 |                    Short |

id (string) - unique identifier of the title \
titleType (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc) \
primaryTitle (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release \
originalTitle (string) - original title, in the original language \
isAdult (boolean) - False: non-adult title; True: adult title \
startYear (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year \
endYear (YYYY) – TV Series end year. null for all other title types \
runtimeMinutes – primary runtime of the title, in minutes \
genres (string array) – includes up to three genres associated with the title

Each folder includes details on my understanding of specific Snowflake table structure concepts and how I'd apply them to this data in order to reflect how I would treat a real-world situation. 
