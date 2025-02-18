# EESSI Governance

## Motivation and goals
<!-- First, let's address the 'why'-->
The EESSI open source project was started by a small group of HPC engineers and support staff, working towards a common goal: a shared software stack of optimized software, that supports a wide range of systems. Collaboration was done based on implicit rules, and the group was small enough to easily reach consensus-based solutions. As the community grew, we have formalized the implicit rules for collaboration in this governance document, thus allowing for a structured and formalized way in which _all_ community members can contribute to the project and gain influence on it's direction.

The value of EESSI grows exponentially with two things: the amount of systems that make the EESSI software stack available, and the amount of software that is available in the EESSI software stack. Thus, the first goal of this governance is to make sure everyone in the community feels sufficiently included so that they are willing to contribute to EESSI (rather than build their own solution).

The second goal of this governance is to make clear how and by whom decisions in EESSI are taken. This is because _trust_ in this process is important, both to infrastructure providers making the EESSI software stack is available on their systems, as well as by end-users of the software. Note that this concerns both large decisions (e.g. which architectures to support) and small decisions (e.g. whether to accept a certain contribution to add software to EESSI).

To achieve both goals, our governance is based on the meritocracy governance model.<!-- Is this indeed what we want? Is this what we actually describe below? We COULD be less open, and it COULD be better for the security aspect of things... Maybe we should just revisit this at the end - we could say it is inspired by, et...--->

## Roles and Responsibilities

<!-- TODO make a chart similar to the governance map at https://ubuntu.com/community/governance ?-->

General note:
- All roles affecting security (Infrastructure maintainers, Code maintainers, Deployers, Builders): how do we ensure security?
- Should probably be a limited group of people, and at least 1 person in the current group should know the new person _personally_ before accepting into the group. Should probably state this explicitely in the governance
- For most teams, I think they can decide themselves who joins and who doesn't. I.e. builders can accept other builders. Questions: does it have to be unanimous? Other constraints set through policy (e.g. need to know someone personally)
- For the Steering committee: we could _start_ with self-appointed. Elections only make sense if there are multiple people who would even _want_ to fullfill this role. Otherwise, they can just distract from the work as they _are_ a lot of work for everyone (grooming candidates, having a voting system, who gets to vote, how do you make sure everyone is who they say - a person could have two GH handles and try to vote twice - etc.

### Steering Committee

- Governance
- Policy
- Arbitrage. E.g. if a contributor and a builder/deployer/... disagree, the Steering committee does arbitrage. => How do we ensure that we act fairly when steering committee members are directly involved? Can the rest of the steering committee still judge fairly?
- Consult on large technical decisions? Or does it take them? Or do we need a technical board? Or is the idea that the steering committee sets the policies and e.g. the maintainers team is free to implement anything within the policy limits? Can the steering committee overrule the maintainers team?
- How is the steering committee composed (election?)
- How are people removed from the steering committee (next election? Step down? Unanimous vote by the others?)

The members of the _Interim Steering Committee_ are listed below. Each member of the _Interim Steering Committee_ also
nominate an alternate should they not be able to attend a meeting of the committee.

* _Interim Steering Committee Lead_: Kenneth Hoste ([Ghent University](https://www.ugent.be/en)), [@boegel](https://github.com/boegel)
    * _Alternate: Lara Peeters ([Ghent University](https://www.ugent.be/en)), :material-github: [@laraPPr](https://github.com/laraPPr)_
* Alan O'Cais ([CECAM](https://www.cecam.org/), [University of Barcelona](https://web.ub.edu/inici)), :material-github: [@ocaisa](https://github.com/ocaisa)
    * _Alternate: Davide Grassano ([CECAM](https://www.cecam.org/)), :material-github: [@crivella](https://github.com/crivella)_
* Bob Dröge ([University of Groningen](https://www.rug.nl/)), :material-github: [@bedroge](https://github.com/bedroge)
    * _Alternate: Henk-Jan Zilverberg ([University of Groningen](https://www.rug.nl/)), :material-github: [@zilverberg](https://github.com/zilverberg)_
* Caspar van Leeuwen ([SURF](https://www.surf.nl/en)), :material-github: [@casparvl](https://github.com/casparvl)
    * _Alternate: Satish Kamath ([SURF](https://www.surf.nl/en)), :material-github: [@satishskamath](https://github.com/satishskamath)_
* Thomas Röblitz ([University of Bergen](https://www.uib.no/en)), [@trz42](https://github.com/trz42)
    * _Alternate: Terje Kvernes ([University of Oslo](https://www.uio.no/english/)), :material-github: [@terjekv](https://github.com/terjekv)_

### Code owners
Owners in the Github sense, not in the legal sense
- Assign GH rights
- Deploy GH apps
- (Very?) high level of trust needed. Could get malicious things in through publicly visible means. Maybe also invisible (GH app configs?).

### Code maintainers

- Github
- How does one become code maintainer? How does one get removed from this group?
- High level of trust needed. These people can make build bots sneak in arbitrary things (but it is publicly visible in the code).

### Infrastructure maintainers

- Stratum 0, Stratum 1, build infrastructure, SMEE server (or is this not able to inject anything due to the secret we use on the webhook payload?)
- Policy: we only ingest from infrastructured maintained by the Infrastructure maintainers
- Very high level of trust needed. These people can sneak in arbitrary things _without_ it being publicly visible (i.e. directly in stratum 0, or on build infrastructure through hooks, modification of the bot to package additional things in the tarball, etc).

### Deployers

- Have the power to deploy software, i.e. tell the Stratum 0 to ingest software into the repository
- Within policy limits, deployers decide what gets deployed and what not
- Policy gets set by Steering Committee
- Policy: never deploy software that was not build on an infrastructure maintained by the Infrastructure Maintainers.
- Policy: never deploy software that was build by anyone that does _not_ have the Builders role.
- How does one get this right? How is it removed?
- High level of trust needed. Can deploy malicious things, but would be publicly visible.

### Builders

- Has the power to command (at least one) build bot. 
- Medium level of trust needed. Can not deploy malicious things, but could run malicious things on build infrastructure.

### Contributors

- Anyone who makes PRs

### Users

- Anyone who uses the EESSI software


EESSI recognises that formal governance is essential given the ambitions of the project, not just for EESSI
itself but also to those who would adopt EESSI and/or fund its development.

EESSI is, therefore, in the process of adopting a formal governance model. To facilitate this process it has created an
_Interim Steering Committee_ whose role is to progress this adoption while also providing direction to the project.
