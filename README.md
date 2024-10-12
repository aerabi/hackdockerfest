# Hackdockerfest

Hacktoberfest + Docker + Meetup + Oktoberfest :beer:

## About

Hackdockerfest is a Docker-themed Hacktoberfest celebration and meetup, happening since 2021.

- **2021**: The project was to contribute Docker security tips to this repository, and the results were presented in [a live stream](https://www.youtube.com/live/S7T2y6UjQmQ?si=YlwGPypwKW1oE46o).
- **2022**: There was a local meetup in Freiburg with 2 talks, one about SBOMs and how to generate them from Docker images. The project was creating [an events website using MEAN stack](https://github.com/aerabi/events), and document every step of the way. The result was turned into [a blog post published on Docker's blog](https://www.docker.com/blog/containerizing-an-event-posting-app-built-with-the-mean-stack/).
- **2023**: The meetup had two talks, one about the latest Docker Con, and the other one about using Docker Compose with Traefik.
- **2024**: The meetup is scheduled to happen on October 25th. The project is to contribute to a Docker Compose cheat sheet file (#51).



## Getting Started

<img src="black-forest-techies.png" width=200>

- [Black Forest Techies](https://discord.gg/vjauK5qa) Discord server
- [Hackdockerfest 2024 (in Freiburg)](https://www.meetup.com/docker-black-forest/events/303671875/) Meetup event
- [Hackdockerfest 2023 (in Freiburg)](https://www.meetup.com/docker-black-forest/events/296483825/) Meetup event
- [Hackdockerfest 2022 project repository](https://github.com/aerabi/events)
- [Hackdockerfest 2022 (in Freiburg)](https://www.meetup.com/docker-black-forest/events/287845505/) Meetup event
- [Hackdockerfest 2021](https://youtu.be/S7T2y6UjQmQ) YouTube live

![](https://secure.meetupstatic.com/photos/event/c/a/6/b/600_523731819.webp?w=750)

## Supply Chain Security

- Check NPM packages: `npm audit`
- Check NPM packages using Snyk: `npm i snyk` and then `snyk test`
- Check Docker image: `docker scout cves <image-name>`
- Export Docker image dependencies: `docker sbom <image-name>`
- What is SBOM:
  + [Generate the SBOM for Docker images](https://docs.docker.com/engine/sbom/)
  + [Build a software bill of materials (SBOM) for open source supply chain security](https://snyk.io/blog/building-sbom-open-source-supply-chain-security/)
- Which package to use: Snyk Advisor, e.g. for [`@rxjsx/rxjsx`](https://snyk.io/advisor/npm-package/@rxjsx/rxjsx)

## Contribute

Add more tips, tricks, or references to this document. This repo is Hacktoberfest participant and your contributions count towards the Hacktoberfest prize.

More repos to contribute to:

- [Events](https://github.com/aerabi/events)
- [RxJSx](https://github.com/rxjsx/rxjsx)

## Contributors

[![List of Contributors](https://contrib.rocks/image?repo=aerabi/hackdockerfest)](https://github.com/aerabi/hackdockerfest/graphs/contributors)
