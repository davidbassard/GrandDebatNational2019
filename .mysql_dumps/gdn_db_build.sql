# Foreword:
# The building of the database is carried out in 39 steps, numbered from 1 to 39
# Warning, before to executing all SQL queries: 
# - download the 3 csv files, named here survey_raw.csv, contribution_raw.csv and zipcode_raw.csv.
# - Check the path of each csv file in steps 13, 14 and 15

# Create the database "gdn_db"
# --------------------------------------------------------------
CREATE DATABASE IF NOT EXISTS gdn_db DEFAULT CHARSET = UTF8MB4;

# Create the various temporary tables
# --------------------------------------------------------------
# 1- tmp_survey
CREATE TABLE IF NOT EXISTS tmp_survey (
	id VARCHAR(255),
    createdAt VARCHAR(255),
    publishedAt VARCHAR(255),
    updatedAt VARCHAR(255),
    authorId VARCHAR(255),
    authorType VARCHAR(255),
    authorZipCode VARCHAR(255),
    sr1 VARCHAR(255),
    sr2 VARCHAR(255),
    sr3 VARCHAR(255),
    sr4 VARCHAR(255),
    sr5 VARCHAR(255),
    sr6 VARCHAR(255),
    sr7 VARCHAR(255)
    ) 
    ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

# 2- tmp_contribution
CREATE TABLE IF NOT EXISTS tmp_contribution (
	reference VARCHAR(255),
    title VARCHAR(255),
    createdAt VARCHAR(255),
    publishedAt VARCHAR(255),
    updatedAt VARCHAR(255),
    trashed VARCHAR(255),
    trashedStatus VARCHAR(255),
    authorId VARCHAR(255),
    authorType VARCHAR(255),
    authorZipCode VARCHAR(255),
    cr1 TEXT,
    cr2 TEXT,
    cr3 TEXT,
    cr4 TEXT,
    cr5 TEXT,
    cr6 TEXT,
    cr7 TEXT,
    cr8 TEXT,
    cr9 TEXT,
    cr10 TEXT,
    cr11 TEXT,
    cr12 TEXT,
    cr13 TEXT,
    cr14 TEXT,
    cr15 TEXT,
    cr16 MEDIUMTEXT
    ) 
    ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

# 3- tmp_zipcode
CREATE TABLE IF NOT EXISTS tmp_zipcode (
	inseeCode VARCHAR(255),
    cityName VARCHAR(255),
    zipCode VARCHAR(255),
    routingLabel VARCHAR(255),
    line5 VARCHAR(255),
    gps VARCHAR(255)
    )
    ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

# Create the various tables
# --------------------------------------------------------------
# 4- author
CREATE TABLE IF NOT EXISTS author (
	id MEDIUMINT UNSIGNED AUTO_INCREMENT,
	authorId VARCHAR(255) UNIQUE NOT NULL DEFAULT '',
	authorType VARCHAR(255) NOT NULL DEFAULT '',
	tmp_authorZipCode VARCHAR(255) NOT NULL DEFAULT '',
	PRIMARY KEY (id)
	) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

# 5- authorType
CREATE TABLE IF NOT EXISTS authorType (
	id TINYINT UNSIGNED AUTO_INCREMENT,
	label VARCHAR(255) UNIQUE NOT NULL DEFAULT '',
	PRIMARY KEY (id)
	) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

# 6- question
CREATE TABLE IF NOT EXISTS question (
	id TINYINT UNSIGNED AUTO_INCREMENT,
	label VARCHAR(255) UNIQUE NOT NULL DEFAULT '',
	id_questionType TINYINT UNSIGNED NOT NULL DEFAULT 0,
	id_form TINYINT UNSIGNED NOT NULL DEFAULT 0,
	PRIMARY KEY (id)
	) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

# 7- questionType
CREATE TABLE IF NOT EXISTS questionType (
	id TINYINT UNSIGNED AUTO_INCREMENT,
	label VARCHAR(255) UNIQUE NOT NULL DEFAULT '',
	PRIMARY KEY (id)
	) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

# 8- form
CREATE TABLE IF NOT EXISTS form (
	id TINYINT UNSIGNED AUTO_INCREMENT,
	label VARCHAR(255) UNIQUE NOT NULL DEFAULT '',
	PRIMARY KEY (id)
	) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

