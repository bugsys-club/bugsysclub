"""Génère le site Bugsy's Social Club en français (index.html) et en anglais (en/index.html).
Modifier les textes dans TEXTES, puis lancer : python3 build.py
"""
import os

SITE_URL = "https://bugsys-club.github.io/bugsysclub/"

LOGO = """<svg viewBox="0 0 220 220" role="img" aria-label="Monogramme BS de Bugsy’s Social Club">
  <defs><linearGradient id="or" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#F3DE9C"/><stop offset="0.45" stop-color="#C9A45C"/>
    <stop offset="0.7" stop-color="#7E6127"/><stop offset="1" stop-color="#F3DE9C"/></linearGradient></defs>
  <circle cx="110" cy="110" r="104" fill="none" stroke="url(#or)" stroke-width="3"/>
  <circle cx="110" cy="110" r="95" fill="none" stroke="url(#or)" stroke-width="1.5"/>
  <circle cx="110" cy="110" r="88" fill="none" stroke="url(#or)" stroke-width="1"/>
  <text x="110" y="138" text-anchor="middle" font-family="Monoton, serif" font-size="76" fill="url(#or)">BS</text>
</svg>"""

TEXTES = {
    "fr": {
        "lang": "fr", "dossier": "", "autre": "en/", "autre_label": "EN",
        "title": "Bugsy’s Social Club — Café, steak house & club à Yaoundé",
        "description": "Bugsy’s Social Club, à Bastos, Yaoundé : café le matin, steak house et fruits de mer le jour, soul jazz et musiques africaines le jeudi, DJ sets funky, hip-hop et deep house la nuit.",
        "nav": ["Le concept", "La carte", "Le jazz", "La galerie", "Le club", "La danse", "Membres", "Contact"],
        "danse_eyebrow": "L’école de danse",
        "danse_titre": "Danse et books",
        "danse_intro": "Le jour, la piste du club devient un studio. On y apprend, on y répète, et on y fait les images qui font connaître les danseurs.",
        "danse_styles": ["Afro", "Hip-hop", "Contemporain", "Salsa", "Street jazz", "Modern jazz"],
        "danse_rdv": [("Cours · du lundi au jeudi, en journée", "Tous niveaux, du premier pas au danseur confirmé."), ("Books photo", "Shootings pour les artistes et les compagnies : portraits, mouvement, scène.")],
        "danse_alts": ["Dos nu d’une danseuse sur fond noir, drapé rouge", "Danseuses et danseur de contemporain sur fond noir", "Duo de danse, bras levés", "Danseuse au sol sous une lumière cuivrée", "Danseuse en cambré, cheveux au sol", "Trois danseuses d’afro en plein air", "Danseuse au sol, jambe tendue vers le ciel", "Danseuse au corps peint devant un mur de graffitis", "Couple de salsa en mouvement, robe rouge sur le parquet"],
        "sous": "Steak house & sea food · Yaoundé",
        "accroche": "Un café le matin, une grande table le soir, un club la nuit.",
        "cta": "Ouverture prochaine",
        "concept_eyebrow": "Le concept",
        "concept_titre": "Une adresse, trois temps",
        "concept_intro": "Au cœur du quartier Bastos, Bugsy’s réunit sous le même toit un café, un steak house et un club, dans l’esprit des clubs américains des années 40.",
        "temps": [
            ("8h – 11h", "Le Café", "Espresso, café de l’Ouest camerounais, petit-déjeuner d’affaires."),
            ("12h – 23h", "Le Restaurant", "Grill et fruits de mer, relevés de poivre de Penja et de sauces maison."),
            ("Jeudi – samedi, 23h – 4h", "Le Club", "DJ sets funky, hip-hop et deep house : la salle du dîner devient la piste."),
        ],
        "galerie_alt": ["Grand plateau de viandes braisées, riz rouge et sauces maison", "Poisson braisé, salsa de poivrons et citron vert", "Cocktail servi dans une timbale en cuivre", "Verre de vin rouge au-dessus d’une table garnie", "Champagnes sur une table du lounge"],
        "racines_alt": ["Acacia solitaire dans la savane au coucher du soleil", "Barques de pêche colorées sur une plage africaine"],
        "carte_eyebrow": "La carte",
        "cuisine_alts": ["Côte de bœuf tomahawk suspendue au-dessus du gril", "La brigade en cuisine dresse des entrecôtes et des frites", "Carafe de cognac extra dans la lumière du bar", "Crêpes flambées à l’orange"],
        "carte_titre": "Les saveurs d’ici, le grill en plus",
        "carte_pdf": ["Télécharger la carte du restaurant (PDF)", "Télécharger la carte du bar et du club (PDF)"],
        "carte_prix": "Prix en francs CFA, service compris · Allergènes sur demande · L’abus d’alcool est dangereux pour la santé",
        "jazz_eyebrow": "Le jazz",
        "jazz_titre": "Le jazz en signature",
        "musique_titre": "L’inspiration musicale",
        "galerie_eyebrow": "La galerie",
        "galerie_titre": "Vernissages",
        "galerie_intro": "Les toiles exposées aux murs de Bugsy’s. Une nouvelle exposition chaque trimestre, un vernissage un mercredi par mois.",
        "galerie_cartel": "Collection Bugsy’s",
        "galerie_alts": ["Peinture abstraite aux aplats rouges, jaunes et bleus", "Peinture d’un léopard des neiges aux yeux turquoise", "Toile abstraite aux symboles dorés sur fond rouge et bleu"],
        "jazz_alt": ["Scène de jazz tamisée : contrebasse, batterie, piano et micro à la lueur des bougies", "Peinture d’une chanteuse de jazz accompagnée d’un pianiste et d’un contrebassiste", "Club de jazz art déco : chanteuse sur scène, danseurs et banquettes de velours rouge"],
        "jazz_intro": "Du soul jazz aux grooves africains, le Cameroun a donné à la musique quelques-unes de ses plus grandes voix. Chez Bugsy’s, on dîne au son d’un live, puis les platines prennent le relais.",
        "rdv": [("Jeudis Soul Jazz · 20h – 23h", "Soul jazz et musiques africaines en live pendant le dîner, puis le DJ prend le relais."), ("Galerie tournante", "Peintres et sculpteurs camerounais aux murs, œuvres à vendre."), ("Vernissage · un mercredi par mois", "Soirée sur invitation autour de l’artiste exposé.")],
        "club_alt": "Peinture d’une danseuse en robe rouge tourbillonnante, à la lueur des bougies",
        "club_eyebrow": "Le club",
        "club_titre": "Jazz and Night Club",
        "club_intro": "Du jeudi au samedi, de 23h à 4h : DJ sets funky, hip-hop et deep house, service bouteilles et entrée offerte aux clients du dîner.",
        "membres_eyebrow": "Membres",
        "membres_titre": "Le cercle Bugsy’s",
        "membres_intro": "Trois cartes pour les habitués du club. Les avantages de chaque niveau seront annoncés à l’ouverture.",
        "niveaux": ["Membre", "Gold", "Black"],
        "contact_eyebrow": "Contact",
        "contact_titre": "Ouverture prochaine",
        "contact_intro": "Réservations, privatisations et cartes de membre : les coordonnées seront publiées ici très bientôt.",
        "lieu": "Bastos · Yaoundé · Cameroun",
        "footer": "© Bugsy’s Social Club · Yaoundé",
        "fondateur": "Fondé par Guy Erick Tamokwe",
        "partenaires_eyebrow": "Partenaires",
        "partenaires_texte": "Bugsy’s s’associe aux compagnies, aux festivals et aux maisons qui partagent sa vision de Yaoundé : la danse, le jazz et la création, au même endroit.",
        "partenaires_btn": "Devenir partenaire",
        "form": {"nom": "Nom", "email": "E-mail", "objet": "Objet", "objets": ["Réservation", "Privatisation", "Carte de membre", "Partenariat", "Autre demande"], "message": "Message", "envoyer": "Envoyer", "merci": "Merci, votre message a bien été envoyé. Nous vous répondrons très vite.", "erreur": "L’envoi n’a pas abouti. Merci de réessayer dans un instant."},
        "contact_intro_form": "Réservations, privatisations et cartes de membre : écrivez-nous, nous vous répondrons personnellement.",
    },
    "en": {
        "lang": "en", "dossier": "../", "autre": "../", "autre_label": "FR",
        "title": "Bugsy’s Social Club — Café, steak house & club in Yaoundé",
        "description": "Bugsy’s Social Club, in Bastos, Yaoundé: a café by morning, a steak house & seafood restaurant by day, soul jazz and African music on Thursdays, funky, hip-hop and deep house DJ sets by night.",
        "nav": ["The concept", "The menu", "Jazz", "The gallery", "The club", "Dance", "Members", "Contact"],
        "danse_eyebrow": "The dance school",
        "danse_titre": "Dance and books",
        "danse_intro": "By day, the club floor becomes a studio. Dancers come to learn, to rehearse, and to make the images that get them seen.",
        "danse_styles": ["Afro", "Hip-hop", "Contemporary", "Salsa", "Street jazz", "Modern jazz"],
        "danse_rdv": [("Classes · Monday to Thursday, daytime", "All levels, from first steps to experienced dancers."), ("Photo books", "Shoots for artists and dance companies: portraits, movement, stage.")],
        "danse_alts": ["Bare back of a dancer against black, red drape", "Contemporary dancers against a black background", "Dance duo, arms raised", "Dancer on the floor under copper light", "Dancer in a backbend, hair on the floor", "Three afro dancers outdoors", "Dancer on the floor, one leg raised to the sky", "Body-painted dancer against a graffiti wall", "Salsa couple in motion, red dress on the dance floor"],
        "sous": "Steak house & sea food · Yaoundé",
        "accroche": "A café by morning, a grand table by evening, a club by night.",
        "cta": "Opening soon",
        "concept_eyebrow": "The concept",
        "concept_titre": "One address, three moments",
        "concept_intro": "In the heart of Bastos, Bugsy’s brings a café, a steak house and a club under one roof, in the spirit of 1940s American supper clubs.",
        "temps": [
            ("8am – 11am", "The Café", "Espresso, coffee from Cameroon’s West region, business breakfasts."),
            ("Noon – 11pm", "The Restaurant", "Grill and seafood, with Penja pepper and house sauces."),
            ("Thursday – Saturday, 11pm – 4am", "The Club", "Funky, hip-hop and deep house DJ sets: the dining room becomes the dance floor."),
        ],
        "galerie_alt": ["Platter of braised meats, red rice and house sauces", "Braised fish with pepper salsa and lime", "Cocktail served in a copper cup", "Glass of red wine above a laid table", "Champagne on a lounge table"],
        "racines_alt": ["Lone acacia tree on the savannah at sunset", "Colourful fishing boats on an African beach"],
        "carte_eyebrow": "The menu",
        "cuisine_alts": ["Tomahawk steak hanging over the grill", "The kitchen brigade plating sliced steaks and fries", "Decanter of extra cognac in the bar light", "Orange crêpes, flambéed"],
        "carte_titre": "Local flavours, and the grill",
        "carte_pdf": ["Download the restaurant menu (PDF)", "Download the bar & club menu (PDF)"],
        "carte_prix": "Prices in CFA francs, service included · Allergens on request · Please drink responsibly",
        "jazz_eyebrow": "Jazz",
        "jazz_titre": "Jazz at the heart",
        "musique_titre": "Musical inspiration",
        "galerie_eyebrow": "The gallery",
        "galerie_titre": "Opening Nights",
        "galerie_intro": "The paintings on the walls of Bugsy’s. A new exhibition every quarter, an opening night one Wednesday a month.",
        "galerie_cartel": "Bugsy’s collection",
        "galerie_alts": ["Abstract painting in red, yellow and blue blocks", "Painting of a snow leopard with turquoise eyes", "Abstract canvas with golden symbols on red and blue"],
        "jazz_alt": ["Dimly lit jazz stage: double bass, drums, piano and microphone by candlelight", "Painting of a jazz singer with a pianist and a double bass player", "Art deco jazz club: singer on stage, dancers and red velvet banquettes"],
        "jazz_intro": "From soul jazz to African grooves, Cameroon has given music some of its greatest voices. At Bugsy’s, dinner comes with live music, then the decks take over.",
        "rdv": [("Soul Jazz Thursdays · 8pm – 11pm", "Live soul jazz and African music over dinner, then the DJ takes over."), ("Rotating gallery", "Cameroonian painters and sculptors on the walls, works for sale."), ("Opening night · one Wednesday a month", "An invitation-only evening around the featured artist.")],
        "club_alt": "Painting of a dancer in a swirling red dress, by candlelight",
        "club_eyebrow": "The club",
        "club_titre": "Jazz and Night Club",
        "club_intro": "Thursday to Saturday, 11pm to 4am: funky, hip-hop and deep house DJ sets, bottle service and free entry for dinner guests.",
        "membres_eyebrow": "Members",
        "membres_titre": "The Bugsy’s circle",
        "membres_intro": "Three cards for the club’s regulars. The benefits of each tier will be announced at the opening.",
        "niveaux": ["Member", "Gold", "Black"],
        "contact_eyebrow": "Contact",
        "contact_titre": "Opening soon",
        "contact_intro": "Bookings, private events and membership cards: contact details will be published here very soon.",
        "lieu": "Bastos · Yaoundé · Cameroon",
        "footer": "© Bugsy’s Social Club · Yaoundé",
        "fondateur": "Founded by Guy Erick Tamokwe",
        "partenaires_eyebrow": "Partners",
        "partenaires_texte": "Bugsy’s works with the companies, festivals and houses that share its vision of Yaoundé: dance, jazz and creation, under one roof.",
        "partenaires_btn": "Become a partner",
        "form": {"nom": "Name", "email": "Email", "objet": "Subject", "objets": ["Booking", "Private event", "Membership card", "Partnership", "Other enquiry"], "message": "Message", "envoyer": "Send", "merci": "Thank you, your message has been sent. We will reply very soon.", "erreur": "Your message could not be sent. Please try again in a moment."},
        "contact_intro_form": "Bookings, private events and membership cards: write to us and we will reply personally.",
    },
}

