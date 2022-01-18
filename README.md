# text_handler

<sub><b>Purpose:</b> Imagine product descriptions are as below, I built a text handler to transform them into a desired format that imporves customer experiences</sub>

<sub><b>inputs = </b><br/>
           ['outer: 25% Nylon, 75% Cotton; inner: 10% Cotton, 90% Wool', <br/>
           'inner: 10% Cotton, 90% Wool; outer: 90% Cotton, 10% Leather',<br/>
           'outer: 10% Viscose, 90% Cotton; base: 100% Cotton',<br/>
           'outer: 25% Nylon, 75% Cotton; inner: 10% Cotton, 90% Wool; base: 10% Cotton, 90% Wool',<br/>
           'base: 10% Cotton, 90% Wool; outer: 25% Nylon, 75% Cotton; inner: 10% Cotton, 90% Wool']<br/></sub>

<sub><b>TASK 1</b>: handling layers seperately -> solution: regular expression<br/>
<b>TASK 2</b>: make percentages in descending order -> solution: data structure -> dict<br/>


<sub><b>outputs = </b><br/>
outer: 75% Cotton, 25% Nylon; inner: 90% Wool, 10% Cotton<br/>
inner: 90% Wool, 10% Cotton; outer: 90% Cotton, 10% Leather<br/>
outer: 90% Cotton, 10% Viscose; base: 100% Cotton<br/>
outer: 75% Cotton, 25% Nylon; inner: 90% Wool, 10% Cotton; base: 90% Wool, 10% Cotton<br/>
base: 90% Wool, 10% Cotton; outer: 75% Cotton, 25% Nylon; inner: 90% Wool, 10% Cotton<br/></sub>
