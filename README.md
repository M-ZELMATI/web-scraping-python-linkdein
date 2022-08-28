# web-scraping-python-linkdein
apply  web scraping on job search in linkedin 

#Introduction :

Ce mini projet se concentre sur les mécanismes de base du scraping web : comment utiliser
Python pour demander des informations à un serveur web, comment effectuer une
manipulation de base de la réponse du serveur et comment commencer à interagir avec un site
web de manière automatisée. Nous naviguerons sur Internet avec aisance, en construisant des
scrapeurs qui pourront d’un domaine à l'autre, collecter des informations et les stocker pour
une utilisation ultérieure.<br/>
Pour être honnête, le web scraping est un domaine fantastique et très populaire qui permet
d’extraire des données sur des sites web. C’est particulièrement utile quand vous avez surfé sur
internet et trouvé les informations que vous cherchiez. Mais Aie ! comment récupérer ces
informations si le site ne les publie pas (sous forme d’API ou d’export CSV). Durant cette
recherche nous allons comprendre ce qu’est le scraping, les étapes essentielles pour collecter
tous ses informations dont qu’elles ont besoin de cette pratique ainsi qu’un exemple afin de
vous familiariser avec la notion.<br/>
#Définition du Web Scraping
Le terme scraping vient de verbe « to scrape » en anglais, signifie gratter. Scraper des
données, c’est donc littéralement gratter des informations depuis une page web. En d’autres
mots, on pourrait apparenter cela à un copier-coller.
Mais avec le scraping, tout est automatique. Inutile de passer des heures à répéter Ctrl + C /
Ctrl + V ! Cette opération est réalisée par un bot qui est capable de passer d’une page à une
autre sur un site web pour récupérer toutes les données. Dans ce cas, on parle aussi alors de
crawling.<br/>
Le web scraping est une pratique informatique utilisée pour extraire un large ensemble de
données non structurées à partir d’un site web. Cette méthode permet de collecter des données
non structurées et les enregistrer dans un format structuré. Il existe plusieurs méthodes pour
scraper un site web comme les services en ligne, les API ou bien à partir de vos propres codes.
Pourquoi faire du web Scrappring avec Python ?<br/>

Facilité d’utilisation : Python est très simple à coder, vous n’aurez pas à utiliser des points-
virgules à chaque retour de ligne ou bien des accolades à chaque début de condition. La notion d’indentation permet aussi d’avoir un code propre et lisible.

__Large collection de librairies :__ Python dispose d’une immense collection de librairies comme
Numpy, Matplotlib, Pandas etc... Chose qui permet de fournir à l’utilisateur plusieurs méthodes
et services pour différentes raisons. En plus il vous sera très utile dans le traitement des données
extraites du site.
Langage non typé : l’une des qualités de Python est que vous ne devez pas définir les types des
variables. Vous pouvez les utiliser directement quand vous souhaitez. Cette pratique permet de
gagner du temps.
Syntaxe facilement compréhensible : La syntaxe de Python est facilement compréhensible vu
qu’elle est très similaire à la langue anglaise. La notion d’indentation facilite aussi la tâche vu
qu’elle permet de séparer les blocs du code.
Moins de code. Plus d’efficacité : le web scrapping a pour but de vous faire gagner du temps !
mais on ne veut pas écrire de longs programmes qui vont consommer le temps gagné !
Heureusement qu’en Python, de petits programmes exécutent des tâches immenses.
Communauté : Supposons que vous avez rencontré une difficulté ou une erreur lors de la
programmation ? Pas besoin de vous affoler. Python a l’une des plus grandes communautés
actives dans le monde de la programmation ou vous pouvez poser toutes vos questions et avoir
des réponses convaincantes à ses dernières.
Comment fonctionne le web scraping ?
Le schéma de fonctionnement du processus de scraping est très simple. Dans un premier temps,
le développeur du scraper analyse le code source HTML de la page à laquelle il s’intéresse.
Habituellement, le code contient des schémas clairs permettant d’extraire les informations
désirées. Le scraper est programmé pour ces schémas. Le reste du travail est effectué par le
scraper de façon automatisée et consiste à :
1) consulter un site Internet à une adresse URL,<br/>
2) extraire automatiquement les données structurées selon les schémas,<br/>
3) rassembler, enregistrer, analyser, combiner les informations extraites, etc.<br/>
Chaque site internet est conçu différemment. Différents scripts sont dès lors programmés pour
extraire les données des différents sites. Dans un premier temps, il faut observer la structure du

