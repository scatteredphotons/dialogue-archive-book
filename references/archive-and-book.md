# Archive and book assembly

Read this file only for file organization, deduplication, or final-book work.

## Archive structure

Use the user's established hierarchy when one exists. A useful default is:

```text
Project or life domain/
  Technical accumulation/
    Engineering debug/
    Design iteration/
    Paper iteration/
  Psychological and intellectual growth/
Human observations/
Internship or work experience/
```

The hierarchy is descriptive, not mandatory. New parent nodes require a genuinely distinct life domain; do not create a new folder for every article.

## Inventory and deduplication

1. Inventory the candidate tree before planning the book.
2. Treat matching SHA-256 values as exact duplicate bytes.
3. Treat normalized-title matches as review candidates, not proof. Inspect their content and archive status.
4. Preserve the accepted formal copy. Exclude temporary renders, local drafts, rejected articles, and superseded variants from the manifest.
5. Never delete ambiguous files merely to make the list tidy.

Maintain a manifest with ordered volumes and chapters. It should record at least title, source path or stable file identity, destination volume, and acceptance status. The manifest—not filesystem ordering—defines book order.

## Book design

Organize the book by meaningful arcs rather than file creation time alone. Within each arc, chronology is usually the clearest default. Add only front matter that improves later browsing:

- cover and subtitle;
- short preface explaining the selection principle;
- table of contents with verified physical page numbers;
- restrained volume dividers;
- global page numbers;
- nested PDF bookmarks.

Preserve chapter interiors unless normalization is necessary for legibility. A book may contain intentionally different chapter styles when those styles reflect different kinds of memory.

## Verification

After assembly:

1. Confirm the expected number of accepted chapters.
2. Confirm the actual page count.
3. Verify every table-of-contents page number against its chapter start.
4. Verify bookmark hierarchy and metadata.
5. Render all pages, not a sample.
6. Inspect contact sheets plus every suspicious page at full resolution.
7. Check that Chinese glyphs render visually; successful text extraction alone is insufficient.
8. Re-render individually if a renderer produces a truncated image before concluding that the PDF is damaged.

Deliver only after the repaired PDF has passed the same checks again.
