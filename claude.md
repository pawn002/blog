# Blog Project Guidelines

## Project Overview
Personal blog built with Eleventy (11ty) focusing on accessibility advocacy, ethical AI, and inclusive design. Deployed to GitHub Pages.

## Tech Stack
- **Static Site Generator**: Eleventy 3.x
- **Templating**: Nunjucks (njk)
- **CSS**: Standard CSS in `public/css/`
- **Image Optimization**: @11ty/eleventy-img with custom shortcode

## Directory Structure
- `content/` - Markdown blog posts and pages (Eleventy input directory)
- `content/blog/` - Blog posts
- `public/img/` - Images (copied to `/img/` in build output)
- `_includes/` - Nunjucks templates and layouts
- `_config/` - Eleventy plugins (filters.js, images.js)
- `_site/` - Build output
- `docs/` - GitHub Pages deployment directory

## Images
- Store images in `public/img/`
- Use the custom image shortcode for optimization:
  ```
  {% image "img/filename.png", "Descriptive alt text" %}
  ```
- Images are automatically optimized to AVIF, WebP, and PNG formats at multiple widths (400, 800, original)
- All images MUST have meaningful, descriptive alt text (WCAG compliance)

## Blog Post Conventions
- Front matter required: title, description, date, tags
- Tags are comma-separated in front matter
- Use semantic heading hierarchy (h2 for main sections, h3 for subsections)
- Avoid superlative language (e.g., "genius", "amazing", "revolutionary")
- Maintain a measured, professional tone

## Accessibility Standards
- Follow WCAG 2.1 AA minimum, strive for AAA where practical
- Key guidelines to follow:
  - WCAG 1.4.3 Contrast Minimum
  - WCAG 1.4.6 Contrast Enhanced
  - WCAG 2.1.1 Keyboard
  - WCAG 4.1.2 Name, Role, Value
- All images require descriptive alt text
- Use semantic HTML elements

## Git Workflow
- Main branch: `main`
- Test branch: `test`
- Use semantic commit messages:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `refactor:` for code changes that don't add features or fix bugs
  - `chore:` for maintenance tasks
  - `docs:` for documentation changes
- Always propose a commit message.
- Always ask before committing changes
- Always ask before pushing changes

## Build Commands
- `npm run start` - Development server
- `npm run build` - Production build
- `npm run deploy` - Build for GitHub Pages and publish

## Owner Preferences
- Avoid emojis unless explicitly requested
- Use measured, professional language
- Prioritize accessibility in all implementations
- Prefer editing existing files over creating new ones
- Always use context7 when I need code generation, setup or
configuration steps, or library/API documentation. This means
you should automatically use the Context7 MCP tools to resolve
library id and get library docs without me having to
explicitly ask.
