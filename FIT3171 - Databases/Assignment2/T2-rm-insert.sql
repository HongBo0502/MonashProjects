--****PLEASE ENTER YOUR DETAILS BELOW****
--T2-rm-insert.sql

--Student ID:32684673
--Student Name:Kang Hong Bo
--Unit Code:FIT3171
--Applied Class No:5

/* Comments for your marker:
We need to disable the foriegn key of team and entry to insert entries.


*/

-- Task 2 Load the EMERCONTACT, COMPETITOR, ENTRY and TEAM tables with your own
-- test data following the data requirements expressed in the brief

-- =======================================
-- EMERCONTACT
INSERT INTO emercontact (
     ec_phone,
     ec_fname,
     ec_lname
) VALUES (
     6019123456,
     NULL,
     NULL
);

INSERT INTO emercontact (
     ec_phone,
     ec_fname,
     ec_lname
) VALUES (
     6012333444,
     'Jeff',
     'Leong'
);

INSERT INTO emercontact (
     ec_phone,
     ec_fname,
     ec_lname
) VALUES (
     6017999222,
     'Jack',
     NULL
);

INSERT INTO emercontact (
     ec_phone,
     ec_fname,
     ec_lname
) VALUES (
     6013444444,
     NULL,
     'Ally'
);

INSERT INTO emercontact (
     ec_phone,
     ec_fname,
     ec_lname
) VALUES (
     6011222222,
     'Hong Bo',
     'Kang'
);

-- =======================================


-- =======================================
-- COMPETITOR
INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     1,
     'Yi Bin',
     'Sia',
     'M',
     TO_DATE('06/MAY/2002', 'DD/MON/YYYY'),
     'siayibin@gmail.com',
     'N',
     '6011888888',
     'P',
     '6013444444'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     2,
     'Wen Yu',
     'NG',
     'M',
     TO_DATE('29/JUL/2002', 'DD/MON/YYYY'),
     'ngwenyu@gmail.com',
     'N',
     '6011777777',
     'G',
     '6013444444'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     3,
     'Chen Xi',
     'Diong',
     'M',
     TO_DATE('08/JUL/2002', 'DD/MON/YYYY'),
     'cdio0004@student.monash.edu',
     'Y',
     '6018383070',
     'F',
     '6011222222'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     4,
     'Qian',
     'Wang',
     'F',
     TO_DATE('05/APR/2001', 'DD/MON/YYYY'),
     'qwan0066@student.monash.edu',
     'Y',
     '6017422919',
     'F',
     '6011222222'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     5,
     'Jeremy',
     'Yoon',
     'M',
     TO_DATE('14/OCT/2000', 'DD/MON/YYYY'),
     'jyoo0005@student.monash.edu',
     'Y',
     '6019882741',
     'F',
     '6011222222'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     6,
     'Audy',
     'Elegant',
     'M',
     TO_DATE('30/Jan/2001', 'DD/MON/YYYY'),
     'aele0002@student.monash.edu',
     'Y',
     '6014992048',
     'T',
     '6019123456'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     7,
     'Jun An',
     'Goi',
     'M',
     TO_DATE('22/MAR/2002', 'DD/MON/YYYY'),
     'jgoy0002@student.monash.edu',
     'Y',
     '6017722982',
     'F',
     '6019123456'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     8,
     'nursyarizan',
     'mohdakbar',
     'F',
     TO_DATE('21/NOV/1985', 'DD/MON/YYYY'),
     'nursyarizan.mohdakbar@monash.edu',
     'Y',
     '6014233456',
     'F',
     '6017999222'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     9,
     'gounoush',
     'abaei',
     'F',
     TO_DATE('08/DEC/1987', 'DD/MON/YYYY'),
     'golnoush.abaei@monash.edu',
     'Y',
     '6019887645',
     'F',
     '6017999222'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     10,
     'Weng Kee',
     'Tham',
     'M',
     TO_DATE('11/AUG/1968', 'DD/MON/YYYY'),
     'Tham.WengKee@monash.edu',
     'Y',
     '6016668886',
     'T',
     '6013444444'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     11,
     'Hui Xuan',
     'Tan',
     'F',
     TO_DATE('23/SEP/1992', 'DD/MON/YYYY'),
     'tan.huixuan@monash.edu',
     'Y',
     '6012881239',
     'T',
     '6012333444'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     12,
     'Foong Wei',
     'Wong',
     'F',
     TO_DATE('08/JAN/1986', 'DD/MON/YYYY'),
     'wong.foong.wei@monash.edu',
     'Y',
     '6015615432',
     'F',
     '6012333444'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     13,
     'Hong Qian',
     'Kang',
     'M',
     TO_DATE('12/FEB/2005', 'DD/MON/YYYY'),
     'kanghongqian212@gmail.com',
     'N',
     '6016716233',
     'G',
     '6011222222'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     14,
     'Hong Wei',
     'Kang',
     'M',
     TO_DATE('16/JUL/2006', 'DD/MON/YYYY'),
     'kanghongwei@gmail.com',
     'N',
     '6019776655',
     'G',
     '6011222222'
);