site. Il faut ensuite regarder les différents groupes de catégories et les éventuelles sous-
catégories. Une fois qu'elles ont été déterminées, ces catégories peuvent être parcourues pour

effectuer le scraping de tous les données et caractéristiques que nous correspondons.<br/>


#L’utilité de langage Python
Le langage de programmation Python est idéal pour créer des logiciels de web scraping. Les
sites Internet sont modifiés en permanence et les contenus du web changent donc au fil du
temps. Le design d’un site Internet peut par exemple être mis au goût du jour ou de nouveaux
éléments de page. Si la structure de la page peut être ajoutés. Un web scraper est pour la
structure spécifique d’une page. Si la nature de page vient à changer, le scraper doit alors être
modifié. Une tâche facilement réalisable avec Python.<br/>
Par ailleurs, Python est particulièrement efficace lorsqu’il s’agit de traiter du texte et de
consulter des ressources web ; deux bases techniques du web scraping. D’autre part, Python
est un standard établi pour l’analyse et le traitement des données. Outre son adéquation
générale, Python séduit également par un écosystème de la programmation très riche, incluant
notamment des bibliothèques, des projets open source, de la documentation et des références
linguistiques ainsi que des contributions sur les forums, des rapports de bugs et des articles de
blog.<br/>
Plusieurs outils de web scraping dédiés très sophistiqués sont disponibles avec Python.
Nous vous présentons ici trois des outils ou bibliothèques les plus connus : Scrpy, Selenium
et BeautifulSoup, ...<br/>

#Le Web Scraping est-il légal ?
Cette question vient souvent à l'esprit. Extraire les informations d'Internet et les
enregistrer dans nos fichiers est-il légal ou non ? La meilleure réponse à cette question est
que certains sites Web autorisent le web scraping et d'autres non. La partie crawler du
Web Scraper explore automatiquement les sites Web et vérifie automatiquement si un site
Web a autorisé ou non le Web Scraping. Si vous voulez savoir qu'un site Web a autorisé
le grattage Web, vous pouvez rechercher le fichier "robot.txt" de ce site Web. Le fichier
robot.txt de certains sites Web est facilement accessible, mais dans certains cas, ils ne le

sont pas. Généralement, vous entrez l'adresse de domaine principale du site Web et faites-
la suivre d'une barre oblique ("/") avec "robots.txt" qui vous mènera à ce fichier et vous

pourrez voir s'ils ont autorisé l'exploration par des robots ou non.<br/>
Faire du web scraping n'est pas un processus illégal d'un point de vue technique. Mais la
pratique consistant à utiliser les données que vous avez extraites d'Internet indique si elles
sont légales ou illégales.<br/>
Il existe certaines stratégies que vous devriez suivre lorsque vous faites du Web
Scraping. Ces stratégies ressemblent aux règles du web scraping légal qui incluent :<br/>

 Vous devez éviter l'utilisation de toute API Web pour le Web Scraping, car cela
peut vous causer des problèmes car vous ne connaissez pas les configurations
de l'API et que se passe-t-il s'ils utilisent les données illégalement en votre nom
pour le grattage Web. Il est donc conseillé d'éviter l'utilisation d'API pour le
Web Scraping.<br/>
 Les données récupérées ne doivent pas être réutilisées sur Internet ou à des fins
commerciales. Comme les données appartiennent au propriétaire d'origine
uniquement. Vous ne devez donc pas l'utiliser à des fins commerciales ou de
marketing.<br/>
 Chaque fois que vous faites du Web Scraping, vous devez d'abord consulter les
conditions générales du service et les lire attentivement pour comprendre s'il y
a quelque chose de vulnérable ou non.<br/>
 Supposons que quelqu'un ait mis des restrictions sur ses données pour le Web
Scraping, vous devriez alors lui demander avant d'aller plus loin.<br/>