# 9- geo
CREATE TABLE IF NOT EXISTS geo (
	id SMALLINT UNSIGNED AUTO_INCREMENT,
	cityName VARCHAR(255) NOT NULL DEFAULT '',
	zipCode VARCHAR(255) NOT NULL DEFAULT '',
	gps VARCHAR(255) NOT NULL DEFAULT '',
	PRIMARY KEY (id)
	) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;
    
# 10- responseType
CREATE TABLE IF NOT EXISTS responseType (
	id SMALLINT UNSIGNED AUTO_INCREMENT,
	label VARCHAR(255) NOT NULL DEFAULT '',
	id_question TINYINT UNSIGNED NOT NULL DEFAULT 0,
	id_questionType TINYINT UNSIGNED NOT NULL DEFAULT 0,
	id_form TINYINT UNSIGNED NOT NULL DEFAULT 0,
	PRIMARY KEY (id)
	) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

# 11- respSurveyEco
CREATE TABLE IF NOT EXISTS respSurveyEco (
	id MEDIUMINT UNSIGNED AUTO_INCREMENT,
	authorId VARCHAR(255) UNIQUE NOT NULL DEFAULT '',
	authorType VARCHAR(255) NOT NULL DEFAULT '',
	date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	sr1 VARCHAR(255) NOT NULL DEFAULT '',
	sr2 VARCHAR(255) NOT NULL DEFAULT '',
	sr3 VARCHAR(255) NOT NULL DEFAULT '',
	sr4 VARCHAR(255) NOT NULL DEFAULT '',
	sr5 VARCHAR(255) NOT NULL DEFAULT '',
	sr6 VARCHAR(255) NOT NULL DEFAULT '',
	sr7 VARCHAR(255) NOT NULL DEFAULT '',
	PRIMARY KEY (id)
	) ENGINE = InnoDB DEFAULT CHARSET = UTF8MB4;

# Loading data into the temporary tables
# --------------------------------------------------------------
# 12- Set the gobal variable 'local_infile' from 'OFF' to "ON"
SHOW GLOBAL VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = ON;

# 13- tmp_survey
START TRANSACTION;
LOAD DATA LOCAL INFILE './survey_raw.csv'
	INTO TABLE tmp_survey
    CHARACTER SET UTF8MB4
    FIELDS TERMINATED BY ','
		OPTIONALLY ENCLOSED BY '\"'
	LINES TERMINATED BY '\n'
    IGNORE 1 LINES;
COMMIT;

# 14- tmp_contribution
START TRANSACTION;
LOAD DATA LOCAL INFILE './contribution_raw.csv'
	INTO TABLE tmp_contribution
    CHARACTER SET UTF8MB4
    FIELDS TERMINATED BY ','
		OPTIONALLY ENCLOSED BY '\"'
	LINES TERMINATED BY '\n'
    IGNORE 1 LINES;
COMMIT;

# 15- tmp_zipcode
START TRANSACTION;
LOAD DATA LOCAL INFILE './zipcode_raw.csv'
	INTO TABLE tmp_zipcode
    CHARACTER SET UTF8MB4
    FIELDS TERMINATED BY ','
		OPTIONALLY ENCLOSED BY '\"'
	LINES TERMINATED BY '\n'
    IGNORE 1 LINES;
COMMIT;

# 16- Set the gobal variable 'local_infile' from 'ON' to "OFF"
SET GLOBAL local_infile = OFF;
SHOW GLOBAL VARIABLES LIKE 'local_infile';

# Structure the final database
# --------------------------------------------------------------
# 17- Insert authorId, authorType, authorZipCode into table author from tmp_survey
START TRANSACTION;
INSERT INTO `author` (`authorId`, `authorType`, `tmp_authorZipCode`)
	SELECT `authorId`, `authorType`, `authorZipCode`
		FROM `tmp_survey`;
COMMIT;

# 18- In author table, replace the empty entries with 'Non Renseigné' in the authorType column
START TRANSACTION;
UPDATE `author`
	SET `authorType` = 'Non renseigné'
	WHERE `authorType` = '';
COMMIT;

# 19- Insert publishedAt, sr1, sr2, sr3, sr4, sr5, sr6, sr7 
# into table respSurveyEco from tmp_survey
START TRANSACTION;
INSERT INTO `respSurveyEco` (`authorId`, `authorType`, `date`, `sr1`, `sr2`, `sr3`, `sr4`, `sr5`, `sr6`, `sr7`)
	SELECT `authorId`, `authorType`, `publishedAt`, `sr1`, `sr2`, `sr3`, `sr4`, `sr5`, `sr6`, `sr7`
		FROM `tmp_survey`;
