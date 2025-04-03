---
title: "Testovacia stránka pre čiastkové súčasti"
date: 2025-03-31T16:49:48+02:00
draft: false
url: "test"
description: "Toto je testovacia stránka demonštrujúca všetky dostupné shortcodes v Hugo boilerplate téme."
---

Toto je testovacia stránka demonštrujúca všetky dostupné shortcodes v Hugo boilerplate téme. Každá sekcia nižšie ukazuje, ako použiť konkrétny shortcode a ako sa zobrazuje používateľom.

## Komponenty líného načítania

### YouTube video s oneskoreným načítaním

Nižšie je YouTube video s oneskoreným načítaním na otestovanie funkcie líného načítania videa:

{{< lazyvideo "8kGxHHhYRmE" "Krásne prírodné video - Uvoľňujúca hudba s prírodnými zvukmi" >}}

Video vyššie sa načíta iba vtedy, keď sa dostane do zobrazenia, čím sa zlepší výkon stránky.

### Obrázok s oneskoreným načítaním

{{< lazyimg "https://images.unsplash.com/photo-1682687982501-1e58ab814714" "Príklad obrázku s oneskoreným načítaním" >}}

### SVG s oneskoreným načítaním

{{< lazysvg "https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/AJ_Digital_Camera.svg" "Príklad SVG s oneskoreným načítaním" >}}

### Prvok picture

{{< picture "https://tailwindcss.com/plus-assets/img/ecommerce-images/home-page-03-featured-category.jpg" "Príklad responzívneho prvku picture" >}}

## Komponenty bannerov

### Banner s tlačidlom

{{< banner-with-button 
    title="Nová funkcia k dispozícii" 
    message="Vyskúšajte naše nové skúsenosti s dashboardom s vylepšenou analytikou." 
    buttonText="Vyskúšajte teraz" 
    buttonUrl="#" 
    dismissable=true 
>}}

### Banner na tmavom pozadí

{{< banner-on-dark 
    message="Výpredaj Black Friday: Získajte 50% zľavu na všetky plány do 30. novembra" 
    url="#" 
    dismissable=true 
>}}

### Banner na firemnej farbe

{{< banner-on-brand 
    message="Pridajte sa k nášmu webináru o aktualizáciách produktov tento piatok" 
    url="#" 
    dismissable=true 
>}}

### Banner s pozadím s efektom žiarenia

{{< banner-with-background-glow 
    message="Naša nová mobilná aplikácia je už k dispozícii na stiahnutie" 
    url="#" 
    dismissable=true 
>}}

### Spodne zarovnaný banner

{{< banner-bottom-aligned 
    message="Táto stránka používa súbory cookies na zlepšenie vášho zážitku" 
    url="#" 
    dismissable=true 
>}}

### Plávajúci banner v dolnej časti

{{< banner-floating-at-bottom 
    message="Ponuka s obmedzenou dobou: Doprava zdarma na všetky objednávky" 
    url="#" 
    dismissable=true 
>}}

### Uprostred plávajúci banner

{{< banner-floating-at-bottom-centered 
    message="Nový blogový príspevok: 10 tipov, ako zlepšiť produktivitu" 
    url="#" 
    dismissable=true 
>}}

### Oznámenie o ochrane súkromia (zarovnané vľavo)

{{< banner-privacy-notice-left-aligned 
    message="Používame súbory cookies na zlepšenie vášho prehliadania, zobrazovanie personalizovaných reklám alebo obsahu a analýzu našej prevádzky." 
    policyUrl="#" 
    acceptText="Prijať všetko" 
    rejectText="Odmietnuť všetko" 
>}}

### Oznámenie o ochrane súkromia (zarovnané na stred)

{{< banner-privacy-notice-centered 
    message="Používame súbory cookies na zlepšenie vášho prehliadania, zobrazovanie personalizovaných reklám alebo obsahu a analýzu našej prevádzky." 
    policyUrl="#" 
    acceptText="Prijať všetko" 
    rejectText="Odmietnuť všetko" 
>}}

### Oznámenie o ochrane súkromia (na celú šírku)

