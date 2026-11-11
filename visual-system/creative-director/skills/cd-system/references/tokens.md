# From direction to tokens

Each token traces to a line in `direction.md`. If you can't point to the line, the value doesn't go in.

## Names

A token name is `category.role`, singular, with the role named by its job: `color.ink`, `type.headline`, `space.margin`. Never name a token by hue (`sky-blue`), by size (`md`, `large`) or by a brand nickname. Put the nickname in `$description` when the person uses one. This is the only naming scheme inside a workspace; `<plugin>/ROUTING.md` says how it relates to `dsn-tokens`.

## Mapping

| Direction says | Tokens |
| --- | --- |
| Color in the visual codes | `color.*`, named by role (ink, paper, accent, muted), never by hue. The accent gets a `$description` saying when to use it |
| Type in the visual codes | `font.display`, `font.text`, then `type.headline`, `type.body`, `type.label` as composite typography tokens |
| Composition (margins, density, grid) | `space.unit`, `space.margin`, and any grid tokens |
| Texture, line weight | `stroke.*`, and a `$description` naming the texture asset if one exists |
| The never list | Not tokens. Leave them in `direction.md`; reviewers check them |

## Values the direction leaves open

The direction says "high-contrast serif," not which one. Pick a short list of two or three real fonts that fit, show them to the approver with a sample headline in each, and let them choose. Do the same for exact colors when the direction only names a family ("one muted green"). Record the choice and the alternatives in the token's `$description`.

Never fill an open value silently. A silent choice is a default, and defaults are how brands start to look alike.

## Fonts

Check each font is licensed for how it'll be used (web, social images, print) and available in the tools that need it. Figma, Paper and Claude Design may each need it installed or loaded. Note substitutions in `$description`.

## Keep mode

Every value comes from the existing brand, exactly. If two sources disagree (the site uses one gray, a past PDF another), list both under "Waiting on a person" in the brand's `context.md` and ask.