INSERT INTO competitor (
     comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) VALUES (
     15,
     'Jing Yi',
     'Tong',
     'F',
     TO_DATE('28/NOV/2002', 'DD/MON/YYYY'),
     'jton0001@student.monash.edu',
     'Y',
     '6016736512',
     'T',
     '6011222222'
);
-- =======================================



-- =======================================
-- ENTRY
ALTER TABLE entry DISABLE CONSTRAINT team_entry_fk;
--1 didnt attend
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     1,
     1,
     NULL,
     NULL,
     15,
     NULL,
     NULL
);
--2, 2 3 same team for event 1
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     1,
     2,
     TO_DATE('09:30:13', 'HH24:MI:SS'),
     TO_DATE('10:18:12', 'HH24:MI:SS'),
     1,
     1,
     3
);
--3
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     1,
     3,
     TO_DATE('09:30:05', 'HH24:MI:SS'),
     TO_DATE('10:23:52', 'HH24:MI:SS'),
     2,
     1,
     3
);
--4 5 6 same team for event 2 
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     2,
     1,
     TO_DATE('08:30:11', 'HH24:MI:SS'),
     TO_DATE('09:40:35', 'HH24:MI:SS'),
     3,
     2,
     1
);
--5
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     2,
     2,
     TO_DATE('08:30:12', 'HH24:MI:SS'),
     TO_DATE('09:53:50', 'HH24:MI:SS'),
     6,
     2,
     1
);
--6
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     2,
     3,
     NULL,
     NULL,
     7,
     2,
     1
);
--7
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     2,
     4,
     TO_DATE('08:30:01', 'HH24:MI:SS'),
     TO_DATE('10:03:12', 'HH24:MI:SS'),
     4,
     3,
     3
);
--8
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     2,
     5,
     TO_DATE('08:30:00', 'HH24:MI:SS'),
     TO_DATE('10:01:35', 'HH24:MI:SS'),
     5,
     3,
     3
);
--9
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     2,
     6,
     NULL,
     NULL,
     13,
     NULL,
     NULL
);
--10
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     2,
     7,
     TO_DATE('08:30:05', 'HH24:MI:SS'),
     TO_DATE('09:59:22', 'HH24:MI:SS'),
     14,
     NULL,
     NULL
);
--11
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     3,
     1,
     TO_DATE('09:00:05', 'HH24:MI:SS'),
     TO_DATE('09:28:19', 'HH24:MI:SS'),
     1,
     NULL,
     NULL
);
--12
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     3,
     2,
     TO_DATE('09:00:12', 'HH24:MI:SS'),
     TO_DATE('09:33:42', 'HH24:MI:SS'),
     13,
     4,
     NULL
);
--13
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     3,
     3,
     TO_DATE('09:00:10', 'HH24:MI:SS'),
     TO_DATE('09:43:26', 'HH24:MI:SS'),
     14,
     4,
     NULL
);
--14
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     5,
     1,
     TO_DATE('08:00:01', 'HH24:MI:SS'),
     TO_DATE('09:51:12', 'HH24:MI:SS'),
     1,
     5,
     3
);
--15
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     5,
     2,
     TO_DATE('08:00:02', 'HH24:MI:SS'),
     TO_DATE('10:11:29', 'HH24:MI:SS'),
     2,
     5,
     3
);
--16
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     5,
     3,
     TO_DATE('08:00:12', 'HH24:MI:SS'),
     TO_DATE('10:24:36', 'HH24:MI:SS'),
     11,
     NULL,
     1
);
--17
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     5,
     4,
     TO_DATE('08:00:14', 'HH24:MI:SS'),
     TO_DATE('10:33:41', 'HH24:MI:SS'),
     8,
     6,
     NULL
);
--18
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     5,
     5,
     TO_DATE('08:00:02', 'HH24:MI:SS'),
     TO_DATE('10:32:12', 'HH24:MI:SS'),
     9,
     6,
     NULL
);
--19
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     6,
     1,
     TO_DATE('08:30:01', 'HH24:MI:SS'),
     TO_DATE('08:44:34', 'HH24:MI:SS'),
     1,
     NULL,
     NULL
);
--20
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     6,
     2,
     TO_DATE('08:30:02', 'HH24:MI:SS'),
     TO_DATE('08:52:12', 'HH24:MI:SS'),
     2,
     NULL,
     NULL
);
--21
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     6,
     3,
     TO_DATE('08:30:05', 'HH24:MI:SS'),
     TO_DATE('08:49:24', 'HH24:MI:SS'),
     3,
     NULL,
     NULL
);
--22
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     6,
     4,
     TO_DATE('08:30:02', 'HH24:MI:SS'),
     TO_DATE('08:55:03', 'HH24:MI:SS'),
     11,
     NULL,
     2
);
--23
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     8,
     1,
     TO_DATE('08:00:06', 'HH24:MI:SS'),
     TO_DATE('09:23:33', 'HH24:MI:SS'),
     8,
     7,
     4
);
--24
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     8,
     2,
     TO_DATE('08:00:07', 'HH24:MI:SS'),
     TO_DATE('09:25:52', 'HH24:MI:SS'),
     9,
     7,
     4
);
--25
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     9,
     1,
     TO_DATE('08:00:01', 'HH24:MI:SS'),
     TO_DATE('10:06:22', 'HH24:MI:SS'),
     7,
     NULL,
     2
);
--26
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     9,
     2,
     TO_DATE('08:00:05', 'HH24:MI:SS'),
     TO_DATE('10:03:19', 'HH24:MI:SS'),
     13,
     NULL,
     NULL
);
--27
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     11,
     1,
     TO_DATE('07:45:05', 'HH24:MI:SS'),
     TO_DATE('11:53:02', 'HH24:MI:SS'),
     1,
     8,
     2
);
--28
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     11,
     2,
     TO_DATE('07:45:02', 'HH24:MI:SS'),
     TO_DATE('12:23:31', 'HH24:MI:SS'),
     2,
     8,
     2
);
--29
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     11,
     3,
     TO_DATE('07:45:01', 'HH24:MI:SS'),
     TO_DATE('14:05:44', 'HH24:MI:SS'),
     10,
     NULL,
     3
);
--30
INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     13,
     1,
     TO_DATE('08:00:01', 'HH24:MI:SS'),
     TO_DATE('9:43:52', 'HH24:MI:SS'),
     3,
     NULL,
     NULL
);
-- =======================================


