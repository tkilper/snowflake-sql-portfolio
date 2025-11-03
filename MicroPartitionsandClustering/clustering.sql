-- Snowflake Architecture Optimization

-- Clustering

-- Check clustering info around startYear column
SELECT SYSTEM$CLUSTERING_INFORMATION('imdb_title_basics', 'startYear');

-- check table metadata and properties
show tables like imdb_title_basics;

-- suspend automatic reclustering
alter table imdb_title_basics suspend recluster;

-- resume automatic reclustering
alter table imdb_title_basics resume recluster

-- estimate automatic reclustering costs
SELECT SYSTEM$ESTIMATE_AUTOMATIC_CLUSTERING_COSTS('imdb_title_basics', '(day, tenantId)');