---
title: "Testovacia stránka pre čiastočné zobrazenia"
date: 2025-03-31T16:49:48+02:00
draft: false
url: "test"
description: "Toto je testovacia stránka, ktorá demonštruje všetky dostupné shortcode v Hugo boilerplate téme."
---

Toto je testovacia stránka, ktorá demonštruje všetky dostupné shortcode v Hugo boilerplate téme. Každá sekcia nižšie ukazuje, ako použiť konkrétny shortcode a ako sa zobrazuje používateľom.

## Komponenty s oneskoreným načítaním

### YouTube video s oneskoreným načítaním

Nižšie je uvedené YouTube video s oneskoreným načítaním, ktoré otestuje funkciu oneskoreného načítania videa:

{{< lazyvideo "8kGxHHhYRmE" "Krásne prírodné video - Relaxačná hudba s prírodnými zvukmi" >}}

Video vyššie by sa malo načítať iba vtedy, keď príde do zobrazenia, čím sa zlepší výkon stránky.

### Obrázok s oneskoreným načítaním

{{< lazyimg "https://images.unsplash.com/photo-1682687982501-1e58ab814714" "Príklad obrázka s oneskoreným načítaním" >}}

### SVG s oneskoreným načítaním

{{< lazysvg "https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/AJ_Digital_Camera.svg" "Príklad SVG s oneskoreným načítaním" >}}

### Element picture

{{< picture "https://tailwindcss.com/plus-assets/img/ecommerce-images/home-page-03-featured-category.jpg" "Príklad responzívneho elementu picture" >}}

## Bannerové komponenty

### Banner s tlačidlom

{{< banner-with-button 
    title="Nová funkcia k dispozícii" 
    message="Vyskúšajte náš nový dashboard s vylepšenou analytikou." 
    buttonText="Vyskúšajte teraz" 
    buttonUrl="#" 
    dismissable=true 
>}}

### Banner na tmavom pozadí

{{< banner-on-dark 
    message="Black Friday výpredaj: Získajte 50% zľavu na všetky plány až do 30. novembra" 
    url="#" 
    dismissable=true 
>}}

### Banner s firemnou farbou

{{< banner-on-brand 
    message="Zúčastnite sa nášho webinára o aktualizáciách produktov tento piatok" 
    url="#" 
    dismissable=true 
>}}

### Banner s pozadím s efektom žiarenia

{{< banner-with-background-glow 
    message="Naša nová mobilná aplikácia je teraz dostupná na stiahnutie" 
    url="#" 
    dismissable=true 
>}}

### Banner zarovnaný dole

{{< banner-bottom-aligned 
    message="Táto stránka používa cookies na zlepšenie vášho zážitku" 
    url="#" 
    dismissable=true 
>}}

### Plávajúci banner dole

{{< banner-floating-at-bottom 
    message="Ponuka na obmedzený čas: Doprava zadarmo na všetky objednávky" 
    url="#" 
    dismissable=true 
>}}

### Stredovo plávajúci banner

{{< banner-floating-at-bottom-centered 
    message="Nový blogový príspevok: 10 tipov pre lepšiu produktivitu" 
    url="#" 
    dismissable=true 
>}}

### Ochrana osobných údajov (zarovnané vľavo)

{{< banner-privacy-notice-left-aligned 
    message="Používame cookies na zlepšenie vášho prehliadania, zobrazovanie personalizovaných reklám alebo obsahu a analýzu našej návštevnosti." 
    policyUrl="#" 
    acceptText="Prijať všetko" 
    rejectText="Odmietnuť všetko" 
>}}

### Ochrana osobných údajov (zarovnané na stred)

{{< banner-privacy-notice-centered 
    message="Používame cookies na zlepšenie vášho prehliadania, zobrazovanie personalizovaných reklám alebo obsahu a analýzu našej návštevnosti." 
    policyUrl="#" 
    acceptText="Prijať všetko" 
    rejectText="Odmietnuť všetko" 
>}}

### Ochrana osobných údajov (na celú šírku)

{{< banner-privacy-notice-full-width 
    message="Používame cookies na zlepšenie vášho prehliadania, zobrazovanie personalizovaných reklám alebo obsahu a analýzu našej návštevnosti." 
    policyUrl="#" 
    acceptText="Prijať všetko" 
    rejectText="Odmietnuť všetko" 
>}}

## Komponenty kategórií

### Náhľad troch stĺpcov s popisom

{{< categories-preview-three-column-with-description 
    heading="Nakupujte podľa kolekcie" 
    description="Každú sezónu spolupracujeme s návrhármi svetovej úrovne na vytvorení kolekcie inšpirovanej prírodou." 
    backgroundColor="bg-white" 
>}}

