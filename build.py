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
        "description": "Bugsy’s Social Club, à Bastos, Yaoundé : café le matin, steak house et fruits de mer le jour, jazz le jeudi et club DJ la nuit.",
        "nav": ["Le concept", "La carte", "Le jazz", "Le club", "Membres", "Contact"],
        "sous": "Steak house & sea food · Yaoundé",
        "accroche": "Un café le matin, une grande table le soir, un club la nuit.",
        "cta": "Ouverture prochaine",
        "concept_eyebrow": "Le concept",
        "concept_titre": "Une adresse, trois temps",
        "concept_intro": "Au cœur du quartier Bastos, Bugsy’s réunit sous le même toit un café, un steak house et un club, dans l’esprit des clubs américains des années 40.",
        "temps": [
            ("8h – 11h", "Le Café", "Espresso, café de l’Ouest camerounais, petit-déjeuner d’affaires."),
            ("12h – 23h", "Le Restaurant", "Grill et fruits de mer, relevés de poivre de Penja et de sauces maison."),
            ("Jeudi – samedi, 23h – 4h", "Le Club", "DJ résident et service bouteilles : la salle du dîner devient la piste."),
        ],
        "galerie_alt": ["Grand plateau de viandes braisées, riz rouge et sauces maison", "Poisson braisé, salsa de poivrons et citron vert", "Cocktail servi dans une timbale en cuivre", "Verre de vin rouge au-dessus d’une table garnie", "Champagnes sur une table du lounge"],
        "racines_alt": ["Acacia solitaire dans la savane au coucher du soleil", "Barques de pêche colorées sur une plage africaine"],
        "carte_eyebrow": "La carte",
        "carte_titre": "Le grill, relevé de touches africaines",
        "carte": [
            ("Le grill", [("Côte de bœuf maturée", "Pour deux, découpée en salle"), ("Filet de bœuf", "Sauce au poivre blanc de Penja"), ("Côtelettes d’agneau", "Marinade aux épices du marché"), ("Demi-poulet braisé façon DG", "Plantains mûrs, légumes croquants")]),
            ("La mer", [("Bar braisé entier", "Salsa crue, citron vert, alloco"), ("Gambas grillées", "Beurre citronné, riz jollof"), ("Capitaine au mbongo tchobi", "Sauce noire aux épices, bâton de manioc"), ("Le Plateau Bugsy’s", "Pour deux, gambas, poisson braisé, calamars")]),
            ("Le bar", [("The Bugsy", "Bourbon, sirop de bissap, angostura"), ("Penja Old Fashioned", "Whisky, sirop au poivre de Penja, orange"), ("Copper Mule", "Vodka, gingembre frais, citron vert"), ("Bissap Royal", "Sirop de bissap maison, champagne brut")]),
        ],
        "jazz_eyebrow": "Le jazz",
        "jazz_titre": "Le jazz en signature",
        "jazz_alt": ["Scène de jazz tamisée : contrebasse, batterie, piano et micro à la lueur des bougies", "Peinture d’une chanteuse de jazz accompagnée d’un pianiste et d’un contrebassiste", "Club de jazz art déco : chanteuse sur scène, danseurs et banquettes de velours rouge"],
        "jazz_intro": "Le Cameroun a donné au jazz quelques-unes de ses plus grandes voix. Chez Bugsy’s, on dîne au son d’un trio, puis la nuit commence.",
        "rdv": [("Jeudis Jazz · 20h – 23h", "Trio afro-jazz et soul pendant le dîner, puis le DJ prend le relais."), ("Galerie tournante", "Peintres et sculpteurs camerounais aux murs, œuvres à vendre."), ("Vernissage · un mercredi par mois", "Soirée sur invitation autour de l’artiste exposé.")],
        "club_eyebrow": "Le club",
        "club_titre": "Quand la nuit commence",
        "club_intro": "Du jeudi au samedi, de 23h à 4h : DJ résident, service bouteilles et entrée offerte aux clients du dîner.",
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
    },
    "en": {
        "lang": "en", "dossier": "../", "autre": "../", "autre_label": "FR",
        "title": "Bugsy’s Social Club — Café, steak house & club in Yaoundé",
        "description": "Bugsy’s Social Club, in Bastos, Yaoundé: a café by morning, a steak house & seafood restaurant by day, jazz on Thursdays and a DJ club by night.",
        "nav": ["The concept", "The menu", "Jazz", "The club", "Members", "Contact"],
        "sous": "Steak house & sea food · Yaoundé",
        "accroche": "A café by morning, a grand table by evening, a club by night.",
        "cta": "Opening soon",
        "concept_eyebrow": "The concept",
        "concept_titre": "One address, three moments",
        "concept_intro": "In the heart of Bastos, Bugsy’s brings a café, a steak house and a club under one roof, in the spirit of 1940s American supper clubs.",
        "temps": [
            ("8am – 11am", "The Café", "Espresso, coffee from Cameroon’s West region, business breakfasts."),
            ("Noon – 11pm", "The Restaurant", "Grill and seafood, with Penja pepper and house sauces."),
            ("Thursday – Saturday, 11pm – 4am", "The Club", "Resident DJ and bottle service: the dining room becomes the dance floor."),
        ],
        "galerie_alt": ["Platter of braised meats, red rice and house sauces", "Braised fish with pepper salsa and lime", "Cocktail served in a copper cup", "Glass of red wine above a laid table", "Champagne on a lounge table"],
        "racines_alt": ["Lone acacia tree on the savannah at sunset", "Colourful fishing boats on an African beach"],
        "carte_eyebrow": "The menu",
        "carte_titre": "The grill, with African touches",
        "carte": [
            ("The grill", [("Dry-aged rib of beef", "For two, carved at the table"), ("Beef fillet", "White Penja pepper sauce"), ("Lamb cutlets", "Market spice marinade"), ("Half chicken, DG style", "Ripe plantain, crisp vegetables")]),
            ("The sea", [("Whole braised sea bass", "Raw salsa, lime, alloco"), ("Grilled king prawns", "Lemon butter, jollof rice"), ("Captain fish in mbongo tchobi", "Spiced black sauce, cassava stick"), ("The Bugsy’s platter", "For two, prawns, braised fish, squid")]),
            ("The bar", [("The Bugsy", "Bourbon, hibiscus syrup, bitters"), ("Penja Old Fashioned", "Whisky, Penja pepper syrup, orange"), ("Copper Mule", "Vodka, fresh ginger, lime"), ("Bissap Royal", "House hibiscus syrup, brut champagne")]),
        ],
        "jazz_eyebrow": "Jazz",
        "jazz_titre": "Jazz at the heart",
        "jazz_alt": ["Dimly lit jazz stage: double bass, drums, piano and microphone by candlelight", "Painting of a jazz singer with a pianist and a double bass player", "Art deco jazz club: singer on stage, dancers and red velvet banquettes"],
        "jazz_intro": "Cameroon has given jazz some of its greatest voices. At Bugsy’s, dinner comes with a live trio, and then the night begins.",
        "rdv": [("Jazz Thursdays · 8pm – 11pm", "An afro-jazz and soul trio over dinner, then the DJ takes over."), ("Rotating gallery", "Cameroonian painters and sculptors on the walls, works for sale."), ("Opening night · one Wednesday a month", "An invitation-only evening around the featured artist.")],
        "club_eyebrow": "The club",
        "club_titre": "When the night begins",
        "club_intro": "Thursday to Saturday, 11pm to 4am: resident DJ, bottle service and free entry for dinner guests.",
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
    },
}

