# Blueprints/Systems

## Purpose

Cross-cutting or manager-style Blueprint systems that are not Actor Components and not framework Cores (for example save orchestration helpers, audio directors, or puzzle managers — only when approved).

## Allowed Assets

- `BP_` system / manager Blueprints authorized by technical design

## Examples

- Reserved for approved systems (Save helpers, Audio director, Puzzle manager, etc.)

## Best Practices

- Confirm ownership against `architecture.md` before adding a system Blueprint.
- Prefer GameInstance / Components when they already own the responsibility.
- Avoid creating a second system that duplicates an existing one.