__Flux de processus général de grattage Web__
1. Envoyez une requête HTTP à l'URL de la page Web.<br/>
2. Le serveur répondra avec le contenu HTML de la page Web.<br/>
3. Collectez les données pertinentes à partir du contenu de la réponse.<br/>
4. Organiser les données dans un format structuré<br/>
5. Éliminer les données inutiles, redondantes et manquantes<br/>
6. Stockez les données sous une forme utile à l'utilisateur.<br/>
#Recherche requise avant le raclage
Si vous ciblez un site Web pour en extraire des données, nous devons comprendre son échelle
et sa structure. Voici quelques-uns des fichiers que nous devons analyser avant de
commencer le scraping web.<br/>
Analyse de robots.txt
En fait, la plupart des éditeurs autorisent les programmeurs à explorer leurs sites Web dans
une certaine mesure. Dans un autre sens, les éditeurs souhaitent que des parties spécifiques
des sites Web soient explorées. Pour définir cela, les sites Web doivent établir des règles pour
indiquer quelles parties peuvent être explorées et lesquelles ne peuvent pas l’être. Ces règles
sont définies dans un fichier appelé robots.txt .<br/>
*robots.txt* est un fichier lisible par l'homme utilisé pour identifier les parties du site Web
que les robots d'exploration sont autorisés ou non autorisés à gratter. Il n'y a pas de format
standard de fichier robots.txt et les éditeurs de site Web peuvent faire des modifications selon
leurs besoins. Nous pouvons vérifier le fichier robots.txt pour un site Web particulier en
fournissant une barre oblique et robots.txt après l'url de ce site Web. Par exemple, si nous
voulons le vérifier pour Google.com, nous devons taper https://www.google.com/robots.txt et
nous obtiendrons quelque chose comme suit :<br/>
__User-agent: *<br/>
Disallow:/search<br/>
Allow:/search/about<br/>
Allow:/search/static<br/>
Allow:/search/howsearchworks<br/>
Disallow:/sdch<br/>
Disallow:/groups<br/>
Disallow:/indexl?<br/>
Disallow:/?<br/>
Allow:/?hl=<br/>
Disallow:/?hl=*&<br/>
Allow:/?hl=*&gws_rd=ssl$<br/>__
and so on........<br/>
Certaines des règles les plus courantes définies dans le fichier robots.txt d’un site Web sont
__les suivantes:<br/>
User-agent: BadCrawler<br/>
Disallow:/<br/>__
La règle ci-dessus signifie que le fichier robots.txt demande à un robot avec l’agent
utilisateur BadCrawler de ne pas explorer son site Web.<br/>
__User-agent: *<br/>
Crawl-delay: 5<br/>
Disallow:/trap<br/>__
La règle ci-dessus signifie que le fichier robots.txt retarde un robot pendant 5 secondes entre
les demandes de téléchargement pour tous les agents utilisateurs pour éviter de surcharger le
serveur. Le lien /trap tentera de bloquer les robots malveillants qui suivent les liens interdits.
Il existe de nombreuses autres règles qui peuvent être définies par l’éditeur du site Web en
fonction de leurs besoins. Certains d’entre eux sont discutés ici -Par exemple :<br/>
__User-agent: *<br/>
Allow: /<br/>__
Cela indique que vous autorisez tous les robots d’explorations à explorer et indexer la totalité
de votre site.<br/>
Autre exemple :<br/>
__User-agent: Googlebot<br/>
Allow: /<br/>__
Cela indique que vous autorisez seulement Googlebot à explorer et à indexer la totalité de
votre site.

Les directives les plus utilisées dans le fichier robots.txt :<br/>
 User-agent: [obligatoire, un ou plusieurs par groupe] : nom d’un robot de moteur de
recherche (logiciel de robot d’exploration) auquel la règle s’applique<br/>
 Disallow: [au moins une ou plusieurs entrées Disallow ou Allow par règle] :
répertoire ou page, relatifs au domaine racine, qui ne doivent pas être explorés par le
user-agent.<br/>
 Allow: [au moins une ou plusieurs entrées Disallow ou Allow par règle] : répertoire
ou page, relatifs au domaine racine, qui doivent être explorés par le user-agent
mentionné précédemment.<br/>
 Sitemap: [facultatif, zéro ou plus par fichier] : emplacement d’un sitemap pour ce
site Web. L’URL fournie doit être complète.<br/>

Autoriser l'accès complet<br/>
__User-agent: *<br/>
Disallow:__<br/>
Si vous trouvez cela dans le fichier robots.txt d'un site Web que vous essayez d'explorer, vous
avez de la chance. Cela signifie que toutes les pages du site peuvent être explorées par des
robots.<br/>
Bloquer tous les accès<br/>
__User-agent: *<br/>
Disallow:<br/> /__
Vous devriez éviter un site avec ceci dans son fichier robots.txt. Il stipule qu'aucune partie du
site ne doit être visitée à l'aide d'un robot d'exploration automatisé et que la violation de cela
pourrait entraîner des problèmes juridiques.<br/>
Accès partiel<br/>
__User-agent: *<br/>
Disallow: /dossier/<br/>__