ANCRES = ["concept", "carte", "jazz", "club", "membres", "contact"]
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
        "servesCuisine": ["Steakhouse", "Seafood", "Cameroonian"],
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
    carte = "".join(
        f'<div><h3>{titre}</h3>' + "".join(f'<p class="plat"><strong>{n}</strong><span>{desc}</span></p>' for n, desc in plats) + "</div>"
        for titre, plats in t["carte"])
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
  <nav class="nav">{nav}<a class="lang" href="{t['autre']}" hreflang="{'en' if t['lang']=='fr' else 'fr'}">{t['autre_label']}</a></nav>
</div></header>
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
  <div class="carte">{carte}</div>
</div></section>

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
</div></div></section>

<section class="section" id="club"><div class="wrap"><div class="jazz">
  <img src="{d}assets/img/champagne.jpg" alt="{t['galerie_alt'][4]}" loading="lazy">
  <div>
    <p class="eyebrow">{t['club_eyebrow']}</p>
    <h2>{t['club_titre']}</h2>
    <p class="intro">{t['club_intro']}</p>
  </div>
</div></div></section>

<section class="section clair" id="membres"><div class="wrap">
  <p class="eyebrow">{t['membres_eyebrow']}</p>
  <h2>{t['membres_titre']}</h2>
  <p class="intro">{t['membres_intro']}</p>
  <div class="membres">{membres}</div>
</div></section>

<section class="section contact" id="contact"><div class="wrap">
  <p class="eyebrow">{t['contact_eyebrow']}</p>
  <h2>{t['contact_titre']}</h2>
  <p class="intro">{t['contact_intro']}</p>
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
