--****PLEASE ENTER YOUR DETAILS BELOW****
--T4-rm-alter.sql

--Student ID:32684673
--Student Name:Kang Hong Bo
--Unit Code:FIT 3171
--Applied Class No:5

/* Comments for your marker:




*/

--4(a)
--select (entry_finishtime-entry_starttime)*24*60 as entry_elapsedtime from entry ;
     
Alter table entry add (entry_elapsedtime number(5,2) default 0);
COMMENT ON COLUMN entry.entry_elapsedtime IS
     'The total time recorded for a run';
update entry set entry_elapsedtime=(entry_finishtime-entry_starttime)*24*60;
commit;
--4(b)

drop table charityraised CASCADE CONSTRAINTS;
drop table official CASCADE CONSTRAINTS;
create table charityraised(
     team_id         NUMBER(3) NOT NULL,
     charityraised_id number(3) not null,
     char_id  NUMBER(3) NOT NULL,
     carn_date       DATE NOT NULL,
     charityraised_percent number (3) not null
     );
COMMENT ON COLUMN charityraised.team_id IS
     'Team identifier (unique)';     
COMMENT ON COLUMN charityraised.charityraised_id IS
     'Charity Raised recorded identifier';
COMMENT ON COLUMN charityraised.char_id IS
     'Charity unique identifier';
COMMENT ON COLUMN charityraised.carn_date IS
     'Date of carnival (unique identifier)';
COMMENT ON COLUMN charityraised.charityraised_percent IS
     'Percentage donated for cetain charity';
ALTER TABLE charityraised ADD CONSTRAINT charityraised_pk PRIMARY KEY ( team_id ,charityraised_id);

ALTER TABLE charityraised
     ADD CONSTRAINT team_charityraised_fk FOREIGN KEY ( team_id )
          REFERENCES team (team_id);
ALTER TABLE charityraised
     ADD CONSTRAINT charity_charityraised_fk FOREIGN KEY ( char_id )
          REFERENCES charity ( char_id );
ALTER TABLE charityraised
     ADD CONSTRAINT carnival_charityraised_fk FOREIGN KEY ( carn_date )
          REFERENCES carnival ( carn_date);
insert into charityraised (
     team_id         ,
     charityraised_id  ,
     char_id  ,
     carn_date       ,
     charityraised_percent 
     )Values(4,1,1, TO_DATE('01/OCT/2021', 'DD/MON/YYYY'),50);
insert into charityraised (
     team_id         ,
     charityraised_id  ,
     char_id  ,
     carn_date       ,
     charityraised_percent 
     )Values(4,2,3, TO_DATE('01/OCT/2021', 'DD/MON/YYYY'),50);     
select * from charityraised;


--4(c)

create table official (
     off_id number(3) not null,
     comp_no  NUMBER(5) NOT NULL,
     carn_date DATE NOT NULL,
     off_role varchar(20) not null
);
COMMENT ON COLUMN official.off_id IS
     'Official identifier';
COMMENT ON COLUMN official.comp_no IS
     'Unique identifier for a competitor';  
COMMENT ON COLUMN official.carn_date IS
     'Date of carnival (unique identifier)'; 
COMMENT ON COLUMN official.off_role IS
     'Official role';


ALTER TABLE official ADD CONSTRAINT official_pk PRIMARY KEY ( off_id ,carn_date);

ALTER TABLE official
     ADD CONSTRAINT competitor_official_fk FOREIGN KEY ( comp_no )
          REFERENCES competitor ( comp_no);
ALTER TABLE official
     ADD CONSTRAINT carnival_official_fk FOREIGN KEY (carn_date )
          REFERENCES carnival ( carn_date);

