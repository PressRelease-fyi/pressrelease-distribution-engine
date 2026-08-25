#!/usr/bin/env python3
"""
PressRelease Distribution Engine
A software toolkit for preparing, organizing, and managing press release
distribution workflows. Helps businesses, agencies, and publishers streamline
release creation, media targeting, distribution planning, and publication tracking.

https://pressrelease.fyi
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def format_channel(channel: str) -> str:
    return " ".join(w.capitalize() for w in channel.split("-"))


def get_priority_action(scores: dict) -> str:
    labels = {
        "release_quality": "Release Quality",
        "media_match": "Media Match",
        "distribution_reach": "Distribution Reach",
        "publication_rate": "Publication Rate",
        "syndication": "Syndication",
        "ai_visibility": "AI Visibility",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_distribution_channels(quality: int, media: int, reach: int, ai: int) -> dict:
    return {
        "Newswire": min(100, round(quality * 1.0)),
        "Media Outlets": min(100, round(media * 1.0)),
        "Online PR": min(100, round(reach * 1.0)),
        "AI Platforms": min(100, round(ai * 1.0)),
    }


def run_pr_distribution(
    release: str,
    channel: str = "newswire",
    release_quality: int = 88,
    media_match: int = 82,
    distribution_reach: int = 85,
    publication_rate: int = 78,
    syndication_score: int = 90,
    ai_visibility: int = 84,
) -> dict:
    """
    Run the PressRelease Distribution Engine across all distribution signals.

    Args:
        release: Press release title or identifier
        channel: Primary distribution channel
        release_quality: Release content quality score (0-100)
        media_match: Media targeting match score (0-100)
        distribution_reach: Distribution reach score (0-100)
        publication_rate: Publication and pickup rate score (0-100)
        syndication_score: Syndication breadth score (0-100)
        ai_visibility: AI platform visibility score (0-100)

    Returns:
        dict with individual distribution scores, overall distribution index,
        and distribution channel breakdown
    """
    scores = {
        "release_quality": release_quality,
        "media_match": media_match,
        "distribution_reach": distribution_reach,
        "publication_rate": publication_rate,
        "syndication": syndication_score,
        "ai_visibility": ai_visibility,
    }
    overall_distribution_index = round(sum(scores.values()) / 6)

    return {
        "release": release,
        "channel": format_channel(channel),
        "release_quality_score": release_quality,
        "media_match_score": media_match,
        "distribution_reach_score": distribution_reach,
        "publication_rate_score": publication_rate,
        "syndication_score": syndication_score,
        "ai_visibility_score": ai_visibility,
        "overall_distribution_index": overall_distribution_index,
        "priority_action": get_priority_action(scores),
        "distribution_channels": get_distribution_channels(release_quality, media_match, distribution_reach, ai_visibility),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    release = args[0] if len(args) > 0 else "release-title"
    channel = args[1] if len(args) > 1 else "newswire"
    release_quality = int(args[2]) if len(args) > 2 else 88
    media_match = int(args[3]) if len(args) > 3 else 82
    distribution_reach = int(args[4]) if len(args) > 4 else 85
    publication_rate = int(args[5]) if len(args) > 5 else 78
    syndication_score = int(args[6]) if len(args) > 6 else 90
    ai_visibility = int(args[7]) if len(args) > 7 else 84

    result = run_pr_distribution(
        release, channel, release_quality, media_match,
        distribution_reach, publication_rate, syndication_score, ai_visibility
    )

    print(f"Release: {result['release']}")
    print(f"Channel: {result['channel']}")
    print("=" * 45)
    print(f"Release Quality Score:         {result['release_quality_score']}/100  [{get_status(result['release_quality_score'])}]")
    print(f"Media Match Score:             {result['media_match_score']}/100  [{get_status(result['media_match_score'])}]")
    print(f"Distribution Reach Score:      {result['distribution_reach_score']}/100  [{get_status(result['distribution_reach_score'])}]")
    print(f"Publication Rate Score:        {result['publication_rate_score']}/100  [{get_status(result['publication_rate_score'])}]")
    print(f"Syndication Score:             {result['syndication_score']}/100  [{get_status(result['syndication_score'])}]")
    print(f"AI Visibility Score:           {result['ai_visibility_score']}/100  [{get_status(result['ai_visibility_score'])}]")
    print("=" * 45)
    print(f"Overall Distribution Index:    {result['overall_distribution_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nDistribution Channels:")
    for channel, score in result['distribution_channels'].items():
        print(f"  {channel:<24} {score}/100")


if __name__ == "__main__":
    main()
