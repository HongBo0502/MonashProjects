--****PLEASE ENTER YOUR DETAILS BELOW****
--T5-rm-alter.sql

--Student ID:
--Student Name:
--Unit Code:
--Applied Class No:

/* Comments for your marker:




*/

--5(a)


create or replace trigger add_entry_check 
before insert on entry 
for each row
declare 
var_comp_found number;
var_event_found number;

begin

select count(*) into var_event_found from entry where event_id in (select event_id from event where carn_date =(select carn_date from event where event_id=:new.event_id and comp_no=:new.comp_no)) ;
if (var_event_found != 0)then
    raise_application_error(-20111,'competitor must not enroll multiple events in the same carnival');
end if;
    
end;
/
-- Test Harness for 5(a) --
set echo on
-- Prior state
select * from entry;
-- Test trigger - insert entry with collision of carnival - failed ( event that competitor 7 enrolled 2 , 9 which will trigger if the insert event 1 , 6, 7, 8)
insert into entry
values(
     1,
     (select max(entry_no)from entry where event_id=1)+1,
     null,
     null,
     7,
     null,
     null,
     null
);
--post state
select * from entry;

--test 2 which do not coolide with the enrolled carnival
--Prior state
select * from entry;
--test trigger - insert entry with no collision of carnival - success 
insert into entry
values(
     10,
     (select count(*)+1
          FROM
               entry
          WHERE 
          event_id=10),
     null,
     null,
     7,
     null,
     null,
     null
);
--Post state
select * from entry;

rollback;
set echo off;
--5(b)
     
Alter table eventtype add (eventtype_record number(5,2) default null, eventtype_recordholder number(3) default null);
COMMENT ON COLUMN eventtype.eventtype_record IS
     'The fastest elapsed time for the event';
COMMENT ON COLUMN eventtype.eventtype_recordholder IS
     'The record holder of the elapsed time';



create or replace trigger records_for_event
before update of entry_finishtime on entry 
for each row

begin
     
     
     :new.entry_elapsedtime:=(:new.entry_finishtime-:new.entry_starttime)*24*60;
     
     if(:new.entry_elapsedtime< :old.entry_elapsedtime)then
     update eventtype set eventtype_record = :new.entry_elapsedtime where eventtype_code in(select eventtype_code from event where event_id=:new.event_id);
     update eventtype set eventtype_recordholder = :new.comp_no where eventtype_code in(select eventtype_code from event where event_id=:new.event_id);
     end if;                                           
