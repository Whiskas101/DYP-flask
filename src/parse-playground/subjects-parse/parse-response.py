


response="""
<script>
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
<div
    style="width: 100%; margin: 10px 0; font-weight: bold; overflow: auto;color: #82152C;font-family: SourceSansPro-Semibold;">
    <div style="float: left;">BAIML-2022-A</div>
    <div style="float: right;">Semester IV (08.01.24 to 30.04.24)</div>
</div>
<h4 class="mycl-hdr"><span class="mycl-icon mystats-icon"></span>My Stats</h4>
<div class="progress_container">
    <div class="progress_row progress">
        <div class="progress-radial-container">
            <div class="progress-radial progress-80 setsize" id="aggregateattcircle">
                <div class="overlay setsize">
                    <p class="circular_value">
                        80<span id="overall_attendancepercent"> %</span><span class ="circlesubtext">Overall Attendance</span>
                    </p>
                </div>
            </div>
        </div>
        <div class="progress-radial-container">
            <div class="progress-radial progress-100 setsize" id="totalactiveclassescircle">
                <div class="overlay setsize">
                    <p class="circular_value">5<span class ="circlesubtext">Enrolled</br>Classes</span></p>
                </div>
            </div>
        </div>
        <div class="progress-radial-container">
            <div class="progress-radial progress-100 setsize" id="marketplacecircle">
                <a class="nav-to-mtp" href="https://mydy.dypatil.edu/rait/local/dypmarket/index.php" target="_blank">
                    <div class="overlay setsize">
                        <p class="circular_value">0<span class ="circlesubtext">Items</br>Uploaded</span></p>
                    </div>
                </a>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript">
    $( document ).ready(function() {
                            $(".setsize").each(function() {
                                $(this).height($(this).width());
                            });
                        });
                        $(window).on('resize', function(){
                            $(".setsize").each(function() {
                                $(this).height($(this).width());
                            });
                        });
</script>
<h4 class="mycl-hdr"><span class="mycl-icon mycls-icon"></span>My Classes</h4>
<table class="generaltable" id="tbl-subject">
    <thead>
        <tr>
            <th class="header c0" style="" scope="col"></th>
            <th class="header c1 lastcol" style="" scope="col"></th>
        </tr>
    </thead>
    <tbody>
        <tr class="">
            <td class="cell c0" style="">
                <div class="subjectcontainer;">
                    <div class="imgcontainer"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/block_academic_status/1709815567/subject1" alt="Semester Pic" class="subject-img" />
                    </div>
                    <div class="subcontent-container">
                        <h4 class="cfullname text-center cmn-label">Programming with Python</h4>
                        <div class="istruinfocontainer"><span class="instrinfosub cmn-label">Instructor : </span>
                            <div>Uttam Waghmode</div>
                        </div>
                        <div class="attendance-container">
                            <span class="attendance-label cmn-label">Attendance : </span>
                            <div class="prg-container">
                                <div class="progress" id="linearprogress">
                                    <div id="prog-bar-cont">
                                        <div id="prog-bar">
                                            <div id="background">
                                                <span class="prgbg" style = "width: 96%"></span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <span class="attendance-total">96%</span>
                            </div>
                        </div>
                        <div class="launchbtncontainer text-right"><a
                                href="https://mydy.dypatil.edu/rait/course/view.php?id=5922" target="_blank"
                                class="launchbutton">Launch</a></div>
                    </div>
                </div>
            </td>
            <td class="cell c1 lastcol" style="">
                <div class="subjectcontainer;">
                    <div class="imgcontainer"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/block_academic_status/1709815567/subject2" alt="Semester Pic" class="subject-img" />
                    </div>
                    <div class="subcontent-container">
                        <h4 class="cfullname text-center cmn-label">Operating System</h4>
                        <div class="istruinfocontainer"><span class="instrinfosub cmn-label">Instructor : </span>
                            <div>Priya Mule</div>
                        </div>
                        <div class="attendance-container">
                            <span class="attendance-label cmn-label">Attendance : </span>
                            <div class="prg-container">
                                <div class="progress" id="linearprogress">
                                    <div id="prog-bar-cont">
                                        <div id="prog-bar">
                                            <div id="background">
                                                <span class="prgbg" style = "width: 81.48%"></span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <span class="attendance-total">81.48%</span>
                            </div>
                        </div>
                        <div class="launchbtncontainer text-right"><a
                                href="https://mydy.dypatil.edu/rait/course/view.php?id=5921" target="_blank"
                                class="launchbutton">Launch</a></div>
                    </div>
                </div>
            </td>
        </tr>
        <tr class="">
            <td class="cell c0" style="">
                <div class="subjectcontainer;">
                    <div class="imgcontainer"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/block_academic_status/1709815567/subject3" alt="Semester Pic" class="subject-img" />
                    </div>
                    <div class="subcontent-container">
                        <h4 class="cfullname text-center cmn-label">Software Engineering</h4>
                        <div class="istruinfocontainer"><span class="instrinfosub cmn-label">Instructor : </span>
                            <div>Somnath Tandale</div>
                        </div>
                        <div class="attendance-container">
                            <span class="attendance-label cmn-label">Attendance : </span>
                            <div class="prg-container">
                                <div class="progress" id="linearprogress">
                                    <div id="prog-bar-cont">
                                        <div id="prog-bar">
                                            <div id="background">
                                                <span class="prgbg" style = "width: 56.52%"></span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <span class="attendance-total">56.52%</span>
                            </div>
                        </div>
                        <div class="launchbtncontainer text-right"><a
                                href="https://mydy.dypatil.edu/rait/course/view.php?id=5920" target="_blank"
                                class="launchbutton">Launch</a></div>
                    </div>
                </div>
            </td>
            <td class="cell c1 lastcol" style="">
                <div class="subjectcontainer;">
                    <div class="imgcontainer"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/block_academic_status/1709815567/subject4" alt="Semester Pic" class="subject-img" />
                    </div>
                    <div class="subcontent-container">
                        <h4 class="cfullname text-center cmn-label">Artificial Intelligence</h4>
                        <div class="istruinfocontainer"><span class="instrinfosub cmn-label">Instructor : </span>
                            <div>Poonam Gadage</div>
                        </div>
                        <div class="attendance-container">
                            <span class="attendance-label cmn-label">Attendance : </span>
                            <div class="prg-container">
                                <div class="progress" id="linearprogress">
                                    <div id="prog-bar-cont">
                                        <div id="prog-bar">
                                            <div id="background">
                                                <span class="prgbg" style = "width: 84.62%"></span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <span class="attendance-total">84.62%</span>
                            </div>
                        </div>
                        <div class="launchbtncontainer text-right"><a
                                href="https://mydy.dypatil.edu/rait/course/view.php?id=5919" target="_blank"
                                class="launchbutton">Launch</a></div>
                    </div>
                </div>
            </td>
        </tr>
        <tr class="lastrow">
            <td class="cell c0" style="">
                <div class="subjectcontainer;">
                    <div class="imgcontainer"><img src="https://mydy.dypatil.edu/rait/theme/image.php/essential/block_academic_status/1709815567/subject5" alt="Semester Pic" class="subject-img" />
                    </div>
                    <div class="subcontent-container">
                        <h4 class="cfullname text-center cmn-label">Formal Language Automata Language</h4>
                        <div class="istruinfocontainer"><span class="instrinfosub cmn-label">Instructor : </span>
                            <div>Shital Mali</div>
                        </div>
                        <div class="attendance-container">
                            <span class="attendance-label cmn-label">Attendance : </span>
                            <div class="prg-container">
                                <div class="progress" id="linearprogress">
                                    <div id="prog-bar-cont">
                                        <div id="prog-bar">
                                            <div id="background">
                                                <span class="prgbg" style = "width: 78.13%"></span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <span class="attendance-total">78.13%</span>
                            </div>
                        </div>
                        <div class="launchbtncontainer text-right"><a
                                href="https://mydy.dypatil.edu/rait/course/view.php?id=5923" target="_blank"
                                class="launchbutton">Launch</a></div>
                    </div>
                </div>
            </td>
            <td class="cell c1 lastcol" style=""> </td>
        </tr>
    </tbody>
</table>
<script type="text/javascript">
    $(document).ready(function(){
                                $("#tbl-subject").DataTable({
                                    "pageLength":2,
                                    "lengthChange":false,
                                    "bInfo":false,
                                    "ordering": false
                                });
                            });
</script>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(response, 'lxml')

subject_container = soup.find_all(class_="subcontent-container")
result = []
for subject in subject_container:
    
    
    #convert to raw string, so it can be parsed after being converted to BS4
    subject = str(subject)
    soup = BeautifulSoup(subject, 'lxml')

    #Name
    subject_name = soup.find('h4')
    subject_name = subject_name.contents[0] # getting the data within the actual tag that stored the name

    #Instructor
    subject_instructor = soup.select_one('.istruinfocontainer > div') # probably meant to write "instructor-info-container" but you never know 💀
    subject_instructor = subject_instructor.contents[0]

    #Subject Attendance
    subject_attendance = soup.select_one('.prg-container > span') #progress container is the weird horizontal graph thingy
    subject_attendance = subject_attendance.contents[0]
    
    subject_link = soup.find('a')
    subject_link = subject_link['href']
    
    subject_dict = {
            'name':subject_name,
            'instructor':subject_instructor,
            'attendance':subject_attendance,
            'link':subject_link
        }
        
    result.append(subject_dict)

print(result)



