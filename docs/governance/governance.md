<!-- 

A project charter discusses _what the open source project is and why it exists_. Governance discusses _how the open source project operates_.
-->

# Project Governance

As stated in the [Charter](charter.md), this project governance _only_ covers collaboration on the `software.eessi.io` CernVM-FS repository, it does not cover other CernVM-FS repositories under the eessi.io namespace. In other words, when the sections below mention the EESSI CernVM-FS repository, this implies the `software.eessi.io` repository specifically. Thus, this governance only addresses contributing to, building for, deploying to, ingesting in, providing, or using the `software.eessi.io` repository.

The only exception to this is the Steering Committee, which has authority over all the `eessi.io` CernVM-FS repositories.

## 1. Guiding Principles
<!-- Optional section to state high-level principles like openness, meritocracy, consensus, etc. -->
The value of EESSI grows exponentially with two things: the amount of systems that make EESSI available, and the amount of software that is available in EESSI. Thus, the first goal of this governance is to make sure everyone in the community feels sufficiently included so that they are willing to contribute to EESSI (rather than build their own solution).

The second goal of this governance is to make clear how and by whom decisions in EESSI are taken. This is because trust in this process is important, both to infrastructure providers making the EESSI software stack available on their systems, as well as for end-users of the software. Note that this concerns both large decisions, such as which architectures are supported in EESSI, as well as small decisions, such as making a specific software package available in EESSI.

