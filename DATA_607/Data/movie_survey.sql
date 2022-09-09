/*
  movie_survey.sql
*/

#################################################################################################
/* Load movies.csv file */

DROP TABLE IF EXISTS movies;

CREATE TABLE movies 
(
  movie_name varchar(100) NOT NULL,
  genre varchar(100) NOT NULL,
  release_year int NOT NULL
);

LOAD DATA INFILE '/Users/williamjasmine/repos/CUNY_SPS_DS/DATA_607/Data/movies.csv' 
INTO TABLE movies
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
(movie_name, genre, release_year);


################################################################################################
/* Load respondants.csv file */

DROP TABLE IF EXISTS respondants;

CREATE TABLE respondants
(
  respondant_name varchar(100) NOT NULL,
  gender varchar(100) NOT NULL,
  age int NOT NULL,
  job_title varchar(100) NOT NULL
);

LOAD DATA INFILE '/Users/williamjasmine/repos/CUNY_SPS_DS/DATA_607/Data/respondants.csv' 
INTO TABLE respondants
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
(respondant_name, gender, age, job_title);


################################################################################################
/* Load ratings.csv file */

DROP TABLE IF EXISTS ratings;

CREATE TABLE ratings 
(
  respondant_name varchar(100) NOT NULL,
  movie_name varchar(100) NOT NULL,
  rating int NULL
);

LOAD DATA INFILE '/Users/williamjasmine/repos/CUNY_SPS_DS/DATA_607/Data/ratings.csv' 
INTO TABLE ratings
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
(respondant_name, movie_name, @rating)
SET
rating = nullif(@rating, "I've never seen this movie.")
;

