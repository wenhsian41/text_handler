# text_handler

inputs are as below<br/><br/>
inputs = <br/>
           ['outer: 25% Nylon, 75% Cotton; inner: 10% Cotton, 90% Wool', <br/>
           'inner: 10% Cotton, 90% Wool; outer: 90% Cotton, 10% Leather',<br/>
           'outer: 10% Viscose, 90% Cotton; base: 100% Cotton',<br/>
           'outer: 25% Nylon, 75% Cotton; inner: 10% Cotton, 90% Wool; base: 10% Cotton, 90% Wool',<br/>
           'base: 10% Cotton, 90% Wool; outer: 25% Nylon, 75% Cotton; inner: 10% Cotton, 90% Wool']<br/>

TASK 1: handling layers seperately -> solution: regular expression<br/>
TASK 2: make percentages in descending order -> solution: data structure -> dict<br/>


desired final output
outer: 75% Cotton, 25% Nylon; inner: 90% Wool, 10% Cotton
inner: 90% Wool, 10% Cotton; outer: 90% Cotton, 10% Leather
outer: 90% Cotton, 10% Viscose; base: 100% Cotton
outer: 75% Cotton, 25% Nylon; inner: 90% Wool, 10% Cotton; base: 90% Wool, 10% Cotton
base: 90% Wool, 10% Cotton; outer: 75% Cotton, 25% Nylon; inner: 90% Wool, 10% Cotton
