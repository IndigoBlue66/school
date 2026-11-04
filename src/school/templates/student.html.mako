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
      <tr>
      <th>Nickname:</th>
      <td>${student.nickname}</td>
    </tr> 
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
  <h2> Grades </h2>
  <table>
    <tr>
      <td></td><th>Letter Grade</th>
    </tr>
<%block>
% for subject in student.subjects:
      <tr>
      <th>${subject.name}:</th>
      <td>${subject.letter_grade}</td>
% for grade in subject.grades:
      <td>${grade}</td>
% endfor
    </tr>
% endfor
</%block> 
  </table>
</%block>