{{< banner-privacy-notice-full-width 
    message="Používame súbory cookies na zlepšenie vášho prehliadania, zobrazovanie personalizovaných reklám alebo obsahu a analýzu našej prevádzky." 
    policyUrl="#" 
    acceptText="Prijať všetko" 
    rejectText="Odmietnuť všetko" 
>}}

## Komponenty kategórií

### Náhľad: tri stĺpce s popisom

{{< categories-preview-three-column-with-description 
    heading="Nakupujte podľa kolekcie" 
    description="Každú sezónu spolupracujeme s dizajnérmi svetovej triedy na vytvorení kolekcie inšpirovanej prírodou." 
    backgroundColor="bg-white" 
>}}

### Náhľad: tri stĺpce

{{< categories-preview-three-column 
    heading="Nakupujte podľa kategórie" 
    backgroundColor="bg-gray-100" 
>}}

### Náhľad s obrázkovými pozadiami

{{< categories-preview-with-image-backgrounds 
    heading="Nakupujte podľa štýlu" 
    browseAllText="Zobraziť všetky štýly" 
    browseAllUrl="#" 
    backgroundColor="bg-white" 
>}}

### Náhľad s posúvajúcimi kartami

{{< categories-preview-with-scrolling-cards 
    heading="Prezrieť kategórie" 
    browseAllText="Zobraziť všetky kategórie" 
    browseAllUrl="#" 
    backgroundColor="bg-gray-100" 
>}}

### Produktový zoznam: karta s úplnými detailmi

{{< categories-product-list-card-with-full-details 
    heading="Vybrané produkty" 
    backgroundColor="bg-white" 
>}}

### Produktový zoznam s obrazovým prekrytím a tlačidlom pridať

{{< categories-product-list-with-image-overlay-and-add-button 
    heading="Novinky" 
    buttonText="Pridať do tašky" 
    backgroundColor="bg-gray-100" 
>}}

### Produktový zoznam s cenou v riadku a CTA odkazom

{{< categories-product-list-with-inline-price-and-cta-link 
    heading="Odporúčané produkty" 
    viewAllText="Zobraziť všetky produkty" 
    viewAllUrl="#" 
    ctaText="Zobraziť detaily" 
    backgroundColor="bg-white" 
>}}

### Produktový zoznam s vysokými obrázkami

{{< categories-product-list-with-tall-images 
    heading="Teraz v trende" 
    backgroundColor="bg-gray-100" 
>}}

## Obsahové komponenty

### Obsah so stredovým zarovnaním

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

### CTA na tmavom panely

{{< cta-dark-panel 
    heading="Ste pripravení začať?" 
    description="Kontaktujte nás alebo si vytvorte účet." 
    primaryButtonText="Kontaktovať predaj" 
    primaryButtonUrl="#" 
    secondaryButtonText="Vytvoriť účet" 
    secondaryButtonUrl="#" 
>}}

### Jednoduchá CTA na stred

{{< cta-simple-centered 
    heading="Zvýšte svoju produktivitu" 
    description="Začnite používať našu aplikáciu ešte dnes." 
    buttonText="Začať" 
    buttonUrl="#" 
    backgroundColor="bg-white" 
>}}

### Jednoduchá CTA s rozložením

{{< cta-simple-justified 
    heading="Ste pripravení pustiť sa do toho?" 
    description="Začnite dnes svoj bezplatný skúšobný čas." 
    buttonText="Zaregistrujte sa zadarmo" 
    buttonUrl="#" 
    backgroundColor="bg-gray-100" 
>}}

## FAQ komponenty

### Akordeón FAQ so stredovým zarovnaním

{{< faq-centered-accordion 
    heading="Často kladené otázky" 
    backgroundColor="bg-white" 
>}}

## Komponenty funkcií

### Funkcie v troch stĺpcoch

{{< features-three-column 
    heading="Funkcie" 
    description="Naša aplikácia poskytuje kompletné riešenie pre správu vašich obchodných potrieb." 
    backgroundColor="bg-gray-100" 
>}}

### Funkcie so sieťou štyroch obrázkov

{{< features-with-4-images-grid 
    heading="Technické špecifikácie" 
    description="Nasledujúce špecifikácie robia tento produkt výnimočným v porovnaní s konkurenciou." 
    backgroundColor="bg-white" 
>}}

### Funkcie so striedajúcimi sa sekciami

