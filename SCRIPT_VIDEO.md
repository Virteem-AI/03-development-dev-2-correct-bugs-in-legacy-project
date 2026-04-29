# Script vidéo - DEV-2

## Alignement avec `New_training_content.md`

"Ce script reprend deux sources : `Script — Using Copilot Chat as an Analysis Assistant`, pour la partie debugging avec Agent Mode, et `Script — Using Copilot to Analyze and Improve Existing Code`, pour l'analyse de code existant."

"Le contenu source explique que Copilot peut lire le code, analyser une erreur, proposer une cause, appliquer une correction et relancer les tests. Ce Hands On met exactement cette boucle en pratique."

## Concept couvert

"Ce Hands On couvre le debugging agentique et la boucle Implementation-Verification. Dans un workflow classique, un développeur lit les erreurs, inspecte le code, corrige, puis relance les tests. Avec un agent, la boucle reste la même, mais l'IA peut aider à analyser plus vite et à proposer les corrections."

"Le concept important est que les tests deviennent le garde-fou de l'agent. On ne fait pas confiance à une correction parce qu'elle semble plausible ; on la valide avec la suite de tests."

"La deuxième idée est que le debugging est un dialogue. On ne demande pas seulement 'fix it'. On donne à l'agent le contexte : les fichiers concernés, la sortie de test, le comportement attendu. Plus le signal est clair, meilleure est l'analyse."

"La troisième idée est la comparaison d'agents. Copilot Agent Mode et Claude Code peuvent avoir des styles différents : l'un peut corriger rapidement, l'autre peut expliquer davantage ou proposer une stratégie différente. L'exercice entraîne à superviser ces approches."

## Mise en situation

"Le projet fourni contient une application Flask volontairement cassée et une suite de tests pytest. Les tests définissent le comportement attendu : création de tâche, mise à jour, suppression et capacité à lancer l'application."

"Au départ, les tests échouent. C'est normal : ils servent à guider l'analyse."

"À l'écran, montrez `buggy_app.py` sans révéler immédiatement tous les bugs. Puis ouvrez `test_buggy_app.py` et expliquez que les tests décrivent le contrat attendu."

"Expliquez que l'on va partir des tests, pas d'une lecture exhaustive du code. C'est une pratique efficace : les échecs donnent une priorité et évitent de corriger au hasard."

## Démonstration du début

"Je commence par lancer `pytest test_buggy_app.py -v`. Je lis les premières erreurs, puis je les donne à Copilot. Je lui demande de corriger les bugs dans `buggy_app.py` et de relancer les tests après chaque correction."

"Je montre qu'il ne faut pas tout corriger sans validation. Après chaque modification importante, on revient à pytest pour vérifier si la situation s'améliore."

"Montrez un premier échec simple, par exemple une route incorrecte ou un mauvais status code. Demandez à Copilot d'expliquer la cause avant d'appliquer la correction."

"Après la correction, relancez les tests. Soulignez que la progression est visible : on passe de plusieurs échecs à moins d'échecs. Cette progression guide la suite."

"Quand tous les tests passent avec Copilot, expliquez la deuxième partie : remettre le projet dans l'état initial ou comparer conceptuellement avec Claude Code. L'objectif n'est pas de faire une compétition, mais d'observer les différences de raisonnement et de workflow."

## Consignes pour l'exercice

"Vous devez corriger les cinq bugs jusqu'à obtenir une suite verte. Ensuite, si Claude Code est disponible, recommencez l'exercice avec le même prompt et comparez les approches."

"À la fin, vous devez pouvoir expliquer chaque bug, le test qui le détectait, et la façon dont l'agent a raisonné ou itéré."

## Erreurs fréquentes à mentionner

"Première erreur : appliquer plusieurs corrections sans relancer les tests. On perd alors le lien entre cause et effet."

"Deuxième erreur : accepter une correction qui modifie les tests au lieu de corriger le code. Dans cet exercice, les tests définissent le comportement attendu ; ils ne doivent pas être affaiblis."

"Troisième erreur : ne pas demander d'explication. Un bug corrigé mais non compris risque de revenir."

## Conclusion

"Ce Hands On montre que l'agent est très utile pour accélérer le debugging, mais que la méthode reste essentielle : observer, analyser, corriger, vérifier."

"Le réflexe à retenir : les tests sont la source de feedback. L'agent propose, mais la boucle de validation décide."
