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
  <table style="margin: 0 auto; text-align: left;">
    <tr>
      <th>Student-ID:</th>
      <td>${student.id}</td>
    </tr>
    <tr>
      <th>Date of Birth:</th>
      <td>${student.birthday}</td>
    </tr>
  </table>
</%block>
