--****PLEASE ENTER YOUR DETAILS BELOW****
--T3-rm-dm.sql

--Student ID:32684673 
--Student Name:Kang Hong Bo  
--Unit Code: FIT 3171
--Applied Class No: 5

/* Comments for your marker:




*/

--3(a)
DROP SEQUENCE competitor_seq;

DROP SEQUENCE team_seq;

CREATE SEQUENCE competitor_seq START WITH 100 INCREMENT BY 1;

CREATE SEQUENCE team_seq START WITH 100 INCREMENT BY 1;

--3(b)
INSERT INTO emercontact (
     ec_phone,
     ec_fname,
     ec_lname
) VALUES (
     '0476541234',
     'Jack',
     'Kai'
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
     competitor_seq.NEXTVAL,
     'Daniel',
     'Kai',
     'M',
     TO_DATE('23/MAY/1999', 'DD/MON/YYYY'),
     'dkai0017@student.monash.edu',
     'Y',
     '0433255678',
     'F',
     '0476541234'
);

INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     (
          SELECT
               event_id
          FROM
               event
          WHERE
                    carn_date = (
                         SELECT
                              carn_date
                         FROM
                              carnival
                         WHERE
                              upper(carn_name) = upper('RM Autumn Series Caulfield 2022')
                    )
               AND eventtype_code = (
                    SELECT
                         eventtype_code
                    FROM
                         eventtype
                    WHERE
                         upper(eventtype_desc) = upper('21.1 Km Half Marathon')
               )
     ),
     (select count(*)+1
          FROM
               entry
          WHERE 
          event_id=(
          SELECT
               event_id
          FROM
               event
          WHERE
                    carn_date = (
                         SELECT
                              carn_date
                         FROM
                              carnival
                         WHERE
                              upper(carn_name) = upper('RM Autumn Series Caulfield 2022')
                    )
               AND eventtype_code = (
                    SELECT
                         eventtype_code
                    FROM
                         eventtype
                    WHERE
                         upper(eventtype_desc) = upper('21.1 Km Half Marathon')))),
     NULL,
     NULL,
     competitor_seq.CURRVAL,
     NULL,
     (
          SELECT
               char_id
          FROM
               charity
          WHERE
               upper(char_name) = upper('Beyond Blue')
     )
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
     competitor_seq.NEXTVAL,
     'Annabelle',
     'Kai',
     'F',
     TO_DATE('23/MAY/1999', 'DD/MON/YYYY'),
     'akai0037@student.monash.edu',
     'Y',
     '0433259876',
     'F',
     '0476541234'
);

INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     (
          SELECT
               event_id
          FROM
               event
          WHERE
                    carn_date = (
                         SELECT
                              carn_date
                         FROM
                              carnival
                         WHERE
                              upper(carn_name) = upper('RM Autumn Series Caulfield 2022')
                    )
               AND eventtype_code = (
                    SELECT
                         eventtype_code
                    FROM
                         eventtype
                    WHERE
                         upper(eventtype_desc) = upper('21.1 Km Half Marathon')
               )
     ),
     (select count(*)+1
          FROM
               entry
          WHERE 
          event_id=(
          SELECT
               event_id
          FROM
               event
          WHERE
                    carn_date = (
                         SELECT
                              carn_date
                         FROM
                              carnival
                         WHERE
                              upper(carn_name) = upper('RM Autumn Series Caulfield 2022')
                    )
               AND eventtype_code = (
                    SELECT
                         eventtype_code
                    FROM
                         eventtype
                    WHERE
                         upper(eventtype_desc) = upper('21.1 Km Half Marathon')))),
         
     NULL,
     NULL,
     competitor_seq.CURRVAL,
     NULL,
     (
          SELECT
               char_id
          FROM
               charity
          WHERE
               upper(char_name) = upper('Amnesty Internationa')
     )
);
commit;
--3(c)
ALTER TABLE team DISABLE CONSTRAINT entry_team_fk;
ALTER TABLE entry DISABLE CONSTRAINT team_entry_fk;
update entry set team_id= (team_seq.nextval) where 
          comp_no=(select comp_no from competitor where
          upper(comp_fname)=upper('Annabelle') and upper(comp_lname)=upper('Kai'));
