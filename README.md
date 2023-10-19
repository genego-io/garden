# My digital garden (DG)

This repository holds the code for my [digital garden](https://maggieappleton.com/garden-history). A online exposé of my
ideas, thoughts, skills, interests and everything else I don't deem to be private knowledge and information. Currently
its a work in process (WIP), but should soon be online and available. This repository marks my freedom from third party
applications like Gitbook, Gatsby Cloud, LinkedIn and Wordpress. With this DG I will bring it all together.

## Tech

- Framework: [Django](https://www.djangoproject.com/) & [Wagtail CMS](https://wagtail.org/)
- Domain: https://garden.genego.io, will likely change to another domain at some point
- Interactivity: SASS, [Alpine.js](https://alpinejs.dev/), [HTMX](https://htmx.org/)
- Hosting:  [fly.io](https://fly.io/) Hobby plan during development

### Deploy on fly.io

1. `flyctl auth login`
2. `fly launch`
3. `fly deploy`