COMMIT;

# 20- Insert cityName, zipCode, gps into table geo from table tmp_zipcode
START TRANSACTION;
INSERT INTO `geo` (`cityName`, `zipCode`, `gps`)
	SELECT `cityName`, `zipCode`, `gps`
		FROM `tmp_zipcode`;
COMMIT;

# 21- Insert label into table authorType
START TRANSACTION;
INSERT INTO `authorType` (`label`) 
	VALUES ('Non renseigné'),
		('Citoyen / Citoyenne'),
		('Élu / élue et Institution'),
		('Organisation à but lucratif'),
		('Organisation à but non lucratif');
COMMIT;

# 22- Insert label into table form
START TRANSACTION;
INSERT INTO `form` (`label`) 
	VALUES ('Survey: ecological transition'),
        ('Contribution: ecological transition'),
        ('Survey: taxation and public expenditure'),
        ('Contribution: taxation and public expenditure'),
        ('Survey: democracy and citizenship'),
        ('Contribution: democracy and citizenship'),
        ('Survey: the organization of the State and public services'),
        ('Contribution: the organization of the State and public services');
COMMIT;

# 23- Insert label into table questionType
START TRANSACTION;
INSERT INTO `questionType` (`label`) 
	VALUES ('Closed-ended question'),
        ('Multiple-choice question'),
        ('Open-ended question');
COMMIT;

# 24- Insert label into table question and 
# id_questionType, id_form (FOREIGN KEY)
START TRANSACTION;
INSERT INTO `question` (`label`, `id_questionType`, `id_form`)
	VALUES ("Pensez-vous que vos actions en faveur de l'environnement peuvent vous permettre de faire des économies ?", "1", "1"),
        ("Diriez-vous que vous connaissez les aides et dispositifs qui sont aujourd'hui proposés par l'Etat, les collectivités, les entreprises et les associations pour l'isolation et le chauffage des logements, et pour les déplacements ?", "1", "1"),
        ("Pensez-vous que les taxes sur le diesel et sur l’essence peuvent permettre de modifier les comportements des utilisateurs ?", "1", "1"),
        ("À quoi les recettes liées aux taxes sur le diesel et l’essence doivent-elles avant tout servir ?", "2", "1"),
        ("Selon vous, la transition écologique doit être avant tout financée par :", "2", "1"),
        ("Et qui doit être en priorité concerné par le financement de la transition écologique ?", "2", "1"),
        ("Que faudrait-il faire pour protéger la biodiversité et le climat tout en maintenant des activités agricoles et industrielles compétitives par rapport à leurs concurrents étrangers, notamment européens ?", "2", "1");
COMMIT;

