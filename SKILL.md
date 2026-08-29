---
name: dialogue-archive-book
description: Turn long-running personal chat history into a curated archive of standalone Word chapters and, when requested, an ordered annual PDF book. Use when the user asks to continue collecting conversation assets, identify the next topic, write an approved topic, organize the archive, remove duplicate drafts, or assemble the finished collection.
---

# Dialogue Archive Book

Preserve the user's lived chronology and judgment while converting scattered conversations into durable, readable artifacts. Treat this as editorial curation, not exhaustive transcript export.

## Choose the current mode

- **Discover:** Find the next independent topic after already processed material. Propose only its title, destination, and concise synopsis. Do not draft the chapter before the user accepts it.
- **Write:** After explicit acceptance, recover the relevant evidence, choose the appropriate narrative mode, create one polished Word chapter, render every page, correct layout defects, and save it in the established archive structure.
- **Assemble:** Inventory accepted chapters, exclude rejected and duplicate drafts, propose or apply an ordered book structure, merge the chapters into one PDF, add front matter, page numbers, and bookmarks, then render and inspect every page.

Continue the active mode from the conversation instead of restarting the project. Maintain a small queue when several candidate topics appear, but finish or reject the current topic before moving to the next.

## Editorial authority

The user decides what becomes an asset. A positive reaction to a synopsis may count as acceptance when it is unambiguous; explicit rejection always wins. Do not silently restore a rejected chapter during final assembly.

Separate verified events from reconstruction. When primary chat evidence is incomplete, state the gap and write only what can be supported by available context or the user's recollection. Never invent exact dates, hardware, errors, quotations, motives, or resolutions to make the story neater.

Avoid turning every minor operation into an article. A topic should contain at least one meaningful problem, decision, reversal, technical insight, emotional shift, or human observation. Let simple but accepted topics remain short.

## Reusable resources

- Before choosing voice or structure for a chapter, read [references/editorial-modes.md](references/editorial-modes.md).
- When organizing files, detecting duplicates, or assembling a book, read [references/archive-and-book.md](references/archive-and-book.md).
- For a local asset tree, run `scripts/inventory_assets.py ROOT --output INVENTORY.json`. Use its hashes as evidence of exact duplication; review normalized-title candidates editorially rather than deleting automatically.

## Artifact requirements

For Word and PDF work, use the applicable document/PDF workflow available in the environment. A generated file is not finished until it has been rendered and visually inspected. Check Chinese fonts, long paths, tables, page breaks, orphaned headings, blank pages, and clipped content.

Save final artifacts durably in the user's existing archive when available. Preserve existing files and unrelated edits. Do not delete or overwrite possible duplicates without explicit authorization; exclude superseded drafts from a book manifest instead.

At delivery, report the destination, scope, and any deliberate exclusions. Provide one file entry per artifact so the interface does not make a single file look duplicated.
