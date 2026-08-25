#!/usr/bin/env node

interface PRDistributionInput {
  release: string;
  channel: string;
  releaseQuality: number;
  mediaMatch: number;
  distributionReach: number;
  publicationRate: number;
  syndicationScore: number;
  aiVisibility: number;
}

interface PRDistributionOutput {
  release: string;
  channel: string;
  releaseQualityScore: number;
  mediaMatchScore: number;
  distributionReachScore: number;
  publicationRateScore: number;
  syndicationScore: number;
  aiVisibilityScore: number;
  overallDistributionIndex: number;
  priorityAction: string;
  distributionChannels: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function formatChannel(channel: string): string {
  return channel.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ");
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    releaseQuality: "Release Quality",
    mediaMatch: "Media Match",
    distributionReach: "Distribution Reach",
    publicationRate: "Publication Rate",
    syndication: "Syndication",
    aiVisibility: "AI Visibility",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getDistributionChannels(quality: number, media: number, reach: number, ai: number): Record<string, number> {
  return {
    "Newswire": Math.min(100, Math.round(quality * 1.0)),
    "Media Outlets": Math.min(100, Math.round(media * 1.0)),
    "Online PR": Math.min(100, Math.round(reach * 1.0)),
    "AI Platforms": Math.min(100, Math.round(ai * 1.0)),
  };
}

export function runPRDistribution(input: PRDistributionInput): PRDistributionOutput {
  const scores = {
    releaseQuality: input.releaseQuality,
    mediaMatch: input.mediaMatch,
    distributionReach: input.distributionReach,
    publicationRate: input.publicationRate,
    syndication: input.syndicationScore,
    aiVisibility: input.aiVisibility,
  };
  const overallDistributionIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    release: input.release,
    channel: formatChannel(input.channel),
    releaseQualityScore: input.releaseQuality,
    mediaMatchScore: input.mediaMatch,
    distributionReachScore: input.distributionReach,
    publicationRateScore: input.publicationRate,
    syndicationScore: input.syndicationScore,
    aiVisibilityScore: input.aiVisibility,
    overallDistributionIndex,
    priorityAction: getPriorityAction(scores),
    distributionChannels: getDistributionChannels(input.releaseQuality, input.mediaMatch, input.distributionReach, input.aiVisibility),
  };
}

const args = process.argv.slice(2);
const release = args[0] || "release-title";
const channel = args[1] || "newswire";
const releaseQuality = parseInt(args[2]) || 88;
const mediaMatch = parseInt(args[3]) || 82;
const distributionReach = parseInt(args[4]) || 85;
const publicationRate = parseInt(args[5]) || 78;
const syndicationScore = parseInt(args[6]) || 90;
const aiVisibility = parseInt(args[7]) || 84;

const result = runPRDistribution({
  release, channel, releaseQuality, mediaMatch,
  distributionReach, publicationRate, syndicationScore, aiVisibility,
});

console.log(`Release: ${result.release}`);
console.log(`Channel: ${result.channel}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Release Quality Score:         ${result.releaseQualityScore}/100  [${getStatus(result.releaseQualityScore)}]`);
console.log(`Media Match Score:             ${result.mediaMatchScore}/100  [${getStatus(result.mediaMatchScore)}]`);
console.log(`Distribution Reach Score:      ${result.distributionReachScore}/100  [${getStatus(result.distributionReachScore)}]`);
console.log(`Publication Rate Score:        ${result.publicationRateScore}/100  [${getStatus(result.publicationRateScore)}]`);
console.log(`Syndication Score:             ${result.syndicationScore}/100  [${getStatus(result.syndicationScore)}]`);
console.log(`AI Visibility Score:           ${result.aiVisibilityScore}/100  [${getStatus(result.aiVisibilityScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Distribution Index:    ${result.overallDistributionIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nDistribution Channels:");
Object.entries(result.distributionChannels).forEach(([channel, score]) => {
  console.log(`  ${channel.padEnd(22)} ${score}/100`);
});
