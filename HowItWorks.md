# Introduction #

This is a brief explanation of how Django ids works and why you should'nt worry about performance


# Details #

Django IDS is basicaly a Middleware that checks every field of requests passed to the application. Values are checked vs a rules written as regular expressions that match if a field contains a possible attack string. This could sound quite time consuming but fields are passed to the rules engine only if they pass through the so called "centrifuge". This is a simple algorithm that checks the ratio between the string lenght and the number of special characters in it. If the ratio is high this is probably an attack and so it is passed to the rules engine. Rules are regular expression matching particular kind of attack stings. Rules are categorized by severity [the attack](of.md) and tagged (which is very web 2.0).

# Countermeasureand False positives #

False positives are matching rule that shouldn't. If your django app has a comment system and someone leave something like this

```
you are a <b>*#!'!'</b>
```

Django IDS will catch it as an attack, which, technicaly, is wrong.

Countermeasure to attacks could stop the request raising an http error or proceed with the request.
The attack data is alaways recorded. Is up to the developer deciding what is the desired behaviour