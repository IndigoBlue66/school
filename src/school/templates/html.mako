<!DOCTYPE HTML>
<html>
  <head>
    <%block name="head">
      <style>
        h1                          {font-size:45px; font-weight:bold}
        a                           {color:rgb(96, 192, 0)}
        hr                          {border: 2px solid rgb(96, 192, 0); margin: 0 auto; width: 50%}
        body                        {text-align:center; font-size:20px}
        table                       {text-align:left; margin: 0 auto}
        td                          {padding: 10px 10px}
        .tooltip                    {position: relative;}
        .tooltip-content            {display: inline-block; border-bottom: 1px dotted black;}
        .tooltip .tooltiptext       {position: absolute; left: 100%; top: 50%; transform: translateY(-50%); white-space: nowrap; visibility: hidden; margin-left: 10px; padding: 5px 10px; text-align: center; color: #fff; background-color: #555; border-radius: 5px; opacity: 0; transition: opacity 0.3s;}
        .tooltip:hover .tooltiptext {visibility: visible; opacity: 1}
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