# Check the tables
# ------------------------------------------------------------------------
SHOW DATABASES;
USE gdn_db;
SHOW TABLES;

SELECT * FROM author LIMIT 10;
SELECT * FROM authortype;

SELECT * FROM question;
SELECT * FROM questiontype;

SELECT * FROM responsetype;
SELECT * FROM form;
SELECT * FROM respsurveyeco LIMIT 10;

SELECT * FROM geo LIMIT 10;
SELECT * FROM tmp_contribution LIMIT 10;
SELECT * FROM tmp_survey LIMIT 10;
SELECT * FROM tmp_zipcode LIMIT 10;

# The various queries used by the dashboard
# ------------------------------------------------------------------------
# Q1- Pensez-vous que vos actions en faveur de l'environnement peuvent 
# vous permettre de faire des économies ?
# ------------------------------------------------------------------------
# 1- Get response to the question 1 : Global
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr1) 
        AS reponse 
	FROM respSurveyEco AS rs 
	GROUP BY id_sr1 
    ORDER BY id_sr1;

# 2- Get response to the question 1 : na
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr1) 
        AS reponse 
	FROM respSurveyEco AS rs 
	WHERE id_authorType = 1 
	GROUP BY id_sr1 
    ORDER BY id_sr1;

# 3- Get response to the question 1 : citizen
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
		AS rt 
		WHERE rt.id = rs.id_sr1) 
		AS reponse 
	FROM respSurveyEco AS rs 
	WHERE id_authorType = 2 
	GROUP BY id_sr1 
    ORDER BY id_sr1;

# 4- Get response to the question 1 : Elected official and institution
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
		AS rt 
		WHERE rt.id = rs.id_sr1) 
		AS reponse 
	FROM respSurveyEco AS rs 
	WHERE id_authorType = 3 
	GROUP BY id_sr1 
    ORDER BY id_sr1;

# 5- Get response to the question 1 : for-profit organization
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
		AS rt 
		WHERE rt.id = rs.id_sr1) 
		AS reponse 
	FROM respSurveyEco AS rs 
	WHERE id_authorType = 4 
	GROUP BY id_sr1 
    ORDER BY id_sr1;

# 6- Get response to the question 1 : non-profit organization
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
		AS rt 
		WHERE rt.id = rs.id_sr1) 
		AS reponse 
	FROM respSurveyEco AS rs 
	WHERE id_authorType = 5 
	GROUP BY id_sr1 
    ORDER BY id_sr1;

# ------------------------------------------------------------------------
# Q2- Diriez-vous que vous connaissez les aides et dispositifs qui sont 
# aujourd'hui proposés par l'Etat, les collectivités, les entreprises et 
# les associations pour l'isolation et le chauffage des logements, 
# et pour les déplacements ?
# ------------------------------------------------------------------------
# 7- Get responses to the question 2 : Global
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt
		WHERE rt.id = rs.id_sr2) 
        AS reponse 
	FROM respSurveyEco AS rs 
	GROUP BY id_sr2 
    ORDER BY id_sr2;

# 8- Get response to the question 2 : na
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr2) 
        AS reponse 
	FROM respSurveyEco AS rs 
	WHERE id_authorType = 1 
	GROUP BY id_sr2 
    ORDER BY id_sr2;

# 9- Get response to the question 2 : citizen
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr2) 
        AS reponse 
	FROM respSurveyEco AS rs 
	WHERE id_authorType = 2 
	GROUP BY id_sr2 
    ORDER BY id_sr2;

# 10- Get response to the question 2 : Elected official and institution
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr2) 
        AS reponse 
	FROM respSurveyEco AS rs 
	WHERE id_authorType = 3 
	GROUP BY id_sr2 
    ORDER BY id_sr2;

# 11- Get response to the question 2 : for-profit organization
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr2) 
        AS reponse 
	FROM respSurveyEco AS rs 
	WHERE id_authorType = 4 
	GROUP BY id_sr2 
    ORDER BY id_sr2;
    
# 12- Get response to the question 2 : non-profit organization 
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr2) 
        AS reponse 
	FROM respSurveyEco AS rs 
	WHERE id_authorType = 5 
	GROUP BY id_sr2 
    ORDER BY id_sr2;
    
# ------------------------------------------------------------------------
# Q3- Pensez-vous que les taxes sur le diesel et sur l’essence peuvent 
# permettre de modifier les comportements des utilisateurs ?
# ------------------------------------------------------------------------    
# 13- Get responses to the question 3 : Global
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr3) 
        AS reponse 
	FROM respSurveyEco AS rs 
	GROUP BY id_sr3 
	ORDER BY id_sr3;

# 14- Get response to the question 3 : na
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr3) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 1
	GROUP BY id_sr3 
	ORDER BY id_sr3;

# 15- Get response to the question 3 : citizen
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr3) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 2
	GROUP BY id_sr3 
	ORDER BY id_sr3;

# 16- Get response to the question 3 : Elected official and institution
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr3) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 3
	GROUP BY id_sr3 
	ORDER BY id_sr3;    

# 17- Get response to the question 3 : for-profit organization
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr3) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 4
	GROUP BY id_sr3 
	ORDER BY id_sr3;

# 18- Get response to the question 3 : non-profit organization    
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr3) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 5
	GROUP BY id_sr3 
	ORDER BY id_sr3;

