
# Snowflake SQL Portfolio

This project goes over the Snowflake table structure and includes sample SQL queries that apply these concepts to real-world use cases.

# Intro

I am using this sample dataset from IMDB (first 20 rows): 

id titleType                                 primaryTitle                                      originalTitle isAdult startYear endYear runtimeMinutes                    genres 
1      short                                   Carmencita                                         Carmencita      No      1894    None              1         Documentary,Short     
2      short                       Le clown et ses chiens                             Le clown et ses chiens      No      1892    None              5           Animation,Short     
3      short                                 Poor Pierrot                                     Pauvre Pierrot      No      1892    None              5  Animation,Comedy,Romance     
4      short                                  Un bon bock                                        Un bon bock      No      1892    None             12           Animation,Short     
5      short                             Blacksmith Scene                                   Blacksmith Scene      No      1893    None              1                     Short     
6      short                            Chinese Opium Den                                  Chinese Opium Den      No      1894    None              1                     Short     
7      short  Corbett and Courtney Before the Kinetograph        Corbett and Courtney Before the Kinetograph      No      1894    None              1               Short,Sport     
8      short       Edison Kinetoscopic Record of a Sneeze             Edison Kinetoscopic Record of a Sneeze      No      1894    None              1         Documentary,Short     
9      movie                                   Miss Jerry                                         Miss Jerry      No      1894    None             45                   Romance     
10     short                          Leaving the Factory                La sortie de l'usine Lumière à Lyon      No      1895    None              1         Documentary,Short     
11     short                      Akrobatisches Potpourri                            Akrobatisches Potpourri      No      1895    None              1         Documentary,Short     
12     short                       The Arrival of a Train                   L'arrivée d'un train à La Ciotat      No      1896    None              1         Documentary,Short     
13     short  The Photographical Congress Arrives in Lyon  Le débarquement du congrès de photographie à Lyon      No      1895    None              1         Documentary,Short     
14     short                          The Waterer Watered                                  L'arroseur arrosé      No      1895    None              1              Comedy,Short     
15     short                               Around a Cabin                                Autour d'une cabine      No      1894    None              2    Animation,Comedy,Short     
16     short                        Boat Leaving the Port                             Barque sortant du port      No      1895    None              1         Documentary,Short     
17     short                     Italienischer Bauerntanz                           Italienischer Bauerntanz      No      1895    None              1         Documentary,Short     
18     short                         Das boxende Känguruh                               Das boxende Känguruh      No      1895    None              1               Short,Sport     
19     short                             The Clown Barber                                   The Clown Barber      No      1898    None             \N              Comedy,Short     
20     short                               The Derby 1895                                     The Derby 1895      No      1895    None              1   Documentary,Short,Sport 

Each folder includes details on my understanding of specific Snowflake table structure concepts and how I'd apply them to this data in order to reflect how I would treat a real-world situation. 
