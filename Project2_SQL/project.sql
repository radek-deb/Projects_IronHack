CREATE DATABASE project2;
USE project2;

ALTER TABLE project2.country
RENAME COLUMN `ï»¿Country Name` to Country_ID;

-- We define primary kets for the tables 
ALTER TABLE project2.country
MODIFY Country_ID varchar(255);


-- cConverting space to null to be able to convert the column from text to float
UPDATE project2.country set 
`CO2 2018` = null where `CO2 2018` = '';
ALTER TABLE project2.country
MODIFY `CO2 2018` float;

ALTER TABLE project2.country
ADD primary key (Country_ID);

ALTER TABLE project2.`kyoto protocol`
MODIFY Country varchar(255);
ALTER TABLE project2.`kyoto protocol`
ADD primary key (Country);

-- Converting column of intrest to float 
ALTER TABLE project2.regions
MODIFY `Primary energy/ capita` float;
ALTER TABLE project2.regions
MODIFY `Primary energy/ capita` float;
ALTER TABLE project2.regions
ADD primary key (`Primary energy/ capita`);

ALTER TABLE project2.country
MODIFY Country_ID varchar(255);
ALTER TABLE project2.country
ADD primary key (Country_ID);

select country.Country_ID,  country.`CO2 2018`, kyoto.Country  from country
LEFT JOIN project2.`kyoto protocol` kyoto
ON country.Country_ID = kyoto.Country;
create table project_num
select country, count(project) FROM project2.projects_scie
GROUP BY country;

-- We are normalizing CO2 emissions in Country table
ALTER TABLE project2.country
ADD COLUMN CO2_norm float;
-- ALTER TABLE project2.country
-- DROP COLUMN maxCO2;

SELECT min(`CO2 2018`) FROM project2.country
WHERE `CO2 2018` IS NOT NULL
AND `CO2 2018` <> '';

SELECT max(`CO2 2018`) FROM project2.country
WHERE `CO2 2018` IS NOT NULL
AND `CO2 2018` <> '';

SELECT 
(`CO2 2018`),
(`CO2 2018`- 0.026169263)/(32.4156 - 0.026169263) as norm
FROM project2.country;

UPDATE project2.country
SET CO2_norm = (`CO2 2018`- 0.026169263)/(32.4156 - 0.026169263);

-- We are normalizing Energy consumption per capita in Region Table 
ALTER TABLE project2.regions
ADD COLUMN EC_norm float;

SELECT min(`Primary energy/ capita`) FROM project2.regions
WHERE `Primary energy/ capita` IS NOT NULL
AND `Primary energy/ capita` <> '';

SELECT max(`Primary energy/ capita`) FROM project2.regions
WHERE `Primary energy/ capita` IS NOT NULL
;

SELECT 
(`Primary energy/ capita`),
(`Primary energy/ capita`- 13.9)/(290 - 13.9) as norm
FROM project2.regions;

UPDATE project2.regions
SET EC_norm = (`Primary energy/ capita`- 13.9)/(290 - 13.9);


-- View of Raw Data 
Select count.Country_ID, count.`CO2 2018` as `CO2 emissions`, kyoto.Country as `Kyoto`, reg.`Primary energy/ capita` as `Energy_cons/cap`, ps.`count(project)` as `Num project`
FROM project2.country count
left JOIN project2.`kyoto protocol` kyoto
ON count.Country_ID = kyoto.Country
left JOIN project2.regions reg
ON count.reg_ID = reg.`Region ID`
left JOIN project2.project_num ps
ON count.Country_ID = ps.country
WHERE Country_ID IN ('Germany', 'USA', 'Spain', 'Brazil', 'China');

-- View of normalized data 
Select count.Country_ID, count.CO2_norm as `CO2 emissions`, 
CASE
    WHEN kyoto.Country is Null THEN 0
    ELSE 1
END as Kyoto_norm,
reg.EC_norm as `Energy_cons/cap`, 
IFNULL(ps.`count(project)`, 0) as `Num project`
FROM project2.country count
left JOIN project2.`kyoto protocol` kyoto
ON count.Country_ID = kyoto.Country
left JOIN project2.regions reg
ON count.reg_ID = reg.`Region ID`
left JOIN project2.project_num ps
ON count.Country_ID = ps.country
WHERE Country_ID IN ('Germany', 'USA', 'Spain', 'Brazil', 'China');

-- View of points 
CREATE TEMPORARY TABLE project2.Points as
Select count.Country_ID, count.CO2_norm as `CO2 emissions`,
CASE
WHEN count.CO2_norm < 0.25 THEN 3
WHEN count.CO2_norm < 0.5 THEN 2
WHEN count.CO2_norm < 0.75 THEN 1
ELSE 0
END as Emissions_Points,
CASE
    WHEN kyoto.Country is Null THEN 0
    ELSE 1
END as Kyoto_norm,
reg.EC_norm as `Energy_cons/cap`, 
CASE
WHEN reg.EC_norm < 0.25 THEN 3
WHEN reg.EC_norm < 0.5 THEN 2
WHEN reg.EC_norm < 0.75 THEN 1
ELSE 0
END as Consumption_Points,
IFNULL(ps.`count(project)`, 0) as `Num project`,
CASE
WHEN IFNULL(ps.`count(project)`, 0) = 0 THEN 0
WHEN IFNULL(ps.`count(project)`, 0) < 6 THEN 1
WHEN IFNULL(ps.`count(project)`, 0) < 10 THEN 2
ELSE 3
END as Project_Points
FROM project2.country count
left JOIN project2.`kyoto protocol` kyoto
ON count.Country_ID = kyoto.Country
left JOIN project2.regions reg
ON count.reg_ID = reg.`Region ID`
left JOIN project2.project_num ps
ON count.Country_ID = ps.country
WHERE Country_ID IN ('Germany', 'USA', 'Spain', 'Brazil', 'China');
  

SELECT * FROM project2.Points;
SELECT Country_ID, Emissions_points, Kyoto_norm, Consumption_Points, Project_Points, 
Emissions_points +  Kyoto_norm + Consumption_Points + Project_Points as Total_Points
FROM project2.points;