__User-agent: *<br/>
Disallow: /file.html<br/>__
Certains sites n'autorisent l'exploration que de sections ou de fichiers particuliers sur leur
site. Dans de tels cas, vous devez demander à vos robots de ne pas toucher aux zones
bloquées.<br/>

Robot d’exploration (User-Agent). Ces robots sont surnommés « Web crawleurs » ou
« SEO spiders », analysent et récupèrent des ressources sur des pages web. Bien que ce soit
un simple programme informatique, la connaissance de son fonctionnement s’avère cruciale
en matière de référencement naturel.<br/>
#Pourquoi Python est-il bon pour le scraping Web ?
Il peut y avoir un certain nombre de raisons de choisir Python pour le Web
Scraping. Certaines des raisons courantes sont les suivantes :
 Syntaxe facile : La syntaxe de Python utilisée pour le Web Scraping est très
simple et peut être comprise facilement. La syntaxe est comme une déclaration
en anglais qui vous aide à la comprendre facilement et
correctement. L'indentation utilisée dans le code Python aide également
l'utilisateur à différencier les parties du code pour le rendre facile à
comprendre.<br/>
 Grande communauté : Python est un langage de programmation populaire et
l'une des raisons de sa popularité est qu'il a une grande
communauté. L'avantage d'avoir un large support communautaire est que si
vous êtes coincé quelque part à écrire votre code, vous n'avez pas à vous en
soucier. La communauté Python est la plus active à partir de laquelle vous
pouvez demander de l'aide.<br/>
 Facile à coder : Python est facile à programmer et vous n'avez même pas
besoin d'utiliser des points-virgules (;) et des accolades ("}") n'importe où dans
le code, ce qui le rend plus simple et plus facile.<br/>
 Typé dynamiquement : le langage de programmation Python est typé
dynamiquement et vous n'avez pas besoin de définir des types de données pour
les variables avant de l'utiliser. Vous pouvez utiliser directement la variable
avec n'importe quel type de données chaque fois que nécessaire. Cette pratique
permet de gagner du temps pour coder et réduit également la ligne de code que
vous écrivez.<br/>
 Un petit code peut gérer de grandes tâches : Web Scraping est bénéfique
pour gagner du temps car il automatise la tâche manuelle d'extraction
d'informations. Vous pensez peut-être que le temps que vous avez économisé
dans le web scraping est consacré au temps d'écriture du code. Mais ce n'est pas
vrai, vous n'avez pas besoin d'écrire un énorme code pour le scraping
Web. C'est un autre avantage de l'utilisation de Python pour le scraping Web,
vous n'avez pas à écrire de code volumineux pour le scraping Web ou les tâches volumineuses. Parce que le petit code peut aussi faire de grandes tâches
très facilement en Python.<br/>
 Énorme collection de bibliothèques et de framework : Python possède une
grande collection de bibliothèques qui peuvent être utilisées à plusieurs fins
dans Web Scraping. Certaines des bibliothèques populaires de Python
incluent Matplotlib , NumPy , Pandas , etc.<br/>

Voilà donc les raisons du choix de Python pour le Web Scraping. Il peut y avoir plus de

raisons aussi. Mais les raisons courantes sont celles que nous avons discutées ci-
dessus. En conclusion, on peut dire que Python est l'un des langages les plus adaptés pour

faire du Web Scraping.<br/>

#Les composants d'une page Web
Avant de commencer à écrire du code, nous devons comprendre un peu la structure d'une
page Web. Nous utiliserons la structure du site pour écrire du code qui nous permettra
d'obtenir les données que nous voulons récupérer. Comprendre cette structure est donc une
première étape importante pour tout projet de récupération Web.<br/>
Lorsque nous visitons une page Web, notre navigateur Web adresse une requête à un serveur
Web. Cette requête s'appelle une GETrequête, puisque nous recevons des fichiers du
serveur. Le serveur renvoie ensuite des fichiers qui indiquent à notre navigateur comment
afficher la page pour nous. Ces fichiers comprendront généralement :<br/>
 HTML — le contenu principal de la page.<br/>
 CSS - utilisé pour ajouter un style pour rendre la page plus agréable.<br/>
 JS — Les fichiers Javascript ajoutent de l'interactivité aux pages Web.<br/>
 Images — les formats d'image, tels que JPG et PNG , permettent aux pages Web
