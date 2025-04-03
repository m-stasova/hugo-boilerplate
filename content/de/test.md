---
title: "Testseite für Partials"
date: 2025-03-31T16:49:48+02:00
draft: false
url: "test"
description: "Dies ist eine Testseite, um alle verfügbaren Shortcodes im Hugo-Boilerplate-Theme zu demonstrieren."
---

Dies ist eine Testseite, um alle verfügbaren Shortcodes im Hugo-Boilerplate-Theme zu demonstrieren. Jeder nachfolgende Abschnitt zeigt, wie ein bestimmter Shortcode verwendet wird und wie er den Nutzern angezeigt wird.

## Lazy-Loading Komponenten

### Lazy-geladenes YouTube-Video

Unten ist ein lazy-geladenes YouTube-Video, um die Lazy-Loading-Funktionalität für Videos zu testen:

{{< lazyvideo "8kGxHHhYRmE" "Schönes Naturvideo - Entspannte Musik mit Naturgeräuschen" >}}

Das obenstehende Video sollte erst geladen werden, wenn es in den sichtbaren Bereich kommt, um die Seitenleistung zu verbessern.

### Lazy-geladenes Bild

{{< lazyimg "https://images.unsplash.com/photo-1682687982501-1e58ab814714" "Beispiel für ein lazy-geladenes Bild" >}}

### Lazy-geladene SVG

{{< lazysvg "https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/AJ_Digital_Camera.svg" "Beispiel für eine lazy-geladene SVG" >}}

### Picture-Element

{{< picture "https://tailwindcss.com/plus-assets/img/ecommerce-images/home-page-03-featured-category.jpg" "Beispiel für ein responsives Picture-Element" >}}

## Banner-Komponenten

### Banner mit Button

{{< banner-with-button 
    title="Neues Feature verfügbar" 
    message="Probieren Sie unsere neue Dashboard-Erfahrung mit verbesserten Analysen aus." 
    buttonText="Jetzt ausprobieren" 
    buttonUrl="#" 
    dismissable=true 
>}}

### Banner auf dunklem Hintergrund

{{< banner-on-dark 
    message="Black Friday Sale: Erhalten Sie bis zum 30. November 50% Rabatt auf alle Tarife" 
    url="#" 
    dismissable=true 
>}}

### Banner in Markenfarbe

{{< banner-on-brand 
    message="Nehmen Sie diesen Freitag an unserem Webinar über Produktupdates teil" 
    url="#" 
    dismissable=true 
>}}

### Banner mit Hintergrund-Glow

{{< banner-with-background-glow 
    message="Unsere neue mobile App ist jetzt zum Download verfügbar" 
    url="#" 
    dismissable=true 
>}}

### Unten ausgerichtetes Banner

{{< banner-bottom-aligned 
    message="Diese Seite verwendet Cookies, um Ihre Erfahrung zu verbessern" 
    url="#" 
    dismissable=true 
>}}

### Schwebendes Banner am unteren Rand

{{< banner-floating-at-bottom 
    message="Nur für kurze Zeit: Kostenloser Versand für alle Bestellungen" 
    url="#" 
    dismissable=true 
>}}

### Zentriertes schwebendes Banner

{{< banner-floating-at-bottom-centered 
    message="Neuer Blogbeitrag: 10 Tipps für mehr Produktivität" 
    url="#" 
    dismissable=true 
>}}

### Datenschutzhinweis (linksbündig)

{{< banner-privacy-notice-left-aligned 
    message="Wir verwenden Cookies, um Ihr Surferlebnis zu verbessern, personalisierte Werbung oder Inhalte bereitzustellen und unseren Traffic zu analysieren." 
    policyUrl="#" 
    acceptText="Alle akzeptieren" 
    rejectText="Alle ablehnen" 
>}}

### Datenschutzhinweis (zentriert)

{{< banner-privacy-notice-centered 
    message="Wir verwenden Cookies, um Ihr Surferlebnis zu verbessern, personalisierte Werbung oder Inhalte bereitzustellen und unseren Traffic zu analysieren." 
    policyUrl="#" 
    acceptText="Alle akzeptieren" 
    rejectText="Alle ablehnen" 
>}}

### Datenschutzhinweis (volle Breite)

{{< banner-privacy-notice-full-width 
    message="Wir verwenden Cookies, um Ihr Surferlebnis zu verbessern, personalisierte Werbung oder Inhalte bereitzustellen und unseren Traffic zu analysieren." 
    policyUrl="#" 
    acceptText="Alle akzeptieren" 
    rejectText="Alle ablehnen" 
>}}

## Kategorie-Komponenten

### Vorschau in drei Spalten mit Beschreibung

