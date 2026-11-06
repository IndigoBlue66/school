<%inherit file="html.mako"/>
<%block name="header">\
  <h1>${school.name}</h1>
  <hr>
</%block>
<%block name="main">\
  <h2>Students</h2>
  <table>
% for student in school.students:
    <tr>
      <td><a href="students/student_${student.id}.html">${student.first_name} ${student.surname}</a></td>
      <td class="tooltip"><span class="tooltip-content">${student.overall_avg}</span><span class="tooltiptext">Average over all Subjects</span></td>
    </tr>
% endfor
  </table>
</%block>