CARTE_FR = [
  ("Le restaurant", "12h – 23h", [
    ("Salades et entrées", "", [
      ("Salade Bugsy’s", "Avocat, crevettes, mangue, vinaigrette passion", "6 000"),
      ("Salade Bastos", "Crudités, avocat, œuf, vinaigrette maison", "4 000"),
      ("Soya", "Brochettes de bœuf épicées au grill, oignons, piment", "3 500")]),
    ("Spécialités", "", [
      ("Ndolé aux crevettes", "Feuilles de ndolé, arachides, crevettes, plantain mûr", "7 000"),
      ("Poulet DG", "Plantains mûrs, carottes, haricots verts", "7 500"),
      ("Mafé, au choix", "Sauce à l’arachide, riz blanc · bœuf ou poulet 6 000 · agneau 7 500", "dès 6 000"),
      ("Yassa, au choix", "Oignons confits au citron, riz blanc · poulet 6 500 · poisson 8 000 · crevettes 9 000", "dès 6 500"),
      ("Poisson braisé entier", "Bar ou capitaine, alloco, bâton de manioc", "9 000"),
      ("Capitaine au mbongo tchobi", "Sauce noire aux épices, bâton de manioc", "9 000")]),
    ("Le grill", "Sauce au poivre blanc de Penja ou piment maison", [
      ("Dibi d’agneau", "Agneau braisé, oignons, moutarde, alloco", "9 000"),
      ("Entrecôte tranchée, 300 g", "Servie en poêle, fleur de sel, frites maison ou alloco", "12 000"),
      ("Gambas grillées", "Beurre citronné, riz jollof", "12 000")]),
    ("À partager", "", [
      ("Le Plateau Bugsy’s", "Pour deux : ndolé, poulet DG, poisson braisé, soya, trois accompagnements", "25 000")]),
    ("Accompagnements", "Alloco · Riz blanc · Riz jollof · Miondo · Bâton de manioc · Frites maison", [
      ("L’accompagnement", "", "1 500")]),
    ("Desserts", "", [
      ("Salade de fruits frais", "Mangue, ananas, papaye", "3 000"),
      ("Beignets soufflés", "Caramel de bissap", "2 500"),
      ("Crème brûlée", "Vanille ou bissap", "3 500"),
      ("Fondant au cacao du Cameroun", "Cœur coulant, glace vanille", "4 000")]),
  ]),
  ("Le café, le bar et le club", "8h – 4h", [
    ("Le café · 8h – 11h", "", [
      ("Espresso", "", "1 500"), ("Café filtre de l’Ouest", "", "2 000"), ("Cappuccino", "", "2 500"),
      ("Toast avocat, œufs brouillés", "", "5 500"),
      ("Petit-déjeuner Bugsy’s", "Viennoiserie, jus pressé, boisson chaude", "6 500")]),
    ("Cocktails signature", "", [
      ("The Bugsy", "Bourbon, sirop de bissap, angostura", "8 500"),
      ("Flamingo", "Gin, passion, hibiscus, tonic", "7 500"),
      ("Penja Old Fashioned", "Whisky, sirop au poivre de Penja, orange", "8 500"),
      ("Copper Mule", "Vodka, gingembre frais, citron vert, timbale de cuivre", "7 000"),
      ("Gold Rush Espresso", "Vodka, café de l’Ouest, liqueur de cacao", "8 000"),
      ("Bissap Royal", "Sirop de bissap maison, champagne brut", "9 000")]),
    ("Sans alcool", "", [
      ("Foléré gingembre", "", "3 500"), ("Citronnade menthe", "", "3 500"),
      ("Mangue-passion pressé", "", "4 000"), ("Copper Mule sans alcool", "", "4 500")]),
    ("Vins et bière", "", [
      ("Vin au verre", "", "5 000"), ("Bouteille de vin", "", "dès 25 000"),
      ("Coupe de champagne", "", "12 000"), ("Bière", "", "2 000")]),
    ("Le club · jeudi à samedi, 23h – 4h", "Softs et glace inclus avec chaque bouteille · Entrée offerte aux clients du dîner", [
      ("Champagne brut", "", "75 000"), ("Champagne blanc de blancs", "", "110 000"), ("Champagne rosé", "", "120 000"),
      ("Vodka premium, 70 cl", "", "60 000"), ("Whisky 12 ans, 70 cl", "", "70 000"), ("Cognac VSOP, 70 cl", "", "85 000")]),
    ("Grandes maisons", "Au salon ou au club", [
      ("Dom Pérignon", "Champagne millésimé, 75 cl", "450 000"),
      ("Petrus", "Pomerol, 75 cl", "sur demande"),
      ("Lise Baccara Extra", "Cognac, 70 cl", "250 000")]),
  ]),
]
CARTE_EN = [
  ("The restaurant", "Noon – 11pm", [
    ("Salads and starters", "", [
      ("Bugsy’s salad", "Avocado, prawns, mango, passion fruit dressing", "6 000"),
      ("Bastos salad", "Raw vegetables, avocado, egg, house dressing", "4 000"),
      ("Soya", "Spiced grilled beef skewers, onions, chilli", "3 500")]),
    ("Local specialities", "", [
      ("Ndolé with prawns", "Ndolé leaves, peanuts, prawns, ripe plantain", "7 000"),
      ("Chicken DG", "Ripe plantain, carrots, green beans", "7 500"),
      ("Mafé, your choice", "Peanut sauce, white rice · beef or chicken 6 000 · lamb 7 500", "from 6 000"),
      ("Yassa, your choice", "Onions slow-cooked with lemon, white rice · chicken 6 500 · fish 8 000 · prawns 9 000", "from 6 500"),
      ("Whole braised fish", "Sea bass or captain fish, alloco, cassava stick", "9 000"),
      ("Captain fish in mbongo tchobi", "Spiced black sauce, cassava stick", "9 000")]),
    ("The grill", "White Penja pepper sauce or house chilli", [
      ("Lamb dibi", "Braised lamb, onions, mustard, alloco", "9 000"),
      ("Sliced rib-eye, 300 g", "Served in the pan, sea salt flakes, house fries or alloco", "12 000"),
      ("Grilled king prawns", "Lemon butter, jollof rice", "12 000")]),
    ("To share", "", [
      ("The Bugsy’s platter", "For two: ndolé, chicken DG, braised fish, soya, three sides", "25 000")]),
    ("Sides", "Alloco · White rice · Jollof rice · Miondo · Cassava stick · House fries", [
      ("Side dish", "", "1 500")]),
    ("Desserts", "", [
      ("Fresh fruit salad", "Mango, pineapple, papaya", "3 000"),
      ("Puff-puff", "Bissap caramel", "2 500"),
      ("Crème brûlée", "Vanilla or bissap", "3 500"),
      ("Cameroon cocoa fondant", "Molten centre, vanilla ice cream", "4 000")]),
  ]),
  ("The café, the bar and the club", "8am – 4am", [
    ("The café · 8am – 11am", "", [
      ("Espresso", "", "1 500"), ("Filter coffee from the West region", "", "2 000"), ("Cappuccino", "", "2 500"),
      ("Avocado toast, scrambled eggs", "", "5 500"),
      ("Bugsy’s breakfast", "Pastry, fresh juice, hot drink", "6 500")]),
    ("Signature cocktails", "", [
      ("The Bugsy", "Bourbon, hibiscus syrup, bitters", "8 500"),
      ("Flamingo", "Gin, passion fruit, hibiscus, tonic", "7 500"),
      ("Penja Old Fashioned", "Whisky, Penja pepper syrup, orange", "8 500"),
      ("Copper Mule", "Vodka, fresh ginger, lime, copper cup", "7 000"),
      ("Gold Rush Espresso", "Vodka, West region coffee, cacao liqueur", "8 000"),
      ("Bissap Royal", "House hibiscus syrup, brut champagne", "9 000")]),
    ("Alcohol-free", "", [
      ("Ginger foléré", "", "3 500"), ("Mint lemonade", "", "3 500"),
      ("Fresh mango-passion", "", "4 000"), ("Alcohol-free Copper Mule", "", "4 500")]),
    ("Wine and beer", "", [
      ("Wine by the glass", "", "5 000"), ("Bottle of wine", "", "from 25 000"),
      ("Glass of champagne", "", "12 000"), ("Beer", "", "2 000")]),
    ("The club · Thursday to Saturday, 11pm – 4am", "Soft drinks and ice included with every bottle · Free entry for dinner guests", [
      ("Brut champagne", "", "75 000"), ("Blanc de blancs champagne", "", "110 000"), ("Rosé champagne", "", "120 000"),
      ("Premium vodka, 70 cl", "", "60 000"), ("12-year-old whisky, 70 cl", "", "70 000"), ("Cognac VSOP, 70 cl", "", "85 000")]),
    ("Prestige bottles", "In the lounge or at the club", [
      ("Dom Pérignon", "Vintage champagne, 75 cl", "450 000"),
      ("Petrus", "Pomerol, 75 cl", "on request"),
      ("Lise Baccara Extra", "Cognac, 70 cl", "250 000")]),
  ]),
]