d'afficher des images.<br/>
Une fois que notre navigateur a reçu tous les fichiers, il rend la page et nous l'affiche.
Il y a beaucoup de choses qui se passent dans les coulisses pour bien rendre une page, mais
nous n'avons pas à nous en soucier lorsque nous grattons le Web. Lorsque nous effectuons du
web scraping, nous nous intéressons au contenu principal de la page Web, nous examinons
donc principalement le HTML.<br/>
HTML
HyperText Markup Language (HTML) est le langage dans lequel les pages Web sont créées.
Cependant, HTML n'est pas un langage de programmation, comme Python. C'est un langage
de balisage qui indique à un navigateur comment afficher le contenu.<br/>
HTML a de nombreuses fonctions similaires à ce que vous pourriez trouver dans un
traitement de texte comme Microsoft Word - il peut mettre du texte en gras, créer des
paragraphes, etc.<br/>
Si vous connaissez déjà le langage HTML, n'hésitez pas à passer à la section suivante de ce
didacticiel . Sinon, faisons un tour rapide du HTML afin d'en savoir assez pour gratter
efficacement.<br/>


HTML se compose d'éléments appelés balises . La balise la plus basique est
la <html>balise. Cette balise indique au navigateur Web que tout ce qu'il contient est
HTML. Nous pouvons créer un document HTML simple en utilisant simplement cette
balise :<br/>

<html><br/>
</html><br/>
Nous n'avons pas encore ajouté de contenu à notre page, donc si nous consultions notre
document HTML dans un navigateur Web, nous ne verrions rien :
A l'intérieur même d'une htmlbalise, on peut mettre deux autres balises : la headbalise et
la bodybalise.<br/>
Le contenu principal de la page Web va dans la bodybalise. La headbalise contient des
données sur le titre de la page et d'autres informations qui ne sont généralement pas utiles
pour le scraping Web :
<br/>
<html><br/>
<head><br/>
</head><br/>
<body><br/>
</body><br/>
</html><br/>
Nous n'avons toujours pas ajouté de contenu à notre page (qui va à l'intérieur de
la bodybalise), donc si nous ouvrons ce fichier HTML dans un navigateur, nous ne verrons
toujours rien :<br/><br/>
Vous avez peut-être remarqué ci-dessus que nous plaçons les balises headet bodyà l'intérieur
de la htmlbalise. En HTML, les balises sont imbriquées et peuvent aller à l'intérieur d'autres
balises.<br/>
Nous allons maintenant ajouter notre premier contenu à la page, à l'intérieur
d'une pbalise. La pbalise définit un paragraphe, et tout texte à l'intérieur de la balise est
affiché comme un paragraphe séparé :<br/>

<html><br/>
<head><br/>
</head><br/>
<body><br/>
<p><br/>
Here's a paragraph of text!<br/>
</p><br/>
<p><br/>
Here's a second paragraph of text!<br/>  
  
  </p><br/>
</body><br/>
</html><br/>
Rendu dans un navigateur, ce fichier HTML ressemblera à ceci :<br/>
Voici un paragraphe de texte !<br/>
Voici un deuxième paragraphe de texte !<br/>
Les balises ont des noms couramment utilisés qui dépendent de leur position par rapport aux
autres balises :<br/>
 child— un enfant est une balise à l'intérieur d'une autre balise. Ainsi, les deux pbalises
ci-dessus sont toutes deux des enfants de la bodybalise.<br/>

 parent— un parent est la balise à l'intérieur de laquelle se trouve une autre balise. Ci-
dessus, la htmlbalise est le parent de la bodybalise.<br/>

 sibiling— un sibiling est une balise imbriquée dans le même parent qu'une autre
balise. Par exemple, headet bodysont frères et sœurs, puisqu'ils sont tous les deux à
l'intérieur de html. Les deux pbalises sont sœurs, puisqu'elles sont toutes les deux à
l'intérieur de body.<br/>
Nous pouvons également ajouter des propriétés aux balises HTML qui modifient leur
comportement. Ci-dessous, nous ajouterons du texte supplémentaire et des hyperliens à l'aide
de la abalise.<br/>
  
