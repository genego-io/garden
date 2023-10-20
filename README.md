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

## Features

### Blog

Simple blog where I share my thoughts and ideas, currently hosted at https://blog.genego.io (Gatsby cloud)

- Comments
- Ongoing series
- Upcoming blog posts (pre-draft)
- Newsletter integration

### Article section

For larger postings, case-studies, etc. Things which are too big to large to be a blogpost.

### About

A about me page, where I outline who I am, what I do, and what I have to offer the world of software

Currently hosted at https://edwin.genego.io (Gitbook free)

- Portfolio section (replaces the need to visit various sites)
- Services section (replaces LinkedIn)
- Work section (replaces LinkedIn)