# 25- Insert label into table responseType and 
# id_question, id_questionType, id_form (FOREIGN KEY)
START TRANSACTION;
INSERT INTO `responseType` (`label`, `id_question`, `id_questionType`, `id_form`) 
	VALUES ("Sans avis", "1", "1", "1"),
		("Oui", "1", "1", "1"),
        ("Non", "1", "1", "1"),
        ('Sans avis', "2", "1", "1"),
        ("Oui", "2", "1", "1"),
        ("Non", "2", "1", "1"),
        ("Sans avis", "3", "1", "1"),
        ("Oui", "3", "1", "1"),
        ("Non", "3", "1", "1"),
        ("Sans avis", "4", "2", "1"),
        ("À baisser d’autres impôts comme par exemple l’impôt sur le revenu ?", "4", "2", "1"),
        ("À financer des investissements en faveur du climat ?", "4", "2", "1"),
        ("À financer des aides pour accompagner les Français dans la transition écologique ?", "4", "2", "1"),
        ("Sans avis", "5", "2", "1"),
        ("Par le budget général de l’État", "5", "2", "1"),
        ("Par la fiscalité écologique", "5", "2", "1"),
        ("Les deux", "5", "2", "1"),
        ("Je ne sais pas", "5", "2", "1"),
        ("Sans avis", "6", "2", "1"),
        ("Les administrations", "6", "2", "1"),
        ("Les administrations|Les entreprises", "6", "2", "1"),
        ("Les administrations|Les entreprises|Les particuliers", "6", "2", "1"),
        ("Les administrations|Les entreprises|Les particuliers|Tout le monde", "6", "2", "1"),
        ("Les administrations|Les entreprises|Tout le monde", "6", "2", "1"),
        ("Les administrations|Les entreprises|Tout le monde|Les particuliers", "6", "2", "1"),
        ("Les administrations|Les particuliers", "6", "2", "1"),
        ("Les administrations|Les particuliers|Les entreprises", "6", "2", "1"),
        ("Les administrations|Les particuliers|Les entreprises|Tout le monde", "6", "2", "1"),
        ("Les administrations|Les particuliers|Tout le monde", "6", "2", "1"),
        ("Les administrations|Les particuliers|Tout le monde|Les entreprises", "6", "2", "1"),
        ("Les administrations|Tout le monde", "6", "2", "1"),
        ("Les administrations|Tout le monde|Les entreprises", "6", "2", "1"),
        ("Les administrations|Tout le monde|Les entreprises|Les particuliers", "6", "2", "1"),
        ("Les administrations|Tout le monde|Les particuliers", "6", "2", "1"),
        ("Les administrations|Tout le monde|Les particuliers|Les entreprises", "6", "2", "1"),
        ("Les entreprises", "6", "2", "1"),
        ("Les entreprises|Les administrations", "6", "2", "1"),
        ("Les entreprises|Les administrations|Les particuliers", "6", "2", "1"),
        ("Les entreprises|Les administrations|Les particuliers|Tout le monde", "6", "2", "1"),
        ("Les entreprises|Les administrations|Tout le monde", "6", "2", "1"),
        ("Les entreprises|Les administrations|Tout le monde|Les particuliers", "6", "2", "1"),
        ("Les entreprises|Les particuliers", "6", "2", "1"),
        ("Les entreprises|Les particuliers|Les administrations", "6", "2", "1"),
        ("Les entreprises|Les particuliers|Les administrations|Tout le monde", "6", "2", "1"),
        ("Les entreprises|Les particuliers|Tout le monde", "6", "2", "1"),
        ("Les entreprises|Les particuliers|Tout le monde|Les administrations", "6", "2", "1"),
        ("Les entreprises|Tout le monde", "6", "2", "1"),
        ("Les entreprises|Tout le monde|Les administrations", "6", "2", "1"),
        ("Les entreprises|Tout le monde|Les administrations|Les particuliers", "6", "2", "1"),
        ("Les entreprises|Tout le monde|Les particuliers", "6", "2", "1"),
        ("Les entreprises|Tout le monde|Les particuliers|Les administrations", "6", "2", "1"),
        ("Les particuliers", "6", "2", "1"),
        ("Les particuliers|Les administrations", "6", "2", "1"),
        ("Les particuliers|Les administrations|Les entreprises", "6", "2", "1"),
        ("Les particuliers|Les administrations|Les entreprises|Tout le monde", "6", "2", "1"),
        ("Les particuliers|Les administrations|Tout le monde", "6", "2", "1"),
        ("Les particuliers|Les administrations|Tout le monde|Les entreprises", "6", "2", "1"),
        ("Les particuliers|Les entreprises", "6", "2", "1"),
        ("Les particuliers|Les entreprises|Les administrations", "6", "2", "1"),
        ("Les particuliers|Les entreprises|Les administrations|Tout le monde", "6", "2", "1"),
        ("Les particuliers|Les entreprises|Tout le monde", "6", "2", "1"),
        ("Les particuliers|Les entreprises|Tout le monde|Les administrations", "6", "2", "1"),
        ("Les particuliers|Tout le monde", "6", "2", "1"),
        ("Les particuliers|Tout le monde|Les administrations", "6", "2", "1"),
        ("Les particuliers|Tout le monde|Les administrations|Les entreprises", "6", "2", "1"),
        ("Les particuliers|Tout le monde|Les entreprises", "6", "2", "1"),
        ("Les particuliers|Tout le monde|Les entreprises|Les administrations", "6", "2", "1"),
        ("Tout le monde", "6", "2", "1"),
        ("Tout le monde|Les administrations", "6", "2", "1"),
        ("Tout le monde|Les administrations|Les entreprises", "6", "2", "1"),
        ("Tout le monde|Les administrations|Les entreprises|Les particuliers", "6", "2", "1"),
        ("Tout le monde|Les administrations|Les particuliers", "6", "2", "1"),
        ("Tout le monde|Les administrations|Les particuliers|Les entreprises", "6", "2", "1"),
        ("Tout le monde|Les entreprises", "6", "2", "1"),
        ("Tout le monde|Les entreprises|Les administrations", "6", "2", "1"),
        ("Tout le monde|Les entreprises|Les administrations|Les particuliers", "6", "2", "1"),
        ("Tout le monde|Les entreprises|Les particuliers", "6", "2", "1"),
        ("Tout le monde|Les entreprises|Les particuliers|Les administrations", "6", "2", "1"),
        ("Tout le monde|Les particuliers", "6", "2", "1"),
        ("Tout le monde|Les particuliers|Les administrations", "6", "2", "1"),
        ("Tout le monde|Les particuliers|Les administrations|Les entreprises", "6", "2", "1"),
        ("Tout le monde|Les particuliers|Les entreprises", "6", "2", "1"),
        ("Tout le monde|Les particuliers|Les entreprises|Les administrations", "6", "2", "1"),
        ("Sans avis", "7", "2", "1"),
        ("Cofinancer un plan d’investissement pour changer les modes de production", "7", "2", "1"),
        ("Modifier les accords commerciaux", "7", "2", "1"),
        ("Taxer les produits importés qui dégradent l’environnement", "7", "2", "1");