<html><br/>
<head><br/>
</head><br/>
<body><br/>
<p><br/>
Here's a paragraph of text!<br/>
<a href="https://www.dataquest.io">Learn Data Science Online</a>
</p><br/>
<p><br/>
Here's a second paragraph of text!<br/>
<a href="https://www.python.org">Python</a> </p><br/>
</body></html><br/>
Voici à quoi cela ressemblera :<br/>
Voici un paragraphe de texte ! Apprendre la science des données en ligne<br/>
Voici un deuxième paragraphe de texte ! Python<br/>
Dans l'exemple ci-dessus, nous avons ajouté deux abalises. ales balises sont des liens et
indiquent au navigateur de rendre un lien vers une autre page Web. La hrefpropriété de la
balise détermine où va le lien.<br/>
aet psont des balises html extrêmement courantes. En voici quelques autres :<br/>
 div— indique une division ou une zone de la page.<br/>
 b— met en gras tout texte à l'intérieur.<br/>
 i- met en italique tout texte à l'intérieur.<br/>
 table— crée un tableau.<br/>
 form— crée un formulaire de saisie.<br/>
Pour une liste complète des balises, regardez ici .<br/>
Avant de passer au web scraping proprement dit, découvrons les propriétés classet id. Ces
propriétés spéciales donnent des noms aux éléments HTML et facilitent leur interaction lors
du grattage.<br/>
Un élément peut avoir plusieurs classes et une classe peut être partagée entre des
éléments. Chaque élément ne peut avoir qu'un seul identifiant, et un identifiant ne peut être
utilisé qu'une seule fois sur une page. Les classes et les identifiants sont facultatifs et tous les
éléments n'en auront pas.<br/>
Nous pouvons ajouter des classes et des identifiants à notre exemple :<br/>

<html><br/>
<head><br/>
</head><br/>
<body><br/>
<p class="bold-paragraph"><br/>
Here's a paragraph of text!<br/>
<a id="learn-link">Learn Data Science Online</a><br/>
</p><br/>
<p class="bold-paragraph extra-large"><br/>
Here's a second paragraph of text!<br/>
<a class="extra-large">Python</a><br/>
</p><br/>
</body><br/>
</html><br/>
Voici à quoi cela ressemblera :<br/>
Voici un paragraphe de texte ! Apprendre la science des données en ligne<br/>
Voici un deuxième paragraphe de texte ! Python<br/>
Comme vous pouvez le constater, l'ajout de classes et d'identifiants ne modifie en rien le
rendu des balises.<br/>
  
  
  
  Utilisation de Web Scraping pour améliorer la sécurité d'un site Web.<br/>
Est-ce que on peut désormais déterminer comment protéger nos sites Web contre ces
opérations malveillantes ? Avec une connaissance approfondie du web scraping, arrêter ces
attaques peut être plus facile à gérer..<br/>
Certaines des méthodes que l'on peut utiliser pour améliorer la cybersécurité contre le web
scraping incluent :.<br/>
Détecter toutes les activités de bot.<br/>
Les attaques de scraping Web sont lancées et menées par des bots. Mais si les entreprises
peuvent détecter leurs activités dès les premiers stades de l'attaque, il est possible de les
empêcher..<br/>
Les gens doivent continuer à vérifier souvent leurs modèles de trafic et leurs journaux. S'ils
identifient des activités les alertant d'une éventuelle attaque malveillante, ils peuvent se
déplacer rapidement pour limiter l'accès du bot ou même bloquer complètement l'opération.
Les indicateurs d'une attaque de grattage Web incluent :.<br/>
 Tente d'accéder aux fichiers cachés.<br/>
 Actions répétitives provenant de la même IP.<br/>

__2. Autres conseils pour identifier les attaques de Web Scraping__
Alors que la méthode la plus courante utilisée par les gens pour détecter les activités des
bots sur leurs sites Web est basée sur l'IP, les bots deviennent de plus en plus sophistiqués. Ils
peuvent naviguer entre des milliers voire des millions d'adresses IP.<br/>
Par conséquent, pour être plus efficace, il faut utiliser d'autres approches pour détecter tout
indicateur indiquant que leur site Web est attaqué. Ces indicateurs incluent la vitesse à
laquelle le faux utilisateur remplit les formulaires, les clics et les mouvements de la souris.
Les méthodes à utiliser pour détecter ces indicateurs comprennent :<br/>
 Utilisation de JavaScript : avec JavaScript, les sites Web peuvent collecter de nombreuses
