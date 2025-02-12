response = """
<html>
<head><script>
    function read()
    {
        document.getElementById('readmore').style.display = 'block';
        document.getElementById('readless').style.display = 'none';
        document.getElementById('myDiv').style.display = 'none';
    }
    function loadXMLDoc(path)
    {
//alert(path);
        document.getElementById('readmore').style.display = 'none';
        document.getElementById('myDiv').style.display = 'block';
        var xmlhttp;
        if (window.XMLHttpRequest)
        {
            xmlhttp = new XMLHttpRequest();
        }
        else
        {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange = function ()
        {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
            {
                document.getElementById("myDiv").innerHTML = xmlhttp.responseText;
            }
        }
        xmlhttp.open("GET", path + "/blocks/academic_status/more.php", true);
        xmlhttp.send();
    }
</script>
</head><body><div style="width: 100%; margin: 10px 0; font-weight: bold; overflow: auto;color: #82152C;font-family: SourceSansPro-Semibold;"><div style="float: left;">BAIML-2022-A</div><div style="float: right;">Semester VI (06.01.25 to 26.04.25)</div></div><table class="generaltable" id="local_timetable_studentlayout" width="100%">
<thead>
<tr>
<th class="header c0" style="text-align:left;" scope="col">   </th>
<th class="header c1" style="text-align:left;width:10%;" scope="col">9:00-10:00</th>
<th class="header c2" style="text-align:left;width:10%;" scope="col">10:00-11:00</th>
<th class="header c3" style="text-align:left;width:10%;" scope="col">11:00-12:00</th>
<th class="header c4" style="text-align:left;width:10%;" scope="col">12:00-1:00</th>
<th class="header c5" style="text-align:left;width:10%;" scope="col">1:00-2:00</th>
<th class="header c6" style="text-align:left;width:10%;" scope="col">2:00-3:00</th>
<th class="header c7" style="text-align:left;width:10%;" scope="col">3:00-4:00</th>
<th class="header c8 lastcol" style="text-align:left;width:10%;" scope="col">4:00-5:00</th>
</tr>
</thead>
<tbody><tr class="">
<td class="cell c0" style="text-align:left;">Mon</td>
<td class="cell c1" style="text-align:left;width:10%;" colspan="0"><div id="837Mcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c2" style="text-align:left;width:10%;" colspan="0"><div id="837Mcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c3" style="text-align:left;width:10%;" colspan="0"><div id="837Mcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c4" style="text-align:left;width:10%;" colspan="0"><div id="837Mcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c5" style="text-align:left;width:10%;" colspan="1"><div id="6113Mcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Cryptography and Network Security</span>  </li><li><b>Inst:</b> Ganesh  Ingale </li>
            <li><b>Room:</b> 315 </li>
           </ul><div></div></div></td>
<td class="cell c6" style="text-align:left;width:10%;" colspan="1"><div id="6114Mcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Wireless Networking</span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 315 </li>
           </ul><div></div></div></td>
<td class="cell c7" style="text-align:left;width:10%;" colspan="1"><div id="6115Mcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Data Visualization</span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 404 </li>
           </ul><div></div></div></td>
<td class="cell c8 lastcol" style="text-align:left;width:10%;" colspan="0"><div id="837Mcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
</tr>
<tr class="">
<td class="cell c0" style="text-align:left;">Tue</td>
<td class="cell c1" style="text-align:left;width:10%;" colspan="0"><div id="837TUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c2" style="text-align:left;width:10%;" colspan="1"><div id="6110TUcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Advanced Machine Learning </span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 404 </li>
           </ul><div></div></div></td>
<td class="cell c3" style="text-align:left;width:10%;" colspan="0"><div id="837TUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c4" style="text-align:left;width:10%;" colspan="0"><div id="837TUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c5" style="text-align:left;width:10%;" colspan="0"><div id="837TUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c6" style="text-align:left;width:10%;" colspan="1"><div id="6114TUcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Wireless Networking</span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 302 </li>
           </ul><div></div></div></td>
<td class="cell c7" style="text-align:left;width:10%;" colspan="1"><div id="6115TUcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Cryptography and Network Security</span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 406 </li>
           </ul><div></div></div></td>
<td class="cell c8 lastcol" style="text-align:left;width:10%;" colspan="0"><div id="837TUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
</tr>
<tr class="">
<td class="cell c0" style="text-align:left;">Wed</td>
<td class="cell c1" style="text-align:left;width:10%;" colspan="0"><div id="837Wcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c2" style="text-align:left;width:10%;" colspan="1"><div id="6110Wcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Project Management</span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 314 </li>
           </ul><div></div></div></td>
<td class="cell c3" style="text-align:left;width:10%;" colspan="1"><div id="6111Wcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Cryptography and Network Security</span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 412-A </li>
           </ul><div></div></div></td>
<td class="cell c4" style="text-align:left;width:10%;" colspan="0"><div id="837Wcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c5" style="text-align:left;width:10%;" colspan="1"><div id="6113Wcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Big Data Analytics </span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 412-A </li>
           </ul><div></div></div></td>
<td class="cell c6" style="text-align:left;width:10%;" colspan="1"><div id="6114Wcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Wireless Networking</span>  </li><li><b>Inst:</b> </li>
            <li> </li>
           </ul><div></div></div></td>
<td class="cell c7" style="text-align:left;width:10%;" colspan="0"><div id="837Wcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c8 lastcol" style="text-align:left;width:10%;" colspan="0"><div id="837Wcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
</tr>
<tr class="">
<td class="cell c0" style="text-align:left;">Thu</td>
<td class="cell c1" style="text-align:left;width:10%;" colspan="1"><div id="6109THcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Big Data Analytics </span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 404 </li>
           </ul><div></div></div></td>
<td class="cell c2" style="text-align:left;width:10%;" colspan="1"><div id="6110THcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Data Visualization</span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 406 </li>
           </ul><div></div></div></td>
<td class="cell c3" style="text-align:left;width:10%;" colspan="1"><div id="6111THcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Project Management</span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 314 </li>
           </ul><div></div></div></td>
<td class="cell c4" style="text-align:left;width:10%;" colspan="0"><div id="837THcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c5" style="text-align:left;width:10%;" colspan="0"><div id="837THcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c6" style="text-align:left;width:10%;" colspan="0"><div id="837THcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c7" style="text-align:left;width:10%;" colspan="0"><div id="837THcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c8 lastcol" style="text-align:left;width:10%;" colspan="0"><div id="837THcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
</tr>
<tr class="">
<td class="cell c0" style="text-align:left;">Fri</td>
<td class="cell c1" style="text-align:left;width:10%;" colspan="0"><div id="837Fcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c2" style="text-align:left;width:10%;" colspan="1"><div id="6110Fcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Data Visualization</span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 412-A </li>
           </ul><div></div></div></td>
<td class="cell c3" style="text-align:left;width:10%;" colspan="1"><div id="6111Fcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Advanced Machine Learning </span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 412-A </li>
           </ul><div></div></div></td>
<td class="cell c4" style="text-align:left;width:10%;" colspan="0"><div id="837Fcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c5" style="text-align:left;width:10%;" colspan="1"><div id="6113Fcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Big Data Analytics </span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 412-B </li>
           </ul><div></div></div></td>
<td class="cell c6" style="text-align:left;width:10%;" colspan="1"><div id="6114Fcelldata"><ul class="local_timetable_studentcell" style="color:#353535;"><li><span style="font-size: 15px;color: #000;">Project Management</span>  </li><li><b>Inst:</b> </li>
            <li><b>Room:</b> 314 </li>
           </ul><div></div></div></td>
<td class="cell c7" style="text-align:left;width:10%;" colspan="0"><div id="837Fcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c8 lastcol" style="text-align:left;width:10%;" colspan="0"><div id="837Fcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
</tr>
<tr class="">
<td class="cell c0" style="text-align:left;">Sat</td>
<td class="cell c1" style="text-align:left;width:10%;" colspan="0"><div id="837SAcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c2" style="text-align:left;width:10%;" colspan="0"><div id="837SAcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c3" style="text-align:left;width:10%;" colspan="0"><div id="837SAcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c4" style="text-align:left;width:10%;" colspan="0"><div id="837SAcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c5" style="text-align:left;width:10%;" colspan="0"><div id="837SAcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c6" style="text-align:left;width:10%;" colspan="0"><div id="837SAcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c7" style="text-align:left;width:10%;" colspan="0"><div id="837SAcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c8 lastcol" style="text-align:left;width:10%;" colspan="0"><div id="837SAcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
</tr>
<tr class="lastrow">
<td class="cell c0" style="text-align:left;">Sun</td>
<td class="cell c1" style="text-align:left;width:10%;" colspan="0"><div id="837SUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c2" style="text-align:left;width:10%;" colspan="0"><div id="837SUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c3" style="text-align:left;width:10%;" colspan="0"><div id="837SUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c4" style="text-align:left;width:10%;" colspan="0"><div id="837SUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c5" style="text-align:left;width:10%;" colspan="0"><div id="837SUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c6" style="text-align:left;width:10%;" colspan="0"><div id="837SUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c7" style="text-align:left;width:10%;" colspan="0"><div id="837SUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
<td class="cell c8 lastcol" style="text-align:left;width:10%;" colspan="0"><div id="837SUcelldata"><ul class="local_timetable_celldata">
                        <li>      </li>
                        <li>       </li>
                        <li>       </li>
                        <li></li></ul><div></div></div></td>
</tr>
</tbody>
</table>
</body>
<html>
"""