To achieve both goals, our governance is based on the [meritocracy](https://en.wikipedia.org/wiki/Meritocracy) governance model.

## 2. Roles and Responsibilities { #roles-and-responsibilities }

Below, the roles and responsibilities related to the EESSI project are discussed. The group of people with a common role will be referred to as a Team in the remainder of this document. Exceptions are Contributors, System administrators of systems providing EESSI and End-users (these are not considered to be Teams). Each individual in a Team will be referred to as a Team Member.

### 2.1 Owners of the `EESSI` GitHub organization & repositories
<!-- Define who contributors are and what they can do (e.g., file issues, submit PRs). -->
The owners of the [EESSI GitHub organization](https://github.com/EESSI) & repositories are those individuals with `owner` rights on the EESSI GitHub organization or one of its associated repositories.

EESSI GitHub organization & repository owners are responsible for setting permissions on the code repositories, compliant to the defined roles and responsibilities. They are also responsible for managing GitHub Apps for the EESSI build bots.

### 2.2 EESSI GitHub repository maintainers
EESSI GitHub repository maintainers are individuals with write access to (one or more of) the EESSI GitHub repositories.

EESSI GitHub repository maintainers are responsible for reviewing and merging PRs.

### 2.3 EESSI Infrastructure maintainers
EESSI Infrastructure maintainers are those individuals that maintain the Central Server for the EESSI CernVM-FS repository (the CernVM-FS Stratum 0), the _public_ mirror servers (CernVM-FS Stratum 1's), and EESSI build infrastructure (e.g. hosting the EESSI build bot).

Infrastructure maintainers are responsible for monitoring and maintaining their respective infrastructure, and provide access to those who need it according to the Roles and Responsibilities described here. Note that maintainers of build infrastructure have the right to limit access to a _subset_ of the Deployers and Builders as described in 2.4 and 2.5. Furthermore, they are _not_ allowed to give access to others that are not part of the EESSI Infrastructure maintainers, Deployers or Builders teams.

### 2.4 Builders { #builders }
Adding software to EESSI requires three steps (see [the contribution workflow](../adding_software/overview.md) documentation):

1. The software needs to be built (compiled);
2. A tarball of the software installation needs to be uploaded to a central location (e.g. S3 bucket) where the Central Server for the EESSI CernVM-FS repository can pick it up;
3. The Central Server for the EESSI CernVM-FS repository needs to ingest the tarball.

Builders are those individuals that have permissions to build software through one or more of the EESSI build bots, i.e. step 1 in this process.

Builders are responsible for reviewing contributions. They should, for example, check that contributions adhere to the contribution guidelines, that a contribution will not trigger execution of any unintended or unwanted code, etc. They are also responsible for triggering builds for contributors who want to add software to the EESSI software stack.

### 2.5 Deployers
Deployers are those individuals that have permissions to deploy software through one or more of the EESSI build bots to a central location (e.g. S3 bucket), i.e. they are essentially responsible for step 2 as it is described in the [Builders](#builders) Section.

Deployers should check the file list of the produced tarballs (as it is reported by the build bot) for unexpected items. They should also check if all officially supported hardware targets have been built for.

### 2.6 Ingesters
Ingesters are those individuals that have permissions to ingest a tarball into the EESSI CernVM-FS repository, i.e. they are essentially responsible for step 3 as it is described in the [Builders](#builders) Section.

Ingesters have merge permissions on the (private) `EESSI/staging` GitHub repository.

Ingesters should check the contents of the tarball as it is reported in the pull requests in the `EESSI/staging` repository. This essentially provides a second check (next to that done by Deployers) on the contents of the tarball.

### 2.7 Contributors

Contributors are individuals that make a contribution by opening a pull request to one of the repositories in the EESSI GitHub organization.

Contributors that propose adding software to EESSI in their contributions are responsible for checking that the license of the software they want to add allows its use in EESSI (e.g. allows redistribution). Contributors should also make an effort to ensure that their contributions don't add any malicious code. Finally, contributors should ensure that they adhere to the [Contribution Policy](../adding_software/contribution_policy.md).

### 2.8 System administrators of systems providing EESSI

System administrators of systems providing EESSI are administrators of systems (such as, but not limited to cloud and HPC systems) that make the EESSI software stack available to their users.

System administrators of systems providing EESSI should make sure that their system does not put any disproportionate load on the public EESSI CernVM-FS infrastructure. Typically, this means that they should adhere to best practices for CernVM-FS caching in a way that fits the size and nature of their system (e.g. by setting up a private CernVM-FS Stratum 1, a proxy, and/or a properly sized local cache).

System administrators agree to the [Terms of Use](terms_of_use.md) when making EESSI available on the systems they manage.

### 2.9 End-Users

End-Users are individuals that use any of the software provided by the EESSI software stack.

End users agree to the [Terms of Use](terms_of_use.md) when using the software installations provided by EESSI.

## 3. Decision-Making

This section applies to the decision making procedure for the Teams discussed in the [Roles and Responsibilities](#roles-and-responsibilities) Section. The Steering Committee has its own Decision-Making procedure (defined in the [Voting by the Steering Communittee](#voting-by-sc) Section).

### 3.1 Consensus Seeking

Decisions are made by seeking consensus. Each Team member is responsible for deciding whether an issue or decision is significant or sensitive enough to warrant discussions within their Team. If so, they should bring it up through the agreed-upon channels (see the [Meetings and Communication](#meetings-and-communication) Section).

### 3.2 Voting

There is no formal voting for Teams, for two reasons:

1. The Teams may be too big to organize voting in a quick, practical way.
2. The obligation to take part in votes may discourage people to become part of these Teams, as it may be seen as a burden.

Voting may nonetheless be used as a way to achieve consensus. For example, asking (a relevant subset of) the Team to vote may be one way to determine the majority opinion. Then, it can be discussed if the majority vote is an acceptable outcome to the Team. If so, consensus is achieved.

### 3.3 Deadlock Resolution

If consensus cannot be reached within the Team, the Steering Committee can take the decision for them. This can be requested by the Team, or done at the initiative of the Steering Committee (if they feel the lack of a decision is preventing the project from moving forward).

Also, if multiple Teams claim ownership over an issue, the Steering Committee can decide which Team is allowed to decide over the issue.

### 3.4 Overturning decisions

The goal is for Teams to operate autonomously as much as possible. 

However, in exceptional cases, the Steering Committee _can_ overrule a decision made by any of the Teams. This power should only be used as a last resort. Examples of when this may be considered include if the Steering Committee feels that a decision endangers the integrity or sustainability of the project, or goes against the policies the Steering Committee has defined. Even then, the Steering Committee should first engage in a discussion with a Team to see if consensus can be achieved on changing the decision.

## 4. Meetings and Communication { #meetings-and-communication }

While each Team is allowed to use the communication channels that their Team jointly agrees upon, the following channels are suggested

- GitHub / GitLab issues
- Slack
- (Periodic or incidental) video calls

## 5. Onboarding and Offboarding
This Section applies to the Teams described in the [Roles and Responsibilities](#roles-and-responsibilities) Section.

### 5.1 Adding Team Members

Teams themselves decide how large their teams should ideally be. They also decide the procedure to add new Team members. The procedure should reflect the sensitivity of the position, i.e. people with certain roles have the ability to (intentionally or unintentionally) compromise the integrity of the EESSI infrastructure. For such roles, the procedure should make sure candidates are extensively vetted and trusted by both the Team as well as the EESSI community as a whole.

As with all decisions the decision to add a Team member is subject to article 3.4.

### 5.2 Removing Team Members

Teams themselves decide the procedure to remove Team members. As for the procedure of adding Team Members, the procedure to remove Team Members should reflect the sensitivity of the position.

As with all decisions, the decision to remove a Team member is subject to article 3.4.

## 6 Steering committee

### 6.1 Responsibilities

The Steering Committee shall be responsible for:

- Outlining the technical direction of the EESSI project and setting priorities
- Conflict resolution: if there is a conflict between the people with the aforementioned roles, the steering committee shall mediate the dispute and make a final decision if consensus cannot be reached
- The [EESSI Charter](charter.md)
- The [EESSI Governance](governance.md)
- The [EESSI Policies](policies.md)

### 6.2 Members and Chairs

The Steering Committee is made up of community members with sustained and recognized contributions over time. Members take part in the Steering Committee as private individuals (i.e. they do not represent their employer(s)).

#### 6.2.1 Termination of membership

Membership of the Steering Committee can terminate in three ways:

- A Member can resign
- A Member may be voted out. In this case, the vote needs to be unanimous between the other Members. This procedure is intended to provide a mechanism for addressing extraordinary circumstances where a member's behavior or actions are deemed severely detrimental to the committee's function or reputation, and/or to the EESSI project.
- If a Member is inactive for 6 months and does not reply to communication from the rest of the Steering Committee, the Member may be voted out by the other Steering Committee members. In this case, [regular voting rules](#voting-by-sc) apply.

#### 6.2.2 New members

New Members must be recommended by one or more Steering Committee members.

The Steering Committee will make the recommendation known to the community, and collect feedback on the recommendation.
The Steering Committee then weighs the feedback, and votes on whether to accept the new member.

In the selection process, the Steering Committee will consider the following:

- The Steering Committee ideally consists of an odd number of Members (to reduce chances of a tie when voting);
- No more than 30% of the Members should be employed by commercial entities (to avoid that the project becomes dominated by commercial interests);
- The number of Members working for the same employer should be limited to 1 (to avoid that the project becomes dominated by a single employer, or a small group of employers);
- The number of Members with the same country of residence should be limited to 2 (to reflect the international nature of the project);
- The composition of the Steering Committee should reflect the EESSI community (to ensure that the community's interests are represented);

Note that if Members change jobs, or move to another country, some of the above criteria that were taken into account during selection may no longer be satisfied. It is up to the Steering Committee to decide if this is problematic, and if so, try to restore balance by requesting someone's resignation.

Members may appoint an alternate that may represent them and vote on their behalf in case they are unavailable. To alternate is appointed by a Member simply by informing the Chair. An alternate may be appointed for a single meeting, or until further notice. If a Member resigns or is voted out from the Steering Committee, their alternate immediately loses any rights they had as an alternate.

#### 6.2.3 Chair

A Chair will be appointed by the Steering Committee to serve for a one-year term. The Chair is responsible for organizing and leading the Steering Committee meetings (e.g. preparing and sending around an agenda, bringing items to a vote, counting the votes, ensuring meeting notes are kept and made available to the Steering Committee Members, etc).

The Chair can appoint another Member to serve as acting Chair for a given meeting or period.

If there is no Chair (e.g. because the Chair's term was completed, or the Chair stepped down from the Steering Committee), any Member can call for and organize a new meeting or electronic vote to appoint a new Chair. Whenever there is no Chair and there is a meeting, the first order of business will be to elect a new Chair.

### 6.3 Voting by the Steering Committee { #voting-by-sc }

#### 6.3.1 Majority vote

General decisions are taken by majority vote, provided that at least 75% of the Members cast a vote.

#### 6.3.2 Ways of voting

Votes can be cast:

- in-person;
- in a virtual meeting;
- via electronic vote (such as by e-mail, or through an approving review in GitHub).

#### 6.3.3 Neutral votes

Members can cast a neutral vote, in which case the vote does count towards the quorum of 75%, but is not including in calculating the majority. Example: in a committee with 7 members, if 3 members vote in favour of a proposal, 2 vote against, and one votes neutral, the quorum is met (6 out of 7 members have voted, i.e. >75%), and the majority (3 out of 5 non-neutral votes) is in favour, so the proposal is accepted.

#### 6.3.4 Abstaining

Members can also abstain from voting, in which case they neither count towards the quorum or calculating the majority. Example: in a committee with 7 members, if 3 members vote in favor, 2 vote against, and one abstains from voting, the quorum of 6 (75% of 7 members, rounded up) is not met.

#### 6.3.5 Ties

In case of a tie, the issue is discussed again, and a second vote is taken. All Members that voted in the first round need to have the opportunity to vote in the second round, which may mean that the vote needs to be postponed to a next meeting (e.g. because one or more Members voted by e-mail, and are not present at the meeting).

#### 6.3.6 Failing to reach quorum

In case the quorum of 75% is not reached, the vote is postponed.

#### 6.3.7 Fully electronic vote

A fully electronic vote (i.e. all Members vote electronically) can be organized by the Chair, in order to prevent having to delay a vote to the next meeting. Such a fully electronic vote is only valid once _all_ Members have cast their vote, or have explicitly stated that they abstain from voting.

#### 6.3.8 Voting topics

Anything may be brought to a vote during the meeting. However, if known up-front, issues that need to be voted on are announced by the Chair at least one week prior to the meeting, to give Members the opportunity to cast an electronic vote if they cannot attend.

#### 6.3.9 Votes on amending Charter or Governance

To amend the Charter, Governance or [Project Policies](policies.md#project-policies), a two-thirds majority of *all* Steering Committee Members needs to be in favour of the amendment. This is irrespective of the number of Members who have actually cast a vote, or are present at a meeting. Since the majority vote is determined based on the total amount of Members (rather than the total amount of votes), there is no quorum for votes on amendments to the Charter, Governance or Project Policies.

### 6.4 Meetings

The Steering Committee will meet as needed, but at least once per quarter. The Chair is responsible for organizing the meeting. Any Member can request the Chair to organize a meeting. Meetings are announced at least 2 weeks in advance, unless _all_ Members have agreed that a meeting on shorter notice is required.

## 7. Code of Conduct
The EESSI Code of Conduct can be found [here](code_of_conduct.md).

<!--
TODO: insert something like a contribution agreement later, once we have agreed, described in docs, etc
## 8. Contribution Agreement
All commit messages for contributions should be signed by the contributor, i.e. they should contain the statement: "Signed-off-by: firstname lastname <email>". With that signature, the contributor agrees to the [Developer Certificate of Origin](https://developercertificate.org/).
-->
## 8. Review and Amendment
Changes to the governance require approval by the Steering Committee, as per the rules described the [Voting by the Steering Committee](governance.md#voting-by-the-steering-committee) section.
