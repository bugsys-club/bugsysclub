"""Génère le site Bugsy's Social Club en français (index.html) et en anglais (en/index.html).
Modifier les textes dans TEXTES, puis lancer : python3 build.py
"""
import os

SITE_URL = "https://bugsys-club.github.io/bugsysclub/"

EVENTAIL = """<svg class="eventail" viewBox="0 0 220 140" role="img" aria-label="Éventail art déco de Bugsy’s Social Club">
  <defs><linearGradient id="orfan" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#F3DE9C"/><stop offset="0.55" stop-color="#C9A45C"/><stop offset="1" stop-color="#8C6A2C"/></linearGradient></defs>
  <g fill="url(#orfan)"><polygon points="88.9,111.8 17.9,90.9 23.1,77.2 90.1,108.6"/><polygon points="90.6,107.7 37.5,79.6 44.2,69.0 92.4,104.9"/><polygon points="93.0,104.0 35.9,57.0 46.1,46.4 95.3,101.6"/><polygon points="96.2,100.9 58.4,54.3 68.7,47.2 98.9,99.0"/><polygon points="99.9,98.5 65.7,32.8 79.2,27.1 102.9,97.2"/><polygon points="104.0,96.8 87.5,39.1 99.8,36.6 107.3,96.2"/><polygon points="108.3,96.1 102.7,22.3 117.3,22.3 111.7,96.1"/><polygon points="112.7,96.2 120.2,36.6 132.5,39.1 116.0,96.8"/><polygon points="117.1,97.2 140.8,27.1 154.3,32.8 120.1,98.5"/><polygon points="121.1,99.0 151.3,47.2 161.6,54.3 123.8,100.9"/><polygon points="124.7,101.6 173.9,46.4 184.1,57.0 127.0,104.0"/><polygon points="127.6,104.9 175.8,69.0 182.5,79.6 129.4,107.7"/><polygon points="129.9,108.6 196.9,77.2 202.1,90.9 131.1,111.8"/></g>
  <path d="M92 118 A18 18 0 0 1 128 118 Z" fill="url(#orfan)"/>
  <rect x="20" y="124" width="180" height="2.5" fill="url(#orfan)"/>
  <rect x="50" y="131" width="120" height="1.2" fill="#C9A45C"/>
</svg>"""

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
        "sous": "Restaurant · Jazz · Art · Dance · Yaoundé",
        "accroche": "Un café le matin, une grande table le soir, un club la nuit.",
        "cta": "Réserver une table",
        "concept_eyebrow": "Le concept",
        "concept_titre": "Une adresse, cinq univers",
        "ambiance_alt": "La salle de Bugsy’s : banquettes de velours rouge, lustre, scène et piano à queue",
        "ambiance_legende": "Vue d’ambiance du projet",
        "concept_intro": "Au cœur du quartier Bastos, Bugsy’s réunit sous le même toit un café, un steak house, un club, une galerie et une école de danse, dans l’esprit des clubs américains des années 40.",
        "temps": [
            ("8h – 11h", "Le matin", "Café et rendez-vous : espresso, café de l’Ouest, petit-déjeuner d’affaires."),
            ("12h – 23h", "Le soir", "Steak house et fruits de mer, classiques du monde, pâtisserie française."),
            ("Jeudi – samedi, 23h – 4h", "La nuit", "Club et soirées privées : DJ sets funky, hip-hop et deep house."),
            ("Un vernissage par mois", "La galerie", "Art et culture : les œuvres de la collection, un nouvel accrochage chaque trimestre."),
            ("Lundi – jeudi, en journée", "L’école de danse", "Cours tous niveaux, ateliers et books photo pour les artistes."),
        ],
        "galerie_alt": ["Grand plateau de viandes braisées, riz rouge et sauces maison", "Poisson braisé, salsa de poivrons et citron vert", "Cocktail servi dans une timbale en cuivre", "Verre de vin rouge au-dessus d’une table garnie", "Champagnes sur une table du lounge"],
        "racines_alt": ["Acacia solitaire dans la savane au coucher du soleil", "Barques de pêche colorées sur une plage africaine"],
        "carte_eyebrow": "La carte",
        "grill_alt": "Pièce de bœuf saisie dans les flammes du grill",
        "bar_alt": "Cocktails alignés sur le comptoir du bar, bouteilles éclairées en arrière-plan",
        "cuisine_alts": ["Côte de bœuf tomahawk suspendue au-dessus du gril", "La brigade en cuisine dresse des entrecôtes et des frites", "Carafe de cognac extra dans la lumière du bar", "Crêpes flambées à l’orange"],
        "carte_titre": "Steak house, sea food et classiques du monde",
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
        "jazz_intro": "Du soul jazz aux grooves africains, le Cameroun a donné à la musique quelques-unes de ses plus grandes voix, de Manu Dibango à Richard Bona. Chez Bugsy’s, on dîne au son d’un live, puis les platines prennent le relais.",
        "rdv": [("Jeudis Soul Jazz · 20h – 23h", "Soul jazz et musiques africaines en live pendant le dîner, puis le DJ prend le relais."), ("Galerie tournante", "Peintres et sculpteurs camerounais aux murs, œuvres à vendre."), ("Vernissage · un mercredi par mois", "Soirée sur invitation autour de l’artiste exposé.")],
        "club_alt": "Peinture d’une danseuse en robe rouge tourbillonnante, à la lueur des bougies",
        "club_eyebrow": "Le club",
        "club_titre": "Jazz and Night Club",
        "club_intro": "Du jeudi au samedi, de 23h à 4h : DJ sets funky, hip-hop et deep house, service bouteilles et entrée offerte aux clients du dîner.",
        "membres_eyebrow": "Membres",
        "membres_titre": "Le Cercle Bugsy’s",
        "membres_btn": "Rejoignez le Cercle Bugsy’s",
        "membres_intro": "Trois cartes pour les habitués du club. Les avantages de chaque niveau seront annoncés à l’ouverture.",
        "niveaux": ["Membre", "Gold", "Black"],
        "contact_eyebrow": "Contact",
        "contact_titre": "Ouverture prochaine",
        "contact_intro": "Réservations, privatisations et cartes de membre : les coordonnées seront publiées ici très bientôt.",
        "lieu": "Bastos · Yaoundé · Cameroun",
        "footer": "© Bugsy’s Social Club · Yaoundé",
        "fondateur": "Fondé par Guy Erick Tamokwe",
        "facebook": "Suivez-nous sur Facebook",
        "instagram": "Guy sur Instagram",
        "recrut_eyebrow": "Nous recrutons",
        "recrut_titre": "Rejoins la maison",
        "recrut_intro": "Tu aimes la gastronomie, le jazz et les belles nuits ? Bugsy’s prépare son ouverture et constitue son équipe.",
        "recrut_postes": [("Chef cuisinier", "Steak house, sea food et classiques du monde"), ("Serveurs et serveuses", "Service en salle, accueil des membres, élégance"), ("Barman ou barmaid", "Cocktails signature, bouteilles de collection")],
        "recrut_btn": "Postuler",
        "partenaires_eyebrow": "Partenaires",
        "partenaires_texte": "Bugsy’s s’associe aux compagnies, aux festivals et aux maisons qui partagent sa vision de Yaoundé : la danse, le jazz et la création, au même endroit.",
        "partenaires_btn": "Devenir partenaire",
        "form": {"nom": "Nom", "email": "E-mail", "objet": "Objet", "objets": ["Réservation", "Privatisation", "Carte de membre", "Partenariat", "Candidature", "Autre demande"], "message": "Message", "envoyer": "Envoyer", "merci": "Merci, votre message a bien été envoyé. Nous vous répondrons très vite.", "erreur": "L’envoi n’a pas abouti. Merci de réessayer dans un instant."},
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
        "sous": "Restaurant · Jazz · Art · Dance · Yaoundé",
        "accroche": "A café by morning, a grand table by evening, a club by night.",
        "cta": "Book a table",
        "concept_eyebrow": "The concept",
        "concept_titre": "One address, five worlds",
        "ambiance_alt": "The Bugsy’s dining room: red velvet chairs, chandelier, stage and grand piano",
        "ambiance_legende": "Design concept view",
        "concept_intro": "In the heart of Bastos, Bugsy’s brings a café, a steak house, a club, a gallery and a dance school under one roof, in the spirit of 1940s American supper clubs.",
        "temps": [
            ("8am – 11am", "Morning", "Coffee and meetings: espresso, West Cameroon coffee, business breakfasts."),
            ("Noon – 11pm", "Evening", "Steak house and seafood, world classics, French pâtisserie."),
            ("Thursday – Saturday, 11pm – 4am", "Night", "Club and private parties: funky, hip-hop and deep house DJ sets."),
            ("One opening a month", "The gallery", "Art and culture: works from the collection, rehung every quarter."),
            ("Monday – Thursday, daytime", "The dance school", "Classes for all levels, workshops and photo books for artists."),
        ],
        "galerie_alt": ["Platter of braised meats, red rice and house sauces", "Braised fish with pepper salsa and lime", "Cocktail served in a copper cup", "Glass of red wine above a laid table", "Champagne on a lounge table"],
        "racines_alt": ["Lone acacia tree on the savannah at sunset", "Colourful fishing boats on an African beach"],
        "carte_eyebrow": "The menu",
        "grill_alt": "Beef seared in the flames of the grill",
        "bar_alt": "Cocktails lined up on the bar counter, lit bottles behind",
        "cuisine_alts": ["Tomahawk steak hanging over the grill", "The kitchen brigade plating sliced steaks and fries", "Decanter of extra cognac in the bar light", "Orange crêpes, flambéed"],
        "carte_titre": "Steak house, seafood and world classics",
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
        "jazz_intro": "From soul jazz to African grooves, Cameroon has given music some of its greatest voices, from Manu Dibango to Richard Bona. At Bugsy’s, dinner comes with live music, then the decks take over.",
        "rdv": [("Soul Jazz Thursdays · 8pm – 11pm", "Live soul jazz and African music over dinner, then the DJ takes over."), ("Rotating gallery", "Cameroonian painters and sculptors on the walls, works for sale."), ("Opening night · one Wednesday a month", "An invitation-only evening around the featured artist.")],
        "club_alt": "Painting of a dancer in a swirling red dress, by candlelight",
        "club_eyebrow": "The club",
        "club_titre": "Jazz and Night Club",
        "club_intro": "Thursday to Saturday, 11pm to 4am: funky, hip-hop and deep house DJ sets, bottle service and free entry for dinner guests.",
        "membres_eyebrow": "Members",
        "membres_titre": "The Bugsy’s Circle",
        "membres_btn": "Join the Bugsy’s Circle",
        "membres_intro": "Three cards for the club’s regulars. The benefits of each tier will be announced at the opening.",
        "niveaux": ["Member", "Gold", "Black"],
        "contact_eyebrow": "Contact",
        "contact_titre": "Opening soon",
        "contact_intro": "Bookings, private events and membership cards: contact details will be published here very soon.",
        "lieu": "Bastos · Yaoundé · Cameroon",
        "footer": "© Bugsy’s Social Club · Yaoundé",
        "fondateur": "Founded by Guy Erick Tamokwe",
        "facebook": "Follow us on Facebook",
        "instagram": "Guy on Instagram",
        "recrut_eyebrow": "We are hiring",
        "recrut_titre": "Join the house",
        "recrut_intro": "Love fine food, jazz and great nights out? Bugsy’s is getting ready to open and building its team.",
        "recrut_postes": [("Head chef", "Steak house, seafood and world classics"), ("Waiters and waitresses", "Table service, welcoming members, elegance"), ("Bartender", "Signature cocktails, collector’s bottles")],
        "recrut_btn": "Apply",
        "partenaires_eyebrow": "Partners",
        "partenaires_texte": "Bugsy’s works with the companies, festivals and houses that share its vision of Yaoundé: dance, jazz and creation, under one roof.",
        "partenaires_btn": "Become a partner",
        "form": {"nom": "Name", "email": "Email", "objet": "Subject", "objets": ["Booking", "Private event", "Membership card", "Partnership", "Job application", "Other enquiry"], "message": "Message", "envoyer": "Send", "merci": "Thank you, your message has been sent. We will reply very soon.", "erreur": "Your message could not be sent. Please try again in a moment."},
        "contact_intro_form": "Bookings, private events and membership cards: write to us and we will reply personally.",
    },
}

