CREATE DATABASE USERS_1;
 USE USERS_1;
 CREATE TABLE USERS(USERS_ID INT PRIMARY KEY , NAME VARCHAR(50), AGE INT);
 CREATE TABLE TASKS(TASK_ID INT PRIMARY KEY ,USERS_ID INT , FOREIGN KEY(USERS_ID) REFERENCES USERS(USERS_ID),DIFFICULTY INT ,TIME_SPENT INT ,TIME_PRESSURE INT,TIMESTAMP DATETIME );
 CREATE TABLE BEHAVIOUR_LOGS(Log_ID INT PRIMARY KEY AUTO_INCREMENT,USERS_ID INT, FOREIGN KEY(USERS_ID) REFERENCES USERS(USERS_ID),FOCUS_SCORE INT,DISTRACTION_COUNT INT , ACTION_TYPE VARCHAR(50),TIMESTAMP DATETIME);
 CREATE TABLE AUDIT_LOGS(LOG_ID INT PRIMARY KEY AUTO_INCREMENT,USERS_ID INT , FOREIGN KEY(USERS_ID) REFERENCES USERS(USERS_ID), ACTION VARCHAR(100) , TIMESTAMP DATETIME);
 INSERT INTO USERS (USERS_ID, name, age) VALUES (1, 'Amit', 20), (2, 'Neha', 21), (3, 'Rahul', 22), (4, 'Sneha', 20), (5, 'Arjun', 23);
 INSERT INTO TASKS (task_id, USERS_ID, difficulty, time_spent, time_pressure, timestamp) VALUES -- Amit (Normal) 
 (1, 1, 4, 45, 3, '2026-03-30 10:00:00'), (2, 1, 5, 60, 4, '2026-03-31 11:00:00'), (3, 1, 6, 70, 5, '2026-04-01 09:30:00'),
 -- Neha (Increasing Stress)
 (4, 2, 6, 80, 6, '2026-03-30 09:00:00'), (5, 2, 7, 100, 7, '2026-03-31 10:30:00'), (6, 2, 9, 130, 9, '2026-04-01 11:30:00'),
 -- Rahul (Overloaded) 
 (7, 3, 9, 140, 9, '2026-03-30 08:30:00'), (8, 3, 10, 150, 10, '2026-03-31 09:30:00'), (9, 3, 9, 160, 10, '2026-04-01 10:30:00'), 
 -- Sneha (Moderate)
 (10, 4, 5, 60, 5, '2026-03-30 10:15:00'), (11, 4, 6, 75, 6, '2026-03-31 11:15:00'), (12, 4, 7, 85, 6, '2026-04-01 12:00:00'), 
 -- Arjun (High Pressure) 
 (13, 5, 6, 70, 8, '2026-03-30 09:45:00'), (14, 5, 7, 90, 9, '2026-03-31 10:45:00'), (15, 5, 8, 110, 9, '2026-04-01 11:45:00');
 INSERT INTO BEHAVIOUR_LOGS (USERS_ID, focus_score, distraction_count, action_type, timestamp) VALUES 
 -- Amit (Stable) 
 (1, 8, 1, 'study', '2026-03-30 10:00:00'), (1, 7, 2, 'study', '2026-03-31 10:00:00'), (1, 7, 2, 'study', '2026-04-01 10:00:00'),
 -- Neha (Declining focus) 
 (2, 7, 2, 'study', '2026-03-30 09:00:00'), (2, 5, 4, 'switch_task', '2026-03-31 09:30:00'), (2, 4, 6, 'distraction', '2026-04-01 10:00:00'),
 -- Rahul (Severe drift) 
 (3, 5, 5, 'switch_task', '2026-03-30 08:30:00'), (3, 3, 8, 'distraction', '2026-03-31 09:00:00'), (3, 2, 10, 'idle', '2026-04-01 09:30:00'),
 -- Sneha (Moderate)
 (4, 7, 2, 'study', '2026-03-30 10:15:00'), (4, 6, 3, 'study', '2026-03-31 11:15:00'), (4, 5, 4, 'switch_task', '2026-04-01 12:00:00'), 
 -- Arjun (Distraction rising) 
 (5, 6, 3, 'study', '2026-03-30 09:45:00'), (5, 5, 5, 'switch_task', '2026-03-31 10:45:00'), (5, 4, 7, 'distraction', '2026-04-01 11:45:00');
 INSERT INTO AUDIT_LOGS (USERS_ID, action, timestamp) VALUES 
 (1, 'Inserted task data', '2026-03-30 10:01:00'), (1, 'Inserted behavior log', '2026-03-30 10:02:00'),
 (2, 'Inserted task data', '2026-03-31 10:31:00'), (2, 'Inserted behavior log', '2026-03-31 09:31:00'), 
 (3, 'Inserted task data', '2026-03-31 09:31:00'), (3, 'Inserted behavior log', '2026-04-01 09:31:00'), 
 (4, 'Inserted task data', '2026-04-01 12:01:00'), (4, 'Inserted behavior log', '2026-04-01 12:01:30'), 
 (5, 'Inserted task data', '2026-04-01 11:46:00'), (5, 'Inserted behavior log', '2026-04-01 11:46:30');
INSERT INTO USERS(USERS_ID,NAME,AGE) VALUES(6,"Sheetal",18);
INSERT INTO TASKS(USERS_ID, DIFFICULTY, TIME_SPENT, TIME_PRESSURE, TIMESTAMP)
VALUES (6, 8, 120, 9, NOW());
ALTER TABLE TASKS
ADD CONSTRAINT CHK_DIFFICULTY
CHECK(DIFFICULTY BETWEEN 1 AND 10);
ALTER TABLE TASKS
ADD CONSTRAINT CHK_TIME_PRESSURE
CHECK(TIME_PRESSURE BETWEEN 1 AND 10);
ALTER TABLE BEHAVIOUR_LOGS
ADD CONSTRAINT CHK_FOCUS_SCORE
CHECK(FOCUS_SCORE BETWEEN 1 AND 10);
