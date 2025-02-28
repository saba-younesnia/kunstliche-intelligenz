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

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Immobilienpreisvorhersage:

Dieses Projekt entwickelt ein maschinelles Lernmodell zur Vorhersage von Hauspreisen in Ames, Iowa. Der verwendete Datensatz umfasst Immobilienmerkmale wie Größe, Lage und Ausstattung. Als Modell kommt ein Random Forest Regressor zum Einsatz, der den Zusammenhang zwischen den Features und dem Verkaufspreis (SalePrice) analysiert.

Datenvorverarbeitung: Irrelevante Spalten wie Order, Alley, Pool QC und weitere wurden entfernt, da sie entweder keine Aussagekraft besaßen oder zu viele fehlende Werte aufwiesen. Fehlende Werte wurden je nach Datentyp behandelt – kategorische Features wie MSZoning erhielten den Platzhalter 'None', während numerische Spalten mit dem Mittelwert der jeweiligen Spalte aufgefüllt wurden. Anschließend wurden kategorische Features mithilfe von Label-Encoding (z. B. für Neighborhood) in numerische Werte umgewandelt. Alle numerischen Features wurden zudem mit dem StandardScaler standardisiert, um eine einheitliche Skalierung zu gewährleisten.

Modellierung: Die Daten wurden in 80 % Trainings- und 20 % Testdaten aufgeteilt (test_size=0.2). Das Random-Forest-Modell wurde mit 100 Bäumen (n_estimators=100) und einem festen random_state=42 trainiert, um Reproduzierbarkeit zu sichern. Die Analyse der Feature-Wichtigkeiten identifizierte Schlüsselmerkmale wie Overall Qual und Gr Liv Area als entscheidende Preistreiber.

Ergebnisse: Das Modell erreichte einen MAE (Mean Absolute Error) von 16.036,61 und einen MSE (Mean Squared Error) von 719.155.170,50. Der R²-Score von 0,91 zeigt, dass 91 % der Varianz im Verkaufspreis durch das Modell erklärt werden – ein Hinweis auf hohe Vorhersagegenauigkeit.