{{< features-with-alternating-sections 
    heading="Kľúčové funkcie" 
    description="Náš produkt je navrhnutý na riešenie vašich každodenných problémov." 
    backgroundColor="bg-gray-100" 
>}}

### Funkcie s miznúcim obrázkom

{{< features-with-fading-image 
    heading="Špecifikácie produktu" 
    description="Všetko, čo potrebujete vedieť o našom produkte." 
    backgroundColor="bg-white" 
>}}

### Funkcie s hlavičkou, obrázkami a popismi

{{< features-with-header-images-and-descriptions 
    heading="Ako to funguje" 
    description="Náš jednoduchý proces od začiatku až do konca." 
    backgroundColor="bg-gray-100" 
>}}

### Funkcie s úvodom a záložkami

{{< features-with-intro-and-tabs 
    heading="Funkcie produktu" 
    description="Preskúmajte rôzne aspekty nášho produktu." 
    backgroundColor="bg-white" 
>}}

### Funkcie s rozdeleným obrázkom

{{< features-with-split-image 
    subheading="Navrhnuté pre podniky" 
    heading="Správne funkcie pre váš biznis" 
    description="Náš produkt je navrhnutý tak, aby vyhovoval špecifickým potrebám moderných podnikov." 
    backgroundColor="bg-gray-100" 
>}}

### Funkcie s obdĺžnikovými obrázkami

{{< features-with-square-images 
    subheading="Prečo si vybrať nás" 
    heading="Funkcie, ktoré nás odlišujú" 
    description="Náš produkt obsahuje všetko, čo potrebujete na rýchly štart." 
    backgroundColor="bg-white" 
>}}

### Funkcie s vrstvenými obrázkami

{{< features-with-tiered-images 
    subheading="Výkonné funkcie" 
    heading="Všetko, čo potrebujete pre úspech" 
    backgroundColor="bg-gray-100" 
>}}

### Funkcie so širokými obrázkami

{{< features-with-wide-images 
    subheading="Intuitívne rozhranie" 
    heading="Navrhnuté pre produktivitu" 
    description="Naše prehľadné rozhranie vám pomáha sústrediť sa na to, čo je dôležité." 
    backgroundColor="bg-white" 
>}}

## Komponenty päty

### Päta so štyrmi stĺpcoch

{{< footer-four-column 
    backgroundColor="bg-gray-900" 
>}}

### Jednoduchá centrálna päta

{{< footer-simple-centered 
    backgroundColor="bg-gray-900" 
>}}

## Komponenty hlavičky

### Hlavička so stredovým zarovnaním

{{< header-centered 
    heading="Vitajte na našej webovej stránke" 
    description="Objavte naše produkty a služby." 
    backgroundColor="bg-white" 
>}}

### Jednoduchá hlavička

{{< header-simple 
    heading="O nás" 
    description="Dozviete sa viac o našej spoločnosti a misii." 
    backgroundColor="bg-gray-100" 
>}}

## Hero komponenty

### Jednoduchý centrálny hero

{{< hero-simple-centered 
    heading="Platforma novej generácie" 
    description="Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure qui lorem cupidatat commodo." 
    primaryButtonText="Začať" 
    primaryButtonUrl="#" 
    secondaryButtonText="Dozvedieť sa viac" 
    secondaryButtonUrl="#" 
    backgroundColor="bg-white" 
>}}

### Rozdelený hero s kódom

{{< hero-split-with-code 
    heading="Vyvíjajte s dôverou" 
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." 
    buttonText="Začať" 
    buttonUrl="#" 
    codeLanguage="javascript" 
    codeContent="function example() {console.log(\"Hello world!\");}" 
    backgroundColor="bg-gray-100" 
>}}

### Rozdelený hero s obrázkovými dlaždicami

{{< hero-split-with-image-tiles 
    heading="Navrhnite svoj ďalší projekt" 
    description="Vytvorte krásne dizajny s našou jednoduchou platformou." 
    buttonText="Začať navrhovať" 
    buttonUrl="#" 
    backgroundColor="bg-white" 
>}}

### Rozdelený hero s obrázkom