from bs4 import BeautifulSoup, Tag
import json
soup = BeautifulSoup(response, 'lxml')

# table = soup.select('tbody')
# print(table)

days = soup.select('td') # selecting a table row


overall_timetable_data = {}
timetable = []
day_data = {}


class_data = [x.get_text() if x is not None else "" for x in soup.select_one('div').select('div')]
overall_timetable_data['class'] = class_data[0]
overall_timetable_data['semester'] = class_data[1]



def handle_subject(td : Tag, i : int):
    # Noob solution
    # time_map = {
    #     0: 9,
    #     1: 10,
    #     2: 11,
    #     3: 12,
    #     4: 1,
        
    # }
    
    # instead of a map, I used a pro gamer move ( i legit have nothing else to do bruh )
    def handle_time(i):
        time = (9 + i - 1) 
        if time > 12: 
            time = time - 12
        return time
    
    default_return = {
            "subject": "",
            "room": "",
            "start" : "",
            "end" : "",
        } 
    
    items = day.find_all("li")
    if items is None:
        return default_return

    
    return {
        "subject": items[0].get_text().strip(),
        "room": items[2].get_text().strip(),
        "start" : f"{handle_time(i)}:00",
        "end" : f"{handle_time(i+1)}:00"
    }
    
    
    

i = 0
temp_timetable = {}
temp_day_array = []
temp_day_name = ""
for day in days: 
    match i:
        case 0:
            # print("\nday : ", day.get_text(strip=True)) # <td class="cell c0" style="text-align:left;">Mon</td>
            temp_day_name = day.get_text(strip=True)
        
        case _ :
            data = handle_subject(day, i)
            # print(data)
            temp_day_array.append(data)
            # print(temp_day_array)
            
            
        
    if i == 8 : 
        # The entire day has been parsed
        # push the day's data into the overall timetable
        # print(temp_day_array)
        
        temp_timetable[temp_day_name] = temp_day_array
        
        # resetting the temp variables 
        temp_day_array = []
        temp_day_name = ""  
            
        
    i = (i + 1) % 9
    # break 

overall_timetable_data['timetable'] = temp_timetable

print(json.dumps(overall_timetable_data, indent=6))



