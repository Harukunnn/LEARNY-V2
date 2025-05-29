# FSRS 2024 Mathematics

This document provides a very short overview of the formulas used in the FSRS 2024
spaced repetition algorithm. The algorithm models the stability of a memory as a
function of the review history. At each review, the rating given by the user
influences the next interval and the ease factor of the card.

The main equations rely on the weight vector `w` which is fitted from empirical
review data. The stability `s` of a card is updated according to:

```
s_next = s * (1 + w[2] * (rating - 2))
```

The next interval is computed from stability using:

```
interval = max(1, round(s_next))
```

The ease factor evolves slowly toward a target depending on the rating:

```
ease_next = max(1.3, ease + 0.15 * (rating - 2))
```

For a full description see the [FSRS specification](https://github.com/open-spaced-repetition/fsrs4anki/wiki/Algorithm).

