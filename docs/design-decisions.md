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


# Tournament Participation Policy and strict rule that all teams and clubs must understand.
* Teams register individually before scheduling.
* scheduling is an explicit organizer action. 
* at least four and at most eight teams must be registered before scheduling
* fixture generation creates every unordered team pair exactly once.
* Registration closes when fixtures are generated.
* Fixtures cannot be re-generated during the same season.
* Fixtures cannot be regenerated during the same season.

## our system should be able to register up to 4 or 8 as mazimum teams first before fixture could take place and ehrn fixture takes plave then it blocks Registration for that season.