CARTES = {"fr": CARTE_FR, "en": CARTE_EN}

# Formspree : identifiant du formulaire (ex. "xyzabcde"). Vide = formulaire masqué.
FORMSPREE_ID = ""

def formulaire(t):
    if not FORMSPREE_ID:
        return ""
    f = t["form"]
    options = "".join(f'<option>{o}</option>' for o in f["objets"])
    return f'''<form class="formulaire" action="https://formspree.io/f/{FORMSPREE_ID}" method="POST" data-merci="{f['merci']}" data-erreur="{f['erreur']}">
    <div class="champs">
      <label>{f['nom']}<input type="text" name="nom" required autocomplete="name"></label>
      <label>{f['email']}<input type="email" name="email" required autocomplete="email"></label>
    </div>
    <label>{f['objet']}<select name="objet">{options}</select></label>
    <label>{f['message']}<textarea name="message" rows="5" required></textarea></label>
    <input type="text" name="_gotcha" class="piege" tabindex="-1" autocomplete="off" aria-hidden="true">
    <button class="btn" type="submit">{f['envoyer']}</button>
    <p class="retour" role="status"></p>
  </form>
  <script>
  document.querySelectorAll('[data-objet]').forEach(function (b) {{
    b.addEventListener('click', function () {{ var sel = document.querySelector('.formulaire select'); if (sel) sel.value = b.dataset.objet; }});
  }});
  document.querySelectorAll('.formulaire').forEach(function (form) {{
    form.addEventListener('submit', function (e) {{
      e.preventDefault();
      var retour = form.querySelector('.retour'), bouton = form.querySelector('button');
      bouton.disabled = true;
      fetch(form.action, {{ method: 'POST', body: new FormData(form), headers: {{ 'Accept': 'application/json' }} }})
        .then(function (r) {{ if (!r.ok) throw r; form.reset(); retour.textContent = form.dataset.merci; }})
        .catch(function () {{ retour.textContent = form.dataset.erreur; }})
        .finally(function () {{ bouton.disabled = false; }});
    }});
  }});
  </script>'''

