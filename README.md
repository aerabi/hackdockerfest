# Hackdockerfest 2022

Hacktoberfest + Docker + Meetup + Oktoberfest :beer:

## Getting Started

<img src="black-forest-techies.png" width=200>

- [Black Forest Techies](https://discord.gg/vjauK5qa) Discord server
- [Hackdockerfest 2022 (in Freiburg)](https://www.meetup.com/docker-black-forest/events/287845505/) Meetup event
- [Hackdockerfest 2021](https://youtu.be/S7T2y6UjQmQ) YouTube live

## Supply Chain Security

- Check NPM packages: `npm audit`
- Check NPM packages using Snyk: `npm i snyk` and then `snyk test`
- Check Docker image: `docker scan <image-name>`
- Export Docker image dependencies: `docker sbom <image-name>`
- What is SBOM:
  + [Generate the SBOM for Docker images](https://docs.docker.com/engine/sbom/)
  + [Build a software bill of materials (SBOM) for open source supply chain security](https://snyk.io/blog/building-sbom-open-source-supply-chain-security/)
- Which package to use: Snyk Advisor, e.g. for [`@rxjsx/rxjsx`](https://snyk.io/advisor/npm-package/@rxjsx/rxjsx)

## Contribute

Add more tips, tricks, or references to this document. This repo is Hacktoberfest participant and your contributions count towards the Hacktoberfest prize.

More repos to contribute to:

- [Events](https://github.com/aerabi/events)

## Contributors

[![List of Contributors](https://contrib.rocks/image?repo=aerabi/hackdockerfest)](https://github.com/aerabi/hackdockerfest/graphs/contributors)
