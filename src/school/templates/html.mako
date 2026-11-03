<!DOCTYPE HTML>
<html>
  <head>
    <%block name="head">
      <style>
        h1                {font-size:45px}
        p                 {font-size:20px}
        a                 {font-size:20px; color:rgb(96, 192, 0)}
        hr                {border: 2px solid rgb(96, 192, 0)}
        li                {list-style: square; list-style-position: outside; font-size:20px}
        ul                {display:inline-block; font-size:25px; text-align:left}
        body              {text-align:center}
        table             {font-size:20px; text-align:left}
      </style>
    </%block>
  </head>
 <body>
    <header>
      <%block name="header">\
        <h1> Heading </h1>
      </%block>
    </header>
    <main>
      <%block name="main">\
        <p> Main </p>
      </%block>
    </main>
    <footer>
      <%block name="footer">\
        <hr style="margin-bottom: 50px; margin-top: calc(100% - 50px);">
      </%block>
    </footer>
  </body>
</html>