informations, y compris la résolution/taille de l'écran et les polices installées, entre autres. Par
exemple, recevoir de nombreuses demandes de différents utilisateurs avec les mêmes tailles
d'écran devrait déclencher des drapeaux rouges, surtout si l'utilisateur continue de cliquer sur
un bouton à intervalles réguliers. Il y a de fortes chances que ce soit un grattoir.
 Requêtes répétitives similaires : Même si elles proviennent d'adresses IP différentes, elles
peuvent indiquer une attaque de web scraping.<br/>
 Limitation du débit : on peut ralentir les grattoirs Web en n'autorisant qu'un certain nombre
d'actions particulières à la fois. Par exemple, les propriétaires de sites Web abordent
généralement cela en limitant les recherches effectuées par seconde à partir de n'importe
quelle adresse IP ou utilisateur.<br/>
  
  Utilisation de CAPTCHAS : Les CAPTCHAs (Completely Automated Test to Tell
Computers and Humans Apart) sont conçus pour permettre aux utilisateurs légitimes
(humains) d'accéder aux services d'un site Web tout en filtrant les bots. Le seul problème est
que si de nombreux CAPTCHA rendent un site plus sûr, ils se traduisent souvent par une
expérience utilisateur beaucoup moins agréable.<br/>
#Les bibliothèques utiliser<br/>

Selenium WebDriver : Afin d’optimiser le processus de développement d’une application
sur le temps et les coûts dans Python, Jason Huggins a créé en 2004 l’essentiel de ce qui
constitue aujourd’hui le framework de testing Web Selenium à l’aide de
JavaScriptTestRunner.<br/>
WebDriver est l’interface essentielle permettant la simulation d’interactions avec les
utilisateurs dans n’importe quel navigateur (Firefox, Chrome, Edge, Safari ou Internet
Explorer). Depuis 2018, l’API est un standard W3C officiel.<br/>
 webdriver.Chrome : permettant la simulation d’interactions avec les utilisateurs
dans le navigateur chrome<br/>
 driver.get : La méthode driver.get naviguera vers une page donnée par l'URL.
WebDriver attendra que la page soit entièrement chargée (c'est-à-dire que
l'événement "onload" se soit déclenché) avant de rendre le contrôle à votre test ou
script. Sachez que si votre page utilise beaucoup d'AJAX au chargement,
WebDriver peut ne pas savoir quand il est complètement chargé
exemple : driver.get("http://www.python.org")<br/>
 driver.find_element_by_id : Le premier élément avec la valeur d'attribut id
correspondant à l'emplacement sera renvoyé.<br/>
 send_keys() : La méthode est utilisée pour envoyer du texte à n'importe quel
champ, tel qu'un champ de saisie d'un formulaire ou même pour ancrer un
paragraphe de balise, etc. Elle remplace son contenu sur la page Web de votre
navigateur<br/>
 bs = BeautifulSoup(driver.page_source) : Convertit la page Web / html / xml en
une arborescence composée de balises, d’éléments, D’attributs et de valeurs. Pour
être plus précis,<br/>
 pages=bs.find_all()<br/>
 bs.find : La méthode scanne le document entier à la recherche de résultats, mais
parfois vous ne voulez trouver qu'un seul résultat<br/>
  
  driver.find_element_by_xpath(): Le premier élément avec la syntaxe XPath
correspondant à l'emplacement sera renvoyé.<br/>
 driver.execute_script() : méthode synchrone Exécute JavaScript dans la
fenêtre/le cadre en cours. Il s'agit d'une grande fonctionnalité de Selenium, car
javascript peut tout faire avec un site Web, de l'accès aux API à la lecture de code
en direct.<br/>
 zip_longest(*file_list): Il imprime les valeurs des itérables alternativement en
séquence. Si l'un des itérables est entièrement imprimé, les valeurs restantes sont
remplies par les valeurs affectées au paramètre fillvalue.<br/>

Beautiful Soup est une bibliothèque Python qui utilise votre analyseur html xml pré-
installé et Convertit la page Web / html / xml en une arborescence composée de balises,
d’éléments, D’attributs et de valeurs. Pour être plus précis, l’arbre est constitué de quatre
types d’objets, Tag,NavigableString, BeautifulSoup et Comment. Cet arbre peut ensuite
être « interrogé » en utilisant les Méthodes / propriétés de l’objet BeautifulSoup créé à
partir de la bibliothèque de l’analyseur.<br/>
Le module csv en Python permet d’analyser les fichiers CSV (Comma Separated Values).
Un fichiers CSV contient des valeurs séparées par des virgules, que l’on utilise pour
stocker des données tabulaires.<br/>
En utilisant ce module, qui vient avec Python, nous pouvons facilement lire et écrire dans
des fichiers CSV. Chaque ligne du fichier csv est une ligne d’un tableau.
Itertools : Ce module standardise un ensemble de base d’outils rapides et efficaces en
mémoire qui peuvent être utilisés individuellement ou en les combinant. Ensemble, ils
forment une « algèbre d’itérateurs » rendant possible la construction rapide et efficace
d’outils spécialisés en Python.<br/>
Itertools.zip_longest(*iterables, fillvalue=None) Crée un itérateur qui agrège les éléments
de chacun des itérables. Si les itérables sont de longueurs différentes, les valeurs
manquantes sont remplacées par fillvalue. L’itération continue jusqu’à ce que l’itérable le
plus long soit épuisé.<br/>
Urllib.request : Bibliothèque extensible pour l’ouverture d’URL
Le module urllib.request définit des fonctions et des classes qui aident à ouvrir des URL
(principalement http) dans un monde complexe – authentification de base et digest,
redirections, cookies, etc.<br/>
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None,
cadefault=False, context=None)<br/>
  
  Ouvrez l'URL url , qui peut être une chaîne ou un objet Request .