{{< categories-preview-three-column-with-description 
    heading="Nach Kollektion einkaufen" 
    description="Jede Saison arbeiten wir mit Designern von Weltklasse zusammen, um eine von der natürlichen Welt inspirierte Kollektion zu erstellen." 
    backgroundColor="bg-white" 
>}}

### Vorschau in drei Spalten

{{< categories-preview-three-column 
    heading="Nach Kategorie einkaufen" 
    backgroundColor="bg-gray-100" 
>}}

### Vorschau mit Bildhintergründen

{{< categories-preview-with-image-backgrounds 
    heading="Nach Stil einkaufen" 
    browseAllText="Alle Stile durchsuchen" 
    browseAllUrl="#" 
    backgroundColor="bg-white" 
>}}

### Vorschau mit scrollenden Karten

{{< categories-preview-with-scrolling-cards 
    heading="Kategorien durchsuchen" 
    browseAllText="Alle Kategorien anzeigen" 
    browseAllUrl="#" 
    backgroundColor="bg-gray-100" 
>}}

### Produktlistenkarte mit vollständigen Details

{{< categories-product-list-card-with-full-details 
    heading="Empfohlene Produkte" 
    backgroundColor="bg-white" 
>}}

### Produktliste mit Bildüberlagerung und Hinzufügen-Button

{{< categories-product-list-with-image-overlay-and-add-button 
    heading="Neuankömmlinge" 
    buttonText="In den Warenkorb" 
    backgroundColor="bg-gray-100" 
>}}

### Produktliste mit Inline-Preis und CTA-Link

{{< categories-product-list-with-inline-price-and-cta-link 
    heading="Empfohlene Produkte" 
    viewAllText="Alle Produkte anzeigen" 
    viewAllUrl="#" 
    ctaText="Details anzeigen" 
    backgroundColor="bg-white" 
>}}

### Produktliste mit hohen Bildern

{{< categories-product-list-with-tall-images 
    heading="Aktuelle Trends" 
    backgroundColor="bg-gray-100" 
>}}

## Inhaltskomponenten

### Zentrierter Inhalt

{{< content-centered 
    heading="Über unser Unternehmen" 
    backgroundColor="bg-white" 
>}}

### Geteilter Inhalt mit Bild

{{< content-split-with-image 
    heading="Unsere Mission" 
    imageUrl="https://images.unsplash.com/photo-1551434678-e076c223a692" 
    imageAlt="Team, das zusammenarbeitet" 
    backgroundColor="bg-gray-100" 
>}}

## Call-to-Action Komponenten

### Dunkles Panel CTA

{{< cta-dark-panel 
    heading="Bereit, loszulegen?" 
    description="Kontaktieren Sie uns oder erstellen Sie ein Konto." 
    primaryButtonText="Vertrieb kontaktieren" 
    primaryButtonUrl="#" 
    secondaryButtonText="Konto erstellen" 
    secondaryButtonUrl="#" 
>}}

### Einfacher zentrierter CTA

{{< cta-simple-centered 
    heading="Steigern Sie Ihre Produktivität" 
    description="Starten Sie noch heute mit unserer App." 
    buttonText="Loslegen" 
    buttonUrl="#" 
    backgroundColor="bg-white" 
>}}

### Einfacher, gerechtfertigter CTA

{{< cta-simple-justified 
    heading="Bereit einzutauchen?" 
    description="Starten Sie noch heute Ihre kostenlose Testphase." 
    buttonText="Kostenlos registrieren" 
    buttonUrl="#" 
    backgroundColor="bg-gray-100" 
>}}

## FAQ-Komponenten

### Zentriertes Akkordeon-FAQ

{{< faq-centered-accordion 
    heading="Häufig gestellte Fragen" 
    backgroundColor="bg-white" 
>}}

## Feature-Komponenten

### Drei-Spalten Features

{{< features-three-column 
    heading="Funktionen" 
    description="Unsere Anwendung bietet eine komplette Lösung zur Verwaltung Ihrer Geschäftsanforderungen." 
    backgroundColor="bg-gray-100" 
>}}

### Features mit 4-Bilder-Gitter

{{< features-with-4-images-grid 
    heading="Technische Spezifikationen" 
    description="Die folgenden Spezifikationen heben dieses Produkt von der Konkurrenz ab." 
    backgroundColor="bg-white" 
>}}

### Features mit abwechselnden Abschnitten

{{< features-with-alternating-sections 
    heading="Hauptfunktionen" 
    description="Unser Produkt wurde entwickelt, um Ihre alltäglichen Probleme zu lösen." 
    backgroundColor="bg-gray-100" 
>}}

### Features mit verblassendem Bild

{{< features-with-fading-image 
    heading="Produktspezifikationen" 
    description="Alles, was Sie über unser Produkt wissen müssen." 
    backgroundColor="bg-white" 
>}}

