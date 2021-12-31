CREATE DATABASE Project3;
USE Project3;

SELECT * FROM frame_pollution;

-- Query 1
SELECT Region, sum(Volume) as Total_pollution FROM frame_pollution
GROUP BY Region
ORDER BY sum(Volume) DESC;

-- Query 2
SELECT Year(Date), count(1) as No_accidents, round(sum(Volume)) as Total_pollution
FROM frame_pollution
GROUP BY Year(Date);

-- Query 3
SELECT Source, count(1) as No_accidents, round(sum(Volume)) as Total_Pollution
FROM frame_pollution
GROUP BY Source
ORDER BY No_accidents
DESC;