-- =======================================
-- TEAM
ALTER TABLE team DISABLE CONSTRAINT entry_team_fk;

INSERT INTO team (
     team_id,
     team_name,
     carn_date,
     team_no_members,
     event_id,
     entry_no,
     char_id
) VALUES (
     1,
     'WUQINGCHONGFENG',
     TO_DATE('24/SEP/2021', 'DD/MON/YYYY'),
     2,
     1,
     1,
     3
);

INSERT INTO team (
     team_id,
     team_name,
     carn_date,
     team_no_members,
     event_id,
     entry_no,
     char_id
) VALUES (
     2,
     'TEAM FIT1008',
     TO_DATE('24/SEP/2021', 'DD/MON/YYYY'),
     3,
     2,
     1,
     1
);

INSERT INTO team (
     team_id,
     team_name,
     carn_date,
     team_no_members,
     event_id,
     entry_no,
     char_id
) VALUES (
     3,
     'Team FIT3171',
     TO_DATE('24/SEP/2021', 'DD/MON/YYYY'),
     2,
     2,
     4,
     3
);

INSERT INTO team (
     team_id,
     team_name,
     carn_date,
     team_no_members,
     event_id,
     entry_no,
     char_id
) VALUES (
     4,
     'Kang Family',
     TO_DATE('01/OCT/2021', 'DD/MON/YYYY'),
     2,
     3,
     2,
     NULL
);

INSERT INTO team (
     team_id,
     team_name,
     carn_date,
     team_no_members,
     event_id,
     entry_no,
     char_id
) VALUES (
     5,
     'WUQINGCHONGFENG',
     TO_DATE('01/OCT/2021', 'DD/MON/YYYY'),
     2,
     5,
     1,
     3
);

INSERT INTO team (
     team_id,
     team_name,
     carn_date,
     team_no_members,
     event_id,
     entry_no,
     char_id
) VALUES (
     6,
     'Team Prof',
     TO_DATE('01/OCT/2021', 'DD/MON/YYYY'),
     2,
     5,
     4,
     NULL
);

INSERT INTO team (
     team_id,
     team_name,
     carn_date,
     team_no_members,
     event_id,
     entry_no,
     char_id
) VALUES (
     7,
     'Team Prof',
     TO_DATE('05/FEB/2022', 'DD/MON/YYYY'),
     2,
     8,
     1,
     4
);

INSERT INTO team (
     team_id,
     team_name,
     carn_date,
     team_no_members,
     event_id,
     entry_no,
     char_id
) VALUES (
     8,
     'WUQINGCHONGFENG',
     TO_DATE('14/MAR/2022', 'DD/MON/YYYY'),
     2,
     11,
     1,
     2
);
-- =======================================
ALTER TABLE entry ENABLE CONSTRAINT team_entry_fk;

ALTER TABLE team ENABLE CONSTRAINT entry_team_fk;
commit;