COMMIT;

# 26- Add column id_author to table respSurveyEco and 
# update it with id of table author (FOREIGN KEY)
START TRANSACTION;
ALTER TABLE `respSurveyEco` 
	ADD COLUMN `id_author` 
    MEDIUMINT UNSIGNED DEFAULT 0 AFTER `id`;
UPDATE `author`, `respSurveyEco`
	SET `respSurveyEco`.`id_author` = `author`.`id`
	WHERE `author`.`authorId` = `respSurveyEco`.`authorId`;
ALTER TABLE `respSurveyEco` 
	DROP COLUMN `authorId`;
COMMIT;

# 27- Add column id_authorType to table respSurveyEco and 
# update it with id of table authorType (FOREIGN KEY)
START TRANSACTION;
ALTER TABLE `respSurveyEco` 
	ADD COLUMN `id_authorType` 
    TINYINT UNSIGNED DEFAULT 0 AFTER `id_author`;
UPDATE `authorType`, `respSurveyEco`
	SET `respSurveyEco`.`id_authorType` = `authorType`.`id`
	WHERE `authorType`.`label` = `respSurveyEco`.`authorType`;
UPDATE `respSurveyEco`
	SET `respSurveyEco`.`id_authorType`= 1 
	WHERE `respSurveyEco`.`id_authorType`= '';
ALTER TABLE `respSurveyEco` 
	DROP COLUMN `authorType`;
COMMIT;

# 28- Add id_sr1 column to respSurveyEco and 
# update it with id of table responseType (FOREIGN KEY)
START TRANSACTION;
ALTER TABLE `respSurveyEco` 
	ADD COLUMN `id_sr1` 
    SMALLINT UNSIGNED DEFAULT 0 AFTER `sr1`;
UPDATE `respSurveyEco`
	SET `respSurveyEco`.`id_sr1`= 1
	WHERE `respSurveyEco`.`sr1`= '';
UPDATE `respSurveyEco`
	SET `respSurveyEco`.`id_sr1`= 2
	WHERE `respSurveyEco`.`sr1`= 'Oui';
UPDATE `respSurveyEco`
	SET `respSurveyEco`.`id_sr1`= 3 
	WHERE `respSurveyEco`.`sr1`= 'Non';
ALTER TABLE `respSurveyEco` 
	DROP COLUMN `sr1`;
COMMIT;

# 29- Add id_sr2 column to respSurveyEco and 
# update it with id of table responseType (FOREIGN KEY)
START TRANSACTION;
ALTER TABLE `respSurveyEco` 
	ADD COLUMN `id_sr2` 
    SMALLINT UNSIGNED DEFAULT 0 AFTER `sr2`;
UPDATE `respSurveyEco`
	SET `respSurveyEco`.`id_sr2`= 4 
	WHERE `respSurveyEco`.`sr2`= '';
UPDATE `respSurveyEco`
	SET `respSurveyEco`.`id_sr2`= 5 
	WHERE `respSurveyEco`.`sr2`= 'Oui';
UPDATE `respSurveyEco`
	SET `respSurveyEco`.`id_sr2`= 6 
	WHERE `respSurveyEco`.`sr2`= 'Non';
