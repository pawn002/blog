# pawn002 Blog

## Useful Links

- [pawn002 Blog, prod](https://pawn002.github.io/blog-public/)
- [pawn002 Blog, test](https://pawn002.github.io/blog/)
- [pawn002 GitHub](https://github.com/pawn002)
- [eleventy-base-blog](https://github.com/11ty/eleventy-base-blog)
- [Table Generator](https://www.tablesgenerator.com/markdown_tables#)

## Initial Setup

_draft_

1. Pull down both repos used for this site
2. Modify `publish.js` to reflect paths used by the repos you pulled down.
3. Install dependencies for the working files repo.

_draft_

## Developing the Site Locally

Get Started via:

```bash
 npm run start
```

## Testing the Site Prior to Publishing

Get Started via:

```bash
 npm run build-ghpages-test
```

### Full Process

1. Merge work from `main` into `test` branch.
2. Run `npm run push-to-test`
3. Open browser to [repo Actions page](https://github.com/pawn002/blog/actions) to validate test page is building correctly.
4. Open browser to [test blog page](https://pawn002.github.io/blog/) to review prior to publishing.

## Publishing the Site

After reviewing the test blog page, you can publish the site by running:

```bash
 npm run deploy
```

You can then:

- Open browser to [production Actions page](https://github.com/pawn002/blog-public/actions) to validate page is building correctly.
- Open browser to [production blog page](https://pawn002.github.io/blog-public/) to view published blog.