### Náhľad troch stĺpcov

{{< categories-preview-three-column 
    heading="Nakupujte podľa kategórie" 
    backgroundColor="bg-gray-100" 
>}}

### Náhľad s obrázkovým pozadím

{{< categories-preview-with-image-backgrounds 
    heading="Nakupujte podľa štýlu" 
    browseAllText="Prezrieť všetky štýly" 
    browseAllUrl="#" 
    backgroundColor="bg-white" 
>}}

### Náhľad s rolovacími kartami

{{< categories-preview-with-scrolling-cards 
    heading="Prezrite si kategórie" 
    browseAllText="Zobraziť všetky kategórie" 
    browseAllUrl="#" 
    backgroundColor="bg-gray-100" 
>}}

### Produktová karta s kompletnými detailmi

{{< categories-product-list-card-with-full-details 
    heading="Vybrané produkty" 
    backgroundColor="bg-white" 
>}}

### Produktový zoznam s prekrytím obrázku a tlačidlom Pridať

{{< categories-product-list-with-image-overlay-and-add-button 
    heading="Novinky" 
    buttonText="Pridať do košíka" 
    backgroundColor="bg-gray-100" 
>}}

### Produktový zoznam s cenou vloženou do textu a CTA odkazom

{{< categories-product-list-with-inline-price-and-cta-link 
    heading="Odporúčané produkty" 
    viewAllText="Zobraziť všetky produkty" 
    viewAllUrl="#" 
    ctaText="Zobraziť detail" 
    backgroundColor="bg-white" 
>}}

### Produktový zoznam s vysokými obrázkami

{{< categories-product-list-with-tall-images 
    heading="Teraz populárne" 
    backgroundColor="bg-gray-100" 
>}}

## Komponenty obsahu

### Zarovnaný obsah na stred

{{< content-centered 
    heading="O našej spoločnosti" 
    backgroundColor="bg-white" 
>}}

### Rozdelený obsah s obrázkom

{{< content-split-with-image 
    heading="Naša misia" 
    imageUrl="https://images.unsplash.com/photo-1551434678-e076c223a692" 
    imageAlt="Tím spolupracuje" 
    backgroundColor="bg-gray-100" 
>}}

## Komponenty výzvy k akcii

### Výzva k akcii: tmavé panela

{{< cta-dark-panel 
    heading="Pripravení začať?" 
    description="Kontaktujte nás alebo si vytvorte účet." 
    primaryButtonText="Kontaktovať predaj" 
    primaryButtonUrl="#" 
    secondaryButtonText="Vytvoriť účet" 
    secondaryButtonUrl="#" 
>}}

### Jednoduchá výzva k akcii (zarovnaná na stred)

{{< cta-simple-centered 
    heading="Zvýšte svoju produktivitu" 
    description="Začnite dnes používať našu aplikáciu." 
    buttonText="Začať" 
    buttonUrl="#" 
    backgroundColor="bg-white" 
>}}

### Jednoduchá výzva k akcii (do riadku)

{{< cta-simple-justified 
    heading="Pripravení sa pustiť do toho?" 
    description="Začnite si dnes zadarmo skúšobnú verziu." 
    buttonText="Zaregistrujte sa zadarmo" 
    buttonUrl="#" 
    backgroundColor="bg-gray-100" 
>}}

## Komponenty FAQ

### FAQ s akordeónom, zarovnané na stred

{{< faq-centered-accordion 
    heading="Často kladené otázky" 
    backgroundColor="bg-white" 
>}}

## Komponenty funkcií

### Funkcie v troch stĺpcoch

{{< features-three-column 
    heading="Funkcie" 
    description="Naša aplikácia poskytuje kompletné riešenie pre riadenie potrieb vášho podnikania." 
    backgroundColor="bg-gray-100" 
>}}

### Technické špecifikácie so štvorcovou mriežkou 4 obrázkov

{{< features-with-4-images-grid 
    heading="Technické špecifikácie" 
    description="Nasledujúce špecifikácie robia tento produkt výnimočným oproti konkurencii." 
    backgroundColor="bg-white" 
>}}

### Funkcie so striedajúcimi sa sekciami

{{< features-with-alternating-sections 
    heading="Kľúčové funkcie" 
    description="Náš produkt je navrhnutý tak, aby riešil vaše každodenné problémy." 
    backgroundColor="bg-gray-100" 
>}}

### Špecifikácie produktu s miznúcim obrázkom

{{< features-with-fading-image 
    heading="Špecifikácie produktu" 
    description="Všetko, čo potrebujete vedieť o našom produkte." 
    backgroundColor="bg-white" 
>}}

### Ako to funguje s hlavičkou, obrázkami a popismi