ALTER TABLE `respSurveyEco` 
	DROP COLUMN `sr2`;
COMMIT;

# 30- Add id_sr3 column to respSurveyEco and 
# update it with id of table responseType (FOREIGN KEY)
START TRANSACTION;
ALTER TABLE `respSurveyEco` 
	ADD COLUMN `id_sr3` 
    SMALLINT UNSIGNED DEFAULT 0 AFTER `sr3`;
UPDATE `respSurveyEco`
	SET `respSurveyEco`.`id_sr3`= 7 
	WHERE `respSurveyEco`.`sr3`= '';
UPDATE `respSurveyEco`
	SET `respSurveyEco`.`id_sr3`= 8 
	WHERE `respSurveyEco`.`sr3`= 'Oui';
UPDATE `respSurveyEco`
	SET `respSurveyEco`.`id_sr3`= 9
	WHERE `respSurveyEco`.`sr3`= 'Non';
ALTER TABLE `respSurveyEco` 
	DROP COLUMN `sr3`;
COMMIT;

# 31- Add id_sr4 column to respSurveyEco and 
# update it with id of table responseType (FOREIGN KEY)
START TRANSACTION;
ALTER TABLE `respSurveyEco` 
	ADD COLUMN `id_sr4` 
    SMALLINT UNSIGNED DEFAULT 0 AFTER `sr4`;
UPDATE `responseType`, `respSurveyEco` 
	SET `respSurveyEco`.`id_sr4` = `responseType`.`id` 
	WHERE `responseType`.`label` = `respSurveyEco`.`sr4`;
UPDATE `respSurveyEco` 
	SET `respSurveyEco`.`id_sr4`= 10 
	WHERE `respSurveyEco`.`sr4`= '';
ALTER TABLE `respSurveyEco` 
	DROP COLUMN `sr4`;
COMMIT;

# 32- Add id_sr5 column to respSurveyEco and 
# update it with id of table responseType (FOREIGN KEY)
START TRANSACTION;
ALTER TABLE `respSurveyEco` 
	ADD COLUMN `id_sr5` 
    SMALLINT UNSIGNED DEFAULT 0 AFTER `sr5`;
UPDATE `responseType`, `respSurveyEco`
	SET `respSurveyEco`.`id_sr5` = `responseType`.`id`
	WHERE `responseType`.`label` = `respSurveyEco`.`sr5`;
UPDATE `respSurveyEco` 
	SET `respSurveyEco`.`id_sr5`= 14 
	WHERE `respSurveyEco`.`sr5`= '';
ALTER TABLE `respSurveyEco` 
	DROP COLUMN `sr5`;
COMMIT;

# 33- Add id_sr6 column to respSurveyEco and 
# update it with id of table responseType (FOREIGN KEY)
START TRANSACTION;
ALTER TABLE `respSurveyEco` 
	ADD COLUMN `id_sr6` 
    SMALLINT UNSIGNED DEFAULT 0 AFTER `sr6`;
UPDATE `responseType`, `respSurveyEco` 
	SET `respSurveyEco`.`id_sr6` = `responseType`.`id` 
	WHERE `responseType`.`label` = `respSurveyEco`.`sr6`;
UPDATE `respSurveyEco` 
	SET `respSurveyEco`.`id_sr6`= 19 
	WHERE `respSurveyEco`.`sr6` = '';
ALTER TABLE `respSurveyEco` 
	DROP COLUMN `sr6`;
COMMIT;

# 34- Add id_sr7 column to respSurveyEco and 
# update it with id of table responseType (FOREIGN KEY)
START TRANSACTION;
ALTER TABLE `respSurveyEco` 
	ADD COLUMN `id_sr7` 
    SMALLINT UNSIGNED DEFAULT 0 AFTER `sr7`;
UPDATE `responseType`, `respSurveyEco` 
	SET `respSurveyEco`.`id_sr7` = `responseType`.`id` 
	WHERE `responseType`.`label` = `respSurveyEco`.`sr7`;
UPDATE `respSurveyEco` 
	SET `respSurveyEco`.`id_sr7`= 84 
	WHERE `respSurveyEco`.`sr7` = '';
ALTER TABLE `respSurveyEco` 
	DROP COLUMN `sr7`;
COMMIT;

# 35- Add id_authorType column to author and 
# update it with id of table authorType (FOREIGN KEY)
START TRANSACTION;
ALTER TABLE `author` 
	ADD COLUMN `id_authorType` 
    TINYINT UNSIGNED DEFAULT 0 AFTER `authorId`;
