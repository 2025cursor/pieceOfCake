# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a bilingual marketing website for "Piece Of Cake Merge and Bake" game hosted at piece-of-cake.online. The site embeds the CrazyGames iframe and provides SEO-optimized content in English and Chinese.

## Architecture

- **Static site structure**: No build process, uses vanilla HTML/CSS/JS
- **Bilingual setup**:
  - English: `/index.html`
  - Chinese: `/zh/index.html`
- **SEO assets**: `robots.txt`, `sitemap.xml` at root level
- **Game integration**: Embedded CrazyGames iframe with referrerpolicy controls

## Key Technical Requirements

### SEO Compliance
- Title tags must be 50-60 characters with domain suffix
- Meta descriptions 150-160 characters with keywords
- H1-H3 tags must contain core keywords and long-tail variants
- Target keyword density ≥3% throughout content
- All images require descriptive alt attributes
- Use `nofollow` for external non-trusted links
- Canonical URLs pointing to exact page locations
- Viewport meta tag for mobile responsiveness

### Content Structure
- English articles target 800+ words with keyword density requirements
- Chinese content follows similar structure with cultural adaptations
- Article sections: "What is", "Game Features", "How to Play", "FAQ" pattern
- Language switching via navigation maintains user context

### Iframe Integration
- Game iframe: `https://games.crazygames.com/en_US/piece-of-cake-merge-and-bake/index.html?isNewUser=false`
- YouTube video: `https://www.youtube.com/embed/X62e6XcroWY`
- Both iframes use `loading="lazy"` and proper referrerpolicy

## Styling Guidelines

- **Design system**: Purple/pink gradient theme with cake iconography
- **CSS variables**: Defined in `:root` for consistent theming
- **Responsive**: Mobile-first with clamp() functions for fluid scaling
- **Typography**: Segoe UI for English, Noto Sans SC for Chinese
- **Components**: Reusable classes for hero sections, iframe wrappers, language toggles

## Content Management

When editing content:
- Maintain keyword density requirements for SEO
- Keep bilingual content structurally parallel but culturally adapted
- Update both language versions simultaneously
- Ensure all headings contain target keywords naturally
- Verify canonical URLs point to correct language-specific paths

## File Organization

```
/
├── index.html          # English homepage
├── zh/
│   └── index.html      # Chinese homepage
├── robots.txt          # Search crawler directives
├── sitemap.xml         # URL discovery for search engines
├── instruction.md      # Original project requirements
├── AGENTS.md          # Development workflow guidelines
└── seo_rules_guide.md # SEO compliance checklist
```

## Analytics and Tracking

- Google Analytics integration with ID: G-GRDHEDT25W
- Track iframe interactions and language switching patterns
- Monitor search performance for target keywords

## Deployment Considerations

- Static files can be served from any web server
- Ensure HTTPS for iframe security requirements
- Test iframe loading across different browsers
- Verify hreflang attributes for international SEO