INSERT INTO team (
     team_id,
     team_name,
     carn_date,
     team_no_members,
     event_id,
     entry_no,
     char_id
)Values(
     team_seq.currval,
     'Kai Speedstars',
     (SELECT
                                        carn_date
                                   FROM
                                        carnival
                                   WHERE
                                        upper(carn_name) = upper('RM Autumn Series Caulfield 2022')),
     (select count(*) from entry where team_id=(select team_id from team where upper(team_name)=upper('Kai Speedstars')))+1,
     (
          SELECT
               event_id
          FROM
               event
          WHERE
                    carn_date = (
                         SELECT
                              carn_date
                         FROM
                              carnival
                         WHERE
                              upper(carn_name) = upper('RM Autumn Series Caulfield 2022')
                    )
               AND eventtype_code = (
                    SELECT
                         eventtype_code
                    FROM
                         eventtype
                    WHERE
                         upper(eventtype_desc) = upper('21.1 Km Half Marathon')
               )
     ),
     (Select
          entry_no
          from entry
          where
          comp_no=(select comp_no from competitor where
          upper(comp_fname)=upper('Annabelle') and upper(comp_lname)=upper('Kai'))),
     (
          SELECT
               char_id
          FROM
               charity
          WHERE
               upper(char_name) = upper('Beyond Blue')
     ));
     
ALTER TABLE team ENABLE CONSTRAINT entry_team_fk;
ALTER TABLE entry ENABLE CONSTRAINT team_entry_fk;
commit;
--3(d
delete entry where comp_no=(select comp_no from competitor where
          upper(comp_fname)=upper('Daniel') and upper(comp_lname)=upper('Kai'))
          and event_id=(
          SELECT
               event_id
          FROM
               event
          WHERE
                    carn_date = (
                         SELECT
                              carn_date
                         FROM
                              carnival
                         WHERE
                              upper(carn_name) = upper('RM Autumn Series Caulfield 2022')
                    )
               AND eventtype_code = (
                    SELECT
                         eventtype_code
                    FROM
                         eventtype
                    WHERE
                         upper(eventtype_desc) = upper('21.1 Km Half Marathon')));

INSERT INTO entry (
     event_id,
     entry_no,
     entry_starttime,
     entry_finishtime,
     comp_no,
     team_id,
     char_id
) VALUES (
     (
          SELECT
               event_id
          FROM
               event
          WHERE
                    carn_date = (
                         SELECT
                              carn_date
                         FROM
                              carnival
                         WHERE
                              upper(carn_name) = upper('RM Autumn Series Caulfield 2022')
                    )
               AND eventtype_code = (
                    SELECT
                         eventtype_code
                    FROM
                         eventtype
                    WHERE
                         upper(eventtype_desc) = upper('10 Km Run')
               )
     ),
     (select count(*)+1
          FROM
               entry
          WHERE 
          event_id=(
          SELECT
               event_id
          FROM
               event
          WHERE
                    carn_date = (
                         SELECT
                              carn_date
                         FROM
                              carnival
                         WHERE
                              upper(carn_name) = upper('RM Autumn Series Caulfield 2022')
                    )
               AND eventtype_code = (
                    SELECT
                         eventtype_code
                    FROM
                         eventtype
                    WHERE
                         upper(eventtype_desc) = upper('10 Km Run')))),
     NULL,
     NULL,
     (select comp_no from competitor where
          upper(comp_fname)=upper('Daniel') and upper(comp_lname)=upper('Kai')),
     (select team_id from team where upper(team_name)=upper('Kai Speedstars')),
     (
          SELECT
               char_id
          FROM
               charity
          WHERE
               upper(char_name) = upper('Beyond Blue')
     )
);

update team set team_no_members=(select count(*) from entry where team_id=(select team_id from team where upper(team_name)=upper('Kai Speedstars'))) where upper(team_name)=upper('Kai Speedstars');
commit;

--3(e)
delete entry where comp_no=(select comp_no from competitor where
          upper(comp_fname)=upper('Daniel') and upper(comp_lname)=upper('Kai'))
          and event_id=(
          SELECT
               event_id
          FROM
               event
          WHERE
                    carn_date = (
                         SELECT
                              carn_date
                         FROM
                              carnival
                         WHERE
                              upper(carn_name) = upper('RM Autumn Series Caulfield 2022')
                    )
               AND eventtype_code = (
                    SELECT
                         eventtype_code
                    FROM
                         eventtype
                    WHERE
                         upper(eventtype_desc) = upper('10 Km Run')));


update team set team_no_members=(select count(*) from entry where team_id=(select team_id from team where upper(team_name)=upper('Kai Speedstars'))) where upper(team_name)=upper('Kai Speedstars');

update entry set team_id =null where comp_no=(select comp_no from competitor where
          upper(comp_fname)=upper('Annabelle') and upper(comp_lname)=upper('Kai'));

update entry set char_id=(
          SELECT
               char_id
          FROM
               charity
          WHERE
               upper(char_name) = upper('Beyond Blue')
     )where comp_no=(select comp_no from competitor where
          upper(comp_fname)=upper('Annabelle') and upper(comp_lname)=upper('Kai')) ;
     
delete team where upper(team_name)=upper('Kai Speedstars');

commit;