ANCRES = ["concept", "carte", "jazz", "galerie", "club", "danse", "membres", "contact"]
PHOTOS = ["plateau", "poisson", "cocktail", "vin", "champagne"]


def jsonld(t, url):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": ["Restaurant", "BarOrPub"],
        "name": "Bugsy’s Social Club",
        "url": url,
        "description": t["description"],
        "image": SITE_URL + "assets/img/plateau.jpg",
        "servesCuisine": ["Cameroonian", "African", "Steakhouse", "Seafood"],
        "address": {"@type": "PostalAddress", "addressLocality": "Yaoundé", "addressRegion": "Bastos", "addressCountry": "CM"},
        "inLanguage": t["lang"],
        "founder": {"@type": "Person", "name": "Guy Erick Tamokwe"},
    }
    return json.dumps(data, ensure_ascii=False)


def page(t):
    d = t["dossier"]
    nav = "".join(f'<a href="#{a}">{l}</a>' for a, l in zip(ANCRES, t["nav"]))
    temps = "".join(f'<div class="temps"><div class="heure">{h}</div><h3>{n}</h3><p>{p}</p></div>' for h, n, p in t["temps"])
    galerie = "".join(f'<img src="{d}assets/img/{p}.jpg" alt="{a}" loading="lazy">' for p, a in zip(PHOTOS, t["galerie_alt"]))
    def bloc(cat, note, plats):
        lignes = "".join(
            f'<p class="plat"><span class="ligne"><strong>{n}</strong><b class="prix">{px}</b></span>'
            + (f'<span class="desc">{desc}</span>' if desc else '') + '</p>'
            for n, desc, px in plats)
        return f'<div class="rubrique"><h3>{cat}</h3>' + (f'<p class="note">{note}</p>' if note else '') + lignes + '</div>'
    pdfs = ["bugsys-carte-restaurant.pdf", "bugsys-carte-bar-club.pdf"]
    carte = "".join(
        f'<div class="volet"><p class="volet-titre">{titre} <span>{heures}</span></p><div class="carte">'
        + "".join(bloc(*r) for r in rubriques)
        + f'</div><a class="btn" href="{d}assets/cartes/{pdf}" download>{lien}</a></div>'
        for (titre, heures, rubriques), pdf, lien in zip(CARTES[t["lang"]], pdfs, t["carte_pdf"]))
    rdv = "".join(f'<p class="rdv"><b>{a}</b>{b}</p>' for a, b in t["rdv"])
    classes = ["m-membre", "m-gold", "m-black"]
    membres = "".join(f'<div class="carte-membre {c}"><div class="nom">BUGSY’S</div><div class="niveau">{n.upper()}</div></div>' for c, n in zip(classes, t["niveaux"]))
    url = SITE_URL + ("en/" if t["lang"] == "en" else "")
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['description']}">
<meta name="google-site-verification" content="RqMSrApwnwL7EWHjoufAK615FxAHIwPgRF8zSP913zs">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="fr" href="{SITE_URL}">
<link rel="alternate" hreflang="en" href="{SITE_URL}en/">
<meta property="og:title" content="{t['title']}">
<meta property="og:description" content="{t['description']}">
<meta property="og:image" content="{SITE_URL}assets/img/plateau.jpg">
<meta property="og:url" content="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Limelight&family=Monoton&family=Josefin+Sans:wght@400;600&family=Cormorant+Garamond:ital,wght@1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{d}assets/style.css">
<link rel="icon" href="{d}assets/favicon.svg" type="image/svg+xml">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{jsonld(t, url)}</script>
</head>
<body>
<header class="header"><div class="wrap">
  <a class="brand" href="#top">BUGSY’S</a>
  <nav class="nav">{nav}<a class="lang" href="{t['autre']}" hreflang="{'en' if t['lang']=='fr' else 'fr'}">{t['autre_label']}</a><button class="burger" type="button" aria-expanded="false" aria-controls="sommaire">{'Sommaire' if t['lang']=='fr' else 'Contents'}</button></nav>