# ------------------------------------------------------------------------
# Q4- À quoi les recettes liées aux taxes sur le diesel et l’essence 
# doivent-elles avant tout servir ?
# ------------------------------------------------------------------------
# 19- Get responses to the question 4 : Global  
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr4) 
        AS reponse 
	FROM respSurveyEco AS rs 
	GROUP BY id_sr4 
	ORDER BY id_sr4;

# 20- Get response to the question 4 : na
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr4) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 1
	GROUP BY id_sr4 
	ORDER BY id_sr4;

# 21- Get response to the question 4 : citizen
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr4) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 2
	GROUP BY id_sr4 
	ORDER BY id_sr4;

# 22- Get response to the question 4 : Elected official and institution
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr4) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 3
	GROUP BY id_sr4 
	ORDER BY id_sr4;
        
# 23- Get response to the question 4 : for-profit organization
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr4) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 4
	GROUP BY id_sr4 
	ORDER BY id_sr4;

# 24- Get response to the question 4 : non-profit organization
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr4) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 5
	GROUP BY id_sr4 
	ORDER BY id_sr4;

# ------------------------------------------------------------------------
# Q5- Selon vous, la transition écologique doit être avant tout financée :
# ------------------------------------------------------------------------
# 25- Get responses to the question 5 : Global
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr5) 
        AS reponse 
	FROM respSurveyEco AS rs
	GROUP BY id_sr5 
	ORDER BY id_sr5;

# 26- Get response to the question 5 : na
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr5) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 1
	GROUP BY id_sr5 
	ORDER BY id_sr5;

# 27- Get response to the question 5 : citizen
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr5) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 2
	GROUP BY id_sr5 
	ORDER BY id_sr5;

# 28- Get response to the question 5 : Elected official and institution
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr5) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 3
	GROUP BY id_sr5 
	ORDER BY id_sr5;

# 29- Get response to the question 5 : for-profit organization
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr5) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 4
	GROUP BY id_sr5 
	ORDER BY id_sr5;

# 30- Get response to the question 5 : non-profit organization
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr5) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 5
	GROUP BY id_sr5 
	ORDER BY id_sr5;

# ------------------------------------------------------------------------
# Q6- Et qui doit être en priorité concerné par le financement de la 
# transition écologique ?
# ------------------------------------------------------------------------
# 31- Get responses to the question 6 : Global
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr6) 
        AS reponse 
	FROM respSurveyEco AS rs
	GROUP BY id_sr6 
	ORDER BY nb DESC;

# 32- Get response to the question 6 : na
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr6) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 1
	GROUP BY id_sr6 
	ORDER BY nb DESC;

# 33- Get response to the question 6 : citizen
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr6) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 2
	GROUP BY id_sr6 
	ORDER BY nb DESC;

# 34- Get response to the question 6 : Elected official and institution
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr6) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 3
	GROUP BY id_sr6 
	ORDER BY nb DESC;

# 35- Get response to the question 6 : for-profit organization
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr6) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 4
	GROUP BY id_sr6 
	ORDER BY nb DESC;

# 36- Get response to the question 6 : non-profit organization
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr6) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 5
	GROUP BY id_sr6 
	ORDER BY nb DESC;

# ------------------------------------------------------------------------
# Q7- Que faudrait-il faire pour protéger la biodiversité et le climat 
# tout en maintenant des activités agricoles et industrielles compétitives 
# par rapport à leurs concurrents étrangers, notamment européens ?
# ------------------------------------------------------------------------
# 37- Get responses to the question 7 : Global
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr7) 
        AS reponse 
	FROM respSurveyEco AS rs
	GROUP BY id_sr7 
	ORDER BY id_sr7;

# 38- Get response to the question 7 : na
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr7) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 1
	GROUP BY id_sr7 
	ORDER BY id_sr7;

# 39- Get response to the question 7 : citizen
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr7) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 2
	GROUP BY id_sr7 
	ORDER BY id_sr7;

# 40- Get response to the question 7 : Elected official and institution
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr7) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 3
	GROUP BY id_sr7 
	ORDER BY id_sr7;

# 41- Get response to the question 7 : for-profit organization
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr7) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 4
	GROUP BY id_sr7 
	ORDER BY id_sr7;

# 42- Get response to the question 7 : non-profit organization
SELECT count(*) AS nb, 
	(SELECT label 
		FROM responseType 
        AS rt 
		WHERE rt.id = rs.id_sr7) 
        AS reponse 
	FROM respSurveyEco AS rs
	WHERE id_authorType = 5
	GROUP BY id_sr7 
	ORDER BY id_sr7;

# ------------------------------------------------------------------------
# Q8- Time
# ------------------------------------------------------------------------
# 43- Get number of contribution as a function of time
SELECT `date`, COUNT(*) AS nb 
	FROM respSurveyEco 
	GROUP BY `date` 
	ORDER BY `date`;

# ------------------------------------------------------------------------
# Q9- Not present in the dashboard
# ------------------------------------------------------------------------
# 44- Get the number of each type of author who responded to the survey
SELECT count(*) AS nb, 
	(SELECT label 
		FROM authorType 
        AS aut 
		WHERE aut.id = rs.id_authorType) 
        AS reponse 
	FROM respSurveyEco AS rs
	GROUP BY id_authorType 
	ORDER BY nb DESC;
