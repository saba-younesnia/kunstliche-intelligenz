Vergleich-von-Crossover-Methoden-in-genetischen-Algorithmen-zur-konfliktfreien-Stundenplanerstellung:

Dieses Python-Skript implementiert einen genetischen Algorithmus zur Generierung konfliktfreier Universitätsstundenpläne, bei dem jede Klasse einen eindeutigen Zeitfenster-Slot erhält. Der Fokus liegt auf dem Vergleich dreier Crossover-Methoden – One-Point, Two-Point und Uniform Crossover – um deren Effektivität bei der Lösungsfindung zu bewerten.

Problemstellung:
Das Ziel ist die Zuweisung von 10 Klassen zu 25 verfügbaren Zeitfenstern (Slots 1–25). Eine optimale Lösung liegt vor, wenn zwei Bedingungen erfüllt sind: Erstens dürfen keine zwei Klassen denselben Slot belegen (Konfliktfreiheit), zweitens müssen genau 10 eindeutige Slots vergeben werden.

Lösungsansatz:
Der genetische Algorithmus arbeitet mit einer Population von 10 Chromosomen, wobei jedes Chromosom 10 Gene (Slots) repräsentiert. Die Fitness-Funktion bewertet Lösungen anhand der Anzahl eindeutiger Slots – ein perfekter Stundenplan erreicht den Maximalwert von 10. Der Algorithmus terminiert entweder bei Erfolg (Finden einer konfliktfreien Lösung) oder nach 1000 Generationen.

Drei Crossover-Strategien werden verglichen:
Beim One-Point Crossover wird ein zufälliger Trennpunkt im Chromosom gewählt (z. B. entstehen aus den Eltern [A|B] und [X|Y] die Kinder [A|Y] und [X|B]).
Das Two-Point Crossover verwendet zwei Trennpunkte, um einen Austauschbereich zu definieren (z. B. Eltern [A|B|C] und [X|Y|Z] ergeben [A|Y|C] und [X|B|Z]).
Beim Uniform Crossover wird jedes Gen zufällig von einem Elternteil übernommen (50/50-Chance pro Gen).

Implementierung:
Die Initialpopulation besteht aus 10 vordefinierten Chromosomen mit teilweise doppelten Slots. Die Selektion erfolgt durch Turnierauswahl: Drei zufällig ausgewählte Chromosomen "konkurrieren", wobei das Chromosom mit der höchsten Fitness als Elternteil ausgewählt wird. Eine Mutationsrate von 10 % sorgt für Diversität – bei jeder Mutation wird ein zufälliges Gen durch einen neuen Slot (1–25) ersetzt. Die gesamte Population wird in jeder Generation durch die Nachkommen ersetzt (Generational Replacement).