{{< features-with-header-images-and-descriptions 
    heading="Ako to funguje" 
    description="Náš jednoduchý proces od začiatku po koniec." 
    backgroundColor="bg-gray-100" 
>}}

### Funkcie produktu s úvodom a záložkami

{{< features-with-intro-and-tabs 
    heading="Funkcie produktu" 
    description="Preskúmajte rôzne aspekty nášho produktu." 
    backgroundColor="bg-white" 
>}}

### Funkcie s rozdeleným obrázkom

{{< features-with-split-image 
    subheading="Navrhnuté pre podnikanie" 
    heading="Správne funkcie pre vaše podnikanie" 
    description="Náš produkt je navrhnutý tak, aby riešil konkrétne potreby moderných podnikov." 
    backgroundColor="bg-gray-100" 
>}}

### Funkcie so štvorcovými obrázkami

{{< features-with-square-images 
    subheading="Prečo si vybrať nás" 
    heading="Funkcie, ktoré nás odlišujú" 
    description="Náš produkt obsahuje všetko, čo potrebujete na rýchly štart." 
    backgroundColor="bg-white" 
>}}

### Funkcie s vrstvenými obrázkami

{{< features-with-tiered-images 
    subheading="Silné funkcie" 
    heading="Všetko, čo potrebujete na úspech" 
    backgroundColor="bg-gray-100" 
>}}

### Funkcie so širokými obrázkami

{{< features-with-wide-images 
    subheading="Intuitívne rozhranie" 
    heading="Navrhnuté pre produktivitu" 
    description="Naše čisté rozhranie vám pomáha sústrediť sa na to, čo je dôležité." 
    backgroundColor="bg-white" 
>}}

## Komponenty päty

### Päta so štyrmi stĺpcami

{{< footer-four-column 
    backgroundColor="bg-gray-900" 
>}}

### Jednoduchá centrálná päta

{{< footer-simple-centered 
    backgroundColor="bg-gray-900" 
>}}

## Komponenty hlavičky

### Zarovnaná hlavička na stred

{{< header-centered 
    heading="Vitajte na našej stránke" 
    description="Objavte naše produkty a služby." 
    backgroundColor="bg-white" 
>}}

### Jednoduchá hlavička

{{< header-simple 
    heading="O nás" 
    description="Zistite viac o našej spoločnosti a našej misii." 
    backgroundColor="bg-gray-100" 
>}}

## Hero komponenty

### Jednoduchý hrdinský blok so stredovým zarovnaním

{{< hero-simple-centered 
    heading="Platforma novej generácie" 
    description="Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure qui lorem cupidatat commodo." 
    primaryButtonText="Začať" 
    primaryButtonUrl="#" 
    secondaryButtonText="Viac informácií" 
    secondaryButtonUrl="#" 
    backgroundColor="bg-white" 
>}}

### Rozdelený hrdinský blok s kódom

{{< hero-split-with-code 
    heading="Vyvíjajte s dôverou" 
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." 
    buttonText="Začať" 
    buttonUrl="#" 
    codeLanguage="javascript" 
    codeContent="" 
    backgroundColor="bg-gray-100" 
>}}

### Rozdelený hrdinský blok s obrázkovými dlaždicami

{{< hero-split-with-image-tiles 
    heading="Navrhnite svoj ďalší projekt" 
    description="Vytvorte krásne dizajny s našou ľahko použiteľnou platformou." 
    buttonText="Začať navrhovať" 
    buttonUrl="#" 
    backgroundColor="bg-white" 
>}}

### Rozdelený hrdinský blok s obrázkom

{{< hero-split-with-image 
    heading="Analýzy založené na dátach" 
    description="Premeníme vaše dáta na akčné postrehy s našou analytickou platformou." 
    buttonText="Viac informácií" 
    buttonUrl="#" 
    imageUrl="https://images.unsplash.com/photo-1551434678-e076c223a692" 
    imageAlt="Analýza dashboardu" 
    backgroundColor="bg-gray-100" 
>}}

### Rozdelený hrdinský blok s ukážkou

{{< hero-split-with-screenshot 
    heading="Zefektívnite svoj pracovný tok" 
    description="Naša platforma vám pomáha efektívnejšie riadiť vaše projekty." 
    buttonText="Začať" 
    buttonUrl="#" 
    imageUrl="https://images.unsplash.com/photo-1551434678-e076c223a692" 
    imageAlt="Screenshot aplikácie" 
    backgroundColor="bg-white" 
>}}

## Komponenty stimulov

### 2x2 mriežka s ilustráciami

{{< incentives-2x2-grid-with-illustrations 
    heading="Prečo si vybrať nás" 
    backgroundColor="bg-gray-100" 
>}}