data doit être un objet spécifiant des données supplémentaires à envoyer au serveur, ou
None si ces données ne sont pas nécessaires.<br/>
  
  ![image](https://user-images.githubusercontent.com/100286013/187097030-eceb25be-69e4-45b0-b3ca-b8bf2cc982cb.png)<br/>
  
  # Spécifier l’emplacement de navigateur utiliser dans notre cas ici nous avons travaillé sur lr
navigateur google chrome<br/>
driver=webdriver.Chrome('/Users/HP/AppData/Local/Temp/Rar$EXa10008.12544/chromedr
iver.exe')<br/>
# affiche la page en mode plein d’écran<br/>
driver.maximize_window()<br/>
# Rediriger à la page log in de réseaux professionnelle Linkdein<br/>
  
  
  
  driver.get('https://www.linkedin.com')<br/>
# Importer les données à partir de fichier séparer qui contient l’adresse email et mot de passe
de nous compte sur Linkin<br/>
cordonne = []<br/>
filename="/Users/HP/Desktop/S2 SSI/py/web scraping/cord.txt"
with open(filename) as file:<br/>
for line in file:<br/>
cordonne.append(line.rstrip())<br/>
#Maintenant, nous cherchons le champ d’insérer notre adresse mail sur la page log in par
l’élément ou le inertHTML spécifie par l’id session_key.<br/>
username = driver.find_element_by_id('session_key')<br/>
username.send_keys(cordonne[0])<br/>
sleep(3)<br/>
# La même technique pour remplir notre password sur le champ spécifie par l’id<br/>
session_password.<br/>
password = driver.find_element_by_id('session_password')<br/>
password.send_keys(cordonne[1])<br/>
sleep(3)<br/>
# Déterminer l'emplacement de button connexion par son xpath sur la page login<br/>
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')<br/>
# Click button<br/>
sign_in_button.click()<br/>
# allez et rediriger à url indiquer ci-dessus dont il est la recherche des offres d’emploi que vous
concernez notre cas ici c’est reactjs.<br/>
driver.get('https://www.linkedin.com/jobs/search/?keywords=reactjs')<br/>
  
![image](https://user-images.githubusercontent.com/100286013/187097076-07305863-e383-42dd-8573-4a473f8555f7.png)<br/>
  
  -Déclare 4 liste dans lesquelles on va affecter les textes a partir de convertir les listes des
listes des objets html aux textes par l’utilisation de fonction remplir qui va prendre comme
un argument liste des objets html et parcourir élément par élément et les convertir aux textes
avec des modification sur la forme de données collectées.<br/>
  
  ![image](https://user-images.githubusercontent.com/100286013/187097109-7049431c-ed1b-4691-9fa8-67719b17af13.png)<br/>
  
  
  ![image](https://user-images.githubusercontent.com/100286013/187097117-278ea8a2-3cf3-4074-afcd-e836682be637.png)<br/>
  
  ![image](https://user-images.githubusercontent.com/100286013/187097128-41dcd24b-fe90-449e-9028-b727ff295068.png)