</div></header>
<div class="sommaire" id="sommaire" hidden>
  <p class="sommaire-titre">{'Sommaire' if t['lang']=='fr' else 'Contents'}</p>
  <ol>{"".join(f'<li><a href="#{a}">{l}</a></li>' for a, l in zip(ANCRES, t["nav"]))}</ol>
  <button class="fermer" type="button">{'Fermer' if t['lang']=='fr' else 'Close'}</button>
</div>
<script>
(function () {{
  var b = document.querySelector('.burger'), s = document.getElementById('sommaire');
  function ouvrir(o) {{ s.hidden = !o; b.setAttribute('aria-expanded', o); document.body.style.overflow = o ? 'hidden' : ''; }}
  b.addEventListener('click', function () {{ ouvrir(s.hidden); }});
  s.querySelector('.fermer').addEventListener('click', function () {{ ouvrir(false); }});
  s.querySelectorAll('a').forEach(function (a) {{ a.addEventListener('click', function () {{ ouvrir(false); }}); }});
}})();
</script>
<main id="top">
<section class="hero"><div class="wrap"><div class="hero-frame"><div class="hero-inner">
  {LOGO}
  <h1>BUGSY’S</h1>
  <p class="club">SOCIAL CLUB</p>
  <p class="sous">{t['sous']}</p>
  <p class="accroche">{t['accroche']}</p>
  <a class="btn" href="#contact">{t['cta']}</a>