CARTE_FR = [
  ("Le restaurant", "12h – 23h", [
    ("Bienvenue", "Notre rituel, à l’arrivée et au départ", [
      ("Rhum arrangé maison", "Offert à chaque convive", "offert")]),
    ("Pour commencer", "", [
      ("Os à moelle rôti", "Fleur de sel, pain grillé, persillade", "6 000"),
      ("Salade Bugsy’s", "Avocat, crevettes de Kribi, mangue, vinaigrette passion", "7 000"),
      ("Soya", "Brochettes de bœuf épicées au grill, oignons, piment", "4 500")]),
    ("Le Steak House", "Chaque pièce est servie avec son os à moelle rôti et la sauce Bugsy’s : herbes fraîches, njansang, poivre blanc de Penja · Aussi : béarnaise · mbongo", [
      ("Côte de bœuf maturée, 1 kg", "Pour deux, découpée en salle", "45 000"),
      ("Filet de bœuf, 250 g", "", "18 000"),
      ("Entrecôte tranchée, 300 g", "Servie en poêle, fleur de sel", "15 000"),
      ("Dibi d’agneau", "Agneau braisé, oignons, moutarde", "12 000")]),
    ("Le Sea Food", "Les meilleurs produits de la mer, de Kribi et d’ailleurs", [
      ("Plateau de fruits de mer", "Pour deux : langouste, gambas, crevettes de Kribi, calamars", "55 000"),
      ("Langouste de Kribi grillée", "Beurre au poivre blanc de Penja", "25 000"),
      ("Gambas flambées en salle", "Beurre à l’ail et au gingembre frais", "12 000"),
      ("Poisson braisé entier", "Bar ou capitaine, alloco, bâton de manioc", "12 000")]),
    ("Classiques d’Afrique", "Servis à l’assiette, comme en gastronomie", [
      ("Ndolé aux crevettes", "Arachides, crevettes, plantain mûr", "9 000"),
      ("Poulet DG", "Plantains mûrs, carottes, haricots verts", "9 000"),
      ("Mafé, au choix", "Sauce à l’arachide, riz blanc · bœuf ou poulet 8 000 · agneau 9 500", "dès 8 000"),
      ("Yassa, au choix", "Oignons confits au citron · poulet 8 000 · poisson 10 000 · crevettes 11 000", "dès 8 000"),
      ("Capitaine au mbongo tchobi", "Sauce noire aux épices, bâton de manioc", "12 000")]),
    ("Classiques du monde", "Amérique · Europe · Asie", [
      ("Burger Bugsy’s", "Bœuf maturé, cheddar affiné, oignons confits, frites maison", "9 500"),
      ("Tartare de bœuf au couteau", "Piment doux, câpres, frites maison", "9 500"),
      ("Sole meunière", "Beurre noisette, citron, pommes vapeur", "16 000"),
      ("Tataki de thon", "Sésame, gingembre, sauce ponzu", "11 000"),
      ("Gambas au wok", "Nouilles sautées, légumes croquants", "12 000")]),
    ("Accompagnements", "Frites maison · Alloco · Riz jollof · Miondo · Légumes grillés · Purée maison", [
      ("L’accompagnement", "", "2 000")]),
    ("La pâtisserie française", "", [
      ("Crêpe Suzette", "Flambée au Grand Marnier, en salle", "6 000"),
      ("Mille-feuille", "Crème vanille, caramel", "5 000"),
      ("Profiteroles", "Glace vanille, chocolat chaud", "5 000"),
      ("Crème brûlée", "Vanille ou bissap", "4 500"),
      ("Fondant au cacao du Cameroun", "Cœur coulant, glace vanille", "5 000")]),
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
    ("La cave et la bière", "Bordeaux, Bourgogne, Rhône, Champagne : carte des vins sur demande", [
      ("Vin au verre", "", "5 000"), ("Bouteille de vin", "", "dès 25 000"),
      ("Coupe de champagne", "", "12 000"), ("Bière", "", "2 000")]),
    ("Le club · jeudi à samedi, 23h – 4h", "Softs et glace inclus avec chaque bouteille · Entrée offerte aux clients du dîner", [
      ("Champagne brut", "", "75 000"), ("Champagne blanc de blancs", "", "110 000"), ("Champagne rosé", "", "120 000"),
      ("Vodka premium, 70 cl", "", "60 000"), ("Whisky 12 ans, 70 cl", "", "70 000"), ("Cognac VSOP, 70 cl", "", "85 000")]),
    ("Bouteilles de collection", "Au salon ou au club", [
      ("Dom Pérignon", "Champagne millésimé, 75 cl", "450 000"),
      ("Petrus", "Pomerol, 75 cl", "sur demande"),
      ("Lise Baccara Extra", "Cognac, 70 cl", "250 000")]),
  ]),
]
CARTE_EN = [
  ("The restaurant", "Noon – 11pm", [
    ("Welcome", "Our ritual, on arrival and on leaving", [
      ("House-infused rum", "On the house for every guest", "complimentary")]),
    ("To start", "", [
      ("Roasted bone marrow", "Sea salt, toasted bread, parsley and garlic", "6 000"),
      ("Bugsy’s salad", "Avocado, Kribi prawns, mango, passion fruit dressing", "7 000"),
      ("Soya", "Spiced grilled beef skewers, onions, chilli", "4 500")]),
    ("The Steak House", "Every cut comes with its roasted marrow bone and the Bugsy’s sauce: fresh herbs, njansang, white Penja pepper · Also: béarnaise · mbongo", [
      ("Dry-aged rib of beef, 1 kg", "For two, carved at the table", "45 000"),
      ("Beef fillet, 250 g", "", "18 000"),
      ("Sliced rib-eye, 300 g", "Served in the pan, sea salt flakes", "15 000"),
      ("Lamb dibi", "Braised lamb, onions, mustard", "12 000")]),
    ("The Sea Food", "The finest seafood, from Kribi and beyond", [
      ("Seafood platter", "For two: lobster, king prawns, Kribi prawns, squid", "55 000"),
      ("Grilled Kribi lobster", "White Penja pepper butter", "25 000"),
      ("King prawns flambéed at the table", "Garlic and fresh ginger butter", "12 000"),
      ("Whole braised fish", "Sea bass or captain fish, alloco, cassava stick", "12 000")]),
    ("African classics", "Plated the way fine dining does", [
      ("Ndolé with prawns", "Peanuts, prawns, ripe plantain", "9 000"),
      ("Chicken DG", "Ripe plantain, carrots, green beans", "9 000"),
      ("Mafé, your choice", "Peanut sauce, white rice · beef or chicken 8 000 · lamb 9 500", "from 8 000"),
      ("Yassa, your choice", "Onions slow-cooked with lemon · chicken 8 000 · fish 10 000 · prawns 11 000", "from 8 000"),
      ("Captain fish in mbongo tchobi", "Spiced black sauce, cassava stick", "12 000")]),
    ("World classics", "America · Europe · Asia", [
      ("Bugsy’s burger", "Dry-aged beef, aged cheddar, caramelised onions, house fries", "9 500"),
      ("Hand-cut beef tartare", "Mild chilli, capers, house fries", "9 500"),
      ("Sole meunière", "Brown butter, lemon, steamed potatoes", "16 000"),
      ("Tuna tataki", "Sesame, ginger, ponzu", "11 000"),
      ("Wok-fried king prawns", "Stir-fried noodles, crisp vegetables", "12 000")]),
    ("Sides", "House fries · Alloco · Jollof rice · Miondo · Grilled vegetables · House mash", [
      ("Side dish", "", "2 000")]),
    ("French pâtisserie", "", [
      ("Crêpe Suzette", "Flambéed with Grand Marnier at the table", "6 000"),
      ("Mille-feuille", "Vanilla cream, caramel", "5 000"),
      ("Profiteroles", "Vanilla ice cream, hot chocolate sauce", "5 000"),
      ("Crème brûlée", "Vanilla or bissap", "4 500"),
      ("Cameroon cocoa fondant", "Molten centre, vanilla ice cream", "5 000")]),
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
    ("The cellar and beer", "Bordeaux, Burgundy, Rhône, Champagne: wine list on request", [
      ("Wine by the glass", "", "5 000"), ("Bottle of wine", "", "from 25 000"),
      ("Glass of champagne", "", "12 000"), ("Beer", "", "2 000")]),
    ("The club · Thursday to Saturday, 11pm – 4am", "Soft drinks and ice included with every bottle · Free entry for dinner guests", [
      ("Brut champagne", "", "75 000"), ("Blanc de blancs champagne", "", "110 000"), ("Rosé champagne", "", "120 000"),
      ("Premium vodka, 70 cl", "", "60 000"), ("12-year-old whisky, 70 cl", "", "70 000"), ("Cognac VSOP, 70 cl", "", "85 000")]),
    ("Collector’s bottles", "In the lounge or at the club", [
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

FACEBOOK_URL = "https://www.facebook.com/share/19V8M8bjyL/"
INSTAGRAM_URL = "https://www.instagram.com/guyericktamokwe/"

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
        "servesCuisine": ["Steakhouse", "Seafood", "Cameroonian", "African", "French", "International"],
        "address": {"@type": "PostalAddress", "addressLocality": "Yaoundé", "addressRegion": "Bastos", "addressCountry": "CM"},
        "inLanguage": t["lang"],
        "founder": {"@type": "Person", "name": "Guy Erick Tamokwe", "sameAs": [INSTAGRAM_URL]},
        "sameAs": [FACEBOOK_URL],
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
    visuels = [f'<img src="{d}assets/img/grill-flammes.jpg" alt="{t['grill_alt']}" loading="lazy">', f'<img src="{d}assets/img/bar-cocktails.jpg" alt="{t["bar_alt"]}" loading="lazy">']
    carte = "".join(
        f'<div class="volet"><div class="volet-tete"><p class="volet-titre">{titre} <span>{heures}</span></p>{vis}</div><div class="carte">'
        + "".join(bloc(*r) for r in rubriques)
        + f'</div><a class="btn" href="{d}assets/cartes/{pdf}" download>{lien}</a></div>'
        for (titre, heures, rubriques), pdf, lien, vis in zip(CARTES[t["lang"]], pdfs, t["carte_pdf"], visuels))
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
  <p class="signature">Eat · Drink · Jazz · Dance<span>Live the Experience</span></p>
  <p class="accroche">{t['accroche']}</p>
  <a class="btn" href="#contact" data-objet="{t['form']['objets'][0]}">{t['cta']}</a>
</div></div></div></section>

<section class="section clair" id="concept"><div class="wrap">
  <p class="eyebrow">{t['concept_eyebrow']}</p>
  <h2>{t['concept_titre']}</h2>
  <p class="intro">{t['concept_intro']}</p>
  <figure class="ambiance"><img src="{d}assets/img/ambiance-salle.jpg" alt="{t['ambiance_alt']}" loading="lazy"></figure>
  <div class="trois cinq">{temps}</div>
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
  <p class="membres-cta"><a class="btn" href="#contact" data-objet="{t['form']['objets'][2]}">{t['membres_btn']}</a></p>
</div></section>

<section class="section recrutement"><div class="wrap">
  <p class="eyebrow">{t['recrut_eyebrow']}</p>
  <h2>{t['recrut_titre']}</h2>
  <p class="intro">{t['recrut_intro']}</p>
  <div class="postes">{"".join(f'<div class="poste"><h3>{a}</h3><p>{b}</p></div>' for a, b in t['recrut_postes'])}</div>
  <a class="btn" href="#contact" data-objet="{t['form']['objets'][4]}">{t['recrut_btn']}</a>
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
  <p class="reseaux"><a href="{FACEBOOK_URL}" target="_blank" rel="noopener" aria-label="Facebook" title="Facebook"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2.3H8v3h2.5V21h3z"></path></svg></a><a href="{INSTAGRAM_URL}" target="_blank" rel="noopener" aria-label="Instagram" title="Instagram"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"></rect><circle cx="12" cy="12" r="4"></circle><circle cx="17.5" cy="6.5" r="0.8" fill="currentColor"></circle></svg></a></p>
</div></section>
</main>
<footer class="footer">{t['footer']} <span class="footer-reseaux"><a href="{FACEBOOK_URL}" target="_blank" rel="noopener" aria-label="Facebook" title="Facebook"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2.3H8v3h2.5V21h3z"></path></svg></a><a href="{INSTAGRAM_URL}" target="_blank" rel="noopener" aria-label="Instagram" title="Instagram"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"></rect><circle cx="12" cy="12" r="4"></circle><circle cx="17.5" cy="6.5" r="0.8" fill="currentColor"></circle></svg></a></span></footer>
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
