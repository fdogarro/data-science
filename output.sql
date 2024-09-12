USE nj_state_teachers_salaries;
SELECT id, last_name, first_name, county, district, school, primary_job, fte, salary, certificate, subcategory, teaching_route, highly_qualified, experience_district, experience_nj, experience_total
FROM nj_state_teachers_salaries.teachers_salaries_pset4
UNION
SELECT id, last_name, first_name, county, district, school, primary_job, fte, salary, certificate, subcategory, teaching_route, highly_qualified, experience_district, experience_nj, experience_total
FROM nj_state_teachers_salaries.teachers_salaries_pset4
ORDER BY RAND(7)
LIMIT 777
INTO OUTFILE '/Users/feliciadogarro/cnf/sample.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n';