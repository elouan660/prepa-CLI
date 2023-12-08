#let Exercice(auteur, date, titre, contenu) = [
  #set text(font: "Noto Sans", size: 12pt)
  #align(left)[#auteur \ #date]
  #align(center)[#text(size: 25pt, weight: "bold")[#titre]]
  \ \
  #show heading: it => [
    #if it.level == 1 {
      align(center)[#text(size: 17pt)[#it]]
    } else if it.level == 2{
      underline(text(size: 11pt, weight: "regular")[#it])
    } else {
      
    }
  ]
  #contenu
]