### Features mit Überschrift, Bildern und Beschreibungen

{{< features-with-header-images-and-descriptions 
    heading="So funktioniert es" 
    description="Unser einfacher Prozess von Anfang bis Ende." 
    backgroundColor="bg-gray-100" 
>}}

### Features mit Einleitung und Tabs

{{< features-with-intro-and-tabs 
    heading="Produktfunktionen" 
    description="Entdecken Sie die verschiedenen Aspekte unseres Produkts." 
    backgroundColor="bg-white" 
>}}

### Features mit geteiltem Bild

{{< features-with-split-image 
    subheading="Für Unternehmen entworfen" 
    heading="Die richtigen Funktionen für Ihr Unternehmen" 
    description="Unser Produkt wurde entwickelt, um die spezifischen Bedürfnisse moderner Unternehmen zu erfüllen." 
    backgroundColor="bg-gray-100" 
>}}

### Features mit quadratischen Bildern

{{< features-with-square-images 
    subheading="Warum uns wählen" 
    heading="Funktionen, die uns hervorheben" 
    description="Unser Produkt umfasst alles, was Sie für einen schnellen Einstieg benötigen." 
    backgroundColor="bg-white" 
>}}

### Features mit gestaffelten Bildern

{{< features-with-tiered-images 
    subheading="Leistungsstarke Funktionen" 
    heading="Alles, was Sie zum Erfolg brauchen" 
    backgroundColor="bg-gray-100" 
>}}

### Features mit breiten Bildern

{{< features-with-wide-images 
    subheading="Intuitive Benutzeroberfläche" 
    heading="Entwickelt für Produktivität" 
    description="Unsere klare Benutzeroberfläche hilft Ihnen, sich auf das Wesentliche zu konzentrieren." 
    backgroundColor="bg-white" 
>}}

## Footer-Komponenten

### Vier-Spalten Footer

{{< footer-four-column 
    backgroundColor="bg-gray-900" 
>}}

### Einfacher zentrierter Footer

{{< footer-simple-centered 
    backgroundColor="bg-gray-900" 
>}}

## Header-Komponenten

### Zentrierter Header

{{< header-centered 
    heading="Willkommen auf unserer Website" 
    description="Entdecken Sie unsere Produkte und Dienstleistungen." 
    backgroundColor="bg-white" 
>}}

### Einfacher Header

{{< header-simple 
    heading="Über uns" 
    description="Erfahren Sie mehr über unser Unternehmen und unsere Mission." 
    backgroundColor="bg-gray-100" 
>}}

## Hero-Komponenten

### Einfacher zentrierter Hero

{{< hero-simple-centered 
    heading="Plattform der nächsten Generation" 
    description="Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure qui lorem cupidatat commodo." 
    primaryButtonText="Loslegen" 
    primaryButtonUrl="#" 
    secondaryButtonText="Mehr erfahren" 
    secondaryButtonUrl="#" 
    backgroundColor="bg-white" 
>}}

### Geteilter Hero mit Code

{{< hero-split-with-code 
    heading="Entwickeln Sie mit Zuversicht" 
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." 
    buttonText="Loslegen" 
    buttonUrl="#" 
    codeLanguage="javascript" 
    codeContent="// Example code\nfunction example() {\n  console.log('Hello world!');\n}" 
    backgroundColor="bg-gray-100" 
>}}

### Geteilter Hero mit Bildkacheln

{{< hero-split-with-image-tiles 
    heading="Gestalten Sie Ihr nächstes Projekt" 
    description="Erstellen Sie wunderschöne Designs mit unserer benutzerfreundlichen Plattform." 
    buttonText="Jetzt designen" 
    buttonUrl="#" 
    backgroundColor="bg-white" 
>}}

### Geteilter Hero mit Bild

{{< hero-split-with-image 
    heading="Datenbasierte Einblicke" 
    description="Verwandeln Sie Ihre Daten in umsetzbare Erkenntnisse mit unserer Analyseplattform." 
    buttonText="Mehr erfahren" 
    buttonUrl="#" 
    imageUrl="https://images.unsplash.com/photo-1551434678-e076c223a692" 
    imageAlt="Dashboard analytics" 
    backgroundColor="bg-gray-100" 
>}}

### Geteilter Hero mit Screenshot

{{< hero-split-with-screenshot 
    heading="Optimieren Sie Ihren Arbeitsablauf" 
    description="Unsere Plattform hilft Ihnen, Ihre Projekte effizienter zu verwalten." 
    buttonText="Loslegen" 
    buttonUrl="#" 
    imageUrl="https://images.unsplash.com/photo-1551434678-e076c223a692" 
    imageAlt="Application screenshot" 
    backgroundColor="bg-white" 
>}}

## Incentives-Komponenten