</div></div></div></section>

<section class="section clair" id="concept"><div class="wrap">
  <p class="eyebrow">{t['concept_eyebrow']}</p>
  <h2>{t['concept_titre']}</h2>
  <p class="intro">{t['concept_intro']}</p>
  <div class="trois">{temps}</div>
</div></section>

<section class="section"><div class="wrap"><div class="galerie">{galerie}</div></div></section>

<section class="section illustrations"><div class="wrap"><div class="racines">
    <img src="{d}assets/img/savane.jpg" alt="{t['racines_alt'][0]}" loading="lazy">
    <img src="{d}assets/img/barques.jpg" alt="{t['racines_alt'][1]}" loading="lazy">
</div></div></section>

<section class="section" id="carte"><div class="wrap">
  <p class="eyebrow">{t['carte_eyebrow']}</p>
  <h2>{t['carte_titre']}</h2>
  {carte}
  <p class="mention">{t['carte_prix']}</p>
</div></section>

<section class="section illustrations"><div class="wrap"><div class="cuisine">
  <img src="{d}assets/img/cuisine-tomahawk.jpg" alt="{t['cuisine_alts'][0]}" loading="lazy">
  <img src="{d}assets/img/cuisine-brigade.jpg" alt="{t['cuisine_alts'][1]}" loading="lazy">
  <img src="{d}assets/img/cuisine-cognac.jpg" alt="{t['cuisine_alts'][2]}" loading="lazy">
  <img src="{d}assets/img/cuisine-crepes.jpg" alt="{t['cuisine_alts'][3]}" loading="lazy">