### 3 stĺpce s ilustráciami a hlavičkou

{{< incentives-3-column-with-illustrations-and-header 
    heading="Naše výhody" 
    description="Poskytujeme najlepšie služby v odvetví s týmito kľúčovými výhodami." 
    backgroundColor="bg-white" 
>}}

### 3 stĺpce s ilustráciami a nadpisom

{{< incentives-3-column-with-illustrations-and-heading 
    heading="Naše záruky" 
    backgroundColor="bg-gray-100" 
>}}

### 3 stĺpce s ilustráciami a rozdelenou hlavičkou

{{< incentives-3-column-with-illustrations-and-split-header 
    heading="Prečo nás zákazníci milujú" 
    description="Pomohli sme tisíckam firiem dosiahnuť ich ciele." 
    backgroundColor="bg-white" 
>}}

### 4 stĺpce s ilustráciami

{{< incentives-4-column-with-illustrations 
    backgroundColor="bg-gray-100" 
>}}

## Komponenty menu

### Rozbaľovacie menu, plná šírka, dva stĺpce

{{< menu-flyout-full-width-two-columns 
    buttonText="Riešenia" 
>}}

### Rozbaľovacie menu, plná šírka

{{< menu-flyout-full-width 
    buttonText="Produkty" 
>}}

### Jednoduché rozbaľovacie menu s popismi

{{< menu-flyout-simple-with-descriptions 
    buttonText="Zdroje" 
>}}

### Zoskupené rozbaľovacie menu s akciami v päte

{{< menu-flyout-stacked-with-footer-actions 
    buttonText="Funkcie" 
>}}

### Rozbaľovacie menu, dva stĺpce

{{< menu-flyout-two-column 
    buttonText="Spoločnosť" 
>}}

### Hlavičkové menu

{{< menu-header >}}

## Komponenty cien

### Cena v troch úrovniach

{{< pricing-three-tiers 
    heading="Cenové plány" 
    description="Vyberte si plán, ktorý je pre vás najvhodnejší." 
    backgroundColor="bg-white" 
>}}

## Komponenty produktov

### Rozdelené s obrázkom

{{< products-split-with-image 
    backgroundColor="bg-gray-100" 
>}}

### S galériou obrázkov a rozbaľovacími detailmi

{{< products-with-image-gallery-and-expandable-details 
    backgroundColor="bg-white" 
>}}

### S mriežkou obrázkov

{{< products-with-image-grid 
    backgroundColor="bg-gray-100" 
>}}

### So záložkami

{{< products-with-tabs 
    backgroundColor="bg-white" 
>}}

### S vrstvenými obrázkami

{{< products-with-tiered-images 
    backgroundColor="bg-gray-100" 
>}}

## Komponenty recenzií

### Jednoduché s avatarami

{{< reviews-simple-with-avatars 
    heading="Recenzie zákazníkov" 
    backgroundColor="bg-white" 
>}}

### S prehľadovým grafom

{{< reviews-with-summary-chart 
    heading="Spätná väzba zákazníkov" 
    backgroundColor="bg-gray-100" 
>}}

## Komponenty štatistík

### Jednoduchá mriežka so štatistikami

{{< stats-simple-grid 
    heading="Dôverujú nám firmy po celom svete" 
    description="Pomohli sme tisíckam firiem dosiahnuť ich ciele." 
    backgroundColor="bg-white" 
>}}

## Komponenty tímu

### Mriežka s okrúhlymi obrázkami

{{< team-grid-round-images 
    heading="Náš tím" 
    description="Zoznámte sa s ľuďmi, ktorí stoja za našou spoločnosťou." 
    backgroundColor="bg-gray-100" 
>}}

## Komponenty referencií

### Referencie v mriežke

{{< testimonial-grid 
    heading="Čo hovoria naši zákazníci" 
    backgroundColor="bg-white" 
>}}

### Jednoduchá centrálná referencia

{{< testimonial-simple-centered 
    backgroundColor="bg-gray-100" 
>}}

## Komponenty rozloženia

### Bento mriežka: tri stĺpce

{{< bentogrid-three-column 
    backgroundColor="bg-white" 
>}}

### Bento mriežka: dva riadky

{{< bentogrid-two-row 
    backgroundColor="bg-gray-100" 
>}}

## Komponenty logotypov

### Jednoduché logá

{{< logos-simple 
    heading="Dôverujú nám tieto spoločnosti" 
    backgroundColor="bg-white" 
>}}

### Logá s nadpisom

{{< logos-with-heading 
    heading="Naši partneri" 
    description="Spolupracujeme s najlepšími spoločnosťami v odvetví." 
    backgroundColor="bg-gray-100" 
>}}