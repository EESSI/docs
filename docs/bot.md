# Build-test-deploy bot

Building, testing, and deploying software is done by one or more *bot instances*.


The EESSI build-test-deploy bot :robot: is implemented as a [GitHub App](https://docs.github.com/en/apps/overview)
in the [`eessi-bot-software-layer` repository](https://github.com/EESSI/eessi-bot-software-layer).

It operates in the context of [pull requests](software_layer/adding_software.md#software_layer_pull_request) to
the [`compatibility-layer` repository](https://github.com/EESSI/compatibility-layer) or the
[`software-layer` repository](https://github.com/EESSI/software-layer),
and follows the instructions supplied by humans,
so the procedure of adding software to EESSI is *semi-automatic*.

It leverages the scripts provided in the `bot/` subdirectory of the target repository
(see for example [here](https://github.com/EESSI/software-layer/tree/2023.06/bot)), like `bot/build.sh`
to build software, and `bot/check-result.sh` to check whether the software was built correctly.

## High-level design

The bot :robot: consists of two components: the *event handler*, and the *job manager*.

### Event handler

The bot event handler is responsible for handling
[GitHub events](https://docs.github.com/en/webhooks-and-events/events/github-event-types)
for the GitHub repositories it is registered to.

It is triggered for every event that it receives from GitHub.
Most events are ignored, but specific events trigger the bot to take action.

Examples of actionable events are submitting of a comment that starts with `bot:`,
which may specify an instruction for the bot like [building software](#building),
or adding a `bot:deploy` label (see [deploying](#deploying)).

### Job manager

The bot job manager is responsible for monitoring the queued and running jobs, and reporting back
when jobs completed.

It runs every couple of minutes as a [cron job](https://en.wikipedia.org/wiki/Cron).

## Basics { #basics }

Instructions for the bot :robot: should always start with `bot: `.

To get help from the bot, post a comment with `bot: help`.

To make the bot report how it is configured, post a comment with `bot: show_config`.

### Permissions

The bot :robot: is configured to only act on instructions issued by specific GitHub accounts.

There are separate configuration options for allowing to send instructions to the bot,
to trigger building of software, and to deploy software installations in to the EESSI repository.

!!! note
    Ask for help in the `#software-layer-bot` channel of the EESSI Slack if needed!

## Building { #building }

To instruct the bot :robot: to build software, one or more `build` instructions
should be issued by posting a comment in the pull request (see also [here](software_layer/adding_software.md#bot_build)).

The most basic build instruction that can be sent to the bot is:

```
bot: build
```

!!! warning
    Only use `bot: build` if you are confident that it is OK to do so.

    Most likely, you want to supply one or more filters to avoid that the bot builds for all its configurations.

### Filters

Build instructions can include *filters* that are applied by each bot instance to determine which builds
should be executed, based on:

- `instance`: the `name` of the bot instance, for example `instance:aws` for the bot instance running in AWS;
- `repository`: the target repository, for example `eessi-2023.06-software` which corresponds to the 2023.06 version of the EESSI software layer;
- `architecture`: the name of the [CPU microarchitecture](software_layer/cpu_targets.md), for example `x86_64/amd/zen2`;

!!! note
    Use `:` as separator to specify a value for a particular filter, do not add spaces after the `:`.

    The bot recognizes shorthands for the supported filters, so you can use `inst:...` instead of `instance:...`,
    `repo:...` instead of `repository:...`, and `arch:...` instead of `architecture:...`.

#### Combining filters

You can combine multiple filters in a single `build` instruction.
Separate filters with a space, order of filters does not matter.

For example:

```
bot: build repo:eessi-2023.06-software arch:x86_64/amd/zen2
```

#### Multiple build instructions

You can issue multiple build instructions in a single comment, even across multiple bot instances,
repositories, and CPU targets. Specify one build instruction per line.

For example:

```
bot: build repo:eessi-2023.06-software arch:x86_64/amd/zen3 inst:aws
bot: build repo:eessi-2023.06-software arch:aarch64/generic inst:azure
```

!!! note
    The bot applies the filters with partial matching, which you can use to combine multiple build
    instructions into a single one.

    For example, if you only want to build for all `aarch64` CPU targets, you can use `arch:aarch64` as filter.

    The same applies to the `instance` and `repository` filters.

### Behind-the-scenes

#### Processing build instructions

When the bot receives build instructions through a comment in a pull request,
they are processed by the event handler component. It will:

1) Combine its active configuration (instance name, repositories, supported CPU targets)
   and the build instructions to prepare a list of jobs to submit;

2) Create a working directory for each job, including a Slurm job script that
   runs the `bot/build.sh` script in the context of the changes proposed in the pull request to build the
   software, and runs `bot/check-result.sh` script at the end to check whether the build was successful;

3) Submit each prepared job to a workernode that can build for the specified CPU target, and put a hold on it.

#### Managing build jobs

During the next iteration of the job manager, the submitted jobs are released and queued for execution.

The job manager also monitors the running jobs at regular intervals, and reports back in the pull request
when a job has completed. It also reports the result (`SUCCESS` :grin: or `FAILURE` :cry:), based on the result
of the `bot/check-result.sh` script.

#### Artefacts

If all goes well, each job should produce a tarball as an *artefact*,
which contains the software installations and the corresponding environment module files.

The message reported by the job manager provides an overview of the contents of the artefact,
which was created by the `bot/check-result.sh` script.

## Testing { #testing }

!!! warning
    The test phase is not implemented yet in the bot.

    We intend to use the [EESSI test suite](https://github.com/EESSI/test-suite)
    in different OS configurations to verify that the software that was built works as expected.

## Deploying { #deploying }

To deploy the artefacts that were obtained in the build phase, you should add the `bot: deploy` label
to the pull request.

This will trigger the event handler to upload the artefacts for ingestion into the EESSI repository.

### Behind-the-scenes

The current setup for the [software-layer repository](https://github.com/EESSI/software-layer), is as follows:

* The bot deploys the artefacts (tarballs) to an S3 bucket in AWS, along with a metadata file, using the
  [`eessi-upload-to-staging`](https://github.com/EESSI/eessi-bot-software-layer/blob/main/scripts/eessi-upload-to-staging) script;
* A cron job that runs every couple of minutes on the CernVM-FS Stratum-0 server opens a pull request to
  the (private) [EESSI/staging](https://github.com/EESSI/staging) repository, to move the metadata file for
  each uploaded tarball from the `staged` to the `approved` directory;
* Once that pull request gets merged, the target is automatically ingested into the EESSI repository by a cron job
  on the Stratum-0 server, and the metadata file is moved from `approved` to `ingested` in the `EESSI/staging` repository;