{{< hero-split-with-image 
    heading="Odhadnuté na základe dát" 
    description="Premeníte svoje dáta na využiteľné poznatky s našou analytickou platformou." 
    buttonText="Dozvedieť sa viac" 
    buttonUrl="#" 
    imageUrl="https://images.unsplash.com/photo-1551434678-e076c223a692" 
    imageAlt="Analytika dashboardu" 
    backgroundColor="bg-gray-100" 
>}}

### Rozdelený hero so screenshotom

{{< hero-split-with-screenshot 
    heading="Zefektívnite svoj pracovný tok" 
    description="Naša platforma vám pomáha efektívnejšie spravovať vaše projekty." 
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

### Trojstĺpcové s ilustráciami a hlavičkou

{{< incentives-3-column-with-illustrations-and-header 
    heading="Naše výhody" 
    description="Poskytujeme najlepšie služby v odvetví s týmito kľúčovými výhodami." 
    backgroundColor="bg-white" 
>}}

### Trojstĺpcové s ilustráciami a nadpisom

{{< incentives-3-column-with-illustrations-and-heading 
    heading="Naše záruky" 
    backgroundColor="bg-gray-100" 
>}}

### Trojstĺpcové s ilustráciami a rozdelenou hlavičkou

{{< incentives-3-column-with-illustrations-and-split-header 
    heading="Prečo nás zákazníci milujú" 
    description="Pomohli sme tisícom firiem dosiahnuť ich ciele." 
    backgroundColor="bg-white" 
>}}

### Štvorstĺpcové s ilustráciami

{{< incentives-4-column-with-illustrations 
    backgroundColor="bg-gray-100" 
>}}

## Komponenty menu

### Rozbaľovacie menu cez celú šírku, dve stĺpce

{{< menu-flyout-full-width-two-columns 
    buttonText="Riešenia" 
>}}

### Rozbaľovacie menu cez celú šírku

{{< menu-flyout-full-width 
    buttonText="Produkty" 
>}}

### Jednoduché rozbaľovacie menu s popismi

{{< menu-flyout-simple-with-descriptions 
    buttonText="Zdroje" 
>}}

### Zložené rozbaľovacie menu s akciami v päte

{{< menu-flyout-stacked-with-footer-actions 
    buttonText="Funkcie" 
>}}

### Rozbaľovacie menu s dvoma stĺpcami

{{< menu-flyout-two-column 
    buttonText="Spoločnosť" 
>}}

## Komponenty cien

### Cenové plány v troch úrovniach
{{< pricing-three-tiers 
    heading="Cenové plány" 
    description="Vyberte si plán, ktorý vám najviac vyhovuje." 
    backgroundColor="bg-white" 
>}}

## Komponenty produktov

### Rozdelené s obrázkom

{{< products-split-with-image 
    backgroundColor="bg-gray-100" 
>}}

### S obrázkovou galériou a rozbaľovacími detailmi

{{< products-with-image-gallery-and-expandable-details 
    backgroundColor="bg-white" 
>}}

### S obrázkovou mriežkou

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
    heading="Spätná väzba od zákazníkov" 
    backgroundColor="bg-gray-100" 
>}}

## Štatistické komponenty

### Jednoduchá mriežka štatistík

{{< stats-simple-grid 
    heading="Dôverujú nám firmy z celého sveta" 
    description="Pomohli sme tisícom firiem dosiahnuť ich ciele." 
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

### Mriežka referencií

{{< testimonial-grid 
    heading="Čo hovoria naši zákazníci" 
    backgroundColor="bg-white" 
>}}

### Jednoduchá centrálna referencia

{{< testimonial-simple-centered 
    backgroundColor="bg-gray-100" 
>}}

## Komponenty rozloženia

### Bento mriežka v troch stĺpcoch

{{< bentogrid-three-column 
    backgroundColor="bg-white" 
>}}

### Bento mriežka v dvoch riadkoch

{{< bentogrid-two-row 
    backgroundColor="bg-gray-100" 
>}}

## Komponenty loga

### Jednoduché logá

{{< logos-simple 
    heading="Dôverujú týmto spoločnostiam" 
    backgroundColor="bg-white" 
>}}

### Logá s nadpisom

{{< logos-with-heading 
    heading="Naši partneri" 
    description="Spolupracujeme s najlepšími spoločnosťami v odvetví." 
    backgroundColor="bg-gray-100" 
>}}