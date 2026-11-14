# Becker Therapeutics Tracker

A static, public research site with clickable drug names, developer links, trial identifiers, and claim-level citations.

## Preview

Open `index.html` in a browser. The website is a standalone file with its catalog embedded and requires no server, account, build packages, or API keys.

## Publish

**GitHub Pages:** Create a public repository and upload `index.html` to the repository root. In repository **Settings → Pages**, choose **Deploy from a branch**, select `main`, and use `/ (root)`. The published site will appear at `https://YOUR_USERNAME.github.io/REPOSITORY/`.

**Cloudflare Pages / Netlify:** Upload `index.html` using their static-site deployment workflows.

This package does not publish automatically or include a domain.

## Update the research

1. Edit `catalog.json`. Each program has a source-linked developer, evidence category, status, phase, tissue focus, and an array of sourced claims.
2. Add sources to the top-level `sources` object. Source identifiers are used by both program rows and news updates.
3. Update the `updated` date and append new items to `updates`.
4. Run `python3 build.py` to validate source coverage and rebuild `index.html`.
5. Review the changes against original sources before publishing the updated HTML.

The existing ChatGPT weekly research automation is **not connected** to this site. Publication requires a separate editorial/update process.

## Definitions

- **Studied in Becker:** a Becker cohort or clinical investigation exists. Does not mean the treatment worked.
- **Becker plan / designation:** FDA orphan designation, sponsor-explicit indication, or prospective development. Does not mean Becker enrollment has begun.
- **DMD only / extrapolated:** research in Duchenne with possible shared pathological applicability. Becker efficacy is unproven.

The catalog includes completed and discontinued programs to preserve negative findings. It excludes DMD-specific microdystrophin replacement and most exon-skipping products.

## Source integrity

The builder verifies that every displayed research claim and news item has at least one citation key and that each source has an HTTPS URL. It cannot determine whether the claims are scientifically correct or whether source content changes after verification. Verify source material manually before each publication.

Clinical-trial information originates from sponsor-submitted registries; trial status can lag public announcements. This is a curated snapshot dated November 14, 2026, not medical advice or a complete treatment registry.