</div></div></section>

<section class="section clair" id="jazz"><div class="wrap"><div class="jazz">
  <div>
    <p class="eyebrow">{t['jazz_eyebrow']}</p>
    <h2>{t['jazz_titre']}</h2>
    <p class="intro">{t['jazz_intro']}</p>
    {rdv}
  </div>
  <div class="jazz-photos">
    <img src="{d}assets/img/jazz-scene.jpg" alt="{t['jazz_alt'][0]}" loading="lazy">
    <img src="{d}assets/img/jazz-peinture.jpg" alt="{t['jazz_alt'][1]}" loading="lazy">
    <img src="{d}assets/img/jazz-club.jpg" alt="{t['jazz_alt'][2]}" loading="lazy">
  </div>
</div>
<aside class="encart-musique">
  <p class="encart-titre">{t['musique_titre']}</p>
  <ul>
    <li>Soul Jazz</li>
    <li>African Music</li>
    <li>DJ set<span>Funky · Hip-hop · <i>Deep House</i></span></li>
  </ul>
</aside>
</div></section>

<section class="section galerie-art" id="galerie"><div class="wrap">
  <p class="eyebrow">{t['galerie_eyebrow']}</p>
  <h2>{t['galerie_titre']}</h2>
  <p class="intro">{t['galerie_intro']}</p>
  <div class="oeuvres">
    <figure><img src="{d}assets/img/galerie-abstraction.jpg" alt="{t['galerie_alts'][0]}" loading="lazy"><figcaption>{t['galerie_cartel']}</figcaption></figure>
    <figure><img src="{d}assets/img/galerie-leopard.jpg" alt="{t['galerie_alts'][1]}" loading="lazy"><figcaption>{t['galerie_cartel']}</figcaption></figure>
    <figure><img src="{d}assets/img/galerie-symboles.jpg" alt="{t['galerie_alts'][2]}" loading="lazy"><figcaption>{t['galerie_cartel']}</figcaption></figure>
  </div>