end;
/
-- Test harness for 5(b)
set echo on 
--Initial data
select * from entry;
select * from eventtype;
--update exist data which dont have start and finish time (
update entry set entry_starttime=TO_DATE('09:30:13', 'HH24:MI:SS') where (event_id=1 and entry_no=1);
update entry set entry_finishtime = To_date('9:44:01','HH24:MI:SS') where (event_id=1 and entry_no=1);

--post state
select * from entry;
select * from eventtype;


select * from event;
--test 2
-- update exist data which dont have start time and finish time for diffenrent event
update entry set entry_starttime= TO_DATE('08:30:05', 'HH24:MI:SS') where (event_id=2 and entry_no=3);
update entry set entry_finishtime = To_date('9:14:01','HH24:MI:SS') where (event_id=2 and entry_no=3);

--post state
select * from entry;
select * from eventtype;

--test 3
--update the event same as above which will not change the records
update entry set entry_starttime= TO_DATE('08:30:01', 'HH24:MI:SS') where (event_id=2 and entry_no=6);
update entry set entry_finishtime = To_date('10:04:01','HH24:MI:SS') where (event_id=2 and entry_no=6);


--post state
select * from entry;
select * from eventtype;

rollback;
set echo off;


--5(c)
CREATE OR REPLACE PROCEDURE event_registration (
     in_comp_no in number,
     in_carn_date in date,
     in_eventtype_desc in varchar2,
     in_team_name in varchar2 default null,
     out_message out varchar2
     )as var_carn_date_found number;
          var_eventtype_desc_found number;
          var_team_name_found number;
begin
     select count (*) into var_carn_date_found from carnival where carn_date=in_carn_date;
     select count (*) into var_eventtype_desc_found from eventtype where upper(eventtype_desc)=upper(in_eventtype_desc);
     select count (*) into var_team_name_found from team where upper(team_name) = upper (in_team_name) and event_id=(select event_id from event where eventtype_code=(select eventtype_code from eventtype where upper(eventtype_desc)=upper(in_eventtype_desc) )and carn_date=in_carn_date );
     
     if (var_carn_date_found = 0 or var_eventtype_desc_found=0) then
     out_message := 'The carn_date or eventtype description is not valid';
     else if (in_team_name is not null)then
          if (var_team_name_found = 0) then
              
               insert into entry(event_id,entry_no,entry_starttime,entry_finishtime,comp_no,team_id,char_id) 
               values((select event_id from event where eventtype_code=(select eventtype_code from eventtype where upper(eventtype_desc)=upper(in_eventtype_desc) )and carn_date=in_carn_date ),(select count(*)+1 from entry  where event_id =(select event_id from event where eventtype_code=(select eventtype_code from eventtype where upper(eventtype_desc)=upper(in_eventtype_desc))and carn_date=in_carn_date)),null,null,in_comp_no,null,null);
               insert into team(team_id,team_name,carn_date,team_no_members,event_id,entry_no,char_id) 
               values(team_seq.nextval,in_team_name,in_carn_date,1,(select event_id from event where eventtype_code=(select eventtype_code from eventtype where upper(eventtype_desc)=upper(in_eventtype_desc))and carn_date=in_carn_date),(select entry_no from entry where  event_id=(select event_id from event where eventtype_code=(select eventtype_code from eventtype where upper(eventtype_desc)=upper(in_eventtype_desc))and carn_date=in_carn_date)and comp_no=in_comp_no),null);
               update entry set team_id=team_seq.currval where event_id=(select event_id from event where eventtype_code=(select eventtype_code from eventtype where upper(eventtype_desc)=upper(in_eventtype_desc) )and carn_date=in_carn_date )and comp_no=in_comp_no;
               out_message := 'The reistration for entry and team succeed';
         else 
               insert into entry(event_id,entry_no,entry_starttime,entry_finishtime,comp_no,team_id,char_id)
               values((select event_id from event where eventtype_code=(select eventtype_code from eventtype where upper(eventtype_desc)=upper(in_eventtype_desc) )and carn_date=in_carn_date),(select count(*)+1 from entry  where event_id =(select event_id from event where eventtype_code=(select eventtype_code from eventtype where upper(eventtype_desc)=upper(in_eventtype_desc))and carn_date=in_carn_date)),null,null,in_comp_no,(select team_id from team where upper(team_name)=upper(in_team_name) and event_id=(select event_id from event where eventtype_code=(select eventtype_code from eventtype where upper(eventtype_desc)=upper(in_eventtype_desc) )and carn_date=in_carn_date)),null);
               update team set team_no_members= team_no_members +1  where upper(team_name) = upper (in_team_name);
               out_message := 'The reistration for entry succed and the team was updated';
          end if;
          
     else
          insert into entry(event_id,entry_no,entry_starttime,entry_finishtime,comp_no,team_id,char_id) 
          values((select event_id from event where eventtype_code=(select eventtype_code from eventtype where upper(eventtype_desc)=upper(in_eventtype_desc)) and carn_date=in_carn_date),(select count(*)+1 from entry  where event_id =(select event_id from event where eventtype_code=(select eventtype_code from eventtype where upper(eventtype_desc)=upper(in_eventtype_desc))and carn_date=in_carn_date)),null,null,in_comp_no,null,null);
          out_message := 'The registration for entry succeed';
     end if;
     end if;
end event_registration ;
/
-- Test Harness for 5(c)
set echo on

insert into competitor(comp_no,
     comp_fname,
     comp_lname,
     comp_gender,
     comp_dob,
     comp_email,
     comp_unistatus,
     comp_phone,
     comp_ec_relationship,
     ec_phone
) values (competitor_seq.nextval,'Hong Ze','Kang','M',TO_DATE('22/Jun/1999', 'DD/MON/YYYY'),'kanghongze622@gmail.com','N','6016772344','P','6011222222');
set serveroutput on;
 Declare output varchar2(200);
begin

event_registration(competitor_seq.currval,TO_DATE('24/SEP/2021', 'DD/MON/YYYY'),'5 Km Run','Kang Family',output);

dbms_output.put_line(output);
end;
/
--post state
select * from team;
select * from entry;



-- test for none team name 
 Declare output varchar2(200);
begin

event_registration(competitor_seq.currval,TO_DATE('1/OCT/2021', 'DD/MON/YYYY'),'21.1 Km Half Marathon',null,output);

dbms_output.put_line(output);
end;
/
--post state
select * from team;
select * from entry;
-- test for not valid 
Declare output varchar2(200);
begin

event_registration(competitor_seq.currval,TO_DATE('10/OCT/2021', 'DD/MON/YYYY'),'21.1 Km Half Marathon','Kang Family',output);

dbms_output.put_line(output);
end;
/
--post state
select * from team;
select * from entry;
-- test if the comp is entering the team instead creating a new one
Declare output varchar2(200);
begin

event_registration(competitor_seq.currval,TO_DATE('14/MAR/2022', 'DD/MON/YYYY'),'42.2 Km Marathon','WUQINGCHONGFENG',output);

dbms_output.put_line(output);
end;
/
--post state
select * from team;
select * from entry;



rollback;
set echo off