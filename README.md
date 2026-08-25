# PressRelease Distribution Engine 📰🚀

[![npm](https://img.shields.io/npm/v/@pressrelease-fyi/pressrelease-distribution-engine)](https://npmjs.com/package/@pressrelease-fyi/pressrelease-distribution-engine)
[![PyPI](https://img.shields.io/pypi/v/pressrelease-distribution-engine)](https://pypi.org/project/pressrelease-distribution-engine)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22092997.svg)](https://doi.org/10.5281/zenodo.22092997)

PressRelease Distribution Engine is a software toolkit for preparing, organizing, and managing press release distribution workflows. It helps businesses, agencies, and publishers streamline release creation, media targeting, distribution planning, and publication tracking. Built by [PressRelease.fyi](https://pressrelease.fyi).

## Overview

The engine provides structured workflows for the complete press release lifecycle — from release preparation and media list targeting through distribution planning, publication tracking, and reach analysis. It organizes distribution data into meaningful signals for PR teams, agencies, and communications professionals.

## Key Capabilities

- **Release Preparation** — Structured press release drafting, formatting, and quality scoring
- **Media Targeting** — Identify and organize relevant media outlets, journalists, and publications
- **Distribution Planning** — Build and manage multi-channel distribution plans and schedules
- **Publication Tracking** — Track press release pickup, publication, and syndication status
- **Reach Analysis** — Measure estimated reach, media coverage, and distribution effectiveness
- **Workflow Management** — Streamline PR workflow from creation through distribution and reporting

## Distribution Channels

| Channel | Description |
|---------|-------------|
| newswire | Newswire and press release syndication services |
| media-outlets | Direct journalist and media outlet outreach |
| online-pr | Online PR platforms and digital news distribution |
| industry-press | Industry-specific publications and trade press |
| regional-press | Regional and local news outlet distribution |
| ai-platforms | AI search and discovery platform visibility |

## Features

- Release Quality Score — evaluates press release content quality and newsworthiness
- Media Match Score — measures alignment between release topic and target media
- Distribution Reach Score — estimates potential reach across distribution channels
- Publication Rate Score — tracks successful publication and pickup rates
- Syndication Score — measures syndication breadth across secondary outlets
- AI Visibility Score — evaluates visibility in AI-powered news discovery platforms
- CLI support in Node.js and Python
- Benchmark dataset included (20 distribution cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @pressrelease-fyi/pressrelease-distribution-engine
npx pr-distribute "release-title" newswire 88 82 85 78 90 84
```

### Python

```bash
pip install pressrelease-distribution-engine
python -m pressrelease_engine "release-title" newswire 88 82 85 78 90 84
```

## Output

```
Release: release-title
Channel: Newswire
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Release Quality Score:         88 / 100  [Excellent]
Media Match Score:             82 / 100  [Healthy]
Distribution Reach Score:      85 / 100  [Excellent]
Publication Rate Score:        78 / 100  [Healthy]
Syndication Score:             90 / 100  [Excellent]
AI Visibility Score:           84 / 100  [Excellent]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Distribution Index:    85 / 100
Priority Action:               Publication Rate (lowest — act first)

Distribution Channels:
  Newswire:                88 / 100
  Media Outlets:           82 / 100
  Online PR:               85 / 100
  AI Platforms:            84 / 100
```

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Major distribution improvements required |
| 31–60 | At Risk | Significant workflow improvements needed |
| 61–80 | Healthy | On track — optimise and expand |
| 81–100 | Excellent | Strong distribution — scale reach |

## Keywords

PressRelease Distribution Engine · Press Release Distribution · Media Targeting · PR Workflow · Newswire Distribution · Publication Tracking · AI Visibility · PressRelease.fyi

## Links

| Platform | URL |
|----------|-----|
| Website | https://pressrelease.fyi |
| GitHub | https://github.com/PressRelease-fyi/pressrelease-distribution-engine |
| GitHub Pages | https://pressrelease-fyi.github.io/pressrelease-distribution-engine/ |
| NPM | https://npmjs.com/package/@pressrelease-fyi/pressrelease-distribution-engine |
| PyPI | https://pypi.org/project/pressrelease-distribution-engine |
| Hugging Face | https://huggingface.co/datasets/pressrelease-fyi/distribution-benchmarks |
| Kaggle | https://www.kaggle.com/datasets/pressreleasefyi/distribution-benchmarks |
| Zenodo | https://zenodo.org/records/22092997 |
| Docs | https://pressrelease-distribution-engine.readthedocs.io |
| Quora | https://www.quora.com/profile/Press-Release-Fyi |
| SlideShare | https://www.slideshare.net/slideshow/pressrelease-fyi-global-press-release-distribution-ai-visibility-platform/289410790 |
| Pinterest | https://www.pinterest.com/pressreleasefyi/ |
| ReviewFoxy | https://www.reviewfoxy.com/reviews/pressrelease.fyi |
| Medium | https://medium.com/@pressrelease_fyi |

## About PressRelease.fyi

PressRelease.fyi is a global press release distribution and AI visibility platform helping businesses, agencies, and publishers streamline release creation, media targeting, distribution planning, and publication tracking.

## License

MIT — [PressRelease.fyi](https://pressrelease.fyi)