</div></section>

<section class="section" id="club"><div class="wrap"><div class="jazz">
  <img class="club-image" src="{d}assets/img/club-danseuse.jpg" alt="{t['club_alt']}" loading="lazy">
  <div>
    <p class="eyebrow">{t['club_eyebrow']}</p>
    <h2>{t['club_titre']}</h2>
    <p class="intro">{t['club_intro']}</p>
  </div>
</div></div></section>

<section class="section galerie-art" id="danse"><div class="wrap">
  <div class="jazz">
    <div>
      <p class="eyebrow">{t['danse_eyebrow']}</p>
      <h2>{t['danse_titre']}</h2>
      <p class="intro">{t['danse_intro']}</p>
      <ul class="styles">{"".join(f'<li>{x}</li>' for x in t['danse_styles'])}</ul>
      {"".join(f'<p class="rdv"><b>{a}</b>{b}</p>' for a, b in t['danse_rdv'])}
    </div>
    <div class="danse-photos">{"".join(f'<img src="{d}assets/img/{n}.jpg" alt="{a}" loading="lazy">' for n, a in zip(["danse-dos", "danse-contemporain", "danse-duo", "danse-sol", "danse-solo", "danse-cambre", "danse-graffiti", "danse-afro", "danse-salsa"], t['danse_alts']))}</div>
  </div>
</div></section>

<section class="section clair" id="membres"><div class="wrap">
  <p class="eyebrow">{t['membres_eyebrow']}</p>
  <h2>{t['membres_titre']}</h2>
  <p class="intro">{t['membres_intro']}</p>
  <div class="membres">{membres}</div>
</div></section>

<section class="section clair partenaires"><div class="wrap">
  <p class="eyebrow">{t['partenaires_eyebrow']}</p>
  <p class="partenaires-texte">{t['partenaires_texte']}</p>
  <a class="btn" href="#contact" data-objet="{t['form']['objets'][3]}">{t['partenaires_btn']}</a>
</div></section>

<section class="section contact" id="contact"><div class="wrap">
  <p class="eyebrow">{t['contact_eyebrow']}</p>
  <h2>{t['contact_titre']}</h2>
  <p class="intro">{t['contact_intro_form'] if FORMSPREE_ID else t['contact_intro']}</p>
  {formulaire(t)}
  <p class="lieu">{t['lieu']}</p>
  <p class="fondateur">{t['fondateur']}</p>
</div></section>
</main>
<footer class="footer">{t['footer']}</footer>
</body>
</html>
"""


for cle, t in TEXTES.items():
    chemin = "index.html" if cle == "fr" else "en/index.html"
    os.makedirs(os.path.dirname(chemin) or ".", exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(page(t))
    print("écrit", chemin)

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url><loc>{SITE_URL}</loc>
    <xhtml:link rel="alternate" hreflang="fr" href="{SITE_URL}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}en/"/></url>
  <url><loc>{SITE_URL}en/</loc>
    <xhtml:link rel="alternate" hreflang="fr" href="{SITE_URL}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}en/"/></url>
</urlset>
""")
print("écrit sitemap.xml")
