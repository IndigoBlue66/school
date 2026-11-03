<%inherit file="html.mako"/>
<%block name="header">\
  <h1>${school.name}</h1>
  <hr>
</%block>
<%block name="main">\
  <h2>Students</h2>
  <ul>
% for student in school.students:
    <li><a href="students/student_${student.id}.html">${student.first_name} ${student.surname}</a><br></li>
% endfor
  </ul>
</%block>