UPDATE `authorType`, `author`
	SET `author`.`id_authorType` = `authorType`.`id`
	WHERE `authorType`.`label` = `author`.`authorType`;
ALTER TABLE `author` 
	DROP COLUMN `authorType`;
COMMIT;

# Add all foreign keys and indexes
# --------------------------------------------------------------
# 36- Add foreign key on the column id_authorType to the table author
START TRANSACTION;
ALTER TABLE `author`
	ADD CONSTRAINT `fk_authorType_author` 
    FOREIGN KEY (`id_authorType`) 
    REFERENCES `authorType` (`id`);
COMMIT;

# 37- Add foreign key on the column id_question, id_questionType and 
# id_form to the table responseType, and finally,
# an index fulltext on the column label
START TRANSACTION;
ALTER TABLE `responseType`
	ADD CONSTRAINT `fk_question_responseType` 
    FOREIGN KEY (`id_question`) 
    REFERENCES `question` (`id`);
ALTER TABLE `responseType`
	ADD CONSTRAINT `fk_questionType_responseType` 
	FOREIGN KEY (`id_questionType`) 
	REFERENCES `questionType` (`id`);
ALTER TABLE `responseType`
	ADD CONSTRAINT `fk_form_responseType`
    FOREIGN KEY (`id_form`) 
    REFERENCES `form` (`id`);
ALTER TABLE `responseType` 
	ADD FULLTEXT `idx_full_responseType` (`label`);
COMMIT;

# 38- Add foreign key on the column id_questionType, and 
# id_form to the table question, and finally,
# an index fulltext on the column label
START TRANSACTION;
ALTER TABLE `question`
	ADD CONSTRAINT `fk_questionType_question` 
	FOREIGN KEY (`id_questionType`) 
	REFERENCES `questionType` (`id`);
ALTER TABLE `question` 
	ADD CONSTRAINT `fk_form_question` 
    FOREIGN KEY (`id_form`) 
    REFERENCES `form` (`id`);
ALTER TABLE `question` 
	ADD FULLTEXT `idx_full_question` (`label`);
COMMIT;

# 39- Add foreign key on the column id_author, id_authorType, 
# id_sr1, id_sr2, id_sr3, id_sr4, isr5, id_sr 6 and id_sr7 to
# the table respSurveyEco
START TRANSACTION;
ALTER TABLE `respSurveyEco`
	ADD CONSTRAINT `fk_author_respSurveyEco` 
    FOREIGN KEY (`id_author`) 
    REFERENCES `author` (`id`);
ALTER TABLE `respSurveyEco`
	ADD CONSTRAINT `fk_authorType_respSurveyEco` 
    FOREIGN KEY (`id_authorType`) 
    REFERENCES `authorType` (`id`);
ALTER TABLE `respSurveyEco`
	ADD CONSTRAINT `fk_sr1_respSurveyEco` 
    FOREIGN KEY (`id_sr1`) 
    REFERENCES `responseType` (`id`);
ALTER TABLE `respSurveyEco`
	ADD CONSTRAINT `fk_sr2_respSurveyEco` 
    FOREIGN KEY (`id_sr2`) 
    REFERENCES `responseType` (`id`);
ALTER TABLE `respSurveyEco`
	ADD CONSTRAINT `fk_sr3_respSurveyEco` 
    FOREIGN KEY (`id_sr3`) 
    REFERENCES `responseType` (`id`);
ALTER TABLE `respSurveyEco`
	ADD CONSTRAINT `fk_sr4_respSurveyEco` 
    FOREIGN KEY (`id_sr4`) 
    REFERENCES `responseType` (`id`);
ALTER TABLE `respSurveyEco`
	ADD CONSTRAINT `fk_sr5_respSurveyEco` 
    FOREIGN KEY (`id_sr5`) 
    REFERENCES `responseType` (`id`);
ALTER TABLE `respSurveyEco`
	ADD CONSTRAINT `fk_sr6_respSurveyEco` 
    FOREIGN KEY (`id_sr6`) 
    REFERENCES `responseType` (`id`);
ALTER TABLE `respSurveyEco`
	ADD CONSTRAINT `fk_sr7_respSurveyEco` 
    FOREIGN KEY (`id_sr7`) 
    REFERENCES `responseType` (`id`);
COMMIT;