### 2x2 Raster mit Illustrationen

{{< incentives-2x2-grid-with-illustrations 
    heading="Warum uns wählen" 
    backgroundColor="bg-gray-100" 
>}}

### 3-Spalten mit Illustrationen und Überschrift

{{< incentives-3-column-with-illustrations-and-header 
    heading="Unsere Vorteile" 
    description="Wir bieten den besten Service in der Branche mit diesen wesentlichen Vorteilen." 
    backgroundColor="bg-white" 
>}}

### 3-Spalten mit Illustrationen und Überschrift

{{< incentives-3-column-with-illustrations-and-heading 
    heading="Unsere Garantien" 
    backgroundColor="bg-gray-100" 
>}}

### 3-Spalten mit Illustrationen und geteilter Überschrift

{{< incentives-3-column-with-illustrations-and-split-header 
    heading="Warum Kunden uns lieben" 
    description="Wir haben Tausenden von Unternehmen geholfen, ihre Ziele zu erreichen." 
    backgroundColor="bg-white" 
>}}

### 4-Spalten mit Illustrationen

{{< incentives-4-column-with-illustrations 
    backgroundColor="bg-gray-100" 
>}}

## Menü-Komponenten

### Flyout in voller Breite mit zwei Spalten

{{< menu-flyout-full-width-two-columns 
    buttonText="Lösungen" 
>}}

### Flyout in voller Breite

{{< menu-flyout-full-width 
    buttonText="Produkte" 
>}}

### Einfaches Flyout mit Beschreibungen

{{< menu-flyout-simple-with-descriptions 
    buttonText="Ressourcen" 
>}}

### Gestapeltes Flyout mit Footer-Aktionen

{{< menu-flyout-stacked-with-footer-actions 
    buttonText="Funktionen" 
>}}

### Flyout in zwei Spalten

{{< menu-flyout-two-column 
    buttonText="Unternehmen" 
>}}

## Preis-Komponenten

### Preisgestaltung in drei Stufen

{{< pricing-three-tiers 
    heading="Preispläne" 
    description="Wählen Sie den Plan, der zu Ihnen passt." 
    backgroundColor="bg-white" 
>}}

## Produkt-Komponenten

### Geteilt mit Bild

{{< products-split-with-image 
    backgroundColor="bg-gray-100" 
>}}

### Mit Bildergalerie und erweiterbaren Details

{{< products-with-image-gallery-and-expandable-details 
    backgroundColor="bg-white" 
>}}

### Mit Bildraster

{{< products-with-image-grid 
    backgroundColor="bg-gray-100" 
>}}

### Mit Tabs

{{< products-with-tabs 
    backgroundColor="bg-white" 
>}}

### Mit gestaffelten Bildern

{{< products-with-tiered-images 
    backgroundColor="bg-gray-100" 
>}}

## Bewertungs-Komponenten

### Einfach mit Avataren

{{< reviews-simple-with-avatars 
    heading="Kundenbewertungen" 
    backgroundColor="bg-white" 
>}}

### Mit Zusammenfassungsdiagramm

{{< reviews-with-summary-chart 
    heading="Kundenfeedback" 
    backgroundColor="bg-gray-100" 
>}}

## Statistik-Komponenten

### Einfache Raster-Statistiken

{{< stats-simple-grid 
    heading="Weltweit von Unternehmen vertraut" 
    description="Wir haben Tausenden von Unternehmen geholfen, ihre Ziele zu erreichen." 
    backgroundColor="bg-white" 
>}}

## Team-Komponenten

### Raster mit runden Bildern

{{< team-grid-round-images 
    heading="Unser Team" 
    description="Lernen Sie die Menschen hinter unserem Unternehmen kennen." 
    backgroundColor="bg-gray-100" 
>}}

## Referenz-Komponenten

### Raster-Testimonials

{{< testimonial-grid 
    heading="Was unsere Kunden sagen" 
    backgroundColor="bg-white" 
>}}

### Einfaches zentriertes Testimonial

{{< testimonial-simple-centered 
    backgroundColor="bg-gray-100" 
>}}

## Layout-Komponenten

### Bento-Raster in drei Spalten

{{< bentogrid-three-column 
    backgroundColor="bg-white" 
>}}

### Bento-Raster in zwei Zeilen

{{< bentogrid-two-row 
    backgroundColor="bg-gray-100" 
>}}

## Logos-Komponenten

### Einfache Logos

{{< logos-simple 
    heading="Vertraut von diesen Unternehmen" 
    backgroundColor="bg-white" 
>}}

### Logos mit Überschrift

{{< logos-with-heading 
    heading="Unsere Partner" 
    description="Wir arbeiten mit den besten Unternehmen der Branche zusammen." 
    backgroundColor="bg-gray-100" 
>}}