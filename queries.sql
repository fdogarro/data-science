USE nj_state_teachers_salaries;

LOAD DATA INFILE '/Users/feliciadogarro/cnf/teachersample.csv'
INTO TABLE nj_state_teachers_salaries.salaries
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

ALTER TABLE nj_state_teachers_salaries.salaries
ADD id INT PRIMARY KEY AUTO_INCREMENT;

SELECT AVG(salary) AS average_salary
FROM nj_state_teachers_salaries.salaries;

SELECT COUNT(*) AS salaries_more_than_150
FROM nj_state_teachers_salaries.salaries
WHERE salary > 150000;

SELECT last_name AS more_than_150_less_than_5
FROM nj_state_teachers_salaries.salaries
WHERE salary > 150000
AND experience_total < 5;


SELECT MAX(salary) AS highest_preschool_salary
FROM nj_state_teachers_salaries.salaries
WHERE primary_job = 'Preschool';

SELECT MAX(salary) AS highest_school_counselor_salary
FROM nj_state_teachers_salaries.salaries
WHERE primary_job = 'School Counselor';

SELECT MAX(salary) AS highest_school_principal_salary
FROM nj_state_teachers_salaries.salaries
WHERE primary_job LIKE '%principal%';

SELECT MAX(salary) AS highest_school_psychologist_salary
FROM nj_state_teachers_salaries.salaries
WHERE primary_job = 'School Psychologist';

SELECT MAX(salary) AS highest_school_kindergarten_salary
FROM nj_state_teachers_salaries.salaries
WHERE primary_job = 'Kindergarten';

SELECT last_name, first_name, salary
FROM nj_state_teachers_salaries.salaries
WHERE district = 'Atlantic City'
ORDER BY salary ASC
LIMIT 1;

SELECT COUNT(*) AS total_employees
FROM nj_state_teachers_salaries.salaries
WHERE district = 'Passaic City'
AND experience_total > 10;




