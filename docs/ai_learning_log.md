# TOURNAMENT LAB
## The behaviour of the whole architecture before writing any single  line of code.
* Team IDs should follow [`TM001`], [`TM002`] as an id and also fixture IDs follow [`MOO1`], [`MOO2`] preseiding order
* Team names are trimmed and validated for length and case-insensitive uniqueness.
* Team registration stops after `scheduling`.
* one fixture represent each unordered pair of teams.
* only pending fixtures accepts scores
* every mutating function validates before changing records.
* invalid operations raise ValueError, without patially changing the state. The CLI catches these and display friendly messages.
* standings are recalculated from played matches, they are never saved as independent records.
* JSON loading validates a temporary candidate season before replacing the running season.
