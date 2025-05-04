# EESSI Policies

Should we have separate policies that Teams themselves can set? I.e. distinguish Project and Team policies, where project policies are set by the Steering Committee and Team policies by the respective Teams? Team policies could be ways to formalize concensus-based decisions. Clearly, if Team policies and Project policies contract, Project policy should come first.

EESSI Policies could be things like

- Should build for all architectures
  - If something isn't available for an architecture, the end-user should be informed at runtime, e.g. through an error printed by a modulefile
  - If something cannot be optimized for a micro-architecture, do we provide a less-optimized form (e.g. doesn't build for zen4 but does for zen3, so we provide zen3)?
- Something on the fact that we try to provide a full software Bill-of-Materials for all software we deploy?
- Acceptance of new software for the EESSI repository is "Yes, unless we can't" or "Yes, as long as it meets the Contribution Policy", i.e. we'll accept _anything_ that's reasonable?
- Rebuild policy: when do we rebuild?
- Removal policy: when do we remove?
- Something on optimization?
- Something on contributions _other_ than software for the EESSI repository (i.e. build logic, test suite, build bot). Should a requirement be that we can test it? Or is this too specific and should it be Team Policy?
- Include our current Contribution Policy? Or should that be separate? (it's maybe more a Team Policy?) https://www.eessi.io/docs/adding_software/contribution_policy/
- For security-critical roles (we should define which roles are security critical!), we only adopt new people that we (i.e. at least one person in that Team) knows _personally_.
- Whenever technical choices need to be made between (optimizing for) HPC, Cloud, or a PC, we prioritize HPC usage (?). I.e. if we can choose between two implementations, and one would break usage on HPC, and another would break Cloud usage, and there is no implementation that works on both, we prioritize HPC? Or do we NOT make this explicit? Or: do we only make it explicit for _optimization_ related stuff (but not for 'it works' vs 'it does not work')?

