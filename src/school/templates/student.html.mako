<%inherit file="html.mako"/>
<%block name="header">\
  <h1>${student.first_name} ${student.surname}</h1>
  <hr>
</%block>
<%block name="footer">\
<hr>
<a href="../index.html">Return</a>
</%block>
<%block name="main">\
  <h2>Overview</h2>
  <table>
%if student.nickname:
      <tr>
      <th>Nickname:</th>
      <td>${student.nickname}</td>
    </tr>
%endif
    <tr>
      <th>Gender:</th>
      <td>${student.gender}</td>
    </tr> 
    <tr>
      <th>Date of Birth:</th>
      <td>${student.birthday}</td>
    </tr> 
    <tr>
      <th>Student-ID:</th>
      <td>${student.id}</td>
    </tr>
    <tr>
      <th>Active:</th>
      <td>${student.active}</td>
    </tr>
  </table>
% if student.subjects:
  <h2> Grades </h2>
  <table>
    <tr>
      <td></td><th>Letter Grade</th>
    </tr>
% for subject in student.subjects:
      <tr>
      <th>${subject.name}:</th>
      <td class="tooltip"><span class="tooltip-content">${subject.letter_grade}</span><span class="tooltiptext">Ø ${subject.average_grade}</span></td>
% for grade in subject.grades:
      <td>${grade}</td>
% endfor
    </tr>
% endfor
%endif
  </table>
</%block>
